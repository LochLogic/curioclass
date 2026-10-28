PASS
Counts: blockers 1 (general 0, family 1), should fix 14 (general 12, family 2), polish accepted 13

# target-toss: Refine

Lens files: refine/teaching.md (T), refine/play.md (P), refine/craft.md (C). Read them for frames and detail.
All 9 Done-when pass in every lens. Teaching and Craft each recomputed the ten-frames from real held-click taps
(7/4 and 5/7) and both matched the panel, the Look ten-frames, the bars and the result line. All ten throw cues match
SHAPE S1.E13/E14. No rule-5 content, so no sensitivity agent. "Family" below means the experiment format (a fair
test with one change); there is no engine.

## Blocker
1. **"Same throwers, same line." is false on Close or far?** (T-B1, P-6; family). src.html:313 says it on every
   question card, including the one where the line is the thing that changes, at the moment the tool teaches the fair
   test. Each card says what stays the same and what changes for that card ("Same throwers, same ball. Now from the
   far line."). Fix the spec's Voice table too. Make the Close or far? tip after the answer a result line, not a setup
   instruction (P).

## Should fix
2. **The coached way is always Way A and always 👍** (T-S2; general, BR1 lesson). Position gives the answer away. Put
   the coached way as B on some cards and use neutral vote signs (A / B, not thumbs).
3. **"Same throwers" is never set up** (T-S3; family). A round is 5, 10 or 20 throws, so in a full class Way B gets
   different children. The setup step says how: the same children throw in both rounds, in the same order, and the
   round size fits that (notes.md says the same).
4. **Unvoiced fixed lines** (T-S4; general, K-2 rule). The "Step: LEFT/RIGHT foot" tag (the kindergarten outcome
   itself) is never spoken; the narrator says only "opposite foot". The coach card's placeholder text is never voiced.
   Voice both.
5. **The setup card is incomplete and leaves the hint behind** (T-S6, P-8; family for the content, general for the
   hint). It must say the paper target needs the screen's three rings and hangs clear of the screen, and give a
   ball-fetching rule. With the card open the hint and Read follow the card; at 680x425, 800x500, 375 and 760x900
   steps 3 and 4 are below the fold: keep all steps in view (or scroll inside the card with a cue).
6. **Stop test and Clear the wall sit beside Undo with no way back** (P-1; general). One stray tap loses up to 40 throws
   or a Free throw session; mode buttons and keys 1 to 3 also reset a test silently. Move them away from Undo, smaller,
   with a Yes / No (built in the page) when there are throws to lose.
7. **Start Way B appears where Undo was** (P-2, C-2; general, BR1 lesson). At the 10th Way A throw, an Undo tap starts
   Way B, with no way back into Way A; at 375 the jump pushes Too short, Undo and Stop below the fold. Nothing rebuilds
   under the pointer: keep Undo where it is, put Start Way B elsewhere, and let Undo take back the last Way A throw
   until Way B's first throw.
8. **No way to fix the last Way B throw** (P-3; general). The tool moves to Look after 1.3 s and Look has no Undo. Give
   Look an "Undo last throw" that returns to Way B (or wait for a Done tap).
9. **Misses above the target are hidden under the Way banner** (P-4; general). At every size, in every Test round.
   Keep the banner off the throwing area so every dot shows.
10. **The Guess step has no Back or Stop test** (P-5, T polish; general). The handoff lists it; it wasn't built.
11. **Free throw says "Throw at the target!" with only the screen target shown** (P-7; general). w1-49 puts a paper
    target beside the screen; the welcome and hint say to throw at the paper target and tap where it hit.
12. **Focus drops to the page in Test it** (C-1; general, BR1 lesson). Question card, Way A, Skip the guess, Start Way
    B, Stop test, New question and Test again (src.html:957-973, 1024, 1176-1177). Move focus to the next control.
13. **The first Throw with Bo and the first How to set up wait about 7 s** (C-3; general, BR1 lesson). Bo stays frozen
    behind the safety line (src.html:376, 888, 1111). The first action starts at once; the safety line comes with it or
    after.
14. **The answer card on Look is clipped at 680x425 and 375** (C-4; general). The tip's second line is cut off
    (src.html:142, 781, 837).
15. **"Now you try!" doesn't name the control** (C-5; general). Speak tryBo, which does (src.html:910).

## Polish accepted
16. The tip says so when it differs from the class's own result, instead of overruling it silently (T).
17. Look ten-frames fill hits first, then misses, so they read at a glance (T).
18. notes.md: what to look for at each grade, K, 1 and 2 (T).
19. Overhand cue 2 keeps "elbow up"; cue 5 keeps "toward the target" (T, T nit).
20. "Make a guess!" comes right after a question tap and survives teacher pace (T, P).
21. The round intro says the way's name first (P).
22. Throw with Bo leaves time to do each move (P).
23. Projector: the score larger at 1920x1080, and the answer and Guess card text grows there (P).
24. The first coach line survives a 1 tap/s pace (P).
25. After an Undo, the Coach says card drops a tip from the throw that is gone (C); switching Throw doesn't rewrite
    advice for throws already made (T nit).
26. How to set up is modal (Show me can't run under it) (C).
27. The short-box toggle labels don't clip (C nit).
28. Spec voice table: the cue lines and "Ready, aim..." are events, as the code has them (C nit).

## Spec open questions (not for the builder)
- Confirm the overhand outcome (S1.E14 from grade 2) against the 2014 SHAPE table (T; only a secondary source so far).

## Settled calls
- Catching (T-S5): this tool teaches throwing. The spec and notes say the module is Throwing and Catching and catching
  belongs to a later K-2 tool; that goes on the board, not to the builder.
- K-2 targets are 60 px at every size, including the preview sizes (BUILD lesson wins over the audit's 44 px rule;
  the audit gets fixed).
- Builder spec deviations 1 to 5 and the Way B auto-advance are accepted (T).

## Exit check, round 1

Cold check, 2026-10-28. Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py target-toss` clean, 105 KB (only the
draft "no recording yet" notes). All driving with scripts/drive.py and held clicks (0.12 s), Sound on, at 1366x768
unless named. Frames and logs are in the exit agent's scratch folder exit-tt (out/, z/, m/, v/, run*.out).

### Recomputed from my own taps (Step or stay?, guess Way B, 10 throws a way)
Rings worked out before tapping (target cx 503, cy 460, R 238 page px; gold up to R/3, red up to 2R/3, blue up to R).
Way A: gold (d 0), red (120 = .50R), blue (200 = .84R), above (260 up, ny -1.09), side (300, nx 1.26), Too short,
gold (8.6 px), below (245 down, ny 1.03), blue (233 = .98R), miss (240 = 1.01R) = 5 hits. Way B: side, gold,
Too short, above, blue, side left, red, below, Too short, red left = 4 hits.
- Panel after Way A (r1): "Throw 10 of 10", "Hits: 5", ten-frame in throw order star, ball, ball, x, x / x, star,
  x, ball, x; tally "Hits 5 · Throw 10 of 10". Matches.
- Look (r4, r6): Way A 5 hits, Way B 4 hits, hits first then misses (A: two stars then three balls; B: one star,
  three balls), bars 5/10 and 4/10. Result "Way A got more hits!", then "That's different from our guess. That's why
  we test!" (guess B), then the step tip with no tipDiff (A is the coached way). Matches.
- Where do you look? (s3), guess A, A 10 golds, B 10 Too short: "Way A got more hits!", "That matches our guess!",
  then tipDiff before the look tip, spoken in that order. Matches.
- Big or small? (s1, s2): Way A gold hit, red miss, blue miss, side miss, gold hit = 2; Way B red, blue, gold, red,
  blue = 5 hits; "Way B got more hits!", size tip, no tipDiff. Matches.

### Items
1. PASS. Each card's Way B start line says what stays and the one change, and each matches its card: step "same
   line. Only the feet change" (r3), look "same line. Only where you look changes" (s3), far "same target. Only the
   line changes" (s5), size "same line. Only the target changes" (s2). The Close or far tip is a result line. The
   spec Voice table matches the code.
2. PASS. Coached way is A on step and far, B on look and size; vote signs are ☝️ and ✌️ on the buttons and cards.
3. PASS. startA "Pick your throwers. Each one throws once", Way B "Same throwers, same order"; notes.md says the
   round size fits the throwers.
4. PASS. Cue 3 speaks the foot (f1, left hand: tag, hint and log "Step with your right foot"); coach0 is spoken in
   the Free throw welcome (v1d, v3c).
5. PASS. Setup card has the rings step and the ball-fetch rule; all six steps in view at 680x425, 800x500, 1000x625,
   760x900 and 375 in the host (card scrollHeight = clientHeight); hint shows setupGo; Read reads the steps and
   setupGo with the card open (fo7_read).
6. FAIL (part). Stop test and Clear the wall sit apart, ask Yes / No, focus starts on No, Escape is No (c1, c2, c3,
   c5, c11 to c13); a mode button and key 1 ask during a round (c4, c5). On Look the throws are still there, and a
   mode button drops both rounds with no Yes / No (c10: 20 throws, one tap on Form, test reset). See N1.
7. PASS. At the 10th Way A throw Start Way B takes Too short's place (1104,489) and Undo stays at (1271,489) (r1);
   Undo after the 10th takes it back (r2: 9 throws, Way A open); Undo in an empty Way B reopens Way A with 9 (c8).
   At 375 Start Way B and Undo stay in view (h375_wayAdone).
8. PASS. Look has "Undo last throw" before the answer; it returns to Way B with 9 (r5; fo6b focus on the stage).
9. PASS. Above misses draw over the banner at every size (r1, r3, z680x425_wayA).
10. PASS. The Guess step has "Other question" back to Ask (c9, focus on the first card).
11. PASS. wFree "Throw at the paper target! Then tap the screen where each ball hit." (v3c).
12. PASS for the listed controls: card to Way A (fo1), Way A to the stage (fo2), Way A end to Start Way B (r1),
    Start Way B to the stage (fo3), Show the answer to Test again (fo6), Test again to Way A (fo4), New question and
    Stop test Yes to the first card (fo5, c3), No back to Stop test (c2), Clear Yes to Too short (c11). New gap: N2.
13. PASS. First Throw with Bo: "Ready, aim..." about 130 ms after the tap, safety after boDone (f2); first How to set
    up: the steps first, safety last (f5).
14. PASS. Answer card whole at 680x425 and 375 (z680x425_look, h375_look).
15. PASS. Next cue's fifth and the end of Show me speak tryBo (f4, f3).
16 to 28. PASS. tipDiff (s3); Look hits first (r4); notes per grade; cue lines; "Make a guess!" right after the title
    at 1.6 s and 2 s pace (r6, s1); the way name first (r1); Throw with Bo beats 2.6 to 4.1 s (f2); at 1920 the
    answer text is 24 px and the tally larger (z1920x1080_look); the first coach line at 1 tap/s is spoken (c11); the
    coach card follows Undo and keeps a given tip after a Throw switch (fr1 to fr4); the setup card is modal, Show me
    under it does nothing (fo7_inert); toggle labels unclipped at every size; the spec table has ready as an event.

### Done when
1 to 9 PASS: Form and left hand (f1, Bo mirrored, "Step: RIGHT foot"); a full run's counts (above); small target
(s1); every Undo path (r2, c8, r5); Too short adds a miss; Free throw "Too high" per Throw (fr1 underhand, fr2
overhand) and "Great aiming!" (c12); voice counts (table); 60 px (below); dashed, solid and double ring edges; Motion
off (below).

### Regressions looked for
- Sizes 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812 via drive.py --host, each in
  Form, Ask, Guess (Close or far), Way A, Way A done, Look with the answer, Look at 20 throws, Free throw and the
  setup card (72 frames): every visible control is 60 px or more both ways at every size; no horizontal scroll; the
  hint never overflows; no clipped labels; target 475 px across at 1366x768. Main controls in view everywhere;
  below the fold only the quiet Stop test / Clear and How to set up in short boxes, and Skip the guess / Other
  question at 680x425 and 800x500 (P1).
- Motion off: Bo jumps, timing and narration the same (m1 against m3), Look bars full at once (m2), no infinite
  animations in any shot.
- Saving and reset: only the kit's curio-motion key in localStorage; a mode switch keeps Free throw dots and resets
  Test it to Ask; Throw and Hand switches mid-round keep the round (fo9).
- No console errors or exceptions in any shot (only the host page's own favicon 404). No network requests: resource
  entries empty in every voice shot; the bundle has no URL but the SVG namespace.
- allLines() equals voice/lines.json word for word (84 = 84); no em dashes in src, notes or spec.

### Voice check (held clicks, gaps longer than the lines)
| Line | Kind | Expected | Spoken |
|---|---|---|---|
| cueU1 (cue card x5) | event | 5 | 5 |
| Show me cue lines (Show me x2) | event | 2 each | 2 each |
| tryBo (Show me x2) | how | 1 | 1, then silent |
| ready, boDone (Throw with Bo x2) | event | 2 | 2 |
| question title (card, Other question x5) | event | 5 | 5 |
| guess | how | 1 | 1, then silent 4 |
| wTest | how | 1 | 1, then silent 5 |
| coach (25 Free throws) | event | 5 | 5; no throw speaks |
| wFree, coach0 | how | 1 | 1 |
| setup, setupGo (card x5) | how | 1 | 1, then silent |
| askStop (Stop test, No x5) | event | 5 | 5 |
| wayA, count, doneA (10th throw, Undo x5) | event | 6 | 6 |
| safety | how | 1, whole | 1, but cut short in most runs (N3) |

First tap: a stage tap gets safety then wForm, safety about 150 ms after the tap (v3a); Next cue gets only its cue
(v3b); a mode button gets that mode's welcome (v3c); Read speaks the hint only (v3d); Sound says nothing and Sound
back on brings the welcome once (v3e); a key gets the welcome (v3f). Read stops a cue and Show me waits for it (v4a);
Read works with Sound off (v4b); a mode change after Read speaks at once (v4c). Stale: fast taps then a confirmed
mode switch play no Test line after the switch (v2). Order follows the actions in every log.

### New findings
- **N1 should fix (general; item 6 not finished).** Look still holds both rounds, but a mode button or keys 1 to 3
  drop them with no Yes / No: `testAtRisk` (src.html:1118) checks only steps A and B. c10: 20 throws, one tap on
  Form, all gone. The spec's rule is "with throws to lose"; include Look (at least before the answer).
- **N2 should fix (general, BR1 focus lesson).** Yes on the Yes / No card for a mode button or key leaves focus on
  the page body (c4), because the Yes path never refocuses (src.html:1132-1139, 1286). Put focus on the new mode's
  button, as a plain mode click leaves it.
- **N3 should fix (general, BR1 "no line is lost at a 2 s tap pace").** The welcome puts safety first; the next
  action's `now` line cuts it, and because it started it counts as heard and never comes back. Cut after 2.1 s at a
  2 s pace (s1: Test it, then a card), 2.6 s (f1: Hand, then Next cue), 0.4 s (v2). The safety line for children
  throwing balls is then never heard whole. Let `now` lines wait for safety, or say it again when it was cut.
- P1 polish: Skip the guess and Other question at 680x425, and Other question at 800x500, sit below the panel fold
  (z680x425_guess, z800x500_guess).
- P2 polish: at 375 the Look ten-frames have about 10 px cells (h375_look); the big numerals still read.
- P3 nit: the "✋ Throw: RIGHT hand" tag is never voiced (the foot tag is).
- P4 nit: at 1920x1080 the winner box on Look is mostly empty under the bar; the ten-frames could grow.

### Gate
1. Done when: all 9 pass. 2. Standards: SHAPE S1 taught by the class throwing with Bo and in the fair test; catching
is the settled board item. 3. Defaults: opens on Form; Show me and Throw with Bo work for one child alone. 4. Rule 5:
not needed. 5. Open should-fix: N1, N2, N3. 6. Bundle clean, 105 KB, no console errors, no network requests. 7. Voice
counts right except safety (N3).
Verdict: ROUND 2.

### Left open
N1, N2, N3 (should fix); P1 to P4 (polish, nit). The spec's open question on the S1.E14 grade stays with the spec.

## Exit check, round 2

Cold check, 2026-10-28. Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py target-toss` clean, 108 KB (only the
draft "no recording yet" notes). Driven with scripts/drive.py held clicks (0.12 s), Sound on, 1366x768 unless named.
For ordered click, tap and key sequences (and real keys 1 to 3, which drive.py has no entry for) I ran a copy of
drive.py in my scratch folder with a `seq` list added; the input code is drive.py's own. Speech was timed by wrapping
speechSynthesis.speak (start, end, "interrupted"). Frames and logs: scratch folder exit-tt2 (out_n1, out_n3, out_sz,
out_v, out_misc, sv/*.json, sz/*.json).

### Open items from round 1
- **N1 PASS.** With throws held, a mode button and keys 1, 2 and 3 each ask Yes / No (focus on No), and No (or
  Escape) keeps every throw, at: Way A with 3 throws (n1_a), Way A done with Start Way B up (n1_afull), Way B empty
  with Way A full (n1_b, A 10 kept), Way B with 4 (n1_b), Look before the answer (n1_look, 5 / 5 kept, answer still
  hidden) and Look after it (n1_look, 5 / 5 and the answer kept). The Guess step never holds throws (a question tap
  and Test again start empty, and there is no way back from Way A), so a mode button there switches at once
  (n1_guess, n1_guess_k): nothing is lost. See S2 for the 1.3 s beat before Look.
- **N2 PASS.** Yes on the card lands on the new mode's first control: Free throw button to Too short, Form button to
  Show me, Test it button to the first question card (n2_btn_*), key 1 from Look to Show me (n2_k1), key 2 from Way B
  to the first card (n2_k2). No returns focus to the mode button. Tab from No leaves the card for the browser and
  the next Tab comes back to Yes (x_tab; nit N4).
- **N3 PASS.** Every welcome, at a 2 s and a 0.5 s tap pace, plays the safety line whole (7.13 to 7.18 s, ended,
  not interrupted): stage tap into Form (n3_form), Test it then card, Way A and throws (n3_test), Free throw then six
  throws (n3_free), key 3 then Too short (n3_key3), Left hand first (n3_hand). A reset that cuts it brings it back
  whole in front of the next line: mode button (n3_cut_mode: cut at 1.0 s, again 2.6 to 9.7 s, then wFree), key 1
  (n3_cut_key), Clear the wall Yes / No (n3_cut_clear: again 7.6 to 14.7 s, then the coach line), Stop test No then a
  mode switch (n3_cut_stop) and Stop test Yes (n3_cut_stop_yes). How to set up during it lets it finish
  (n3_cut_setup). Lines behind it wait only as long as it runs: the next line starts 0.15 to 0.3 s after it ends in
  every run, and a newer tap replaces older waiting lines (stale handling, as meant).
- **P1 PASS.** Skip the guess and Other question in view at 800x500 (bottom 427 of 500) and at 680x425 all but 2 px
  (367 to 427 of 425; 680x425_guess).
- **P2 PASS.** At 375 the Look ten-frame cells are 29 px (27 px at 20 throws), readable (h375_look).
- **P3 PASS.** Tapping Left / Right hand speaks handL / handR every time (v_hand: 3 and 2 of 5 taps).
- **P4 PASS.** At 1920x1080 the Look ten-frames fill the winner box (104 px cells, 1920x1080_look).

### Round 1 items still holding
- Same / changes line on every card: the Way B start lines for step, look, far and size each name what stays and the
  one change (L.startB*, spoken at Way B start in v_q, c_far and c_size). The Close or far tip is a result line.
- Mis-tap recovery: Undo after the 10th Way A throw and in an empty Way B (v_wayA: wayA, count, doneA 6 each over 5
  Undo and re-throws), Look's Undo last throw, Stop test and Clear Yes / No (above), Throw and Hand switches keep a
  round (focus_round: 1 throw kept, step A).
- Counts from my own taps, rings worked out first (normalized distance d: gold to 1/3, red to 2/3, blue to 1).
  Close or far?, guess B. Way A: gold (0), red (.50), blue (.90), blue (.95), miss (1.05), miss above (1.2), Too
  short, gold (.28), blue (.98), miss (1.04) = 6. Way B: red (.50), miss (1.2), gold, Too short, red (.42), blue
  (.85), miss below (1.1), miss (1.12), gold (.10), Too short = 5. Tool: "Throw 10 of 10", "Hits: 6" then "Hits: 5",
  ten-frame labels 6 / 4 and 5 / 5, the stage tally, the Look description 6 and 5, Look frames hits first (A: star,
  ball, ball, ball, star, ball, then 4 misses), "Way A got more hits!", "That's different from our guess...", far
  tip, no tipDiff (c_far). Big or small?, 5 throws, guess A: Way A (only gold counts) gold, red miss, gold, blue
  miss, Too short = 2; Way B red, blue, miss, gold, blue (.85) = 4; "Way B got more hits!", differ, size tip, no
  tipDiff (c_size). 20 throws on size: 15 and 10 with tipDiff (look20 frames). All match.

### Regressions looked for
- Sizes 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812 in the host (drive.py
  --host), each in Form, Ask, Guess (far), Way A, Way A done, Way B, Look with the answer, Look at 20, Free throw,
  the setup card and the Yes / No card (88 frames): every visible control 60 px or more both ways; no horizontal
  scroll; no clipped button labels; the answer card whole everywhere (12 px at the preview sizes, 22 px at 1920); the
  setup card fits (scrollHeight = clientHeight). Below the fold only Stop test / Clear and How to set up in short
  boxes, and the settings and How to set up at 760x900 and 375 (as accepted in round 1). Hint: every step of all
  four questions measured at every size; it overflows only on Way B of "Where do you look?" (S1).
- Motion off: calm class on, no infinite animations, Look renders at once (calm_form, calm_look).
- Saving and reset: only curio-motion in localStorage. Nothing takes focus on load. Cue focus kept when the cues
  rebuild on a Throw switch (focus_rebuild).
- allLines() equals voice/lines.json word for word and in order (86 = 86). No em dashes in src, notes, spec, lines.
- No console errors or exceptions in any shot (only the host page's favicon 404). No network requests: resource
  entries empty in every voice shot; the bundle's only URL is the SVG namespace.

### Voice check (held clicks, gaps longer than the lines)
| Line | Kind | Expected | Spoken |
|---|---|---|---|
| cueU1 (cue card x5) | event | 5 | 5 |
| Show me cues (x2) | event | 2 each | 2 each |
| tryBo (Show me x2) | how | 1 | 1, then silent |
| ready, cues, boDone (Throw with Bo x2) | event | 2 each | 2 each |
| question title, wayA / wayB and the ways (card, Other question x5) | event | 5 | 5 each |
| guess | how | 1 | 1, then silent 4 |
| wTest (after Other question x5) | how | 1 | welcome 1, then silent 5 |
| coach (25 Free throws) | event | 5 | 5 |
| wFree, coach0 | welcome | 1 | 1 each |
| setup, setupGo (card x5) | how | 1 | 1, then silent |
| askStop (Stop test, No x5) | event | 5 | 5 |
| wayA, count, doneA (10th throw, Undo x5) | event | 6 | 6 |
| handL / handR (x5) | event | 5 | 5 |
| safety | welcome | 1, whole | 1, whole (N3) |

First tap: the stage gets safety then wForm (n3_form); Next cue only its cue (f_next); a mode button or key its
welcome with safety (n3_test, n3_key3); Read the hint only (f_read); Sound nothing, and Sound back on the welcome
once (f_sound). Read during Show me speaks the hint and Show me waits; a mode change after Read speaks at once; Read
works with Sound off (readrun). Stale: fast taps, a confirmed mode switch, then Test it again: no Test line after
the switch (stale). Order follows the actions in every log.

### New findings
- **S1 should fix (general, BR1 sizes lesson).** On Way B of "Where do you look?" the hint (startBlook, 89
  characters) needs three lines in the short boxes' two-line hint; fitHint stops at 12.5 px, so "hits." runs under
  the Under / Right toggles at 680x425 and 800x500 (680x425_wayB, 800x500_wayB; measured overlap) and overflows its
  box at 1000x625 (still visible there). Every other hint fits at every size. Shorten that line or let the short
  hint take a third line.
- **S2 should fix (general, stale line; N1 edge).** A mode button or key 1 to 3 in the 1.3 s beat after Way B's last
  throw opens the Yes / No card, but T.lookTimer still fires goLook under it: the step turns to Look behind the card,
  and goLook's `now` lines cut "Stop the test?" after 1.0 s and speak "Way A: Five hits." over the card (n1_beat:
  askStop interrupted at 9.6 s, wayA and the count spoken 9.6 to 13.3 s with the card up). No still keeps every
  throw. Clear the timer in askConfirm (start it again on No), or have goLook wait while state.confirm is set.
- P5 polish: Read or Sound off during the safety line cuts it and it never comes back (n3_cut_read, n3_cut_sound:
  Sound back on brings wForm without it). Both are the teacher's own choice and the tip stays on screen.
- P6 polish: a Form session that starts on Throw with Bo and stops it, or uses only Next cue, does not hear the
  safety line until a mode change (x_bo_stop: first at 16.5 s, on Free throw). The fifth Next cue's tryBo could
  carry it.
- P7 polish: on the first question at a 2 s pace the question title and "Make a guess!" wait behind the 7 s safety
  line and are replaced by Way A's lines (n3_test_2s); the guess how-to comes back on the next question. A shorter
  safety line would cost less.
- N4 nit: Tab from No leaves the Yes / No card for the browser chrome; the next Tab returns to Yes (x_tab).
- Kit lead (not this tool): in headless Chrome an utterance spoken right after cancel() sometimes never starts (for
  example n3_form_2s "Let go..."); the log still says spoken. Recorded clips avoid it.

### Gate
1. Done when: all 9 still pass (counts above, Undo paths, small target, Motion off, 60 px, voice counts).
2. Standards: unchanged from round 1. 3. Defaults: unchanged. 4. Rule 5: not needed. 5. Open should-fix: S1, S2.
6. Bundle clean, 108 KB, no console errors, no network requests. 7. Voice counts right.
Verdict: ROUND 2 FAILED (the last round). S1 and S2 are narrow; per REFINE.md Rounds, the integrator fixes them with
an "Integrator fix" note or brings them to Cory.

### Left open
S1, S2 (should fix); P5 to P7 (polish), N4 (nit), the kit lead. The spec's S1.E14 question stays with the spec.

## Integrator fix (S1, S2) and close

Narrow check, 2026-10-28, of the integrator's change to src.html (startBlook shortened, also in spec.md and
voice/lines.json; askConfirm clears Way B's 1.3 s Look timer and No with Way B full opens Look then). Bundle:
`CURIO_DRAFT=1 python scripts/bundle_tool.py target-toss` clean, 108 KB (only the draft "no recording yet" notes).
Driven with a copy of scripts/drive.py with round 2's ordered `seq` list (held clicks 0.12 s, real keys), Sound on,
speech timed by wrapping speechSynthesis.speak. Frames and logs: scratch folder exit-tt3 (out_s1, out_s2, sv/*.json).

- **S1 PASS.** startBlook is now "Same throwers, same order, same line. Only the eyes change. Tap where each ball
  hits." in src.html, spec.md and voice/lines.json. Way B of "Where do you look?", hint text rects against every
  visible button: at 680x425, 800x500 and 1000x625 it fits in two lines at 13.5 px (scrollHeight 39 = clientHeight
  39, text bottom 126, box bottom 129, Under / Right tops 139, no button overlap; 680x425_wayB, 800x500_wayB,
  1000x625_wayB); at 375 in the host (drive.py --host) two lines at 17 px, 49 = 49, nothing touched. Every other
  startB hint fits too (step, far, size: 13 to 13.5 px at the short boxes, 17 px elsewhere, scrollHeight =
  clientHeight), and every step of all four questions plus Form, Show me, Free throw and tryBo fits with no button
  overlap at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375 (hint_*.json).
- **S2 PASS.** Close or far?, 5 throws, guess A. My taps, rings first (d: gold to 1/3, red to 2/3, blue to 1): Way A
  gold (0), red (.5), miss (1.2), blue (.9), miss (1.1) = 3; Way B gold (.1), gold (.2), miss (1.3), red (.5), then
  the last throw blue (.8) = 4. A trigger 0.05 s after that last throw, each in its own run: Free throw button
  (s2_btn_no), key 2 (s2_k2_no), key 1 then Escape (s2_k1_esc), Stop test (s2_stop_no), Form button at 680x425
  (s2_680_no). In every run the Yes / No card opens with focus on No, the step stays Way B and the Look timer is 0
  at 2 s (no Look behind the card); the only line while the card is up is "Stop the test?", which plays until the No
  press (about 3.4 to 3.7 s, cut only by that press; the queued startBfar chain is dropped by hush, nothing else
  speaks). No (or Escape) opens Look with focus on Show the answer and speaks wayA, "Three hits.", wayB, "Four
  hits.", look, each ended, in order. Look shows "Way A: 3 hits. Way B: 4 hits, out of 5 throws each.", frame labels
  3 hits / 4 hits, A gold, red, miss, blue, miss and B gold, gold, miss, red, blue: all match my count. Yes switches
  with focus on the new mode's first control: Free throw button to Too short (s2_btn_yes), key 2 to the first
  question card (s2_k2_yes), key 3 to Too short (s2_k3_yes), Form button to Show me (s2_form_yes, "Where do you
  look?"); the new mode's welcome follows the card, no Look lines.

### Regressions looked for
- Way B auto-advance without a card: the last throw, then 1.8 s, Look up with focus on Show the answer and the same
  five lines and counts, no card (r_auto).
- Stop test: No keeps Way B (5 / 1) with focus back on Stop test; Yes goes to Ask with focus on the first card
  (r_stop). Clear the wall: No keeps 2 throws, focus back on Clear; Yes clears to 0, focus on Too short (r_clear).
- 60 px: every visible control 60 px or more both ways, no clipped labels, no horizontal scroll, at 680x425,
  800x500, 1000x625, 1366x768 (Way B, Look, Yes / No card), 1280x720, 1920x1080, 760x900 (Way B) and 375 in the
  host (Way B, Look, Yes / No card). Below the fold only what round 1 accepted (Stop test and How to set up in the
  short boxes, settings and How to set up at 760x900 and 375).
- allLines() equals voice/lines.json word for word and in order (86 = 86). No em dashes in src, spec, lines.
- No console errors or exceptions in any shot (only the host page's favicon 404); no resource requests.
- The host server is stopped and tools/target-toss/host.html deleted.

### Gate
S1 and S2 fixed, no regressions; round 2's other passes stand. Open: P5 to P7 (polish), N4 (nit), the kit lead,
and the spec's S1.E14 question, as listed in round 2. Verdict: PASS.

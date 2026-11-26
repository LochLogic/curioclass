# Target Toss: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Refine

<!-- part: refine.md -->

PASS
Counts: blockers 1 (general 0, family 1), should fix 14 (general 12, family 2), polish accepted 13

### target-toss: Refine

Lens files: refine/teaching.md (T), refine/play.md (P), refine/craft.md (C). Read them for frames and detail.
All 9 Done-when pass in every lens. Teaching and Craft each recomputed the ten-frames from real held-click taps
(7/4 and 5/7) and both matched the panel, the Look ten-frames, the bars and the result line. All ten throw cues match
SHAPE S1.E13/E14. No rule-5 content, so no sensitivity agent. "Family" below means the experiment format (a fair
test with one change); there is no engine.

#### Blocker
1. **"Same throwers, same line." is false on Close or far?** (T-B1, P-6; family). src.html:313 says it on every
   question card, including the one where the line is the thing that changes, at the moment the tool teaches the fair
   test. Each card says what stays the same and what changes for that card ("Same throwers, same ball. Now from the
   far line."). Fix the spec's Voice table too. Make the Close or far? tip after the answer a result line, not a setup
   instruction (P).

#### Should fix
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

#### Polish accepted
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

#### Spec open questions (not for the builder)
- Confirm the overhand outcome (S1.E14 from grade 2) against the 2014 SHAPE table (T; only a secondary source so far).

#### Settled calls
- Catching (T-S5): this tool teaches throwing. The spec and notes say the module is Throwing and Catching and catching
  belongs to a later K-2 tool; that goes on the board, not to the builder.
- K-2 targets are 60 px at every size, including the preview sizes (BUILD lesson wins over the audit's 44 px rule;
  the audit gets fixed).
- Builder spec deviations 1 to 5 and the Way B auto-advance are accepted (T).

#### Exit check, round 1

Cold check, 2026-10-28. Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py target-toss` clean, 105 KB (only the
draft "no recording yet" notes). All driving with scripts/drive.py and held clicks (0.12 s), Sound on, at 1366x768
unless named. Frames and logs are in the exit agent's scratch folder exit-tt (out/, z/, m/, v/, run*.out).

##### Recomputed from my own taps (Step or stay?, guess Way B, 10 throws a way)
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

##### Items
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

##### Done when
1 to 9 PASS: Form and left hand (f1, Bo mirrored, "Step: RIGHT foot"); a full run's counts (above); small target
(s1); every Undo path (r2, c8, r5); Too short adds a miss; Free throw "Too high" per Throw (fr1 underhand, fr2
overhand) and "Great aiming!" (c12); voice counts (table); 60 px (below); dashed, solid and double ring edges; Motion
off (below).

##### Regressions looked for
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

##### Voice check (held clicks, gaps longer than the lines)
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

##### New findings
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

##### Gate
1. Done when: all 9 pass. 2. Standards: SHAPE S1 taught by the class throwing with Bo and in the fair test; catching
is the settled board item. 3. Defaults: opens on Form; Show me and Throw with Bo work for one child alone. 4. Rule 5:
not needed. 5. Open should-fix: N1, N2, N3. 6. Bundle clean, 105 KB, no console errors, no network requests. 7. Voice
counts right except safety (N3).
Verdict: ROUND 2.

##### Left open
N1, N2, N3 (should fix); P1 to P4 (polish, nit). The spec's open question on the S1.E14 grade stays with the spec.

#### Exit check, round 2

Cold check, 2026-10-28. Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py target-toss` clean, 108 KB (only the
draft "no recording yet" notes). Driven with scripts/drive.py held clicks (0.12 s), Sound on, 1366x768 unless named.
For ordered click, tap and key sequences (and real keys 1 to 3, which drive.py has no entry for) I ran a copy of
drive.py in my scratch folder with a `seq` list added; the input code is drive.py's own. Speech was timed by wrapping
speechSynthesis.speak (start, end, "interrupted"). Frames and logs: scratch folder exit-tt2 (out_n1, out_n3, out_sz,
out_v, out_misc, sv/*.json, sz/*.json).

##### Open items from round 1
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

##### Round 1 items still holding
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

##### Regressions looked for
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

##### Voice check (held clicks, gaps longer than the lines)
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

##### New findings
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

##### Gate
1. Done when: all 9 still pass (counts above, Undo paths, small target, Motion off, 60 px, voice counts).
2. Standards: unchanged from round 1. 3. Defaults: unchanged. 4. Rule 5: not needed. 5. Open should-fix: S1, S2.
6. Bundle clean, 108 KB, no console errors, no network requests. 7. Voice counts right.
Verdict: ROUND 2 FAILED (the last round). S1 and S2 are narrow; per REFINE.md Rounds, the integrator fixes them with
an "Integrator fix" note or brings them to Cory.

##### Left open
S1, S2 (should fix); P5 to P7 (polish), N4 (nit), the kit lead. The spec's S1.E14 question stays with the spec.

#### Integrator fix (S1, S2) and close

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

##### Regressions looked for
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

##### Gate
S1 and S2 fixed, no regressions; round 2's other passes stand. Open: P5 to P7 (polish), N4 (nit), the kit lead,
and the spec's S1.E14 question, as listed in round 2. Verdict: PASS.

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: target-toss

Cold Craft lens, round 1 (2026-10-28). Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py target-toss`, 95 KB.
Driven with `scripts/drive.py` (held clicks, 0.12 s), muted headless Chrome, own profile, ports 9940-9946.

**Counts: blockers 0, should fix 5 (general 5, family 0), polish 2 (general 2), nit 2 (general 2).**

#### Findings

##### Should fix

1. **Focus falls to the page when a Test it step hides the control that was pressed** (general).
   Where: `src.html:957-973` (pickQuestion, makeGuess, startRound), `1024-1029` (stopTest), `1176-1177` (Test again,
   New question). The pressed control's panel or card grid goes `hidden`, nothing else is focused, so a keyboard user
   is dropped to `<body>` and the next Tab starts again at the header.
   How seen: keyboard shots (Enter on the focused control, then `document.activeElement` after 1.8 s). Question card,
   Way A guess, Skip the guess, Start Way B, Stop test, New question and Test again all ended on `BODY` (hidden).
   The good cases already exist in the same file: Way A done focuses Start Way B, Look focuses Show the answer, Show the
   answer focuses Test again, Clear the wall focuses Too short, Escape returns to How to set up. Do the same for the
   rest: after a question card or guess, focus the stage target (it is focusable in a round) or the first control of
   the new step; after Stop test / New question, the first question card; after Test again, Way A's guess button.
   BR1 lesson missed ("focus is kept when controls rebuild").

2. **Start Way B appears exactly where Undo was** (general).
   Where: `src.html:210-215` and `938`. When the last Way A throw lands, Start Way B is unhidden above the Too short /
   Undo / Stop row and pushes it down 68 px.
   How seen: control positions at 1366x768. During Way A, Undo is centered at (1188, 489); after the 10th throw, Start
   Way B is centered at (1188, 489) and Undo moves to (1188, 557). A teacher who reaches for Undo after a stray last tap
   presses Start Way B instead, and from Way B there is no way back into Way A. At 375 wide (iframe host) the same
   jump pushes Too short, Undo and Stop test below the fold (bottom 823 in an 812 px frame).
   Better: keep the row where it is and put Start Way B in a reserved slot (for example in place of Too short, which is
   disabled then, or below the row). BR1 lesson missed ("nothing rebuilds under the pointer").

3. **The first Throw with Bo (and the first How to set up) waits about 7 s behind the safety line** (general).
   Where: `src.html:376`, `888` (`await V.say(withSafety(['ready']), {wait: true})`), `1111`.
   How seen: voice log, fresh page, first tap on Throw with Bo: the safety line starts at 1.3 s, "Ready, aim..." at
   8.1 s; Bo stands still the whole time and the class waiting to shadow him hears a long rule first. How to set up as
   the first tap: safety at 1.3 s, the setup description not before about 6 s. BR1 lesson missed ("the first action
   never waits behind a line"). Better: start the action at once and let the safety line come after (or ride on the
   end of the run, as Show me already does with "Now you try!").

4. **The answer card is clipped at 680x425 and at 375 wide** (general).
   Where: `src.html:142` (`#answer`), `781` (answerH), `837` (`max-height`).
   How seen: Look step with Show the answer pressed (20 throws, tie, guess made). The card's content is 81 px tall in a
   73 px box at 680x425 (68 px at 375); the second line of the voiced tip ("get even better.") is cut at the bottom
   edge (frames `680x425_look20.png`, `375_look20.png`). Fine at 800x500 and up. Clipped text at a STANDARDS size.

5. **"Now you try!" does not name the control** (general).
   Where: `src.html:910` (nextCue, fifth cue). The spoken line is "Now you try!"; the hint says "Now you try! Press
   Throw with Bo to throw together." STANDARDS (Say how to act): the line and the hint name the next action and the
   control. How seen: voice log of six Next cue taps. The tool already has the full line (`tryBo`, spoken after Show
   me); speak that one here too (and `nowYou` can leave `allLines()` and lines.json if nothing else uses it).

##### Polish

6. **Coach says keeps a tip from a throw that was undone** (general). `src.html:1057` (freeUndo). Five throws above
   the target give "Too high..."; Undo takes the fifth away, the card still says "Too high..." about four throws.
   Better: on Undo past a multiple of five, put the card back to the tip for the last full five (or the starting
   "Throw five balls. Then look here."), the way `setThrow` already recomputes it.
7. **How to set up is not modal** (general). `src.html:246-247`, `1108-1118`. With the card open, the panel buttons
   still work: Show me runs Bo and speaks the cues under the card. Better: close the card on any panel or mode action
   (mode switch already does), or mark it `aria-modal` and keep Tab inside it.

##### Nit

8. **Cue lines and "Ready, aim..." are events in the code, how lines in the spec's Voice table** (general).
   `src.html:865, 888, 894, 911, 917`. The code is right for the class (Show me and Throw with Bo must say every cue on
   every run, and a tapped cue card should always speak), and it passes the repeat check that way; but Done when 6
   ("each how-to line once per load") reads wrong against the spec table. Update the spec's table (kind event) so the
   exit check doesn't trip on it.
9. **Short-box toggle labels clip a pixel or two** (general). At 680x425, 800x500 and 1000x625 the Under / Over /
   Right / Left labels are 16 px tall in a 14 px line box (`src.html:83`, line-height 1.05). Not visible in the
   frames; line-height 1.15 would clear it.

#### Checks that passed

- **Contract:** one file, 95 KB, no network requests (the only URL in the bundle is the SVG namespace), kit used
  (`Curio.voice`, `Curio.tone`, the kit's `Curio.audio()` context for the whoosh, `Curio.reduce`/`onMotion`), no
  console errors or exceptions in any run (about 110 shots). Nothing takes focus on load (`BODY`).
- **Hit tapping, pointer:** a full Test it run with real held clicks at 1366x768 (Step or stay?, guess Way A,
  10 taps in Way A including one Too short, Start Way B, 12 taps in Way B including one Too short and one Undo,
  Show the answer). I computed each tap's ring from the target box (center 503,461, R 238) before the run: Way A
  `G R B x x S R x G x` (5 hits), Way B `G R B x R S G R B x` (7 hits). The tool recorded exactly those, the panel
  ten-frame, the Look ten-frames (filled left to right, top row first, stars on the gold hits), the big numerals
  (5 hits / 7 hits), the bars (5/10, 7/10) and the SVG description all agree; "Way B got more hits!" and "That's
  different from our guess" are right (guess was A). Undo in Way B removed only the Way B throw.
- **Small target:** real clicks in Way B of Big or small?: gold = hit with a star, red and blue = misses, rings grey
  with "Only the gold counts"; panel says "Throw 3 of 10, Hits: 1" after the gold, red, blue taps.
- **Keyboard:** Tab reaches the target in a round and in Free throw; the arrow keys move a visible crosshair, Enter
  and Space throw at it (Free throw: 9 x ArrowUp gave a miss at ny -1.08, then hits at ny 0.36); Shift-Tab into the
  stage and Enter finished Way B and focus went to Show the answer. Visible focus ring on the stage and buttons.
  Keys 1 to 3 switch modes; Escape closes the setup card and returns focus.
- **Touch:** the stage listens to `click` with `touch-action: manipulation`, so a finger tap lands where it touches
  (same handler as the mouse path above).
- **Free throw coach (Done when 5):** 25 real taps 2 s apart: 5 above, 5 hits, 5 Too short, 5 to the side, then a
  mix gave "Too high. Let go lower...", "Great aiming!...", "Too short...", "Face the target, and point your hand...",
  "Keep going..." in that order, each spoken.
- **Lines:** `allLines()` returns 74 lines and `voice/lines.json` holds the same 74, word for word and in the same
  order. Every `V.say` uses a key or a value of the line table, so no spoken text is outside it. No em dashes in
  src.html, notes.md, tool.draft.json, prompts.json or lines.json; "Curio Class" never "Curio" alone.
- **Motion off:** the audit found nothing running forever; the Look bars are full on the first frame (frame
  `calmlook.png`), Bo jumps between poses, and the ball lands after the same 760 ms.
- **Saving and reset:** the tool stores nothing (only the kit's Motion choice), and the notes say so. Clear the wall
  empties the dots and the coach card and moves focus to Too short; Stop test and New question return to Ask with
  nothing kept; a mode switch resets Test it and keeps the Free throw dots, as the spec says.
- **Contrast** (recomputed): accent on paper 6.79, white on accent 7.38, ink on paper 14.45, muted on paper 6.43,
  red ring on white 4.85, blue ring on white 5.72, star on gold 8.14, gold button text 9.53, accent text on the wall
  6.05. Rings also differ by edge (dashed, solid, double).
- **Layout:** every state below at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x1000 and 375x812
  (my own iframe host page, served from my scratch folder): Form, Form left hand overhand, Ask, Guess (Close or far?
  with its tape-line note), Way A done, Way B with 20 throws and four Too shorts, Look with 20 throws and the answer,
  Free throw with 44 throws, the setup card. No sideways scroll, no overlapping controls, no hint clipped or below the
  fold, every control 60 px at 1280x720 and up (Done when 7), 48 px in the short boxes (the spec's Layout rule),
  stage and panel side by side at 1000x625. Only findings 2 and 4 above.

#### Standard voice check

Sound on, Motion on, held clicks, fresh page per run, `__tool.vlog` read after each.

| Line | Kind | Run | Expected | Spoken |
|---|---|---|---|---|
| Safety ("Soft balls only...") | how (welcome) | any first tap, then every run | 1 per load | 1 |
| wForm / wTest / wFree | how (welcome) | modes cycled twice, 4.5 s apart | 1 each | 1 each (wTest dropped by a fast switch the first time, spoken at the next entry) |
| Face the target. ... (cue card 3 tapped) | event (see nit 8) | cue card x5, 2.5 s apart | 5 | 5 |
| Next cue lines | event | Next cue x6, 3.5 s apart | 1 each, then wrap | 1 each, cue 1 again on the 6th |
| Now you try! | how | same | 1 | 1 |
| Ready, aim... | event | Throw with Bo x5, 11 s apart (alternate presses stop the run) | 1 per run started | 3 of 3 runs started |
| Great throwing! Press Throw with Bo... | event | same | 1 per finished run | 1 of 1 finished |
| Now you try! Press Throw with Bo... | how | Show me x2, 13 s apart | 1 | 1 (the first dropped by the second Show me, spoken after it) |
| Setup line | how | How to set up / Close x5 | 1 | 1, then silent (heard) |
| Question title + Way A/B lines | event | 3 rounds via Test again | 3 | 3 (2 dropped by my fast Skip the guess, as they should) |
| Make a guess! | how | same | 1 | 0, dropped each time by the fast Skip (never stale-spoken) |
| Way A! / Now Way B! (start) | how | 3 rounds | 1 each | 1 each, then silent |
| Way A: + way line (round start) | event | 3 rounds | 3 | 3 |
| Way A: No hits. Way A is done! | event | 3 rounds | 3 | 3 |
| Way A: / Way B: counts + "Which way got more hits?" | event | 3 rounds | 3 | 3 |
| It's a tie! Try more throws. | event | 3 rounds | 3 | 3 |
| Tip (step) | event | 3 rounds | 3 | 3 |
| Press Test again... | how | 3 rounds | 1 | 1, then silent |
| Coach lines | event | 25 Free throw taps, 2 s apart | 5 | 5, one per fifth throw, right rule each time |
| Single throws | none | every tap | 0 | 0 |

- **Stale lines:** Test it, a card, a guess, two Too shorts and Stop test 0.2 s apart: the round-start lines were
  dropped (`hush`) at Stop test and nothing from the round played after it. Show me, Next cue x2, Free throw, Too
  short, Form 0.2 s apart: each cue cut the one before, the Free throw welcome was dropped at the switch, Form's
  welcome played. A Way A result was dropped (`newer`) once Start Way B was pressed. No line named a hidden or
  disabled control (doneA needs Start Way B, look needs Show the answer, again needs Test again).
- **First-tap timing:** plain stage tap: the welcome (safety first) at about 0.1 s after the tap. Next cue: only its
  cue. Cue card: only its cue. Mode button: safety, then that mode's welcome. Read: the hint only. Sound: nothing;
  Sound off and on brought the skipped welcome once. A key (Tab): the welcome. Throw with Bo: safety first, then
  "Ready, aim..." 7 s later (finding 3).
- **Read:** during Show me, Read cut the cue and spoke the hint, and the run went on with the next cue; with Sound off,
  Read still spoke the hint; a mode change right after Read let the next line start at once.
- **Order:** every spoken line followed the order of its action in every log.

#### Audit pilot

`python scripts/audit_tool.py target-toss <scratch>/audit --port 9940` reported **0 leads** (every size clean,
Motion off clean, 19 one-click walks clean, the five-click checks clean). I confirmed what it covered: first screens
at all eight sizes, Motion off, focus on load and the Form controls' voice all hold on my own frames; none of its rows
was wrong.

It missed everything past one click from Form: focus dropped to the page on six Test it controls (finding 1), Start
Way B landing under Undo (2), the answer card clipped at 680x425 and 375 (4), the ten-frame counts against the taps,
and the 7 s wait in front of the first Throw with Bo (3; its walk logged that the safety line was spoken but does not
judge delay). Its target rule (44 px in the preview sizes) also differs from the BUILD lesson's wording (60 px for
K-2 at every size); this tool's spec allows 48 px in short boxes, so I did not file it, but the two texts should agree.

<!-- end part -->

<!-- part: refine/play.md -->

### target-toss: Play lens (round 1)

Played cold, mostly as a K-2 PE teacher running a block on a projector (tapping where each ball hit at about one tap a
second while the class waits), once as a non-reading K-2 child watching the screen. Draft bundle 95 KB. Real held
clicks over CDP (own runner on drive.py's Chrome, port 9972), frames at every STANDARDS size, 375 through
`drive.py --host` (port 9973; host.html deleted after). No console errors in any run.

Runs: (1) full Test it, "Close or far?", 10 + 10 real taps at 1 s, Look, Show the answer, voice log; (2) Free throw,
17 real taps at 1 s (5 above, 5 hits, 5 side, 2 Too short), then Clear; (3) Form: Show me, Throw with Bo, Overhand +
Left hand, Next cue x6 at 1 s, cue cards; (4) nine states (Ask, Guess far, Way A 20 throws, Way A done, Way B small
target, Look 20 answered, Look 5 answered, Free throw 43 throws, setup card) at 680x425, 800x500, 1000x625, 1280x720,
1366x768, 1920x1080, 760x900 and 375 host. Tap counts checked by hand: Way A 7 of 10, Way B 7 of 10, graph showed 7
and 7 (tie). Coach lines matched the rules (Too high, Great aiming, side tip).

#### Blockers

None.

#### Should fix

1. **Stop test and Clear the wall wipe everything with one tap, and sit right next to Undo.** (general)
   Where: `#t-stop` beside `#t-undo` in the Test round row (src.html:211-215, `stopTest` 1024); `#r-clear` beside
   `#r-undo` (src.html:226-230, `freeClear` 1058). Same size, same style, no confirm, no way back. Seen in frames
   t1-04, f-shorts; after Clear, Undo is disabled and 17 throws were gone (run 2). A teacher reaching for Undo after a
   stray tap, with 20 kids watching, can lose a whole Way A plus Way B (up to 40 throws) or a Free throw session. The
   mode buttons and keys 1 to 3 also reset a test in progress with no prompt. Better: make Stop test and Clear undoable
   (one "Undo clear" / "Bring it back" for a few seconds) or a two-tap confirm, and move them away from Undo (own row,
   quieter style).

2. **Start Way B appears exactly where Undo was.** (general; BR1 lesson "nothing rebuilds under the pointer", "panels
   don't jump")
   Where: `#t-startb` (src.html:210) is shown above the Too short / Undo / Stop row when Way A fills. At 1366x768 the
   row was at y 459-519 (probe); after throw 10, Start Way B occupies y 460-518 and the row drops to 528 (frame
   t1-05). The likeliest moment for an Undo is right after a mis-tapped last throw, and that tap now lands on Start Way
   B, which can't be undone back into Way A. Better: reserve the slot (Start Way B in its own fixed place, or the row
   above it), so nothing moves under the finger.

3. **No recovery from a mis-tapped last throw of Way B.** (general)
   Where: `roundThrow` (src.html:986-989) moves to Look 1.3 s after throw 10; Look has no Undo (`#tg-look`). At a
   1 tap/s pace the teacher sees the wrong dot after the screen has already changed (run 1, frame t1-08 then t1-09). The
   only fix is Stop test and redo both rounds. Better: keep an Undo (or "Back to Way B") on the Look step until Show
   the answer, or stay on Way B with a "See the results" button like Way A's Start Way B.

4. **Misses above the target are hidden under the Way banner in every Test round.** (general)
   Where: `#banner` (src.html:115, placed in `placeOverlays` 836) sits directly above the target, and `targetBox`
   leaves almost no wall above the rings in Test it. A tap at ny -1.18 and -1.25 (real taps, run 1; scripted in the
   size sweep) is counted as a miss in the ten-frame, but its dot is drawn under the banner and never seen, at all
   eight sizes (t1-05, roundA20-*). "Too high" is the most common K-2 miss and the teacher can't check the tap landed.
   Better: draw ball dots above the overlays, or move the banner off the throwing area (into the strip row or the
   panel) and leave a band of wall above the rings.

5. **Guess step has no way back.** (general)
   Where: `#tg-guess` (src.html:194-206). No Stop test or Back on the Guess step (frame t1-02, guessfar-*); the
   handoff says "Stop test is also shown on the Guess step", but it is not. A teacher who tapped the wrong question
   card has to know to press the Test it mode button again. Better: a "Back" / "Other question" button on the Guess step.

6. **"Now Way B! Same throwers, same line." is wrong for Close or far?** (general; words match the state)
   Where: `L.startB` (src.html:313), spoken in run 1 at the start of Way B for "Close or far?", where Way B is "Throw
   from the far line" (banner in frame t1-08 says so). It contradicts the screen and the fair-test idea. Better: a
   per-question line, or "Same throwers. Only one thing changes."

7. **The Free throw welcome says "Throw at the target!" while the screen shows only a big target.** (general; BASELINE
   w1-49)
   Where: `L.wFree` (src.html:301), also the Free throw hint (frame f-00-start). The setup is a paper target beside
   the screen and the safety tip says never throw at the screen; a K-2 child who hears "Throw at the target!" while
   looking at a huge projected target is told the opposite. Better: "Throw at the paper target! Then tap the screen
   where each ball hit." Check the other lines the same way (startA "Tap where each ball hits" is fine).

8. **The setup card leaves the hint (and Read) on the old step, and its steps fall below the fold in small boxes.**
   (general; BR1 lesson "the hint changes at once, Read speaks it")
   Where: `openSetup` (src.html:1108) never sets the hint; the setup line is `hint: false`. With the card open the
   hint still says "Let's learn to throw like Bo. Press Show me..." (setup-* frames), so Read speaks that, not the
   setup. At 680x425, 800x500, 375 and 760x900 the card scrolls and steps 3 and 4 ("Throw soft balls at the paper
   target", "Then tap the screen") are out of view (setup-a sheet); at 760x900 even the picture's labels are cut.
   Better: set the hint to the setup steps (and back on Close), and let the card use the whole page or a side layout
   so all four steps show.

#### Polish

1. **The way name comes last in a round intro.** (general) First run of a session: "Way A! Throw one at a time. Tap
   where each ball hits." then "Way A:" "Throw from the close line." took about 10 s (log 8.7 s to 19 s); for Way B the
   way name ("Throw from the far line.") was still playing at 32-35 s, after throw 8 of 10. Non-readers need the way
   before they throw. Better: speak "Way B: throw from the far line" first, then the how line.
2. **Throw with Bo has no time to do each move.** (general) Each cue starts as soon as the last one ends (log:
   cues 1.5 to 2.9 s apart; minimum beat 1400 ms, shorter than Show me's 1600). A class shadowing a throw needs a beat
   after hearing the cue. Better: a hold of about 1 s after each spoken cue in Throw with Bo (a real "slow beat").
3. **On a projector the score lives in a small side panel.** (general) In a round the stage shows only the target;
   "Throw 3 of 10" (19 px), "Hits: 3" (16 px muted) and a small ten-frame are in the 360 px panel, unchanged at
   1920x1080 (roundA20-1920x1080). The class at the back can't follow the count. Better: a large ten-frame or count
   on the stage (the floor strip has room), as Free throw does with its tally.
4. **Payoff text is small at 1920x1080.** (general) The answer card (`--afs` max 18 px) and Guess cards (way text
   about 20 px in 480 px cards, mostly empty) don't grow on a big screen (look20-1920x1080, t1-02). Better: let them
   scale with the stage like the "13 hits" numerals do.
5. **First coach line is lost at a 1 tap/s pace.** (general) Run 2: the coach line after throw 5 waited behind the
   safety line and welcome (about 10 s of speech) and was dropped when throw 6 came. The card shows it, so nothing is
   lost on screen. Better: let a coach line cut in ahead of a welcome, or shorten the opening lines.
6. **The "Close or far?" tip after Show the answer is a setup instruction.** (general, spec level) After the result
   the tip card says "Make two tape lines: three giant steps..." (t1-11), which belonged before the test. Better: a
   takeaway line ("Closer is easier. Step back when you are ready for a challenge."). This is in the spec's table, so
   it goes to the spec's open questions.

#### Nits

1. Guess Way A, result a tie: "That's different from our guess." A tie line ("It came out even!") would fit better.
2. After switching Overhand or Left hand, the hint still says "Great throwing! Press Throw with Bo to go again."
   (fm-over-left).
3. The crown stars on Look touch the bottom of the step strip at 1366x768 and 680x425 (t1-11, look20-a).
4. "Throw 0 of 10" at the start of a round reads oddly; "Throw 1 of 10" (next throw) or "0 throws" would be clearer.
5. ✋ Right hand and 🤚 Left hand icons look almost the same on a projector.
6. Setup picture: the dashed ball path runs through the "Paper target: throw here" label.

#### Feel

The Test it loop works and is satisfying: ten-frames filling, the purple and star dots, the big "7 hits" columns, the
crown. A 10-throw round at 1 tap/s took about 10 s of tapping and felt right; 20 throws with two ten-frames stays
readable at every size except a tight 375 Look. 5 throws feels short but is fine for a first test. Form is clear and
Bo reads well at every size. The slow and fragile moments are all around mis-taps: the teacher's recovery controls
(Undo) sit next to destructive ones, move under the finger, or vanish at the end of Way B. No step is boring on a
projector, but the opening speech is long (safety line plus welcome about 10 s before the first coach or round line).

#### Frames looked at

s-t1: t1-00 to t1-12 (default, Ask, Guess far, Way A start/5/done/done later, Way B start/done beat, Look, Look later,
answer, answer later). s-t2: f-00-start, f-above, f-hits, f-side, f-shorts, f-cleared. s-t3: fm-show-1, fm-show-3,
fm-show-end, fm-show-after, fm-bo-1, fm-bo-end, fm-over-left, fm-next6, fm-cue4. s-t4: ask, guessfar, roundA20, doneA,
wayBsmall, look20, look5, free, setup at all eight sizes (contact sheets in mont/). Audit frames: size-* and calm.
All in the scratch folder lens-tt-play.

#### Teaching lens comparison

(written after the findings above) Agree on "same line" (they rank it a blocker, I rank it should fix; their
fair-test framing is the stronger case, so I would accept blocker), the missing Back on Guess and the long guess
read-out; they add teaching items I did not look for (Way A always the coached way with 👍, same throwers, foot not
voiced, catching, setup ring sizes); I add the mis-tap recovery and projector items they did not cover.

#### Audit pilot

Confirmed: 0 leads, and its first-screen checks agree with my frames (no clipping, 60 px controls, no fold problem in
Form at any size, Motion off clean, Form controls speak right). Wrong leads: none.
Missed (all past one click): the banner hiding above-target misses, Start Way B appearing under Undo at the end of
Way A, no Undo after Way B's last throw, Stop test / Clear next to Undo, no Back on Guess, wrong "same line" line,
setup card hint/Read and cut-off steps, the first coach line lost at 1 tap/s, and the projector-scale issues.

<!-- end part -->

<!-- part: refine/teaching.md -->

### target-toss: Teaching lens (round 1)

Cold read of spec.md, src.html, notes.md, art/prompts.json, voice/lines.json, handoff.md; STANDARDS, BASELINE (w1-49),
BUILD BR1 lessons. Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py target-toss` (95 KB, clean). Frames and logs in
my scratch folder (lens-tt-teaching): r1/ (a full held-click Test it run), f/ (all ten Form poses, Left hand),
c/ (coach and Show me timing), audit/.

Counts: blockers 1 (general 0, family 1), should fix 5 (general 3, family 2), polish 6, nit 2.
(family = family:target-toss / throwing-lab format; the tool has no engine, so "family" here means "comes from this
tool's experiment format".)

#### Blocker

1. **"Same line" is wrong for the Close or far? card.** src.html:313 `startB` ("Now Way B! Same throwers, same line.")
   is spoken and set as the hint at the start of every Way B, including `far`, where the one thing that changes IS the
   line (Way B = "Throw from the far line"). At the exact moment the tool teaches the fair test it tells the class the
   variable stayed the same. Seen in code (startRound, src.html:968-973; testHint B = L.startB) and the Way B hint frame
   (r1/t5_B3.png shows the line on screen). Fix: a per-question start line, e.g. far: "Now Way B! Same throwers. Now
   use the far line." (and say the kept-same parts per card: step/look/size "same throwers, same line"; far "same
   throwers, same target"). Tag: family (fair-test format). The spec's own Voice table carries the error.

#### Should fix

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

#### Polish

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

#### Nit

13. Switching Throw after a coach line rewrites the advice for the throws already made (underhand "Too high. Let go
    lower..." becomes the overhand line at once; c/ "highU_after_switch"). Fine as advice for the next throws; maybe
    keep the text until the next five. Tag: family.
14. Overhand cue 5 "Follow through across your body." drops "toward the target" from the SHAPE element. Tag: general.

#### Standards (rule 2)

SHAPE.S1, underhand (S1.E13) and overhand (S1.E14): taught by Form (Bo's five poses, glow on the throwing arm and
stepping foot, Throw with Bo shadowing) and practised with real throws in Test it and Free throw, with outcome-based
coaching tied to the cues. All ten cues match the critical elements in the Sources (face, arm back, opposite-foot step,
release knee to waist, follow through to target; side to target, arm back, step, hip and shoulder rotation, follow
through across the body). Poses checked frame by frame (f/form sheet): underhand release at thigh height (computed: ball
at y 66 model units, hip 70, knee 36), overhand arm back with the elbow at shoulder height, the far (opposite) foot
steps and glows, Left hand mirrors and the tag reads "Step: RIGHT foot". Catching: finding 5.
The fair test (NGSS SEP 3, a source, not a module code) is really done by the class (guess, two rounds, compare), with
findings 1-3.

#### Done when

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

#### Giveaways

Nothing on the Look step crowns a side before Show the answer; tips appear only after it; the Guess cards have no
badge, order or length tell except finding 2 (position and thumbs). The counts on the graph are the class's own data,
which is the point.

#### Builder's spec deviations

1. w1-49 setup card and wall-target safety lines: accept; the gaps are finding 6.
2. Cue and `ready` lines as event lines: accept (a silent second demo would teach nothing).
3. Added `tryBo`, `boDone`, `again`: accept; all name a live control and are in lines.json.
4. Coach 7 lines, not 9: accept; the spec's table has 7.
5. Safety after the first Show me run: accept; no ball is thrown in Show me, and it plays before Throw with Bo,
   Test it or Free throw.
6. Stop test on Guess: not built (finding 12). Way B to Look after 1.3 s: accept.

#### Sensitivity

Nothing cultural, Native or hard-history. No sensitivity agent needed.

#### Audit pilot

- Confirmed: 0 leads, and my frames at 1366x768 agree (no clipping, 60 px controls, first-tap safety line, cue lines
  per tap). Wrong leads: none.
- Missed (outside what it can see): the "same line" error (1), the position/thumbs giveaway (2), the fair-test setup
  (3), unvoiced foot tag (4), module scope (5), setup gaps (6), the guess how-line dropped at a teacher's pace after a
  long read-out (11), and the handoff's unbuilt Stop on Guess (12), which needs a screen past one click.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### target-toss handoff

Built 2026-10-28 (Build stage). K-2 PE, teacher led on a projector, no family engine. Draft bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py target-toss`. Voice clips are not recorded yet (`scripts/voice.py target-toss`, bank bright-teacher / Autonoe); `voice/lines.json` holds all 86 lines (after polish round 2) and matches `__tool.allLines()`.

#### Layout of src.html

- Header: three mode buttons (Form, Test it, Free throw; keys 1 to 3), then Motion, Sound, Read.
- Panel (first in the DOM): `#hint`, then `#settings` (Throw: `#s-under`/`#s-over`; Hand: `#s-right`/`#s-left`), then one `.ctl` block per mode, then `.foot` (`#setup-btn` and the `#safety` tip).
  - Form: `#f-show`, `#f-next`, `#f-bo`.
  - Test it: `#tg-guess` (n-5/n-10/n-20, `#g-a`, `#g-b`, `#g-skip`, quiet `#g-back`), `#tg-round` (`#t-count`, `#t-hits`, `#t-frame`, row of `#t-short` / `#t-startb` (takes Too short's slot) / `#t-undo`, then quiet `#t-stop`), `#tg-look` (`#t-back`, `#t-answer`, `#t-again`, `#t-new`).
  - Free throw: `#r-short`, `#r-undo`, `#coach`, then quiet `#r-clear`.
- Stage: `#sv` SVG drawn at real pixel size (`lay()`); the Way banner is drawn in the SVG by `drawBanner` under the ball dots. HTML overlays: `#strip` (Test it steps), `#ask` (question cards), `#guess`, `#cues` (Form cue cards), `#answer`.
- Modals (body level, `.modal`, under the header): `#setup` (How to set up, six steps) and `#confirm` (Yes / No before throws are lost). `modalOn` makes main inert (and the header for confirm); `read` and the hint follow the open card.
- Layouts: `body.side` (default), `stack` (w < 760, or tall and under 1000 wide: controls, then settings, then foot), `short` (h < 640: tighter text, controls stay 60 px, icon above word on settings, `fitHint` steps a long hint down to 12.5 px), `narrow`/`narrowhead`/`tighthead` for the header. Under 480 px wide in stack, the settings also put the icon above the word.
- `window.__tool` exposes state, the voice log, lines, poses and the main actions for checks.

#### Tricky parts

- **Bo** is a small 3D skeleton (yaw plus arm and leg direction vectors in model units) projected side on. `POSES.under` / `POSES.over` have five poses each; `poseTo` tweens 420 ms (a jump with Motion off). Left hand mirrors the whole Bo group and swaps Bo and the target. Tags are measured with `textW` so they never overlap.
- **Show me / Throw with Bo** are async runs with a token (`f.tok`); pressing the same button stops them. Each cue is `setCue(i)` (highlight plus pose) and `V.say(cue, {now, wait})` in the same tick, with a minimum beat of 1600 ms (Show me) or 1400 ms (Bo).
- **Rounds:** `roundThrow` ends Way A by queuing [wayA, hits, doneA] (doneA needs `#t-startb`) and focusing Start Way B. Way B goes to Look after 1.3 s; Undo in that beat cancels it, and Look's `#t-back` (`lookBack`) returns to Way B. `roundUndo` in an empty Way B reopens Way A and pops its last throw.
- **Small target** (`size` question, Way B): `classify` counts only gold as a hit; the outer rings draw grey with "Only the gold counts".
- **Coach** runs on every fifth Free throw over the last five (spec order: hits, above, low, side, keep). `F.log` keeps {n, text}; a line is said with now and is valid for throws n to n+4; `coachCard()` rebuilds the card after an Undo, and a Throw switch never rewrites it.
- `#cues.tight` (number hidden, smaller icon) turns on when the cue card is under 84 px tall or the page is under 560 wide.

#### Deviations from the spec (for Refine to confirm)

1. **Baseline w1-49 applied** (answers the spec's Open question): the target is paper on the wall beside the screen. Added the **📋 How to set up** card and the voiced `setup` line; the safety tip and safety line now say "wall target" / "paper target on the wall beside the screen, never at the screen, a TV, a touch panel or the laptop".
2. Cue lines and `ready` are **event** lines, not how, so Show me and Throw with Bo speak them every run (a how line is spoken only once per load). `nowYou` stays how.
3. Added three lines: `tryBo` ("Now you try! Press Throw with Bo to throw together.", after Show me), `boDone` (after Throw with Bo), `again` (after Show the answer, names Test again and New question).
4. Coach has **7** lines, not the spec's "coach (9)": the spec's own Coach says table lists 7.
5. On the first tap of a mode, safety plays after a Show me run rather than before it, so the poses stay in step with the cues.
6. Stop test is also shown on the Guess step. Way B goes to Look on its own after 1.3 s.

#### Checks run (2026-10-28)

- Audit (`audit_tool.py`, port 9962): first run 2 leads ("Follow through" clipped at 680x425 and 375); fixed with `#cues.tight`; re-run **0 leads**. Motion off clean, held-click walk clean, five-click checks clean.
- Done when 1 to 9: all pass (details in the build report). Form cue state, highlight and spoken line change in the same tick for all five cues, Motion on and off. Test it held-click run: counts equal the recomputed taps (A 3, B 5). Small target: gold hit, red and blue miss in Way B. Free throw: "Too high" for both throws, "Great aiming!" at 3 of 5. No how line spoken twice, no throw tap speaks. Every visible control is at least 60 px with an icon at 1366x768 and 1280x720.
- Frames looked at: every audit size (680x425 to 1920x1080, 760x900, 375 host), the Form Left hand frame, the Way B small-target frame, the Look and answer frame, the 375 setup card, the 375 settings row.
- Fixed after the audit: at 375 wide, the selected border cut the "r" of "Under"; the settings now put the icon above the word under 480 px.

#### Open / next

- Record voice clips (`scripts/voice.py target-toss`).
- At a 2 s tap pace, a line still in the queue is dropped as 'newer' when the next control is pressed (for example `doneA` if Start Way B is pressed at once, or the Look counts if Show the answer is pressed while they play). That is the kit's cut-in rule; the count is always on screen.
- Refine list: not yet received.

#### Polish round 1

Checked by held clicks with scratch `seq.py` runs A to E at 1366x768 (voice log, focus, rects), then `drive.py` sweeps at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812 via `--host` (host.html deleted after): no control under 60 px, no horizontal scroll, no main control off screen, setup card does not scroll, answer card not clipped, 0 console errors (one favicon 404 from the host server). The only remaining flag is the guess cards' keycap emoji (3️⃣/6️⃣) line box, a false positive: the frames show them whole.

1. Fair-test lines per question: `startBstep/look/far/size` say what stays the same and the one change ("Same throwers, same order, same target. Only the line changes." on Close or far?); the far tip is now a result line ("Closer is easier to hit..."). Spec voice and question tables updated. Checked: run B (far) spoke wayB name then startBfar.
2. Coached way swapped to B on Where do you look? and Big or small? (`QS.exp`), vote signs are ☝️ one finger / ✌️ two fingers and the `guess` line says so. Checked: guess frames at every size, run B guess line.
3. Same throwers in the same order: `startA` ("Pick your throwers. Each one throws once, one at a time.") and every startB line; setup step 4; notes say the round size fits the same children throwing in both rounds. Checked: lines in the voice log, notes read.
4. Cue 3 now names the foot from Hand (`stepR` "Step with your left foot, the opposite foot." / `stepL`); the Coach says placeholder is voiced as `coach0` after wFree. Checked: run A Left hand cue 3 spoke stepL; run D voice log has coach0.
5. Setup card rebuilt as a body-level modal: three rings on the paper target, two big steps from the screen, ball pickup rule, six steps in view at every size (sized from the window); hint shows setupGo and Read reads the card. Checked: run E (setup spoken at once, hint setupGo, focus Close, main inert, Escape restores hint and focus); sweep setup frames incl. 680x425, 800x500, 760x900, 375 with `scardScroll` false.
6. Stop test and Clear the wall moved below, quiet dashed style, and ask Yes / No in `#confirm` (focus on No, Escape = No) when throws would be lost; mode buttons and keys 1 to 3 ask too. Checked: run C (No kept A=3, key 3 asked, Yes went to Free throw; Clear asked then focused Too short); confirm frames at every size.
7. Start Way B takes Too short's slot, Undo stays put and takes back Way A's 10th; Undo in an empty Way B reopens Way A. Checked: run B rects (Undo identical before and after the 10th throw), A=9 after Undo, A=9 after Undo in empty B; 375 adone frame shows Start Way B and Undo in view.
8. Look has "Undo last throw" (`#t-back`) back to Way B. Checked: run B, B went 10 to 9 and the round reopened.
9. Way banner drawn in the stage SVG under the dots (no HTML banner); misses above the target clamp below the step strip. Checked: run B above-dots frame and adone frames, every dot visible.
10. Guess step has "Other question" (`#g-back`) back to Ask. Checked: run B, Other question went to Ask with focus on the first question card.
11. Free throw welcome and hint: "Throw at the paper target! Then tap the screen where each ball hit." Checked: run C/D voice log and hint.
12. Focus moves on: question card to Way A, Way A to the stage, end of Way A to Start Way B, Stop test / New question to the first question card, Test again to Way A, Clear to Too short. Checked: run B and C focus readouts.
13. First Throw with Bo starts "Ready, aim..." at once and safety comes after boDone; first How to set up speaks setup at once with safety after. Checked: Bo run log (ready 1356 ms, five cues, boDone 20.0 s, safety 23.9 s); run E log.
14. Answer card measured when shown and placed before draw, so the tip never clips. Checked: sweep `answer` box inside the stage at every size incl. 680x425 (305 to 415) and 375.
15. Next cue's fifth says tryBo ("Now you try! Press Throw with Bo...", needs `#f-bo`); `nowYou` removed. Checked: run A hint after five Next cue taps.
16. `tipDiff` ("Our test came out different this time. Try more throws, then test again.") before the tip when the winner is not the coached way and not a tie. Checked: run B answer text, 1920x1080 look frame.
17. Look ten-frames fill hits first, then misses. Checked: look frames at every size.
18. notes.md "What to look for": K step with the opposite foot, grade 1 two cues, grade 2 all five and a start on overhand. Checked: read.
19. Overhand cue 2 card "Elbow up", line "Bring your arm way back, elbow up."; cue 5 "Follow through across your body, toward the target." Checked: lines.json and Form frames.
20. "Make a guess!" is queued right after the question title, before the Way names. Checked: run B voice log at teacher pace (guess spoken after the title).
21. Round intro says the Way name first, then the start line. Checked: run B voice log.
22. Throw with Bo beat is max(1000 ms after the line, 2200 ms a cue). Checked: Bo run, cues at 3.2, 5.9, 8.8, 12.9, 16.8 s.
23. Projector: floor tally in Test it too ("Hits n · Throw n of N", up to 38 px), question / way / answer type caps raised (34 / 27 / 24). Checked: 1920x1080 frames.
24. First coach line cuts in (now) and stays valid for five throws. Checked: run C and D at 1 tap/s, the first coach line was spoken.
25. Undo rebuilds the Coach card from the log (back to the placeholder when the throw is gone); a Throw switch never rewrites it. Checked: run C coach text after two Undos and after Over / Under switches.
26. How to set up is modal: main is inert, Show me cannot run under it, Escape closes. Checked: run E.
27. Short-box toggle labels line-height 1.15, no clip. Checked: sweep 680x425 / 800x500 frames and the clip check.
28. Spec voice table now lists cue lines, stepR/stepL, ready and boDone as events, plus every new and changed line. Checked: lines.json equals `__tool.allLines()` (84 lines, compared after the last edit).
- Settled: 60 px at every size (`body.short{--ctl:48px}` removed); sweep shows no control under 60 px at any size, 375 included. A long hint in short boxes now steps its font down (`fitHint`) so it never runs under the settings (seen at 680x425 to 1000x625, fixed and rechecked).
- Settled: catching. Spec "Who and how" and notes say the module is Throwing and Catching and catching is a later K-2 tool's job.
- Spec "Open questions" left as is. Bundle rebuilt with `CURIO_DRAFT=1`; voice clips still not recorded (lines changed).

#### Polish round 2

From the exit check, round 1. Checked by held clicks (scratch `seq.py` runs F, G1 to G3 at 1366x768) and `drive.py` sweeps at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812 via `--host` (host.html deleted after), fresh Chrome profiles, 9 states each incl. Look with the answer: no control under 60 px, no horizontal scroll, every main control in view (now also Skip the guess, Other question, Undo last throw, Test again, New question), answer card whole, 0 console errors (one favicon 404 from the host server).

- N1: `testAtRisk` covers every Test it step that holds throws (Look before and after the answer). Checked: run F, Form on Look asked Yes / No (No kept 10 and 10), key 3 after the answer asked; Guess with no throws switched with no card.
- N2: Yes on a mode switch focuses the new mode's first control (`firstCtl`: Show me, the first question card, Too short). Checked: run F, focus r-short after key 3 then Yes, f-show after Form then Yes; Stop test Yes still focuses the first card.
- N3: the safety line plays whole. A tool-level wrapper on `V.say` / `V.how` / `V.hush` / `V.welcome` (no kit change): a `now` line that arrives while safety plays or waits clears the rest of the queue but waits behind safety; a hush that cuts it (mode switch, Yes / No card) sets a flag and the next line that is not a Yes / No question says it again first. Checked: G1 (Test it, card at 2.1 s: safety 1.3 s, the card's title at 9.1 s, after safety ended), G2 (Hand first tap: safety, then the hand line, the Next cue line after), G3 (safety cut by the Yes / No card at 3.2 s, said again at 3.9 s after Yes, then wForm).
- P1: Skip the guess and Other question share a row; short boxes tighten the Guess gaps. Checked: both in view at 680x425 and 800x500 (sweep inview, 680x425 guess frame).
- P2: in the stacked layout the stage grows on Look (min(w x 1.1, h x .55)), with a relayout on entering or leaving Look. Checked: 375 Look cells 29 px at 20 throws (were about 10), Test again and New question still in view (bottom 794 of 812).
- P3: Hand tap says both tags (`handR` / `handL`), after safety on a first tap, never cutting a Show me cue. Checked: G2 log; lines.json now 86 lines and equal to `__tool.allLines()`.
- P4: winner box sized to its column (ten-frames, count and bar) and the column cap raised to 560 px, so ten-frames grow on a projector. Checked: 1920x1080 answer frame, cells 104 px (were 78), box ends under the bar.
- Spec updated (Voice table: handR / handL and the safety rule; Yes / No covers Look and focus after Yes; Guess row; Look stage). Bundle rebuilt with `CURIO_DRAFT=1` (108 KB). Voice clips still not recorded.

<!-- end part -->

## Log

- 2026-11-25: refine.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/craft.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/play.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-10-28)
- 2026-11-25: handoff.md folded in (last changed 2026-10-28)

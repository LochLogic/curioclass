OPEN (round 1, Claude Refine 2026-11-05; Codex fixes next)
Counts: blockers 2 (general 0, family 2), should fix 10 (general 8, family 2), polish accepted 8

# Refine: traffic-light-coder

Lenses: `refine/teaching.md`, `refine/play.md`, `refine/craft.md` (no sensitivity file; none needed, see Settled calls).
Lens scratch: `S:/CurioClass-codex-scratch/traffic-light-coder/` (teaching/, play/, craft/, audit-r1/).
Integrator spot-checks: src.html:796, 818-848, 1210-1224 and 1284-1300 read; `play/out/job5-y10-at43.png` opened
(44.0 s, light YELLOW, ambulance stopped in the queue behind the yellow car, detector on). Both blockers confirmed.

## Blocker
1. **Job 5 "Ambulance never stopped" lies under a long yellow.** src.html:796
   (`if (j === 4 && w.t === 43) w.ambulanceStopped = w.light === 'RED';`), shown at src.html:1216. The check only asks
   "is the light RED at 43.0 s". Change job 5's rule 2 to "If YELLOW and been 10 s then turn RED" (one chip): yellow runs
   38.5 to 48.5, the driver model stops the ambulance (more than 2 s from the line on yellow) from 42.5 s to past 50 s,
   yet every check is green, "Job complete", and the stat says "Never stopped". "been 30 s" on rule 2 and "If YELLOW and
   ambulance coming then keep lights" pass the same way; none needs rule order, which is what job 5 teaches. The same
   10 s yellow also passes job 4. Seen: `play/out/job5-y10-at43.png`, `play/out/job5-y10-report.png`, teaching
   `sim-out.json` j5_yel10 and `amb-out.json` yel10. Fixed: set `ambulanceStopped` from the ambulance car's own
   `stopped` flag on any beat while it is on the street (`ambulanceAt` to `ambulanceUntil` and until it clears the
   crossing), not from the light at 43. Re-run the spec's job 5 worked checks (unfixed: "Had to stop"; top rule: passes)
   and the three cheap programs above (all must now fail with "Had to stop"). Keep the arrival-cause line working.
   (family:robot)
2. **Job 3 passes with the light stuck on red.** src.html:642 (job 3 start) and src.html:822-834 (job 3 checks only
   "Nothing unsafe" and "Every walker crossed"). The brief says the light turns green too soon; the natural grade 3 move,
   deleting rule 4, gives "Job complete", "Every goal is met. Job finished." and Next job, while the same report shows
   "Longest red: 81.5 s" and "Cars waited 10 s or more". Play's brute force (`play/bf.json`) found 82 single edits that
   pass job 3, most broken: delete rule 4, "keep lights", "turn RED" or "turn GREEN" on the wrong light, an ambulance
   condition that never fits, and "If RED then turn YELLOW" (red to yellow, longest red 1 s). Five such passes also earn
   the finale. Seen: `play/out/job3-delete-r4.png`. Fixed: give job 3 one more goal check, in the report's plain words,
   that the cars get their green back after each walk (for example "Cars get a green again": every red ends in GREEN
   and the longest red is under 45 s, reusing the job 4 limit and its "the tool's own limit" label). Then re-run the
   single-edit brute force for job 3: only "walk is done" style fixes may pass, the listed fix ("been 10 s" to "walk is
   done") still passes, and the starting rules still fail with three "Green while crossing". Add one line to notes.md
   saying job 3 now has this check. (family:robot)

## Should fix
3. **Each job's problem is spoken only, never on screen.** Street Jobs job card (src.html:939-942) and `waitingHint()`
   (src.html:873-877). The brief ("Walkers press the button, but the light never changes...", "The light turns green
   too soon...") is the only place the student learns what is wrong; the card shows title and goal, and the hint (which
   Read speaks) is the same generic line for all five jobs. Sound off, a first tap that hushes the brief (it starts at
   8.1 s on a fresh page) or a second visit loses it (BASELINE rule 16). Seen: `audit-r1/state-mode-street-jobs-1366x768.png`,
   Play's flow-jobs log. Fixed: one plain problem line per job on the job card (the brief's first sentence, without the
   fix), and the job's next step in the waiting hint so Read brings it back. Do not state the fix. (general)
4. **The order line blames a rule that did not change the light.** src.html:1219. In job 4 with rule 4 changed but left
   below rule 3 the report says "Rule 3 changed the light first. Rules are checked from the top."; rule 3 starts WALK,
   it does not change the car light, so a student looks at the wrong card. In job 5's starting report the same words
   ("changed the light first") suggest a contest when only one rule existed. Seen: `play/out/job4-order.png`, teaching
   sim `j4_r4below`. Fixed: use the spec's own wording, "Rule N fired first. Rules are checked from the top." (spec
   worked check, job 5), and for job 4 name what it did ("Rule 3 fit first and started WALK."). (family:robot)
5. **Rush Hour's missed-fairness report names no rule.** src.html:839-844 and 1218-1220: the order note only shows when
   rule 4 already has "been 10 s". With only "been 30 s" added (the natural first try) the report shows "Reds under
   45 s" failed and "Longest red: 63 s" and nothing else; the cause (rule 3 starting WALK again and again) is only in
   the ribbon chips. A solo student (rule 4) is stuck. Seen: teaching `sim-out.json` j4_30only. Fixed: when "Reds under
   45 s" (or "Greens at least 30 s") fails, add one line naming the rule that fired most during the longest red, in the
   "Rule N did it" pattern ("Rule 3 started WALK 4 times while cars waited 63 s."). Leave the walker spacing alone; that
   is the spec's open question. (family:robot)
6. **At 760x900 the rule list and Add rule start below the fold.** src.html:393-411 and 473-487, stacked layout. In
   Street Jobs the rules begin about y 690 and Add rule is off screen, so the student scrolls between Run test and the
   rules every round; report and replay push them further. Seen: `audit-r1/state-mode-street-jobs-760x900.png`,
   `audit-r1/state-job-report-760x900.png`. Fixed: at 760x900 keep stage and panel side by side with the compact panel
   (as the short-landscape layout does), or shrink the stage so the first rules and Add rule are visible without page
   scroll. 375 wide in the host stays a stacked page (allowed). (general)
7. **The chip picker hides the rule it edits.** `#picker`, src.html:275-295 and 1293-1300. At 1366x768 the dialog covers
   the left of the rule list; at 680x425 every rule. The slot tabs read only "If light / and... / and... / then...", so
   the student edits one slot of a sentence they can no longer see. Seen: `audit-r1/state-chip-picker-1366x768.png`,
   `craft/v2/picker-680.png`, `audit-r1/state-all-condition-choices-1366x768.png`. Fixed: show the live rule sentence
   at the top of the picker, and put the current value in each tab ("If GREEN", "and button pressed", "and +", "then
   turn YELLOW"). (general)
8. **PUSH TO WALK buttons cover the crosswalk and stopped cars at small sizes.** src.html:155-163 (60 px buttons). At
   680x425 and 375 wide the street is about 100 px tall: the south button sits on the crosswalk and hides the east-lane
   car stopped at the red and its signal dot, the north one covers the west stop line. Seen: `audit-r1/size-680x425.png`,
   `craft/v2/red-stop-680.png` and `craft/v2/zoom-red-680.png`, `audit-r1/size-375x812 (iframe host).png`. Fixed: put
   the buttons on the sidewalks clear of the crosswalk and stop lines (or draw them smaller with the street while the
   hit area stays 44 px or more). 1366x768 is fine; keep it. (general)
9. **The goal card uses symbols and "model limit".** src.html:940-942: "Model limits: green ≥ 30 s; red < 45 s; walker
   wait < 60 s." Grade 3 meets ≥ nowhere else, and the report already says it in words. The spec requires these to be
   labeled as the tool's own limits, so keep that, in plain words: "Fair-time rules (this tool's own): greens at least
   30 s, reds under 45 s, walkers wait under 60 s." Same for job 1. Also rename the job 4 stat "Longest empty red" to
   plain words ("Cars stopped with nobody crossing: N s"), here and in the Empty crosswalk stat. Seen:
   `audit-r1/state-mode-street-jobs-1366x768.png`, `audit-r1/state-rush-hour-1366x768.png`. (general)
10. **The chip line says "Press Add rule" right after Add rule, behind a modal.** src.html:1288-1290 with 1443-1455.
    The first thing heard after pressing Add rule is "...Press Add rule to write a new one.", spoken while the picker
    is open and Add rule is inert behind the backdrop (STANDARDS: no line names a control that is off). Seen:
    `craft/v1` v-add-first log; audit "one held click" row 10. Fixed: the picker's how line names what is in front of
    the student ("Pick a chip, then press Done."); keep the Add rule half for the hint after Done. Update `L`,
    `voice/lines.json` and the spec-matching line table together. (general)
11. **A talk question teaches the wrong rule.** notes.md:51 "Why can a rule at the bottom never get a turn even when its
    condition fits?" is false: job 1's fix passes with the new rule at the bottom (teaching sim `fix1bot`). Fixed: "Why
    can a rule lower down lose its turn even when its condition fits?" (general)
12. **Notes overclaim the standards.** notes.md:77 says the three codes are "practiced directly". All three grade 3
    codes name a combination of sequence, events, iteration and selection; the student authors selection and uses
    events, but never writes the loop (the engine's fixed half-second check) and sequence only emerges from rules.
    Fixed now, inside the spec: notes say honestly which part each code gets here; the panel foot and Step name the
    loop where the student already sees it ("Every half second the light goes once round the loop: check from rule 1.")
    and the job 1 and 2 notes frame the fix as building the GREEN, YELLOW, RED, WALK sequence out of rules. Whether a
    code should move or be shared goes to the spec's open questions below. (general)

## Polish accepted
13. **Mark the finale on screen.** After all five jobs, the last report looks like every other; only the spoken line
    (needs Sound) says it is done. Add a small "All five jobs done" line with the five filled dots on that report. No
    stars, no score. Seen: `play/out/alljobs.png`. (general)
14. **Two ↻ icons at 680x425.** "Default rules" shrinks to a bare ↻ next to "↻ Reset street"; one keeps the program,
    one throws it away. Use a different icon or the short word "Defaults". Seen: `audit-r1/size-680x425.png`. (general)
15. **Watch the Street: one thing to try.** After the first full cycle the hint names one change to try ("Change rule 1
    to turn RED, then press a walk button. What does the street say?"). Hint only, not spoken again. Seen:
    `play/out/watch-walk.png`, `play/out/watch-flash.png`. (general)
16. **Bigger rule text at 1366x768.** src.html:218-221: rule-line 12 px, words and chips 11 px, cards a third empty. Use
    14 px chips and words at 1280x720 and up. Re-check six rules still fit with the allowed inner scroll. Seen:
    `audit-r1/size-1366x768.png`. (general)
17. **Picker option dots in lamp colors.** src.html:1307-1310: GREEN, YELLOW, RED and the three "turn" actions share a
    plain black dot. Color the dot by lamp (the word stays), and give the "turn" actions a small arrow. Seen:
    `audit-r1/state-chip-picker-1366x768.png`. (general)
18. **Announce the report when a played test ends.** src.html:595 and 1147-1160: no focus move, `#hint` not live, the
    report has `role="dialog"` but is not modal. Focus the report heading (preventScroll) on every finish, and drop
    `role="dialog"` (or make it behave like one). (general)
19. **Grey tab on the job card.** `.job-card::before` (src.html:195) reads as a dead drag handle in every Street Jobs
    frame and pokes above the report card at 680x425. Remove it or keep it inside the card. Seen:
    `play/out/grey-bar.png`, `audit-r1/state-job-report-680x425.png`. (general)
20. **Ribbon dots by color only.** src.html:1101-1103. Add a letter (G, Y, R, W) on each fired-rule dot so the light
    each rule set does not rest on color alone. (general)

## Settled calls
- Blocker 1 is fixed inside the spec (its goal says the ambulance never stops; the readout must follow the ambulance).
  A new "Yellow too long" unsafe kind (MUTCD 4D.26, 6 s maximum, already in the spec's sources) adds a fourth unsafe
  kind to a list the spec fixes at three, so it goes to the open questions, not to Codex this round.
- Blocker 2 adds one goal check to job 3. Taken as a fix, not a spec change: the job's brief and its listed fix only
  make sense if the light still turns green, and the check reuses wording and a limit the spec already has. It is
  also raised below so Cory can confirm the job table row.
- Picker (should fix 7): Play tagged it family:robot polish, Craft general should fix. Settled as should fix, general:
  the picker is this tool's own dialog, and hiding the sentence being edited is a flaw a student meets every edit.
- Push buttons (should fix 8): Play said polish, Craft should fix with the stopped car hidden. Settled as should fix.
- Order line (should fix 4) and goal card words (should fix 9): Teaching said polish, Play should fix. Settled as
  should fix; both send a grade 3 reader the wrong way.
- Do not change: job 4's two-change fix and walker spacing (open question); the 375 wide stacked page; the six-rule
  inner scroll; the welcome being skipped after a first tap on a rule card, push button or Send walker (rule 16, the
  premise stays in the panel foot); the "Green while crossing" collision moment (a strong moment, keep it).
- Not a Curiosity; no sensitive topic, nothing cultural or hard-history, so no sensitivity agent. The three walker
  pictures still need Cory's people review (BASELINE rule 11); that is not a Refine item.
- Contract is clean (443 KB, no network, no console errors, kit used, voice table matches lines.json, no em dashes).

## To the spec's open questions
- Add a "Yellow too long" unsafe kind (over 6 s, MUTCD 4D.26) so a long yellow is named with its rule in every job?
- Job 3 now checks that cars get their green back (blocker 2). Confirm the job table row: "safe; all cross; cars get a
  green again".
- Standards: the student never writes the loop or a sequence directly. Keep E3-ALG-PS-01 and E3-PRO-PD-04 here with the
  honest notes from should fix 12, or share them with a grade 3 sibling where the student authors the loop?

## Not taken
- Dead "Six rules is the most" line (Craft nit 9): it is in the spec's line table; harmless; settle at the voice step.
- Reset street hushes the welcome and drops the queued press line (Craft nit 10): the hint still shows the step.
- Seeded Watch traffic mostly blue cars (Play nit 13): random kit draw, cosmetic, no student cost.
- Job 5 starting report wording as its own item (Teaching nit 7): folded into should fix 4.

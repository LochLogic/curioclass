# Play lens: traffic-light-coder (round 1)

Played twice: as a grade 3 student alone at home (Watch the Street first, then Street Jobs one to five), and as a
teacher projecting at 1366x768. Frames are in `S:/CurioClass-codex-scratch/traffic-light-coder/play/out/` (mine) and
`S:/CurioClass-codex-scratch/traffic-light-coder/audit-r1/` (the shared audit). I also tried every job the cheap way:
a brute force over every single edit of each job's starting rules (every chip change, every delete, every swap, and
one added rule of any shape at any position: 1819 to 2281 programs per job) through `__tool.simulate`, saved in
`play/bf.json`.

Counts: blocker 2, should fix 4, polish 5, nit 2.

## Blockers

1. **Job 3 passes with the light stuck on red: delete the "turn GREEN" rule and the job is "complete".**
   Where: Street Jobs, job 3 (src.html:643 starting rules; src.html:822-834 goal checks: job 3 checks only "Nothing
   unsafe" and "Every walker crossed"). What: the brief says "The light turns green too soon. Find the rule that does
   it." The most natural kid move is to delete that rule. The report then says "Job complete", the voice says "Every
   goal is met. Job finished.", and Next job appears, while the same report shows "Longest red: 81.5 s" and "Cars
   waited 10 s or more" (the car-light bar is one long RED). The brute force found 82 single edits that pass job 3;
   most are broken programs: delete rule 4, change it to "keep lights", "If RED and been 10 s then turn RED", "If
   GREEN and been 10 s then turn GREEN", "If RED and ambulance coming then turn GREEN" (all leave the light red to the
   end), and "If RED then turn YELLOW" (red to yellow, longest red 1 s). Five such passes in a row also earn the
   finale "Maple Street is safe and fair". How seen: `play/out/job3-delete-r4.png` (real clicks Run test, Skip to
   report on job 3 with rule 4 removed), bf.json job 3. Fix direction: job 3 needs a check that the cars get their
   green back (for example "Cars get a green again" or the "Reds under 45 s" check jobs 4 uses), so the only passes
   are "walk is done" fixes. Tag: family:robot (the job table's goal checks).

2. **Job 5 "Ambulance never stopped" lies: a long yellow stops the ambulance on the street and the report still
   passes.** Where: Street Jobs, job 5 (src.html:796 `ambulanceStopped = w.light === 'RED'` at t = 43 only). What:
   change rule 2 to "If YELLOW and been 10 s then turn RED" (one chip). Yellow then runs 38.5 to 48.5; the ambulance
   reaches its stop line at 42 and sits STOPPED from 42.5 to past 50 (the driver model stops any car more than 2 s
   from the line on yellow), yet at 43 the light is YELLOW, so the report says "Ambulance never stopped", "Job
   complete", and every check is green. "been 30 s" on rule 2 passes the same way with a 30 s yellow, and so do
   "If YELLOW and ambulance coming then keep lights" programs (yellow held 7.5 s). None of these needs rule order,
   which is what job 5 teaches, and a 10 or 30 s yellow is never called unsafe even though the spec's own source
   (MUTCD 4D.26) puts a yellow at 3 to 6 s. How seen: `play/out/job5-y10-at43.png` (street at 44.0 s: YELLOW, the
   ambulance stopped behind the queue, detector line on), `play/out/job5-y10-report` result text (all checks pass,
   "Never stopped"), and the simulated history in the drive log (`42.5 YELLOW amb x=0.275 STOPPED` ... `50 RED
   STOPPED`). Fix direction: set "Had to stop" from the ambulance's own stopped flag at any time while it is on the
   street, and add a "Yellow too long" unsafe kind over 6 s (sourced). Tag: family:robot.

## Should fix

3. **The job's problem is spoken only, never on screen; Read cannot bring it back.** Where: Street Jobs job card
   (src.html:939-942) and `waitingHint()` (src.html:875). What: the brief ("Walkers press the button, but the light
   never changes. Press Add rule and write the rule that starts it.", "Fix rule one, and add a rule for yellow", "The
   light turns green too soon") is the only place a student learns what is wrong. The card shows only the title and
   goal; the hint is the generic "Tap a rule to change its chips, or press Add rule. Then press Run test." for all
   five jobs, and Read speaks that hint. A student with Sound off, a first tap that cuts the brief, or a second visit
   to the job never sees it (on a fresh page the brief only starts at 8.1 s, after the 6.7 s welcome:
   flow-jobs log). BASELINE rule 16: what the welcome says must stay reachable in the hint or by Read. Better: one
   plain line on the job card ("Walkers press, but the light never changes.") and the job's next step in the hint.
   How seen: `audit-r1/state-mode-street-jobs-1366x768.png`, Read row in the audit table, my flow-jobs log. Tag:
   general.

4. **Job 4's order note blames a rule that does not change the light.** Where: report, src.html:1219. What: job 4
   with rule 4 changed but left below rule 3 says "Rule 3 changed the light first. Rules are checked from the top."
   Rule 3 is "start WALK"; it did not change the car light, it fired first and kept rule 4 from getting a turn. A
   grade 3 reader looking at rule 3 sees no light change and is lost. Use the spec's words ("Rule 3 fired first").
   How seen: job4-order run (report text in the drive log, `play/out/job4-order.png`). Tag: family:robot.

5. **At 760x900 the rule list and Add rule start below the fold.** Where: stacked layout under about 1000 px wide.
   What: in Street Jobs the rules begin at y 690 and Add rule is far below; the student scrolls between Run test and
   the rules every round (STANDARDS: main controls visible without scrolling at every size). Report and replay at the
   same size push them further (audit "choices cut short" leads). How seen:
   `audit-r1/state-mode-street-jobs-760x900.png`, `audit-r1/state-job-report-760x900.png`. Tag: general.

6. **Grade 3 goal card uses symbols and jargon.** Where: src.html:940-942. What: "Model limit: walker wait < 60 s." and
   "Model limits: green ≥ 30 s; red < 45 s; walker wait < 60 s." A grade 3 student meets ≥ nowhere else and "model
   limit" means nothing to them; the report's own check labels are already plain ("Walker waits under 60 s", "Greens
   at least 30 s"). Use those words on the card too ("Fair rules for this job: ..."). Report stat "Longest empty red"
   is the same problem (say "Cars stopped with nobody crossing"). How seen:
   `audit-r1/state-mode-street-jobs-1366x768.png`, `audit-r1/state-rush-hour-1366x768.png`. Tag: general.

## Polish

7. **The chip picker hides the rule it edits and the street.** Where: `#picker` dialog. What: the modal covers the
   rule card and its slot tabs only say "If light / and... / and... / then...", so while choosing a student cannot see
   the sentence they are building, and in Watch the Street ("Changes count at the next check") the street they are
   meant to watch is behind the dialog. Better: show the live rule sentence at the top of the picker and put the
   current value in each tab ("and button pressed"). How seen: `audit-r1/state-all-condition-choices-1366x768.png`.
   Tag: family:robot.

8. **The finale is flat.** Where: job 5 pass after all five. What: the last report looks like every other report;
   the job dots are under it and nothing on screen says all five jobs are done (only the spoken line, which needs
   Sound). Better: a small "All five jobs done" line on the report with the five filled dots, still with no stars.
   How seen: `play/out/alljobs.png`. Tag: general.

9. **At 680x425 the south PUSH TO WALK button sits on the crosswalk.** Where: Watch the Street, compact layout. What:
   the 60 px button covers the lower half of the crosswalk and the near stop line, exactly where walkers step out.
   Better: keep the buttons on the sidewalks or beside the crosswalk at small sizes. How seen:
   `audit-r1/size-680x425.png`. Tag: general.

10. **Two ↻ icons mean different things at 680x425.** Where: Watch the Street, compact panel. What: "Default rules"
    shrinks to a bare ↻ next to the "↻ Reset street" button; one keeps the program, one throws it away. Better: a
    different icon or the short word "Defaults". How seen: `audit-r1/size-680x425.png`. Tag: general.

11. **Watch the Street has nothing to try once the light cycles.** Where: Watch the Street. What: after one press the
    default program cycles and there is no suggestion of what to break or change; the unsafe kinds only show if the
    student happens to edit a chip. Better: the hint, after the first full cycle, names one thing to try ("Change
    rule 1 to turn RED and press the button. What does the street say?"). How seen: `play/out/watch-walk.png`,
    `play/out/watch-flash.png`, `play/out/watch-unsafe.png`. Tag: general.

## Nits

12. A short grey bar sits on the top edge of the job card in every Street Jobs frame (inside `#job-card`, it reads as
    a drag handle that does nothing). `audit-r1/state-mode-street-jobs-1366x768.png`. Tag: general.
13. The seeded Watch traffic is mostly blue cars (three of three in `play/out/watch-ambulance.png`, four of six in
    `watch-walk.png`); the five-car kit rarely shows. Tag: general.

## Checked and fine

Default screen and every mode at all sizes (audit clean rows), Watch press cycle YELLOW, RED, WALK 7 s, FINISH 10 s,
GREEN with the ribbon in step (`watch-walk.png`, `watch-flash.png`), unsafe flash and Watch out line
(`watch-unsafe.png`), replay pause on the named rule (`audit-r1/state-replay-1366x768.png`), job 1, 2 and 4 have no
single-edit pass (job 2 and 4 need the spec's two changes), job 5's rule-order failure and "Two rules fit at once"
line, Motion off (audit clean), voice order on a fresh Street Jobs page (welcome, brief, result: no stale lines).

## Audit pilot

- Leads confirmed: 760x900 rules below the fold / cut by the panel in Street Jobs, report and replay (finding 5);
  375x812 controls below the fold are the expected stacked layout inside the host (not reported).
- Leads wrong or not worth a finding: "welcome not heard" after a first tap on a rule card, push button or Send walker
  in Watch the Street: rule 16 allows it and the premise stays on screen in the panel foot ("Every half second, check
  from rule 1. Only the first rule that fits gets a turn."). Six rules at 1366x768 with one card scrolled is the
  spec's allowed inner scroll.
- Missed by the audit: both blockers (cheap passes and a lying ambulance check need the job logic run with wrong
  programs), the spoken-only job briefs (the audit saw Read speak the generic hint but cannot judge that the brief is
  lost), the wrong rule wording in job 4's order note, the button over the crosswalk at 680x425, and the flat finale.

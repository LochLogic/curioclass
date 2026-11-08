# Teaching lens, round 1: traffic-light-coder

Cold read of spec.md, src.html, notes.md, voice lines in src, audit-r1. Checks run with `scripts/drive.py` on port 9831
through the page's own `__tool.simulate` (the same `when`, `execute`, `tickWorld` and `summarize` the live tool uses):
every job's starting rules, every listed fix, job 4's three variants, job 5 top and bottom, plus cheap-pass attempts.
Scratch: `S:/CurioClass-codex-scratch/traffic-light-coder/teaching/` (sim-out.json, amb-out.json, frames/).

## Findings

### 1. Job 5 passes with a 10 s yellow, and the report says "Never stopped" while the ambulance sits stopped (blocker, family:robot)
- Where: src.html:796 (`if (j === 4 && w.t === 43) w.ambulanceStopped = w.light === 'RED';`), src.html:713-716 (no
  upper limit on yellow), src.html:1216 ("Never stopped").
- What: the ambulance check only asks "is the light RED at 43.0 s". Change job 5's rule 2 from "been 3 s" to "been
  10 s" (no ambulance rule at all): YELLOW 38.5 to 48.5, every goal check passes, "Job complete", and the Ambulance
  stat reads "Never stopped". On the street the ambulance is stopped behind a queued car from 42.5 s to past 50 s
  (x = 0.275, `stopped` true each beat): the driver model stops cars more than 2 s from the line on yellow. The
  readout lies, and the job's whole lesson (an ambulance rule placed at the top wins) is skipped by a cheap tweak a
  grade 3 student will find by sweeping chips. The same 10 s yellow also passes job 4 (j4_yel in sim-out.json).
- Also: the spec's own source (MUTCD 4D.26) gives a 6 s maximum yellow, but the tool never flags a long yellow.
- Better: decide "Had to stop" from the ambulance itself (any beat with the ambulance `stopped` while
  `ambulanceUntil` is live), and add a "Yellow too long" unsafe kind (over 6 s, MUTCD 4D.26) so a long yellow is
  reported with its rule. Re-run the job 5 worked checks after.
- Seen: sim-out.json `j5_yel10` (passed true, amb false); amb-out.json `yel10` trace.

### 2. Two of the three codes ask for sequence and iteration the student never writes (should fix, general)
- Where: module codes E3-ALG-PS-01, E3-PRO-PD-04, E3-PRO-TR-08; notes.md:77 ("practiced directly").
- What: all three grade 3 codes name "a combination of sequence, events, iteration, and selection" (ALG-PS-01:
  create an algorithm with that combination; PD-04: develop code from a student-created algorithm with it; TR-08:
  debug a program with it; wording checked in the CSTA-based BootUp alignment PDF, csteachers.org). The student
  authors selection (rule cards) and uses events (button, ambulance detector). Iteration is the engine's fixed
  half-second check, never written or changed by the student; sequence only emerges from rules as the light cycle.
  The tool teaches selection, events and debugging very well; the "combination" part is mostly mentioned.
- Better (rule 2, no thin activity): either make the existing structure explicit where the student already sees it
  (Step and the panel foot named as "one time round the loop", the job 1 and 2 fixes framed as building the
  GREEN, YELLOW, RED, WALK sequence out of rules, and notes saying honestly which part each code gets) and confirm a
  sibling grade 3 tool covers authored loops and sequences; or note in the spec that ALG-PS-01 and PD-04 are shared
  with a tool where the student writes the loop. Notes.md:77 should not claim the codes are "practiced directly" as
  written today.
- Seen: standard texts vs. src.html controls; no control edits the check cycle.

### 3. Rush Hour's missed-goal report gives a grade 3 student no rule to look at (should fix, family:robot)
- Where: src.html:839-844 and 1218-1220 (order note only when rule 4 already has "been 10 s"); job 4 in spec.
- What: job 4 needs two changes, one of them moving a rule. With only "been 30 s" added (the natural first try,
  and what the brief "long greens" invites), the report shows "Reds under 45 s ✕, Longest red: 63 s" and nothing
  else: no rule number, no order line. The cause (Rule 3 starting WALK four times while the light stays red) is
  only visible by reading the ribbon chips. Solo student (rule 4) is likely stuck here; this is the spec's own open
  question.
- Better: for a failed fairness check, name the rule that fired most during that stretch ("Rule 3 started WALK 4
  times in a row while cars waited 63 s"), the same "Rule N did it" pattern the unsafe lines already teach. Or
  settle the open question by spacing job 4's walkers so one change is enough.
- Seen: sim-out.json `j4_30only` (order false, orderRule shown nowhere for this case).

### 4. Talk question teaches the wrong rule (should fix, general)
- Where: notes.md:51 "Why can a rule at the bottom never get a turn even when its condition fits?"
- What: false as written. A bottom rule fires whenever no higher rule fits: job 1's fix passes with the new rule at
  the bottom (sim `fix1bot`, Rule 4 turns YELLOW at 5.5 s). The point is "when a higher rule fits at the same check".
- Better: "Why can a rule lower down lose its turn even when its condition fits?" or add "when a rule above it fits
  too".

### 5. Order line names "changed the light" for a rule that started WALK (polish, family:robot)
- Where: src.html:843 and 1219.
- What: in job 4 with rule 4 changed but left below rule 3, the report says "Rule 3 changed the light first. Rules
  are checked from the top." Rule 3 starts WALK; it does not change the car light. A student scanning for the rule
  that changed the light will look at the wrong cards.
- Better: "Rule 3 fit first and started WALK. Rules are checked from the top."
- Seen: sim `j4_r4below` (order true, orderRule 3).

### 6. Goal card uses ≥ and < for grade 3 (polish, general)
- Where: src.html:941-942 ("green ≥ 30 s; red < 45 s; walker wait < 60 s").
- What: ≥ is not grade 3 notation, and the goal checks in the report already say it in words ("Greens at least
  30 s", "Reds under 45 s"). Two wordings for one rule.
- Better: "Model limits: greens at least 30 s, reds under 45 s, walkers wait under 60 s." matching the report.

### 7. Job 5's starting report points at order before any second rule exists (nit, family:robot)
- Where: src.html:1218-1220 with job 5's starting rules.
- What: "Rule 1 changed the light first. Rules are checked from the top." shows when no ambulance rule exists yet, so
  nothing competed. It is in the spec and is true, but "first" suggests a contest. "Rule 1 turned the light yellow
  at 38.5 s, so the ambulance met a red." would say what happened.

## Checked and clean
- Done when 1 and 3: worked checks hold to the half second (sim-out.json): job 1 fixed Y 5.5, R 8.5, WALK 9, GREEN
  26.5; job 3 unfixed GREEN 18.5 "Green while crossing" x3; job 4 unfixed WALK 7, 24.5, 42, 59.5, 77, red 86.5;
  "been 30 s" only red 63; rule 4 only greens 0.5; both Y 30, R 33, W 33.5, G 51, Y 81, R 84, W 84.5, longest wait
  41.5; job 5 unfixed Y 38.5, R 41.5, had to stop; top rule Y 46, WALK 49.5.
- Done when 2: each start fails for the table's reason (job 1 0 of 3 crossed, job 2 three "Yellow too short", job 3
  three "Green while crossing", job 4 green 3.5 and red 86.5, job 5 had to stop); each listed fix passes.
- Done when 4: all three unsafe kinds caused on purpose in Watch the Street, each with words and rule number in the
  Watch out line and hazard tag (frames/watch-*.png; "Green while crossing" shows a car driving into the walker, a
  strong moment).
- Done when 5: ambulance rule at the bottom fails with `order` true (line 14); at the top passes.
- Done when 6: replay pauses on the named rule (audit state-replay-1366x768.png); "never fired" tags (audit
  state-job-report-1366x768.png).
- Facts: MUTCD 2009 yellow 3 s minimum (4D.26), walk 7 s, 3.5 ft/s clearance, 35 ft / 3.5 = 10 s (4E.06), all as
  cited; fairness limits labeled as the tool's own. Notes "Good to know" matches the code.
- No hidden-information mode; job briefs guide without stating the fix except job 2 (fine for a builder job).
- Support at home ideas are doable tonight; Key skills are true of this tool. No sensitive topic for rule 8.
- Nothing cultural, Native or hard-history. The three walker images are people art (rule 11, Cory's sheet), not a
  sensitivity item.

## Audit pilot
- Leads confirmed: none bear on teaching; the 375 and 760 fold leads are layout (Play/Craft).
- Leads wrong: none checked as wrong from this lens.
- Missed (outside what it can see): the job 5 "Never stopped" readout that lies under a long yellow (finding 1), the
  standards gap (2), the silent fairness miss in job 4 (3) and the false talk question (4).

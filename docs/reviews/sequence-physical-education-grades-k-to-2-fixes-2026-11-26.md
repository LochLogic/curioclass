# Fixes: scope and sequence of physical-education-grades-k-to-2, 2026-11-26

Fix pass after the Claude expert read (docs/reviews/sequence-physical-education-grades-k-to-2-2026-11-26.md), per
build/scope-writes/AFTERCORE-FIX.md. The Codex read waits for Codex's usage reset (after 2026-11-30). No other
physical education expert read of 2026-11-26 exists, so there are no band items from other courses.

Counts: applied 11 of 11 expert findings and all 8 "Settled by the expert" rows; 4 of the read's "For the lead" items
applied here under lead calls 4 and 7, 1 passed to the structure pass, 1 belongs to the health fixer; lead calls 1,
4, 7, 9 and 11 applied to frame.md; 2 own findings. Not applied: 0.

Days were changed by build/scope-writes/scratch/physical-education-grades-k-to-2/fix_2026-11-26.py and the frame by
fix_frame_2026-11-26.py in the same folder; copies from before the pass are beside them (days-before-fix.csv,
frame-before-fix.md).

## Applied

- **Expert 1 (lead's finding 1)**, days.csv, scope, frame: team talk is now health's five steps word for word, "stop,
  say what happened, listen, find a fair way, an adult helps when words do not work". Day 183 goal (the group then
  tries the fair way, as an action, never a printed step) and note ("health K to 2 unit 14, weeks 13 to 18, comes later
  in the year and teaches the same steps"); day 185 goal quotes the steps; day 189 knowledge prompt asks all five steps
  and conduct adds getting the teacher when words do not work; day 207 note quotes the card. Scope "Shared cards" and
  unit 17. Frame (call 4 and 7): the Models carried team-talk row, unit 17's What students learn and Ends, and the
  Cross-subject row ("health and SEL come later in the year and teach the same steps").
- **Expert 2**, days.csv: all 18 course-level days (43 to 45, 68 to 70, 123 to 125, 148 to 150, 201 to 203, 226 to
  228) now name the stations' space, equipment, no-equipment path and the water break; K year-end, grade 1 year-end,
  grade 2 mid-year (its ball station) and grade 2 year-end carry the swing-space rule; the grade 1 mid-year shapes
  station keeps unit 9's Required access rule. Respond days carry their window's note. Scope and frame course-check
  sections say so.
- **Expert 3 / settled row 5**, days.csv, scope, frame: a second in-place task of the same indicator is recorded at the
  owning unit's last Fluency day and named on the check: day 31 (roll to a seated partner; bounced-ball catch) for
  days 32 and 33; day 40 (kick to a partner) for day 41; day 56 (self-dropped ball struck with the paddle) for days 57
  and 58; day 120 (bounce to a wall and back; balloon hit with a partner) for day 121; day 178 (throw to a partner) for
  day 179; day 210 (self-drop with the long tool) for day 211. Scope "Assessment pattern" lists them; frame Assessment
  bullet states the rule. No day added.
- **Expert 4 / settled row 3**, days.csv: `~` on the reused code of days 19, 38, 65, 66, 74, 79, 88, 118, 142, 167,
  183, 186. A script over the frame's owned-standards column confirms no other unit day claims a code its unit does
  not own.
- **Expert 5 / settled row 8**, frame, scope: frame unit 14's Mugunghwa line no longer says the ministry page "shows it
  among Korea's alleyway games"; it says the page, reopened 2026-11-26, names alleyway games but not Mugunghwa in its
  text, so the source is unconfirmed and the sensitivity agent finds a Korean folk-culture source first (browser
  check: the National Folk Museum of Korea's Encyclopedia of Korean Folk Culture). Scope unit 14 and "What I am unsure
  of" say the same.
- **Expert 6**, days.csv, scope, frame: day 11 conduct "stops on the signal and acts on one cue the teacher gives"
  (S3.2.4 in full); scope unit 1; frame unit 1 Ends.
- **Expert 7**, days.csv, scope, frame: day 159 prompts split, "name one activity you can do with others (S4.2.2);
  name your favorite and say if it is alone or with others (S4.2.4)"; scope unit 14; frame unit 14 What students learn
  and Ends.
- **Expert 8**, days.csv, scope, frame: days 145 and 146 take the pattern's moves from two of the unit's dances, named
  on the check card; scope unit 13; frame unit 13 Ends.
- **Expert 9 / settled row 6**, scope, days.csv: "my goal and one step" in the scope's Shared cards and days 53, 156
  and 173 (the defect row's summary lists days 46, 54, 156, 174 by mistake; these three are the days that changed).
- **Expert 10 / settled row 7**, days.csv: days 234 to 236 have the review stations' space, equipment (the band's
  balls, paddles, ropes, cones, scarves, the calm-down and goal steps cards), swing-space rule and no-equipment path in
  place of the life-jacket kit; their sensitive note keeps emotions. Day 240 names both the water kit and the look-back
  kit. Days 229 to 233 and 237 to 239 keep the life jackets. Day 234 reads "grade 2 unit 16's goal cycle".
- **Expert 11**, days.csv, scope, frame: day 201 conduct "shares the station and its equipment with words (S3.2.3,
  unit 1, as in unit 17)"; `SHAPE.S3.2.3` added to days 201 and 202; scope and frame check tables.
- **Read's For the lead, Syvspring address** (call 4, 7): frame unit 13 and scope Sources carry the live
  folkdancefootnotes.org address.
- **Lead call 1**, frame, scope: frame For the lead 5 (respond days in core weeks) and 6 (after-core check clashes)
  and the course-check intro now say they are settled by CALENDAR.md rule 1 (PE, ELD, visual arts and library are
  specials; grade 2 week 27's only classroom course is health). Scope For the lead 5 dropped.
- **Lead calls 9 and 11**, frame: the check table carries the scope's additions: K year-end travel and freeze reused
  from unit 6's check (collect once) and S3.2.7 conduct; grade 1 mid-year S3.2.1; grade 1 year-end S2.2.9 and S3.2.5
  conduct; grade 2 mid-year S3.2.3 conduct; grade 2 year-end S3.2.9 conduct. The intro states collect once. Scope For
  the lead 3 dropped.
- **Lead call 10**, scope: the list of codes on no course-level check moved from For the lead 1 into the Course-level
  checks section as settled, reason named. For the lead renumbered (2 items left).
- **Own 1**, days.csv: S1.2.11 is one of the "several in-place tasks" indicators the read named but its table gave no
  second task; day 40's closure watch also records taps a few steps forward and a stop, carried to day 41.
- **Own 2**, scope and frame headers name this fix pass.
- Every finding is logged in data/plans/defects.csv (13 rows, status fixed). The frame-wording own row was logged
  with `--made-at=frame` (where the fault was made) rather than `scope`.

## Not applied

- Read's For the lead, health day 72 opening the steps as retrieval: the health K to 2 fixer has it (lead).
- Read's For the lead, the progression note of g2-talk-problems: a shared file, so under For the structure pass.

## Settled

| Judgment | Reuse |
|---|---|
| A shared card is printed in its owner's words; any extra action (here "then try it") is what the group does, never a step on the card | Every PE, health and SEL band that quotes a shared card |
| "Several in-place practice tasks" means at least two recorded tasks: the end task and a second task at the owning unit's last Fluency day's closure watch, named on the check | PE 3 to 5 and on, wherever span wording is plural |
| A course-level window's note names stations, space, equipment, no-equipment path and water break; any striking station carries the swing-space rule | All PE course-level days |
| A reused S3 conduct code outside its owning unit takes `~`; course-level check days keep plain codes | All PE bands |
| A cited source that does not name the game or dance in its own text is "unconfirmed", with a browser-check lead, until the sensitivity agent finds one that does | Cultural units in every PE band |

## For the structure pass

- data/progressions/physical-education.csv, row g2-talk-problems, notes column: old "Introduces team talk as four
  steps a child can say: stop, say what happened, listen, find a fair way (the same words as health's conflict steps,
  g2-v-settle-it-with-words, so a child meets one set), then try it." new "Introduces team talk in the words of
  health's conflict steps (g2-v-settle-it-with-words), so a child meets one set: stop, say what happened, listen, find
  a fair way, an adult helps when words do not work. Trying the fair way is what the group then does, never a printed
  step."
- sequence.py notes "first day in the course for ~SHAPE.S3.2.4" (day 19), "~SHAPE.S3.2.3" (day 38) and
  "~SHAPE.S3.2.5" (day 118): the script counts a `~` code apart from its plain owner, so a review in a later unit
  reads as a first day. These are reviews of codes taught in units 1 and 10; the script could treat `~X` as taught when
  plain X was taught earlier. Notes only, not failures.
- Lens spellings (call 13): a search of docs/agents/lenses/physical-education.md for the common UK forms (colour,
  behaviour, organise, recognise, practise, centre, metre, programme, favourite, licence, judgement) found none.

## For Cory

None.

## Gates

- `python -X utf8 scripts/sequence.py check physical-education-grades-k-to-2`: 0 failures; 3 notes (days 19, 38, 118,
  above).
- `python -X utf8 scripts/frame.py check physical-education-grades-k-to-2`: 0 failures (K 74, 1 74, 2 74 unit days;
  22 units, 240 days).
- `python -X utf8 scripts/plan.py check physical-education-grades-k-to-2`: 0 failures for this course.
- `python -X utf8 scripts/frame.py calendar`: PE K to 2 check weeks are K 18 and 28, grade 1 18 and 28, grade 2 17
  and 27, as the frame sets them; no stagger break (PE is a special under rule 1). No frame change in this pass moves a
  check.

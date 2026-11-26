# Fixes: scope and sequence of social-and-emotional-learning-grades-k-to-2, 2026-11-26

Fix pass under build/scope-writes/AFTERCORE-FIX.md and docs/pipeline/briefs/sequence-fix.md. One read so far: the
Claude expert read docs/reviews/sequence-social-and-emotional-learning-grades-k-to-2-2026-11-26.md. The Codex read
waits for Codex's usage reset and gets its own small pass. The other expert read in the subject (grades 3 to 5) has no
item that touches this course.

Counts. Applied: expert 12 of 12 findings and all 16 rows of "Settled by the expert", plus the read's "For the source
list" item; lead calls 1, 4, 5, 7, 8, 9, 11 (calls 2, 3, 10, 12, 13, 14 needed no change here; 13 goes to the
structure pass); own 4. Not applied: 0.

Days are patched by build/scope-writes/scratch/social-and-emotional-learning-grades-k-to-2/fix_2026-11-26.py (run
after make_days.py; the pre-fix copy is days-before-fix.csv beside it). Frame edits are in fix_frame_2026-11-26.py
(pre-fix copy frame-before-fix.md).

## Applied

- **Expert 1** (pair rehearsals). days.csv: every "teacher or a card plays" note now reads that the teacher (or a
  teacher-held puppet) voices every pressure, dare, push or unkind line; days 43, 44, 45, 87, 88, 90, 101, 154, 155,
  162, 163, 165 add the coach line (teacher voices to the whole class, pairs answer in turn, the partner holds the
  step card; a calm scripted other side only in a plain disagreement); goals of 43, 87, 90, 101, 103, 154, 162, 165,
  166, 167 reworded from "the card playing" to the teacher voicing. .md "Every unit" bullet says it once. frame.md:
  the unit 5, 9, 10 and 16 teacher-note cells gain the pair-rehearsal line (call 4).
- **Expert 2** (grade 2 end pages). days.csv day 159 adds RS8's offer of help and RS7's following a plan not your idea,
  drops the fair-end prompt (the watched I-statement stands for RS5); day 178 adds SM5's materials and SA2's strength
  from the invented teammate's two languages; day 135 adds SO6's "two places or groups with different rules", the day
  134 card stands for SO5; day 191 RD5 reads "at school and at home", the watched team problem stands for RS4 and
  AASL.III.D.2; days 146 and 167 say the watched calm plan stands for SM2 and the watched refusal for RS6. .md
  End-of-unit bullet lists the stand-ins; units 13 to 18 text updated.
- **Expert 3** (collect once). days.csv days 20, 80, 147 keep the calm-down column until days 22, 82, 149. .md
  Evidence bullet and check table; frame.md Evidence bullet and Course-level checks paragraph gain the exception (calls
  7 and 9).
- **Expert 4** (crowded openings). days.csv: the 17 listed days' notes now read "Opening: X; Y and Z are retrieved at
  the start of their own modeled steps" (`retrieves` unchanged). .md Readiness and retrieval bullet says the rule once.
- **Expert 5** (RS1 owner step). days.csv day 131 gives each child one partner idea they do not agree with, met on the
  talk turn card; days 134 and 135 look-fors include it. .md unit 13 text.
- **Expert 6** (disclosure). days.csv: the disclosure line added to days 23, 31, 53, 65, 105, 118, 129, 169, 182. .md:
  "in every unit".
- **Expert 7** (prompt per part). days.csv day 19 four prompts for SM6, SM5, SM3, SM7; day 49 RS3 one way different
  and one way the same; day 92 adds the follower's idea. .md unit 5 text.
- **Expert 8** (kindergarten unit 2 short path). .md Shorter path spells out the six sessions; SM3 and SM7 first
  scored in session 6.
- **Expert 9** (day 176). days.csv day 176 rehearses the timed plan and folder on a practice card, then the class
  starts its plan; day 177's note names the project's two days as carry-out time (book swap shelf started then). Day
  125 (the read's parenthesis) likewise: pairs rehearse on a practice tally, then the class takes its tally and
  chooses; the teacher sets the help up before day 126. .md units 12 and 17 text.
- **Expert 10** (refusal words). days.csv day 89 quotes "say stop, say it again, move away, tell". .md unit 9 text;
  frame.md health table row and unit 9 cell (call 4). Progression note: structure pass.
- **Expert 11** (stale .md). (a) carry-out cue "on the day it starts", family activity on the Respond day. (b) Grade 2
  mid-year check (days 148, 149) adds SA4, the honest action and its cost, on a new case (skills and codes); .md check
  table and unsampled list (SA4 moved out; eight codes sampled); frame.md grade 2 mid-year cell (call 4).
- **Expert 12** (repeated cases). days.csv days 132 to 134 use a recess game rule and a town helper outside the
  school; days 164 and 165 rest the snap judgment on a classmate quiet at lunch; day 148 "an unfair play rule". .md
  units 13 and 16 text. frame.md: SA6 seam row, unit 13 and unit 16 cells (call 11). Progression notes: structure
  pass.
- **Read, For the source list.** .md Sources and frame.md Base text say the Tema International School page describes
  Ampe's play and the myjoyonline page names the game only (call 4: a claim a source does not support).
- **Lead call 1.** frame.md For the lead 10 reworded as settled by CALENDAR.md rule 1 (the week 26 visual arts clash is
  a special; the week 11 and 27 items are SEL respond sessions, not check days). The scope had no matching item.
- **Lead call 5.** frame.md Days bullet: unit 18 group 2 runs Understanding then two Application sessions by GLOSSARY.
  .md For the lead 2 dropped.
- **Lead call 8.** days.csv: every kindergarten and grade 1 day carries its begun codes as `~CASEL...` from the
  progression; day 148 and 149 add `~CASEL.Responsible Decision-Making.2` for the sampled grade 1 row. No day has an
  empty `codes` cell. .md "Which standards fall where" and For the lead 3 dropped.
- **Lead call 9.** frame.md kindergarten, grade 1 and grade 2 mid-year check cells say the calm-down item is collected
  once from the unit's record. .md For the lead 1 dropped; the .md For the lead now reads "None open".
- **Own 1.** Day 178's watched goal plan with a changed step stands for SM4 (adjusting the plan), so the page does not
  ask the changed step twice; keeps the page near the read's eight-prompt budget after two prompts were added.
- **Own 2.** Day 125's goal (see expert 9): the read named it in passing; fixed the same way.
- **Own 3.** Frame wording around finding 12: unit 13 cell "Curio Class writes the club stories" became "the game
  stories".
- **Own 4.** Defects logged with scripts/plan.py, one row per expert finding (12 rows, status fixed, made at scope).

## Not applied

- None.

## Settled (for DIGEST)

| Judgment | Reason |
|---|---|
| In K to 2 pair rehearsal the teacher voices the pressure, dare, push or unkind line to the whole class; the partner coaches with the step card; a calm scripted other side only in a plain disagreement | One adult cannot voice a part for fifteen pairs; the guard holds |
| A watched performance on the Check day stands for a whole code, named in the goal, so the page does not ask it again | Keeps 20-minute Check pages near eight prompts while every part is asked |
| A unit sheet column a later course-level check reuses is kept to that check's respond day | Makes collect once true under the throw-away rule |
| The 4-minute opening holds one retrieval row; others come back at the start of their own modeled step | Fits the frame's session budget; `retrieves` stays complete |
| A Fluency day that would do the real class task rehearses on a practice card; the real task runs as carry-out time or on an Application day | GLOSSARY kinds |
| Begun ids in a band course's earlier years carry `~` codes on every day | Lead call 8 |

## For the structure pass

1. data/progressions/sel.csv, row g1-rel-say-no, notes: old `(the words of health grade 1's ""say stop, move away,
   tell"")`, new `(the words of health grade 1's ""say stop, say it again, move away, tell""; the shared second-push
   words are ""say it again, move away, tell"")`.
2. data/progressions/sel.csv, row g2-soc-fair-rules, notes: old `compares a fair and an unfair game rule in two
   invented clubs`, new `compares a fair and an unfair recess game rule in two invented games (grade 1 rewrote a club
   rule)`. (The read's "For the lead" asked for "a club and a recess game"; its settled table and finding 12 fix set a
   recess game rule, which the days now use, so this wording follows the settled fix.)
3. data/progressions/sel.csv, row g2-sa-snap-judgments, notes: old `a character's snap judgment about a newcomer,
   checks it by asking, and names what the wrong guess cost the newcomer`, new `a character's snap judgment about a
   classmate who is quiet at lunch, checks it by asking, and names what the wrong guess cost that classmate`.
4. data/progressions/sel.csv, row g2-soc-thankful, notes: old `a thank-you card for a school or town helper named in
   the rules unit`, new `a thank-you card for a town helper outside the school named in the rules unit`.
5. Lens spellings (call 13), docs/agents/lenses/sel.md: line 11 `practise` to `practice`; line 83 `behaviour` to
   `behavior`.
6. Calendar: no change needed; `frame.py calendar` shows no break for SEL K to 2 (weeks K 11 and 26, grade 1 9 and 26,
   grade 2 10 and 26).

## For Cory

- None.

## Gates

- `python -X utf8 scripts/sequence.py check social-and-emotional-learning-grades-k-to-2`: 0 failures, no notes.
- `python -X utf8 scripts/frame.py check social-and-emotional-learning-grades-k-to-2`: 0 failures; notes: unit days by
  year K 60, 1 60, 2 60; 18 units, 192 days (180 in units, 12 for checks and respond days).
- `python -X utf8 scripts/frame.py calendar`: no stagger break printed; SEL K to 2 unchanged (no frame change moved a
  unit or check).

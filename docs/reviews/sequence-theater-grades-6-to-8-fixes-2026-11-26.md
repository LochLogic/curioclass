# Fixes: scope and sequence of theater-grades-6-to-8, 2026-11-26

Fix pass per docs/pipeline/briefs/sequence-fix.md with build/scope-writes/ARTS-FIX.md. One read so far: the Claude
expert read docs/reviews/sequence-theater-grades-6-to-8-2026-11-26.md. The Codex read waits for Codex's usage reset
(after 2026-11-30) and gets its own small fix pass then; the brief's Codex and 2026-11-15 lead-call items are skipped.

Counts: applied 10 expert findings (all, with every row of "Settled by the expert"), 7 ARTS-FIX lead calls applied or
confirmed (1, 2, 3, 6, 7, 8 applied; 4 and 5 need no change; 9 is theater 9 to 12 only), 0 band items (none exist),
2 own. Not applied: 0 expert, 0 lead calls; two frame-layer items go to the structure pass.

## Applied

- **Expert 1** (once-a-week path). .md Shorter path: one sentence says S1 stays clean, the retrieval task opens S2
  (two study sessions) or the first rehearsal session (one), never S1. Session moves as settled: day 13 to unit 1 S5;
  25 to unit 2 S2; 39 to unit 3 S3; 77 to unit 5 S5; 102 to unit 7 S3; 141 to unit 9 S5; 168 to unit 11 S3; 182 to
  unit 12 S3. The closing paragraph now says study days are taught in short form, about ten minutes each, so no reader
  takes the path for the full course. The frame split (8, 7, 7, 6, or a plain short-form line) is For the lead item 1
  and the structure pass.
- **Expert 2** (day-2 minutes). days.csv notes of days 2, 20, 36, 50, 66, 84, 100, 114, 130, 148, 164, 178: the 10
  minutes cover both rows, the reteach runs inside them from a printed card while the others do the task, and the
  day's budget is written out (day 2: warm-up routine 15, replacing the 5-minute warm-up). Day 164 moves its
  retrieval to day 165's opener if the walk leaves the room; day 165 says so. .md Minutes bullet, mixed-grade line
  and retrieval table match.
- **Expert 3** (group sheets as individual evidence). days.csv goals of days 37, 40, 101, 104, 164, 165: each student
  fills their own cue sheet, sketch sheet or venue plan, the group's version copied; day 40 each student draws two
  fixes with a reason before the group picks; day 104 each student writes an explain line and speaks one part; day
  110 note marks each student on their part. .md end-of-unit bullet and units 3, 7, 11 assessment lines say so.
- **Expert 4** (every part of each code). Day 63 goal adds each student's line on how their cue is woven in (what,
  when, why); day 97 "body and voice traits that fit the goal"; day 161 "a physical, a vocal and a bodily-response
  choice, each held"; day 61 "action and want, and the view of the community they give"; day 89 frame "claim,
  analysis, background, context: the Gupta court", with days 91 and 94 notes matching. .md unit 4 and 6 lines and the
  checks table match. Frame check-table wording under "For the structure pass".
- **Expert 5** (single-day responding and connecting ids). Codes, skills and a one-line note added on days 10
  (Re8.1.6a), 15 (Re8.1.6c), 29 (Cn11.2.6a), 43 (Re9.1.6c, critique question), 45 (Re9.1.6a), 55 (Cn10.1.6a, critique
  question), 59 (Re8.1.6b), 74 (Re8.1.7a), 79 (Re8.1.7c), 89 (Cn11.2.7a, Cn11.2.7b), 107 (Re9.1.7c, critique
  question), 109 (Re9.1.7a), 122 (Re8.1.7b), 143 (Re8.1.8c), 153 (Cn11.2.8a), 172 (Re9.1.8b, Re9.1.8c, critique
  questions), 186 (Re8.1.8b). Re9.1.8a left at its own full day (171). The .md process table and its paragraph list
  the days; the fold rows for days 10, 45, 74, 109, 122, 186 carry the line into the neighbor's close.
- **Expert 6** (earlier-unit models). `retrieves` added: day 137 th-g7-judge, day 171 th-g8-notice, day 186
  th-g8-design, each a 5-minute opener in its note. .md retrieval section names them.
- **Expert 7** (fold minutes). The drill folds 10, 74, 122, 138 read "5: the drill is that day's warm-up"; the
  observation folds 45, 109, 157 read as settled (groups in parallel, only students still without an observed turn,
  any missing mark taken live before the respond day). Totals stay 480 minutes.
- **Expert 8** (floor line). .md Equipment paragraph now says the unit's floor line is set on its first floor day and
  first Application day, holds on every floor day and is printed on every section plan. Floor line added to days 53,
  105 and 170; days 72, 116, 136, 152 and 181 already had it.
- **Expert 9** (responding as a student act). Days 21 and 151 goals add a one-line audience-journal reaction to a
  choice in the other artist's version or production; day 85 a one-line reaction to the stage manager's opening;
  notes say practice, no id claimed. .md process table updated for units 2, 6, 10.
- **Expert 10** (stale notes). For the lead item 3 replaced with the closed calendar line; the job-message line
  dropped.
- **Lead call 1.** The 10-days-short year reads about four sessions; four fold-in days a year already (twelve in
  all, no spares). The "10 course days" reading in For the lead item 2 dropped; item closed.
- **Lead call 2.** .md "The four processes" now says each year claims all four, a unit claims what its owned rows
  name, practice on an existing day claims no id. Checked by script: no day carries a code outside its unit's owned
  rows (after the expert 5 additions).
- **Lead call 3.** Not-sampled list kept; the line says naming with the reason is enough; For the lead item 1 (old)
  closed as item 2.
- **Lead call 6.** Check-day notes 33, 63, 97, 127, 161, 191 say the check is a showing on a fresh card with its own
  items; the .md Course-level checks paragraph states the rule.
- **Lead call 7.** Checked: no check cell re-asks items a unit gave one to three days before (mid-year checks carry
  the just-assessed unit's records unscored; year-end checks draw on units 1 to 3 of the year). Stated in the .md. No
  frame change.
- **Lead call 8.** school_day formula (ceil(2.5 x course day), band-wide) and the week read-back stated once in the
  .md; every unit and check verified by script to fall in the frame's weeks (units 1 to 9, 10 to 16, 18 to 24, 25 to
  31; checks 17 and 32 each year). Not re-counted to calendar.csv.
- **Lead calls 4, 5, 9.** No change: no baseline sought; band-wide school_day kept; call 9 is theater 9 to 12.
- **Own 1** (rule 2, each part of each code). Day 33 marked "a body choice and traits" for TH:Pr4.1.6b ("try
  different body choices") and TH:Cr3.1.6b ("body and voice traits"). Goal now "body choices tried to show the
  character and body and voice traits used on purpose"; the .md checks table matches.
- **Own 2** (rule 2 re-run). Earlier-grade rows: all one grade back, retrieval, no readiness check (unchanged).
  Checks' sampled codes: 33 (Pr4.1.6b, Cr3.1.6b, Re7.1.6a), 63 (Cr1.1.6a, Pr5.1.6b, Re9.1.6a), 97 (Pr4.1.7b,
  Cr3.1.7b, Re7.1.7a), 127 (Pr4.1.7a, Cr3.1.7c, Re9.1.7a), 161 (Pr4.1.8b, Cr3.1.8b, Re7.1.8a), 191 (Pr4.1.8a,
  Cr1.1.8b, Re9.1.8a), each part now asked. Collect once and end days hold. Our words: every new goal and note
  written fresh.

## Not applied

- **Band items.** No other arts expert read has an "Across the band" section; the shared points (10-days-short
  reading, task form, school_day count) are settled by the ARTS-FIX lead calls and applied above.
- **Frame-layer items** (expert 1's split, expert 4's check-table wording). frame.md unchanged; both under "For the
  structure pass".

## Settled

| Judgment | Reuse |
|---|---|
| On the once-a-week path the retrieval opens S2 or the first rehearsal session, never the hook session | Every arts once-a-week table |
| Day-2 retrieval: 10 minutes for both rows, reteach inside them from a printed card, budget written out | Every arts retrieval day |
| A model reused from an earlier unit of the band gets a 5-minute retrieval in `retrieves` | Arts units leaning on earlier design or judging models |
| Group-made sheets: each student's own copy is the evidence; group presentations, each student speaks one part | Any arts group making or presenting id |
| Single-day responding and connecting ids get a second one-line touch in a later close or as the critique question, coded there | Any arts unit |
| A folded day's second-touch line moves into the neighbor's close | Every arts 10-days-short table |
| Drill folds replace the 5-minute warm-up, never take 8 | Every arts 10-days-short table |

## For the structure pass

1. **docs/courses/theater-grades-6-to-8/frame.md**, "The once-a-week path" bullet (line 41 to 46): after "the scope
   and sequence marks which days merge." add "On this path each study day is taught in short form, about ten minutes,
   so the path is not the full course." Or, if the lead prefers the expert's other option, old "units of 9, 7, 6 and
   6, split as study and demonstration 2, 2, 1, 1; rehearsal, critique and revision 4, 2, 2, 2", new "units of 8, 7,
   7 and 6, split as study and demonstration 2, 2, 1, 1; rehearsal, critique and revision 3, 2, 3, 2" (the design unit
   gets a session for the making alone); the scope's session table would then need a rewrite.
2. **docs/courses/theater-grades-6-to-8/frame.md**, Course-level checks table (expert 4 and own 1):
   - Year 6 mid-year cell, old "a body choice that shows the character (TH:Pr4.1.6b)", new "body choices tried to
     show the character (TH:Pr4.1.6b)".
   - Year 6 year-end cell, old "one tech element woven in from a three-cue card (TH:Pr5.1.6b, unit 3)", new "one tech
     element woven in from a three-cue card, with each student's one line on how their cue is woven in (what, when,
     why) (TH:Pr5.1.6b, unit 3)".
   - Year 7 mid-year cell, old "traits fitting the goal (TH:Cr3.1.7b)", new "body and voice traits that fit the goal
     (TH:Cr3.1.7b)".
   - Year 8 mid-year cell, old "a bodily response held (TH:Cr3.1.8b)", new "a physical, a vocal and a bodily-response
     choice, each held (TH:Cr3.1.8b)".
3. **data/plans/calendar.csv**: regenerate with `frame.py calendar` at commit (lead call 8); no school_day changed.

## For Cory

None.

## Gates

- `python -X utf8 scripts/sequence.py check theater-grades-6-to-8`: 0 failures.
- `python -X utf8 scripts/frame.py check theater-grades-6-to-8`: 0 failures (unit days by year 60, 60, 60; 12 units,
  192 days).
- `python -X utf8 scripts/frame.py calendar`: exits 0, no break; this course's checks stay in weeks 17 and 32 of
  grades 6, 7 and 8 (no frame or school_day change made).
- gate.py not run for a baseline (lead call 4).

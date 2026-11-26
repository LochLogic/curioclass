# Fixes: scope and sequence of visual-arts-grades-3-to-5, 2026-11-26

Fix pass on docs/courses/visual-arts-grades-3-to-5/scope-and-sequence.md and data/plans/visual-arts-grades-3-to-5/days.csv
after the Claude expert read (docs/reviews/sequence-visual-arts-grades-3-to-5-2026-11-26.md), done as
docs/pipeline/briefs/sequence-fix.md with build/scope-writes/ARTS-FIX.md. The Codex read waits for Codex's usage reset
(after 2026-11-30) and gets its own small fix pass then. frame.md is unchanged: no finding changes a unit, its order,
owned rows or day counts; the frame cell wording goes under "For the structure pass". 18 rows of days.csv changed
(days 21, 43, 51, 58, 84, 85, 90, 96, 103, 113, 122, 125, 131, 150, 165, 171, 179, 188), written with the csv module.

**Counts.** Applied: expert 8 of 8 findings (finding 7 in its 6 parts) and all 10 "Settled by the expert" rows; lead
calls 8 of 8 (3 already met, 1 not applicable, 4 applied or routed); band items 0 (no other arts read has an "Across
the band" section; the one shared item, the school_day count, is lead calls 5 and 8); own 3. Not applied: 0. Codex: 0
(read not yet made).

## Applied

- **Expert 1 (once-a-week end sessions).** .md Shorter path, once-a-week bullet: the showing is hung at the end of the
  revision session and visited outside art time (partner class walk-by, a drop-in at arrival or pick-up, a family
  evening), look-fors scored from the kept work; the end session is the check; units 3, 8 and 11 move the self-check to
  the last five minutes of the revision session and hold one written sitting of all items (about 25 minutes) plus the
  teacher's table (about 8). Unit session lists: unit 1 adds the VA:Cr2.2.3a observation note (sessions 12 and 13,
  then 14-16); unit 2 written "8, 9, 11 / 10, 12"; unit 4 1-4 / 5-6 / 7-9 / 11 / 12 (show 62 outside art time); unit 8
  1-2 / 3-5 / 6-8 / 9-10 / 12-13 / 14 (show 125 hung at the end of 9-10); unit 9 adds the VA:Cr2.2.5a note (10-11 and
  12-13); unit 12 1-3 / 4-6 / 7-9 / 11 / 12 (show 190 hung at the end of 7-9); units 2, 3, 5, 6, 7, 10, 11 name which
  local day is the showing and the session it is hung at. Counts unchanged (9, 8, 6, 5; 8, 8, 6, 6; 8, 9, 6, 5).
- **Expert 2 (year-end item forms).** days.csv 51: Re8.1.3a as a comparison of Catlett's Sharecropper and Bearden's
  The Block (quieter mood, media, form); Re9.1.3a as the given three-line checklist applied to a Curio Class sample
  student work, marking the line not yet met with a reason. Day 113: Re8.1.4a kept; Re9.1.4a as a given filled-in van
  Gogh checklist, the same checklist applied to a Chicano Park mural and the given marks judged fair or not, with a
  reason. Day 179: Re8.1.5a as a comparison of the Yangliuqing print and The Flower Carrier (which visual elements
  carry the stronger mood, the ideas each conveys); Re9.1.5a as a Curio Class card, written for the day, judging
  Hazoume's mask by a standard from another time or culture, the child saying why it fits or misfires, naming style,
  media and setting. Notes on all three now name the form used instead of "a different task form". .md checks table
  rows for the three year-ends rewritten; "Drawn from earlier units" bullet: "No check repeats a task form given in
  the two weeks before it" replaced by the expert's sentence. .md For the lead item 1 names the new forms.
- **Expert 3 (same-year retrieval, unit 8 technique).** Five-minute retrieval warm-ups in the note and `retrieves`:
  day 21 and 43 va-g3-look; day 90 va-g4-craft; day 103 va-g4-revise; day 122 va-g4-craft (goal now names the step
  card in hand, unit 5's marks or unit 6's color plan, the child choosing, first steps run on scrap); day 150
  va-g5-craft; day 171 va-g5-revise. .md Readiness: new "Same-year retrieval" bullet listing the seven.
- **Expert 4 (create in units 4 and 12).** Day 58: a finishing detail added to the chosen work with a one-line reason
  before mounting, note "creating (the finishing detail, practice, unscored)". Day 188: one finishing change before
  mounting, named on the label, note "creating (the finishing change, practice, unscored)". No id added to codes
  (lead call 2). Processes lines: "Creating 58 (a finishing detail before mounting)", "Creating 188 (a finishing
  change before mounting)".
- **Expert 5 (unit 6 respond and baseline).** Day 96 goal: the planned change is made on a photocopy of the section or
  painted as a small square to paste onto the panel. Day 84 opens with a two-minute baseline task ("sketch as many
  ways to welcome a new student as you can") before the brainstorm is taught; note names the baseline look. Day 85
  note drops its baseline.
- **Expert 6 (shorter sessions).** .md Shorter path: "Check days stay whole" replaced by the self-check moved to the
  session before and a 29-minute check (set-up 2, written sitting 15, teacher's table 10, clean-up 2), no mounting task
  beyond labeling.
- **Expert 7a.** .md checks table: year 4 school days now (242, 244) and (282, 284).
- **Expert 7b.** .md: every Processes line now reads "Creating ...; presenting ...; responding ...; connecting ...".
- **Expert 7c.** Day 131 note: "sensitivity flag: the agent reads the holding museum's page and a source on the
  Yangliuqing print makers first".
- **Expert 7d.** Day 165 goal: "a pattern of repeated parts"; note: the word symmetry waits for day 167's retrieval.
- **Expert 7e.** Day 125 note: visitors and children say which venue's aim the class show is closest to and what a
  visitor gets from it, practice of VA:Pr6.1.4a; VA:Pr6.1.4a added to day 125's codes (a unit 8 owned id, practice).
- **Expert 7f.** .md 10-days-short bullet: where a fold day is a baseline practice day (8, 10, 23, 44, 68, 102, 133,
  185), its rotating group is observed in the next day's opener.
- **Expert 8 (school_day vs calendar.csv).** Settled by lead calls 5 and 8: the .md's school_day bullet now says the
  count runs across the band (year 3 1 to 160, year 4 161 to 320, year 5 321 to 480), gives the formula once with the
  week formula, and says calendar.csv is regenerated at commit, so no re-count.
- **Lead call 1.** Met already: four named fold-in days a year (160 minutes), the "10 school days, 4 sessions" reading
  only.
- **Lead call 2.** .md "The four processes" bullet rewritten: each year holds all four, each unit touches at least the
  processes the frame names (at least two), no claim outside a unit's owned rows; the ARTS-BRIEF "every unit's days"
  line is no longer stated as the rule. The new create days (58, 188) and the Pr6.1.4a practice (125) cost no day.
- **Lead call 3.** Met already: the 28 codes not sampled are named with reasons; no frame change proposed.
- **Lead call 4.** Not applicable (no baseline refusal met).
- **Lead call 5.** Applied (school_day bullet, band-wide).
- **Lead call 6.** Checked: no course-level check here is a showing or performance; the year-end checks now meet the
  rule by new forms on earlier work (expert 2).
- **Lead call 7.** Applied: the scope draws the year-end items from earlier units' works in a different form and
  carries the unit's records; the frame cells' new wording is under "For the structure pass".
- **Lead call 8.** Applied: school_day not re-counted; checked that every unit and check falls in the frame's weeks
  (script over days.csv, week = (school_day - 160 x (year - 1) - 1) // 5 + 1): units 1 to 4 in weeks 1-9, 10-17,
  19-25, 27-32; checks 18 and 26; units 5 to 8 in 1-8, 9-16, 18-24, 26-32, checks 17 and 25; units 9 to 12 in 1-8,
  9-17, 19-25, 27-32, checks 18 and 26. Formula stated once in the .md.
- **Own 1 (each part of each code).** Day 51's Re8.1.3a comparison, as the expert worded it, named media, form and mood
  but not subject matter; the item now names each work's subject too.
- **Own 2 (rule 2 lists re-run).** Every unit's assumed rows are one grade back and retrieved on the unit's day 2
  (days 2, 20, 38, 54, 66, 82, 100, 116, 130, 146, 166, 182), plus m4-symmetry on day 167; no row is two or more grades
  idle, so no readiness check. Mid-year checks against the two-week rule: day 35's depth item (given sketch) against
  day 31's revision (own work, school days 77 and 87), day 97's three approaches against day 85 (week 11 to 17), day
  163's statement against day 158 (school days 394 and 407): different work or more than ten school days apart; held.
  Collect once: each check carries the just-finished unit's records unscored (days 35, 51, 97, 113, 163, 179); held.
- **Own 3 (.md tidy).** The "Drawn from earlier units" bullet no longer claims a rule it did not meet; the Processes
  lines and the four-processes bullet now agree with the days after the creating practice was added.

## Not applied

- None. The Codex read is not yet made (waits for the reset after 2026-11-30).

## Settled (for DIGEST)

| Judgment | Reuse |
|---|---|
| On a once-a-week path a showing is hung at the end of the revision session and visited outside art time; the end session is the check; two check days become one sitting with the self-check moved earlier | Any arts band course with a showing and a check in one merged session |
| Year-end Re8 and Re9 items right after a unit's Re8 and Re9 assessment use an earlier unit's work in a new form: a comparison of two works, a given checklist checked for fairness, a standard tested against a work | Every arts year-end check that follows a responding unit |
| A same-year lean the frame names in "Why this unit, here" gets a five-minute retrieval warm-up in `retrieves` on the day that uses it | All arts band scopes |
| A presenting unit's create is a finishing change before mounting, practice and unscored, with no id added | Exhibit units in every arts band |
| A baseline look is never on the artifact the unit scores; use a two-minute task before teaching | All arts units with a baseline |
| Shorter-session check: self-check the session before; 2, 15, 10, 2 minutes | Every K to 8 arts check day on a 30 to 35-minute session |

## For the structure pass

1. **docs/courses/visual-arts-grades-3-to-5/frame.md, Course-level checks table, "Year 3 year-end" row, What it checks.**
   Old: "a written response on an unseen work, how its media build subject, one feature of form and mood, and what it
   means (VA:Re8.1.3a), the same work judged with a new three-line checklist (VA:Re9.1.3a),". New: "a comparison of two
   unit 1 works, Catlett's Sharecropper and Bearden's The Block: which uses its media to make the quieter mood, with
   each work's subject and one feature of form (VA:Re8.1.3a), a given three-line checklist applied to a Curio Class
   sample student work, marking the line it does not yet meet with a reason (VA:Re9.1.3a),".
2. **Same table, "Year 4 year-end" row.** Old: "a written item on an unseen work with its background card
   (VA:Re8.1.4a), one checklist used on two unseen works (VA:Re9.1.4a),". New: "a new background card on El-Salahi's
   drawing and how its fact changes the meaning (VA:Re8.1.4a), a Curio Class student's filled-in checklist for the van
   Gogh given, the same checklist applied to a Chicano Park mural, and whether the given marks were fair, with a reason
   (VA:Re9.1.4a),".
3. **Same table, "Year 5 year-end" row.** Old: "a written item on the ideas and mood of an unseen work from its form,
   structure, setting card, subject, visual elements and media (VA:Re8.1.5a), two unseen works from different cultures
   with setting cards and how their judging standards differ (VA:Re9.1.5a),". New: "a comparison of the Yangliuqing
   print and The Flower Carrier: which visual elements carry the stronger mood and the ideas each conveys, read from
   form, structure, setting card, subject and media (VA:Re8.1.5a), a Curio Class card judging Hazoume's mask by one
   standard from another time or culture, and why it fits or misfires, naming the work's style, media and setting
   (VA:Re9.1.5a),".
4. **frame.md, Notes, "The once-a-week path" bullet.** Old: "one making day with the critique; the showing (the
   check); one respond day." New: "one making day with the critique; the showing, hung at the end of the revision
   session and visited outside art time; the check; one respond day. Where a unit has two check days, the self-check
   moves to the end of the revision session and one sitting holds all the unit's items."
5. **frame.md, unit 4 row and For the lead item 2 (stale link, carried from the scope's For the lead item 3, agreed by
   the expert).** Drop the Lakota winter count link to media arts 3 to 5 unit 12 (that frame dropped it); add that
   Lewis Hine (unit 12) is also studied in music 3 to 5.
6. **docs/courses/CALENDAR.md (lead).** Document lead call 5: K to 8 arts band courses count school_day across the band
   (1 to 160, 161 to 320, 321 to 480); then regenerate data/plans/calendar.csv with `frame.py calendar` (this course's
   filled school_day sits one day before today's calendar.csv in places; same weeks).

## For Cory

- Nothing new. The supplies ceiling carried from the frame stands ($60, $50, $50 a class of 30 for years 3, 4 and 5,
  with the pick of $75 a class a year and every free path kept), still unanswered.

## Gates

- `python -X utf8 scripts/sequence.py check visual-arts-grades-3-to-5`: 0 failures.
- `python -X utf8 scripts/frame.py check visual-arts-grades-3-to-5`: 0 failures (unit days 60 a year; 192 days).
- `python -X utf8 scripts/frame.py calendar`: exit 0, no failures; the course breaks no stagger rule (arts are
  specials in K to 5; checks on weeks 18 and 26, 17 and 25, 18 and 26). No frame change was made, so nothing new is
  expected when the calendar is regenerated.
- No em dashes in the two course files or this report.

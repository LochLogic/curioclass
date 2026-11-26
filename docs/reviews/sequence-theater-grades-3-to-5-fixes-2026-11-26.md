# Fixes: scope and sequence of theater-grades-3-to-5, 2026-11-26

Fix pass per build/scope-writes/ARTS-FIX.md and docs/pipeline/briefs/sequence-fix.md. One read so far: the Claude
expert read docs/reviews/sequence-theater-grades-3-to-5-2026-11-26.md. The Codex read waits for Codex's usage reset
(after 2026-11-30) and gets its own small fix pass then.

**Counts.** Applied: expert 9 of 9 findings and 14 of 14 "Settled by the expert" rows; lead calls 7 of 9 applied
(call 4 needs nothing, call 9 is theater 9 to 12 only); band items 0 (none found); own 5. Not applied: expert 1 (the
alternative in finding 3, kept as a scope "For the lead" item). Codex: 0 (read not yet written).

## Applied

- **Expert 1** (once-a-week path, serious; the preferred fix, which changes the frame). frame.md "The once-a-week
  path": on that path each year keeps its year-end check (week 26, respond week 27) and drops the mid-year one;
  sessions now year 3 8, 8, 9, 5; year 4 8, 8, 9, 5; year 5 8, 9, 8, 5 (30 unit sessions a year); the design unit
  starts week 17 (18 in year 5); the story unit's first session is study and teaching only, its baseline run and
  judging teaching open session 2. Scope .md: units 3, 7 and 11 session lists rewritten (no session over three days
  in units 3 and 7; unit 11's session 5 has a minute line); units 4, 8 and 12 sessions 1 and 2 split as the expert
  set, each with a minute line; the Shorter path paragraph and the Course-level checks paragraph say so. days.csv
  unchanged by this finding (the twice-a-week days stand).
- **Expert 2** (10-days-short list). days.csv fold notes: 153 and 171 are no longer fold-in days; 149 (into 148's
  warm-up slot) and 167 (into 168's cue drill) added as spares; 158 moved to the last spare; 134 named in year 5's
  four; 19, 67, 83, 131 now fold into 20, 68, 84, 132. .md table, kinds and totals (year 5 named four save 130,
  all ten 285). Script check: with every fold-in day folded, every owned id still has a teaching day of its own.
- **Expert 3** (critique days 60 and 188). days.csv: day 58's last 5 minutes complete the story map (TH:Cn11.2.3a
  added to its codes), day 186's last 5 minutes the script annotation; days 60 and 188 revise them and hold the
  critique, the revision and one card. .md units 4 and 12 assessment lines.
- **Expert 4** (connecting step). days.csv goals of days 1, 17, 81, 129, 147 add the connecting step, marked
  "practiced, no id claimed" (day 71 stays). .md process lines of units 1, 2, 5, 6, 9, 10 cite 1, 17, 71, 81, 129,
  147 and no longer call days 24, 88, 135 and 153 connecting.
- **Expert 5** (own experiences; frame wording, applied since the finding asks for it). frame.md: the TH:Re8.1.3a,
  TH:Re8.1.4a and TH:Re8.1.5a cells (units 2, 6, 10) ask for at least one experience from this year's theater class,
  an invented one may be the second; the sensitivity paragraph drops "the defended responses of unit 10" from the
  invented-option list and names TH:Re8.1.5b's invented-viewer option as a deliberate trade. days.csv days 24, 31,
  88, 93, 153, 161. .md Sensitivity bullet and units 2, 6, 10.
- **Expert 6** (shorter period). .md "A shorter period": response card 12 minutes, self-check moved to the written
  day (31 minutes), units 2 and 6 keep the marked warm-up with groups of about 3.5 minutes.
- **Expert 7** (every part on checks). days.csv day 163 (two-line record card; TH:Cr2.1.5a marked from the question
  line, no longer live), day 53 (reflection card, one line alone and one with the group), day 181 (self-review after
  the first rehearsal run inside the 8 planning minutes, naming the change in the rerun). .md check table rows.
- **Expert 8.** days.csv days 4, 14, 33 look-fors add "a story the group made up from the card"; day 94 goal and
  note add a line on a choice the student's own pair made. .md unit 6 and the year 3 mid-year row.
- **Expert 9.** .md school_day sentence now reads year 3 + (school_day - 1) // 160; day 183's hook is a paper
  fish-bone cutout, its note names the props rule.
- **Lead call 1.** .md: four named fold-in days a year (year 3 10, 25, 43, 45; year 4 74, 89, 107, 70; year 5 137,
  154, 173, 134), the rest listed as spares in order; the "10 course days" reading dropped. days.csv fold notes say
  "named" or "spare".
- **Lead call 2.** .md bullet "The four processes" replaces "Four processes in every unit": each year carries all
  four, each unit at least its frame row's, practice on a day claims no id. No unit's claims had been stretched; the
  expert's missing-process asks (finding 4) are applied as practice on existing days.
- **Lead call 3.** The .md already names the 49 unsampled codes with reasons; a sentence now ties this to the
  frame's check table.
- **Lead call 5.** Band-wide school_day (3 to 480) kept and stated; .md For the lead item 2 notes it.
- **Lead call 6.** Notes of check days 33, 53, 97, 115, 163, 181, and the .md checks paragraph: a check showing on
  earlier-unit work from a fresh card with its own items meets rule 2.
- **Lead call 7.** Checked: no check re-asks an item given one to three days before; the nearest sampled item was
  last given 10 to 12 weeks earlier. Said once in the .md.
- **Lead call 8.** .md states the formula once: school day ceil(2.5 n), band week (school_day - 1) // 5 + 1, week of
  the year ((school_day - 1) mod 160) // 5 + 1. Script check: every school_day matches it, and units and checks sit
  in the frame's weeks (checks 17, 27; 17, 26; 18, 27).
- **Band items.** No other arts expert read of 2026-11-26 has an "Across the band" section (as the music fix reports
  also found). The theater K to 2 read's once-a-week finding is the same kind as finding 1 here, applied above.
- **Own 1** (rule 2 rerun). Script over days.csv: every id stays in its own year; no fold-in day is the sole
  teaching day of a code; no receiving day carries the 10-minute retrieval; every row assumed is one grade back and
  retrieved in day 2's opener of its unit, so no readiness check.
- **Own 2.** Day 135 had been called connecting in unit 9's process line; removed (it is a set-jobs day).
- **Own 3.** On the once-a-week path the story units' kept cards are completed in the written session's 7 spare
  minutes (the frame's written-day budget), since session 2 cannot hold them.
- **Own 4.** Unit 8's session 2 stays a five-day merge (the unit is fixed at five sessions in weeks 28 to 32); its
  minute line is given and the .md "For the lead" item 3 names it for the unit plan to test.
- **Own 5.** .md header names this fix pass; "For the lead" item 3 rewritten as settled; item 7 added (finding 3's
  alternative).

## Not applied

- **Expert 3, the frame alternative** (critique on two model groups, or the family showing as the showing check).
  Not needed once the cards moved to days 58 and 186; kept as the scope's "For the lead" item 7 in case the unit
  plan finds day 60 or 188 still too full.
- **Codex read.** Not yet written; its own fix pass follows after 2026-11-30.

## Settled

| Judgment | Reuse |
|---|---|
| On a K to 8 arts once-a-week path, a year may keep only its year-end course-level check and give the freed sessions to its heaviest unit, since every id is assessed in its own unit | Arts K to 8 band courses with two checks a year |
| A merged once-a-week session holds at most three days where the weeks allow; a longer merge gets a minute line and is named for the unit plan to test | All arts once-a-week paths |
| A kept card is completed in the last 5 minutes of the run day before the critique, and revised on the critique day, when a 10-day unit's critique day cannot hold it | Arts story units |
| An experience item for TH:Re8 (own experiences) asks for at least one from this year's theater class; an invented one may be the second | Theater courses claiming TH:Re8.1.xa |
| A connecting step on a study day is "practiced, no id claimed" where the unit owns no connecting id | All arts scopes |
| A fold-in receiving day never carries the 10-minute retrieval; a sole teaching day never folds | All arts shorter paths |

## For the structure pass

1. docs/courses/theater-grades-3-to-5/frame.md, Course-level checks table (lead call 7 wording; findings 7 and 8):
   - Year 3 mid-year cell: "characters and a place invented (TH:Cr1.1.3a)" to "characters, a place and a story made
     up from the card (TH:Cr1.1.3a)".
   - Year 3 year-end cell: "a kept reflection line written after the run (TH:Pr6.1.3a, unit 1)" to "a kept
     reflection card written after the run, one line alone and one agreed with the group (TH:Pr6.1.3a, unit 1)".
   - Year 5 mid-year cell: "the scene shaped from the group's questions (TH:Cr2.1.5a), each student's set job" to
     "each student's set job", and "a kept card: a few lines of the character's inner thought (TH:Cr1.1.5c)" to "a
     kept record card of two lines: one group question the scene was shaped from (TH:Cr2.1.5a) and the
     inner-thought line (TH:Cr1.1.5c)".
   - Year 5 year-end cell: "a kept self-review line after the first run (TH:Cr3.1.5a, unit 9)" to "a kept
     self-review line written after the first rehearsal run inside the planning minutes, naming the change made in
     the rerun (TH:Cr3.1.5a, unit 9)".
2. docs/courses/theater-grades-3-to-5/frame.md, Units table unit 1 evidence: "TH:Cr1.1.3a, a guide look-for on the
   showing: a character and a place the group invented, clear to the audience" to "... a character, a place and a
   story the group made up from the card, clear to the audience" (finding 8).
3. Same table, unit 6 evidence: "TH:Re7.1.4a, a kept audience-journal card from the showing day: one choice another
   group's actor made" to "... one choice another group's actor made and one choice the student's own pair made"
   (finding 8).
4. Same table, units 4 and 12 rows, where they say the story map (unit 4) or the script annotation (unit 12) is made
   on the critique day: made at the end of the last fluency run (day 58; day 186) and revised on the critique day
   (finding 3).
5. docs/courses/CALENDAR.md lines 117, 132, 147 (theater 3 to 5 rows): the garbled cells ("week 17 week 17") should
   read "Year 3 mid-year (week 17), Year 3 year-end (week 27)" and the grade 4 and 5 equivalents (same generator fault
   the music fix report names). If CALENDAR.md ever lists once-a-week weeks, theater 3 to 5 on that path has only the
   year-end check (week 26, respond 27).
6. docs/courses/arts/ or build/scope-writes/ARTS-BRIEF.md line "The four processes ... appear in every unit's days":
   to "each year carries all four; each unit at least the processes its frame row names" (lead call 2), for later
   arts writers.

## For Cory

- Supplies ceiling (money), carried from the frame and unchanged: provisional $35, $40 and $30 a class for years 3,
  4 and 5, all optional beside a free path; the frame's pick is a $40 ceiling a class a year.

## Gates

- `python -X utf8 scripts/sequence.py check theater-grades-3-to-5`: 0 failures.
- `python -X utf8 scripts/frame.py check theater-grades-3-to-5`: 0 failures (unit days 60, 60, 60 a year; 192 days).
- `python -X utf8 scripts/frame.py calendar`: runs clean, no failure for this course. The twice-a-week check days
  and weeks are unchanged, so this pass breaks no stagger; the frame change touches only the once-a-week path, which
  the calendar does not read.
- `python -X utf8 scripts/gate.py --course theater-grades-3-to-5`: 0 failing findings for the course (plan failing
  lines fell 1 to 0); the shared index-reports gate exits non-zero on other courses' files (math-kindergarten
  orphans, a science-grade-3 status mark), not this course.

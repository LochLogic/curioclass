# Fixes: scope and sequence of dance-grades-6-to-8, 2026-11-26

Fix pass after the Claude expert read (docs/reviews/sequence-dance-grades-6-to-8-2026-11-26.md), done as
docs/pipeline/briefs/sequence-fix.md with build/scope-writes/ARTS-FIX.md. The Codex read waits for Codex's usage
reset (after 2026-11-30) and gets its own small pass then. Files changed: docs/courses/dance-grades-6-to-8/scope-and-sequence.md,
data/plans/dance-grades-6-to-8/days.csv (by script, csv module) and docs/courses/dance-grades-6-to-8/frame.md (only
where a read finding asks for a frame change). No git.

Counts: applied 27 (expert 8 findings in 12 parts, writer's items 5, lead calls 8, own 4) / not applied 0. Band
items: none (no other arts expert read of 2026-11-26 has an "Across the band" section; dance 3 to 5 finding 7 on the
school_day convention is settled by lead call 8). Codex: none yet.

## Applied

- **Expert 1, settled (units 2, 6, 10 re-merge).** days.csv days 19 to 32, 83 to 96, 147 to 160: sessions 1 days 1-2,
  2 days 3-4, 3 days 5-7, 4 days 8-9, 5 days 10-11, 6 the written day alone (unit day 11's run-through as its
  warm-up), 7 the showing, 8 respond. Scope Shorter path states it.
- **Expert 1, for the lead (frame change), applied.** The only workable option the read names (the other, a 33rd and
  34th session, does not exist): on the once-a-week path only, the written day of units 1, 3, 4, 5, 7, 8, 9, 11, 12
  has no session; its items run as one block (units 1, 9) or two blocks (the rest) of about 12 minutes at the close of
  a later rehearsal session, each a session or more after its teaching, unseen phrase danced at the block's start, one
  prompt per part, scored after the session. Each written day's note and each host session's note names its block.
  frame.md once-a-week bullet names it as the path's one exception to "two kinds of check day, never mixed". The lead
  may revert the frame sentence if it prefers to accept the compression instead.
- **Expert 1, research start.** Days 52, 116, 180 begin in the last ten minutes of session 1, after the hook (notes of
  days 49 to 55, 113 to 119, 177 to 183; frame once-a-week bullet; scope).
- **Expert 1, text.** The Shorter path paragraph says "unit days" and counts them from the unit's first day.
- **Expert 2.** Day 3 goal and note: the waltz's setting on the work card (Vienna's 1860s ballrooms, who danced it,
  what the turning couple meant then, from an open museum or library page, about 5 minutes). Day 55: DA:Cn11.1.6a
  added, last ten minutes draft the waltz context card; day 58 finishes and collects it; day 60 note names both days.
  Scope units 1 and 4 Arc, Assessments and Processes lines changed to match.
- **Expert 3.** Days 32, 96, 160: last ten minutes teach the mid-year check's new material from a Curio Class step
  card (about 16 counts, unscored); days 33, 97, 161 warm-up runs it once; once-a-week in session 8. Scope "New
  material taught first" bullet; frame checks table names the day.
- **Expert 4.** Fold days now 10, 14, 22, 29 / 74, 78, 86, 93 / 139, 150, 157, 169 (notes moved; 41, 59, 105, 123, 187
  cleared). Baseline line added to the table's lead and to the notes of 22, 86, 150, 169. 160 minutes a year kept.
- **Expert 5.** Same-year retrieval warm-ups on days 26, 42, 55, 90, 101, 106, 154, 165, 170 (note and `retrieves`);
  "Same-year retrieval" line in the scope's Readiness and retrieval bullet.
- **Expert 6.** Item wording on days 33, 63, 127, 161, 191 as the read's table; scope "Item wording" bullet; frame
  Course-level checks table cells changed to match.
- **Expert 7.** frame.md: unit 11 row drops "Before unit 12, which stages the revised dance for two spaces"; the
  Leave-out bullet drops unit 12's fallback clause ("revises or stages" now "revises"). No scope change.
- **Expert 8.** Physical education grade 6 unit 6 is weeks 22 to 26 in the scope's lean table, day 11's note and two
  places in frame.md. Day 73 sensitivity line added (and the scope's Sensitivity list). Day 3 out of unit 1's respond
  days, into connect.
- **Writer's item 1** (added samples): frame checks table now names DA:Pr4.1.6c, DA:Pr5.1.7a, DA:Pr4.1.8c.
- **Writer's item 2** (task form): settled by lead call 6; scope For the lead marks it settled.
- **Writer's item 3** (Fluency days): frame Day kinds bullet: three or four in units 1, 5, 9, one to three in the
  14-day units, beside the daily warm-up.
- **Writer's item 4:** frame unit 4 says "unit 1's waltz".
- **Writer's item 5:** replaced by expert 1; scope For the lead rewritten as a settled list.
- **Lead call 1.** Fold table states 10 school days = 4 sessions; 4 fold days a year named. No other reading in the scope.
- **Lead call 2.** Scope "four processes" paragraph: each year carries all four; each unit touches at least the
  frame's named processes; no id outside a unit's owned rows. No unit's claims were stretched (checked: every code on
  every day belongs to its unit's owned rows, the day 55 addition included).
- **Lead call 3.** The "codes not sampled" table stands, with reasons; no frame change proposed.
- **Lead call 4.** Gate baseline refusal ignored (see Gates).
- **Lead call 5.** school_day stays band-wide (1 to 480); the .md says so.
- **Lead call 6.** Notes of days 33, 97, 161 (showing on new material may follow a unit showing) and 63, 127, 191
  (prompts and works differ from the written day two sessions before) say rule 2 is met; scope Checks bullet says
  how the rule is read.
- **Lead call 7.** Checked: no check cell re-asks an item from one to three days before (mid-year checks sample
  unit 1, 5 or 9; year-end checks sample units 1 to 3 of the year). Stated in the scope; no frame wording needed.
- **Lead call 8.** Formula stated once in the .md (ceil(2.5 x n), band-wide; filled school_day wins; not re-counted).
  Script check: every day's school_day equals the formula and every day falls in week ceil(n/2) of its year; checks
  on weeks 17 and 32 in each year.
- **Own 1.** Once-a-week notes said "merged with unit days 78, 79" when they meant course days; every merge note now
  says "days". days.csv.
- **Own 2.** DA:Cn11.1.7a's "suggest why differences developed" was not asked: day 114 (teaching) and day 125 (the
  written item) add one suggestion of why a difference developed. days.csv.
- **Own 3.** Day 191's new Re8.1.8a prompt ordered after the phrase it asks about. days.csv.
- **Own 4.** Rule 2 lists re-run: earlier-grade rows (year 6 retrieves grade 5 rows, years 7 and 8 the year before,
  none two grades idle, so no readiness check); sampled codes per check as the scope table; Collect once (kept
  products collected on making days, none on a check day); each part of each code checked against the words file for
  every end-of-unit item (only Cn11.1.7a was short, own 2); end days 16/17-type pairs in every unit; our words only.

## Not applied

None.

## Settled (for DIGEST)

| Judgment | Reason | Where |
|---|---|---|
| Once-a-week written items as one or two 12-minute timed blocks, a session after their teaching, in every unit without a light session | the only way to keep every assessed part in 32 sessions | frame once-a-week bullet; scope Shorter path; days.csv notes |
| A one-item written day (units 1, 9) gets one block, not two | one prompt per part, nothing padded | days 15, 17, 143, 145 |
| Same-year retrieval is the day's five-minute warm-up, not extra minutes | no day's minute budget changes | days 26, 42, 55, 90, 101, 106, 154, 165, 170 |
| Mid-year check material taught in the respond day's last ten minutes | the showing day has no teaching minutes | days 32, 96, 160 |
| "Why a difference developed" asked on the teaching day and the written item | Cn11.1.7a's last part | days 114, 125 |

## For the structure pass

- docs/agents/decisions/DESK-ANSWERS.md: add one line, "2026-11-26, fix pass (dance 6 to 8 expert read finding 1):
  on the once-a-week path the written check day of a unit with no light session runs as one or two timed blocks of
  about 12 minutes, the path's one exception to two check days; frame.md once-a-week bullet." The lead confirms or
  reverts the frame sentence.
- docs/courses/CALENDAR.md: document school_day for K to 8 band courses as counted across the whole band (lead call
  5); and note that physical education grade 6 unit 6 runs weeks 22 to 26 if CALENDAR.md cites it.
- data/plans/calendar.csv: regenerate with `frame.py calendar` at commit (no day or check moved here).
- Other arts courses with the same once-a-week overload (media arts 3 to 5 finding 2, theater 6 to 8 finding 1,
  dance 9 to 12) may want the same timed-block exception; the lead decides per frame.

## For Cory

Nothing on scope, money, people or audience.

## Gates

- `scripts/sequence.py check dance-grades-6-to-8`: 0 failures.
- `scripts/frame.py check dance-grades-6-to-8`: 0 failures (notes only: 60 unit days a year, 192 days).
- `scripts/frame.py calendar`: dance 6 to 8 checks stay on weeks 17 and 32 in grades 6, 7 and 8; no stagger break
  (no frame change moved a day or a check).
- `scripts/gate.py --course dance-grades-6-to-8`: 0 failing lines for the course; refuses only for no baseline (lead
  call 4). Its index-reports gate exits 1 on another course (science-grade-3 day 12 changed since its sign-off), not
  this one. One lint line ("Curio" split across a line break in frame.md) was found and fixed.

# Fixes: scope and sequence of theater-grades-k-to-2, 2026-11-26

Fix pass per build/scope-writes/ARTS-FIX.md and docs/pipeline/briefs/sequence-fix.md. One read so far: the Claude
expert read docs/reviews/sequence-theater-grades-k-to-2-2026-11-26.md. The Codex read waits for Codex's usage reset
(after 2026-11-30) and gets its own small fix pass then.

**Counts.** Applied: expert 12 of 12 findings (every row of its "Settled by the expert" table; finding 1 and finding 6
change the frame, so frame.md and the scope moved together; findings 9 and 11 were judgment calls, applied at no day),
lead calls 8 of 8 that touch this course (call 9 is theater 9 to 12 only), band items 0 (no other arts expert read
has an "Across the band" section), own 4. Not applied: expert 1 part (finding 12's calendar.csv sync, which is the
lead's at commit; listed under the structure pass). Codex: 0 (read not yet written).

## Applied

- **Expert 1** (once-a-week path, serious; frame layer). frame.md: the session counts become year K 8, 8, 7, 5 and
  year 1 7, 9, 7, 5 (year 2 stays 8, 8, 7, 5; still 28 unit sessions a year), the five-session sentence adds that a
  story unit's study session holds only its study and teaching days, the check-session weeks become 17 and 26 in
  every year with a line that year K's week 17 sits in the kindergarten core weeks 14 to 18 (CALENDAR.md rule 1
  allows it for an arts special), the Units table cells for units 1, 2, 3, 5 and 6 carry the new counts, and For the
  lead item 1 names the new weeks. Scope: every unit's once-a-week line rewritten as the expert set it (unit 3 keeps a
  making session of its own; units 4, 8 and 12 split study 55 to 57, 119 to 121, 183 to 185 from acting, critique and
  revision 58 to 60, 122 to 124, 186 to 188; unit 6 nine sessions of three days; unit 10 145 to 147, 148 to 150,
  151 to 153) and the Shorter path summary. days.csv unchanged (the path lives in the .md).
- **Expert 2** (day 184 over 40 minutes). days.csv day 184 goal and note: the short third race telling is heard inside
  the retrieval opener, whose th-g1-story task is asked of it; the rest of the day goes to the Cherokee story and the
  three-way compare. .md unit 12 Retrieval line and candidate (b).
- **Expert 3** (sole teaching days on the fold list). .md Shorter path: 68 replaced by 70 (into 69, a 15-minute guided
  Turnip segment, saves 25) and 153 by 171 (into 172, its first 15 minutes, saves 25). Both now sit among the spares
  (lead call 1); the rule "the only teaching day of any id never folds" is written into the paragraph.
- **Expert 4** (baseline looks). days.csv notes: the baseline sentence moved from day 3 to 9, 21 to 25, 41 to 45, 132
  to 134, 168 to 166, each naming why the new day is the first where the look-for is performed. .md unit 1, 2, 3, 9
  and 11 lines. Year 2's named fold list: 168 (into 167, a 10-minute segment, saves 30) replaces 166.
- **Expert 5** (each part on two checks). days.csv day 53 goal adds "each child adds one idea of their own to the
  scene" and day 181 goal adds "each group says one line, tries it another way at the teacher's prompt and keeps the
  change", each note saying the item fits inside the group's 4 minutes. .md Course-level checks table, both rows.
- **Expert 6** (plans finished after the making; frame layer). days.csv: day 106 begins the kept prop-sketch; day 110
  (the unit's one making day) labels it with the teacher and now carries TH:Cr1.1.1b, TH:Re9.1.1b, TH:Pr5.1.1b, scored
  with the showing; day 113 is only the revision with each child's "what we changed" line (codes TH:Pr5.1.1b,
  TH:Cr3.1.1c); day 171 draws the set plan, day 172 labels it (scored with the showing), day 177 is only the revision
  (codes TH:Pr5.1.2b, TH:Re9.1.2b); days 114 and 178 notes name the new days. frame.md unit 7 and unit 11 evidence
  cells: "begun on the planning day and labeled on the making day, before the props are finished" and "drawn on the
  planning day and labeled on the first making day, before the set is built". .md units 7 and 11 arcs, Processes and
  end-of-unit lines; Shorter period sentence names making days 110 and 172 to 173.
- **Expert 7** (safe use). .md "Equipment and safe use": the unit's hazards line holds on every floor day; notes name
  only day-specific controls. days.csv: the heap control on 74 to 78, no falls (a slow sink to sitting) and the
  arm's-length mirror on 95 to 100 (replacing the general line), no weapons or contact on 112 to 114, the giant's slow
  walk and the freeze for "scared" on 155 to 158.
- **Expert 8** (two critiques in unit 10). days.csv day 155 goal: rehearse the three moods with the teacher's
  side-coaching, no partner routine; day 156 note: the TH:Cr3.1.2b look-for reads from its critique. .md unit 10 arc
  and Processes.
- **Expert 9** (day 1 crowded; judgment call). days.csv day 1 note and .md unit 1 candidate line: the unit plan may run
  day 1's entering seated so the freeze signal is learned before anyone moves. Worded as "may", for the unit plan.
- **Expert 10** (30-minute showing). .md Shorter period: at 30 minutes groups run about 3.5 minutes (21), the same for
  the teacher's-table day of units 6 and 10.
- **Expert 11** (theater makers in units 5 and 9; optional, 0 days). days.csv day 68 names kamishibai again as a real
  form from unit 1's collection page; day 129 adds one line on a living storyteller or company that tells the
  Panchatantra to children, picked by the unit plan with its rights line. .md units 5 and 9 Processes and For the lead
  item 6 (the lead may strike them).
- **Expert 12** (stale notes). .md core weeks K 14 to 18; For the lead item 5 closed by CALENDAR.md rule 1 (and extended
  to year K's once-a-week week 17); For the lead item 2 shortened, now saying calendar.csv is brought in line at commit.
- **Lead call 1** (10 days short). .md Shorter path: four named fold-in days a year, one per unit (K 7, 24, 29, 46;
  year 1 73, 86, 95, 99; year 2 136, 151, 168, 175), saving 140, 130 and 135 minutes and leaving 60 sessions; the
  other six a year listed as spares in order (all folded: 340, 300, 305, leaving 54). The "10 course days" reading
  dropped.
- **Lead call 2** (four processes). .md "The four processes" bullet replaces "Four processes in every unit": each year
  carries all four, each unit at least what its frame row names, practice named as practice, no id claimed outside a
  unit's owned rows. No unit's claims had been stretched; nothing else changed. For the lead item 3 closed. The expert's
  practice asks (finding 11) applied on existing days.
- **Lead call 3** (codes not sampled). The .md already names the 44 unsampled ids with the reason; kept. The frame
  option is under the structure pass.
- **Lead call 4** (no gate baseline). Nothing needed.
- **Lead call 5** (band-wide school_day). Kept 2 to 479; the .md says it counts across the whole band as frame.py reads
  it.
- **Lead call 6** (two-week rule). days.csv notes on check days 37, 53, 103, 117, 161, 181, and the .md paragraph after
  the checks table: a fresh scene card with its own items, drawn from earlier units, meets the rule though it follows
  a unit showing.
- **Lead call 7** (frame check cell re-asking recent items). Checked: every sampled id comes from a unit that ended at
  least two weeks before its check (day 53 samples units 1 and 2, not unit 3 assessed on days 50 and 51; the same in
  every year). Nothing to change; the .md says so once.
- **Lead call 8** (school_day formula). .md states once: school_day = 160i + 5(week - 1) + 2 or + 4, week of the year
  = (school_day - 160i - 1) // 5 + 1. Script check: every unit and check falls in the frame's weeks (checks K 19 and
  27, year 1 20 and 27, year 2 17 and 27; units in their listed weeks). No school_day changed.
- **Band items.** None: no other arts expert read of 2026-11-26 has an "Across the band" section.
- **Own 1** (rule 2 rerun by script). All 65 ids sit only in their own year; every id is on a teaching day before any
  check; no fold-in day or spare is a baseline, critique, revision, check, respond or family day, or the only teaching
  day of any id. Every year 1 and 2 unit retrieves its one-grade-back row on day 2 (day 184 for unit 12, as the frame
  sets); no row needs a readiness check.
- **Own 2.** Day 113's and day 177's codes trimmed to what a revision day teaches, and day 110's widened to the three
  prop-sketch ids it now labels, so the codes column matches the days (expert 6 follow-through).
- **Own 3.** The heap, falls, weapons and giant controls written from the frame's own hazards cells, word for word in
  substance, so the days and the frame agree.
- **Own 4.** .md header line names this fix pass.

## Not applied

- **Expert 12, calendar.csv sync.** Not this course's file; the lead regenerates it with `frame.py calendar` at commit
  (lead call 8). Listed under the structure pass.
- **Codex read.** Not yet written; its own fix pass follows after 2026-11-30.

## Settled

| Judgment | Reuse |
|---|---|
| A K to 2 once-a-week session holds about three teaching days at most; a making day keeps a session of its own | Every K to 5 arts once-a-week path |
| A story unit's first once-a-week session holds only its study and teaching days; acting starts in session 2 | Arts story units with a family showing |
| A baseline look sits on the first day the main look-for is performed, never on a drill before it | All arts scopes |
| A kept plan card is begun before the making and labeled during it; the revision day adds only a "what we changed" line | Arts units scoring a plan |
| A short extra work for a three-way compare is heard inside the retrieval opener when the retrieval task can be asked of it | Arts and ELA days that add a telling |
| A unit's hazards line holds on every floor day; notes name only day-specific controls where a hazard is rehearsed | All arts scopes with a floor |

## For the structure pass

1. data/plans/calendar.csv: regenerate with `python -X utf8 scripts/frame.py calendar` at commit (lead call 8); it still
   holds frame.py's even spread for this course (school days 3, 45 and so on against days.csv's 2, 44). No school_day
   changed in this pass.
2. docs/courses/CALENDAR.md: if it records once-a-week check weeks for theater K to 2, year K's check session moves from
   week 19 to week 17 (frame "The once-a-week path"); the full-path weeks (19 and 27, 20 and 27, 17 and 27) are
   unchanged. Rule 1 covers week 17 sitting in the kindergarten core weeks.
3. docs/courses/theater-grades-k-to-2/frame.md, For the lead item 1, last sentence ("the grade 2 mid-year respond
   session falls in week 18 ... the calendar pass should decide whether the rule counts it"): replace with "closed:
   CALENDAR.md rule 1, arts specials do not count against the stagger" (expert 12; the scope already closes it).
4. Optional, lead call 3: docs/courses/theater-grades-k-to-2/frame.md Course-level checks table, year-end rows: a
   talk-free kept card for the third unit's ids (a prop-sketch or set-plan item) would raise the sample from 21 of 65
   ids. Not required; the scope names the unsampled ids with the reason.
5. Theater 3 to 5 read finding 1 is the same kind as this course's finding 1; its fixer rebalances its own frame.

## For Cory

Nothing.

## Gates

- `python -X utf8 scripts/sequence.py check theater-grades-k-to-2`: 0 failures.
- `python -X utf8 scripts/frame.py check theater-grades-k-to-2`: 0 failures (unit days by year K 60, 1 60, 2 60).
- `python -X utf8 scripts/frame.py calendar`: 0 failures. This course breaks no stagger rule: arts are specials in K to
  2 (CALENDAR.md rule 1), and the frame change moves only once-a-week sessions, no full-path day or week.

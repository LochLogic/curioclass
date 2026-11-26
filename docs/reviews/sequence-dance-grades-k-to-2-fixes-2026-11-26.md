# Fixes: scope and sequence of dance-grades-k-to-2, 2026-11-26

Course `dance-grades-k-to-2`. Brief: docs/pipeline/briefs/sequence-fix.md as build/scope-writes/ARTS-FIX.md sets it
for the arts run. One read applied: the Claude expert read docs/reviews/sequence-dance-grades-k-to-2-2026-11-26.md.
The Codex read waits for Codex's usage reset (after 2026-11-30) and gets its own small fix pass. Files changed:
docs/courses/dance-grades-k-to-2/scope-and-sequence.md, data/plans/dance-grades-k-to-2/days.csv (by script) and
docs/courses/dance-grades-k-to-2/frame.md (where findings 1, 3 and 4 change the frame).

**Counts.** Expert: 9 of 9 findings applied (two with a stated deviation from the expert's wording), 8 of 8 settled
rows applied (one with a stated deviation). Codex: 0 (read not yet written). Lead calls (ARTS-FIX 1 to 8): 8 applied
(call 4 needs nothing). Band items: 0 touch this course (no other arts read has an "Across the band" section; the one
cross-course item, dance 3 to 5 finding 7 on the school_day convention, is settled by lead calls 5 and 8). Own: 6
applied. Not applied: 0.

## Applied

- **Expert 1** (checks re-collect the unit just scored). days.csv days 35 to 36, 51 to 52, 97 to 98, 113 to 114, 161
  to 162, 177 to 178: `codes` now hold only the live sample; goals rewritten; each note names the ids "reused from
  day N's record, not collected again". Live samples: day 35 Pr5.1.Kb, Pr4.1.Kb, Pr4.1.Ka, Pr5.1.Kc; day 51
  Cr1.1.Ka, Pr4.1.Kc, Cr2.1.Kb; day 97 Pr5.1.1c, Pr4.1.1b, Pr4.1.1a; day 113 Cr1.1.1b, Re7.1.1a, Cr2.1.1b; day 161
  Pr4.1.2b, Pr5.1.2c, Pr4.1.2a; day 177 Cr1.1.2b, Cr2.1.2b. frame.md Course-level checks table: all six cells
  rewritten to match, plus one line in the paragraph under it. Scope: Course-level checks table, its notes, the
  unsampled list and For the lead items 1 and 2 rewritten. Two deviations from the expert's list, both because of
  lead call 7 and the frame's "at most one talk or show item a child":
  - Day 113 keeps Re7.1.1a as the expert proposed, but draws it from unit 5's folklórico work card instead of a new
    teacher phrase, so it is an earlier unit's work in a different form from day 111's unseen phrase (lead call 7).
  - Day 177 drops Re8.1.2a from the live sample. The expert kept it as a talk item and also made Cr2.1.2b's reason
    "the one talk item"; both cannot hold. Re8.1.2a was scored on day 175, so it is reused from that record. Year 2
    samples 5 ids live, the band 18 of 63.
- **Expert 2** (each part of each code). Check days as above, with every part on each goal. Day 110 goal and note:
  "why the dancer might have picked it" added to the Re9.1.1a talk item; day 159 goal and note: Cr1.1.2a's two parts
  (moves that show the card's starting point as a look-for; the kept card's two more idea places). Scope unit 7 and
  unit 10 Assessments match. The day 113 Cr3.1.1a and day 177 Cr3.1.2a gaps went with the codes (now reused).
- **Expert 3** (once-a-week merges). Scope "Once a week" lines: unit 1 now 9 sessions (4 to 8 merged), unit 3 37 to
  39; 40 to 43; 44 to 47, unit 4 6 sessions (53 to 55; 56 to 58; 59 to 61), unit 7 99 to 101; 102 to 105; 106 to 109,
  unit 8 115 to 117; 118 to 121; 122 to 125, unit 11 163 to 165; 166 to 169; 170 to 173, unit 12 179 to 181; 182 to
  185; 186 to 189, each third session noting the critique and the rehearsed change together. Shorter path: year K
  counts 9, 7, 6 and 6, and the line on the retrieval running in the first session after the hook. frame.md Units
  table: unit 1 "Once-a-week path: 10 sessions" to 9, unit 4 "5 sessions" to 6 (year still 32).
- **Expert 4** (physical education in the same weeks). days.csv notes on days 66 and 70 (physical education grade 1
  unit 8) and day 130 (grade 2 unit 15), in the expert's words. Scope Leans paragraph rewritten: names physical
  education K unit 7, grade 1 unit 8 and grade 2 unit 15, drops "No bridge needed", and names computer science grade
  2's dance cards as computer science's lean. frame.md physical education table: three rows added (da-k-ideas with
  k-express-feel; da-g1-technique, da-g1-elements with g1-travel-ways, g1-move-words; da-g2-technique with
  g2-travel-jump-balance).
- **Expert 5** (fold-in days). Fold-in note removed from days 24, 44, 69, 86, 122, 133 and 150; added to 6, 14, 73,
  89, 106, 138 and 153; kept on 11, 27, 103, 167 and 170. Each now reads "no baseline look, no candidate work and
  nothing assessed". Day 167's note says its candidate is a dropped one (nothing watched). Scope Shorter path lists
  the new days and why day 41 is kept.
- **Expert 6** (same-year retrievals). days.csv day 102 `retrieves` + da-g1-elements and note; day 165 + da-g2-elements
  and note. Scope same-year list and the units 7 and 11 "Why this order" lines.
- **Expert 7** (year-end checks on a dance months old). Days 112 and 176 notes: the pairs not retrying rehearse the
  unit 5 (unit 9) dance from its step card; days 113 and 177 notes: the warm-up runs it once. Scope units 7 and 11
  Assessments name it.
- **Expert 8** (baseline looks on first-teaching days). Day 104 and 168 "Baseline look begins" removed; day 103 note's
  pointer removed; baselines added on 171 and 185; day 189 note now points at 185. Deviation: unit 7's baseline goes
  to day 107, not 106, because the expert's own finding 5 makes 106 a fold-in day with no baseline; 107 is unit 7's
  first making day, as 171 is unit 11's. Scope units 7, 11 and 12 Assessments updated.
- **Expert 9** (text). "168 in the twelve units" to 180; For the lead item 3 now points to the frame's For the lead 1.
- **Lead call 1.** Four fold-in days a year (finding 5); the scope names the 10 school days reading only.
- **Lead call 2.** Scope "Kinds of day" gets a four-processes line: each year has all four, each unit claims only
  what its frame row names, other processes are touched as practice; no unit's claims were stretched, so no id moved.
- **Lead call 3.** The unsampled list names the 45 ids with reasons; a further frame change is under For the lead.
- **Lead call 4.** Nothing to do.
- **Lead call 5.** school_day stays counted across the band (1 to 480); the .md says so.
- **Lead call 6.** Each check note now says it is a showing on earlier-unit work with its own items.
- **Lead call 7.** Applied through finding 1: reused records named; live items drawn from earlier units in a new form.
  The frame cells were rewritten in frame.md because finding 1 asks for the frame change.
- **Lead call 8.** The scope's First page states the formula once: for day n in year y with m = n - 64y,
  school_day = 160y + 5(ceil(m / 2) - 1) + 2 (m odd) or + 4 (m even). The fix script asserted it on all 192 rows and
  that each check falls in its frame week (18, 26; 17, 25; 17, 25).
- **Own 1.** Day 97: Pr4.1.1a asked in every part (shape, level and facing changes, curved and zigzag paths, a line
  then a circle); the expert's "a path with a facing change" covered only part.
- **Own 2.** Day 161: Pr4.1.2a adds "circle around a spot and then turn in place" (circling told from turning); the
  expert's wording left that part out.
- **Own 3.** Day 177's two-talk-item clash (see Expert 1).
- **Own 4.** Day 106's baseline and fold-in clash (see Expert 8).
- **Own 5.** Scope unsampled count recounted after the rewrite: 18 live (7, 6, 5), 45 not, the reused ids marked.
- **Own 6.** Rule 2 lists re-run: the earlier-grade rows table still holds (every row one grade back, retrieval on day
  2, no readiness owed); each check's codes now asked in every part; Collect once holds on all six checks; end days
  cover every owned id (gate); no em dashes, "Curio Class" in full, US spelling (grep).

## Not applied

None.

## Settled (for DIGEST)

| Judgment | Reason |
|---|---|
| A check's `codes` list only the live sample; ids reused from the unit record are named in the note, not in `codes` | The record is not collected again, so the check day does not claim it |
| When a reused id and a new talk item compete for the one talk item a child, the reused id stays reused | Frame rule: at most one talk or show item a child after the group's turn |
| A response id sampled live two days after its unit scored it is drawn from an earlier unit's work card, not a new teacher phrase | Lead call 7: earlier units' works in a different form |
| A baseline that clashes with a fold-in day moves to the unit's first making day | Keeps both the short year and the growth evidence |
| Expert-proposed look-for wording is still checked against the words file part by part | Days 97 and 161 needed parts the read left out |

## For the structure pass

- docs/courses/physical-education-grades-k-to-2/frame.md, Cross-subject table, after line 301 (the
  g1-dance-moves row): add three rows naming dance K to 2: "| g1-travel-ways, g1-move-words (unit 8, grade 1 weeks 1
  to 4) | arts da-g1-technique, da-g1-elements (dance K to 2 unit 5, grade 1 weeks 1 to 9) | PE: ways to travel and
  changing path, speed and direction as motor skill; dance: the traveling used as material for paths, formations and
  speeds | Same weeks; PE teaches its cue words; dance uses them where taught and teaches only the dance words |";
  "| g2-travel-jump-balance (unit 15, grade 2 weeks 1 to 4) | arts da-g2-technique (dance K to 2 unit 9, grade 2 weeks
  1 to 9) | PE: a linked travel, jump and balance as motor skill; dance: pathways and sequences that travel | Same
  weeks; as above |"; "| k-express-feel (unit 7, kindergarten weeks 29 to 32) | arts da-k-ideas (dance K to 2 unit 2,
  kindergarten weeks 11 to 17) | PE: moving to show a feeling; dance: moves that express a feeling | Dance teaches
  first; PE may retrieve the feeling dances |".
- data/plans/calendar.csv: regenerate with `frame.py calendar` (lead call 8); no week changes for this course.
- docs/courses/CALENDAR.md: document the band-long school_day count (lead call 5, lead's task).
- data/plans/later.csv L107: if the row cites a per-course sampled count, dance K to 2 is now 18 of 63 live.
- frame.md's Course-level checks cells were changed here (finding 1 asks for it); nothing more for this frame.

## For Cory

None new. The frame's own items stand (a filmed set of unseen phrases; the $50 supplies ceiling).

## Gates

- `python -X utf8 scripts/sequence.py check dance-grades-k-to-2`: 0 failures.
- `python -X utf8 scripts/frame.py check dance-grades-k-to-2`: 0 failures (unit days 60 a year; 192 days, 180 in units).
- `python -X utf8 scripts/frame.py calendar`: dance K to 2 at K weeks 18 and 26, grades 1 and 2 weeks 17 and 25,
  unchanged; no stagger break (arts are specials in K to 5 and do not count against it). No frame change moved a day
  or a week, so nothing new for the regenerated calendar.

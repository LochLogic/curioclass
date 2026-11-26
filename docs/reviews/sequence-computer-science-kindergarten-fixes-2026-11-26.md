# Fixes: scope and sequence of computer-science-kindergarten, 2026-11-26

Applied 11, not applied 1. By source: expert read 9 applied (findings 1 to 6, and finding 7's year-end sample, day
kind and stale wording), 1 not applied (finding 7's source-map.csv, waits on L149); lead calls 2 applied (1, 3; 4, 5
and 8 carried the frame wording above); band items 0 (no item in the grades 1 to 5 reads touches kindergarten); own 2.
No Codex read yet (after 2026-11-30, its own pass).

## Applied

- **Expert 1** (days.csv days 5, 12, 21, 27, 31; .md Evidence, units 1, 3, 5 and the checks table; frame.md units 1, 3,
  5 and the Course-level checks table): every check item now asks each part of its id. Day 12 PS-01: follow a new
  three-card picture algorithm (draw a circle, color it, draw a line under it), then order a routine and name it.
  Days 21 and 27 RD-06: a dot where the robot is after each card on a three-square strip, then the end square
  circled. Day 5 HW-11: tool, job and person triples. Day 31 CE-16: one device circled in each of a home, a school and
  a workplace picture. Day 27: the answer-card placing carries DI-09's collect part.
- **Expert 2** (days.csv days 5, 6, 12, 13, 21, 22, 27, 28, 31, 32; .md Evidence and Shorter path; frame.md Evidence):
  about 4 minutes a group of six; groups not reached are heard in the first 10 minutes of the respond day at every
  length, collected once. Day 12's IM-03 answer runs on three picture prompts (choose, parts, order), one word each.
  Days 5 and 31 got the same line too, for one rule across all five sittings.
- **Expert 3** (days.csv `retrieves` days 12, 16, 18, 20, 21; day 5's opener; .md Readiness and retrieval): day 12
  k-tools-jobs, 16 k-sort-attributes, 18 k-people-steps, 20 k-public-private, 21 k-device-manners; day 5 keeps
  k-tools-jobs as a spoken "what is this tool's job" with the mystery bag. Days 15, 17, 19 keep the previous day.
  Day 27: see Own 1.
- **Expert 4** (days.csv day 15 goal and note; .md unit 3; frame.md unit 3 session 2): trace the worked path, then
  pairs lay and walk it and the same path one square longer; the first own route is day 19.
- **Expert 5 / lead call 1** (days.csv days 11, 26; .md units 2 and 4, For the lead): `observe` cleared, notes now
  "Notes by exception on the class checklist"; the observe sentences and For the lead 1 removed.
- **Expert 6** (days.csv): frame sensitivity lines on days 3, 8, 25, 27, 31; online-safety line on days 5, 6, 12, 13,
  27, 28; put-away line on day 14; day 21's route on a table mat; day 22 has the floor-grid lines and put-away;
  trailing spaces on days 17 and 18 cut. .md safety list now "days 14 to 20 and 22"; unit 1 and unit 4 sensitivity
  lists match the days.
- **Expert 7, year-end sample** (days.csv days 27 and 28 skills and codes; .md checks table and "Codes no check
  samples"; frame.md Course-level checks table): day 27's paper task adds "glue three arrow cards to reach the star"
  (PD-04) and "circle what this sign tells us to do" (VD-05). Only HW-11 (day 5) and the unit 5 ids stay off a check,
  with the reason named. Applied under lead calls 4 and 8 (check-table wording, no unit, day count or owned row moved).
- **Expert 7, day 25's kind / lead call 5** (frame.md Day kinds; .md unit 4; days.csv day 25 note): the bullet now
  reads unit 4 session 4 for Application, session 3 Understanding; For the lead 2 removed.
- **Expert 7, stale wording / lead call 3** (frame.md For the lead 4): "until it is loaded" now inside
  Pending(later.csv L149 ...). frame.py check passes.
- **Own 1** (days.csv day 27): `retrieves` set to k-people-steps, not the read's k-symbols. With the VD-05 item added,
  k-symbols is scored on day 27, so a k-symbols opener would warm up a scored row (the read's own rule). k-people-steps
  is the row the read found least retrieved, and day 27 scores nothing of it.
- **Own 2** (.md line 3): "catalogue" to "catalog".
- **Rule 2 re-run**: no earlier-grade rows (kindergarten, no `assumes`); each check's codes match its items; collect
  once holds (spoken overflow is the same sitting's evidence); no check repeats a task form from the two weeks before
  (the strip form is on day 21 and day 27, six weeks apart); our words throughout. Nothing else found.

## Not applied

- **Expert 7, source-map.csv**: waits on L149 (lead call 2). The .md's "Sources not yet loaded" list stays as the
  placement record and now says so.

## Settled

| Judgment | Reason |
|---|---|
| A check day's opener never retrieves a row the same day scores; pick the least retrieved row it does not score | Keeps the check clean and feeds the spacing report |
| Spoken overflow to the first 10 minutes of the respond day holds on every check, at every length | 30 children in five groups do not fit a 20-minute sitting |
| A "describe how" id at K is scored on paper by a dot after each step, not by the end state alone | The verb is seen with no reading and no spoken minutes added |
| A check item for a "for different users" or "home, school and work" id asks each named part | Each part of each code (rule 2) |

## For the structure pass

- None for shared files. The frame's For the lead 2 (APPROACH.md Pacing line for the check-stands-for-unit pattern)
  stays the lead's, as before; sequence.py already accepts it.

## For Cory

Nothing.

## Gates

- `scripts/sequence.py check computer-science-kindergarten`: 0 failures.
- `scripts/frame.py check computer-science-kindergarten`: 0 failures (was 1, line 238).
- `scripts/frame.py calendar`: grade K computer science weeks 12 and 27, shared with health (12, 27) and library
  (27), all specials under CALENDAR.md rule 1, so no stagger break; no frame change moved a week.
- `scripts/gate.py --course computer-science-kindergarten`: exit 0, 0 failing findings against the baseline, 1 new note line (the plan gate's failing lines fell 1 to 0). The
  index-reports gate exits non-zero, as it did before this pass. The one baseline lint line is "Open
  Government Licence" in frame.md, the known exception (lead call 12).
- Defects logged: 10 expert rows (9 fixed, 1 rejected) and 2 writer rows, all `--made-at=scope`.

# Fixes: scope and sequence of computer-science-grade-4, 2026-11-26

Applied 9 / not applied 0. Expert read: 6 findings applied (plus every row of its Settled table), 0 not applied.
Codex read: none yet (waits for Codex's usage reset after 2026-11-30, its own fix pass then). Lead calls (CS-FIX.md):
1, 4, 5, 7 applied; 2, 3, 6, 8 to 12 needed nothing here. Band items: none (no other computer science read names an
item that touches grade 4). Own: 1.

## Applied

- **Expert 1** (days.csv days 5, 17, 31; scope units 1, 3, 5 Assessments; frame.md Units table end-of-unit cells for
  units 1, 3 and 5): day 5 asks for two new faults, one hardware (an accessory cable) and one software (a setting or
  the wrong window), each worked to a safe fix that is checked (E4-SYS-HW-12), and a device life with one effect on
  resources, one on the environment and one user action (E4-SYS-IM-15). Day 17's case card asks for one person and one
  group who could be helped or hurt (E4-DAT-IM-11). Day 31's worker case asks what they had to learn when the tool
  arrived and one way they keep learning (E4-SOC-CE-19). The frame carried the same gap: fixed there under lead call 4.
- **Expert 2** (scope Shorter path): the day 6 fold row now names where the E4-SYS-NT-14 retry (day 11's retrieval)
  and the E4-SYS-IM-15 retry (day 9's retrieval in the short year) go, and day 12 adds both to its reteach. "The two
  30-minute sittings" now reads "The four". In a 30-minute period day 5's fault items run on picture fault cards with no
  device close (also in day 5's note).
- **Expert 3** (days.csv day 9; scope unit 2 Assessments; scope For the lead): day 9's `assess` cleared; note now
  "The fixed algorithm is collected and read beside day 11; it is practice, not scored." For the lead 1 dropped (lead
  call 1). Day 23 keeps `end` (expert settled).
- **Expert 4** (days.csv days 23, 24; scope unit 4 Assessments and year-end paragraph; frame.md year-end check row):
  the team quiz rubric has three look-fors per member, the third being the member's test-table rows (tested when the
  part was added and again after the revision); day 24 says E4-PRO-TR-08 is met by the debug item together with that
  record.
- **Expert 5** (days.csv days 1, 13, 14, 15, 19, 20): days 19 and 20 carry unit 4's driver and navigator line
  (switch every eight minutes, a student who cannot use the keyboard or mouse navigates); days 1, 13, 14, 15 add
  "Pairs switch at the keys halfway."
- **Expert 6** (days.csv day 11; scope mid-year paragraph; frame.md mid-year check row and Models carried row): the
  E4-SYS-HW-12 sample is "a new picture fault card that shows the device's response after each chosen step".
- **Lead call 5** (frame.md Day kinds bullet; scope Kinds bullet; scope For the lead 2 dropped): the Fluency list no
  longer names unit 4 session 3; the bullet says that session modifies a working program but first teaches the
  test-table and the piece-by-piece method, so it is Understanding, as GLOSSARY says.
- **Lead call 7**: eight defect rows logged with `plan.py defect --status=fixed --made-at=scope` (expert 1 twice,
  once for days.csv and once for frame.md; expert 2 to 6; lead call 5).
- **Own**: the scope's header line now says it was fixed the same day after the expert read. The rule 2 lists were
  re-run: every assumed row is grade 3's and opens as retrieval on its first-use day. Each check's sampled codes
  match the frame (day 11: PS-01, IM-03, HW-12, SE-13; day 24: unit 4 plus PS-01, IM-11, NT-14). The three unsampled
  codes (IM-15, DC-09, DI-10) stay listed. Every part of each code now has its own prompt. End days are 5, 17 and 31,
  with days 11 and 24 standing for units 2 and 4. The read's own words are used (no "Base" outside credit lines).
  Nothing else was found.

## Not applied

None.

## Settled (for DIGEST)

| Judgment | Reason |
|---|---|
| A code with two named parts (hardware and software; resources and environment; individuals and groups; adopts and keeps updating) gets one prompt per part on its end-of-unit item | A met mark must be backed for each part |
| A course-level check standing for a unit's end needs no `end` on a unit teaching day; a kept-work practice is "read beside, practice, not scored" | sequence.py takes a C Check the day after the unit (lead call 1) |
| A scored team product that is a real part of the end-of-unit keeps its `end` (grade 4 day 23) | Frame-write rule 19 |
| "Repeatedly through development" (TR-08) is met by the sitting's debug item together with the team build's test-table record | One item cannot show the repeated part |
| A fault sampled on paper uses a fault card that shows the device's response after each step, never a still picture | An apply look-for needs a fix and a check |
| A short year that folds a respond day names a retry for every code the folded day covered | Folded work must land somewhere |

## For the structure pass

None. The frame changes are wording only (no unit, day count or owned row moved), so calendar.csv and frames.csv
need nothing.

## For Cory

Nothing.

## Gates

- `python -X utf8 scripts/sequence.py check computer-science-grade-4`: 0 failures.
- `python -X utf8 scripts/frame.py check computer-science-grade-4`: 0 failures (5 units, 32 days). `frame.py check`
  across all frames: no failures.
- `python -X utf8 scripts/frame.py calendar`: grade 4 computer science checks stay in weeks 11 and 24. Computer science
  in K to 5 is a special (CALENDAR.md rule 1), so this course breaks no stagger rule.
- `python -X utf8 scripts/gate.py --course computer-science-grade-4`: 0 failing findings against the baseline. The one
  lint line is "licence" in "Open Government Licence v3.0" (frame.md line 66), a proper name kept as a known exception
  (lead call 12). The gate's index-reports step exits non-zero for reasons outside this course.

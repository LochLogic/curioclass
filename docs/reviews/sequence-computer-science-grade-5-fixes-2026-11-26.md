# Fixes: scope and sequence of computer-science-grade-5, 2026-11-26

Fix pass after the Claude expert read docs/reviews/sequence-computer-science-grade-5-2026-11-26.md, under
build/scope-writes/CS-FIX.md and docs/pipeline/briefs/sequence-fix.md. The Codex read waits for Codex's usage reset
(after 2026-11-30) and gets its own small fix pass then.

Counts: applied 20 (expert 8 findings and all 12 Settled rows, lead calls 1, 2, 4, 5, 7, 11; own 2) / not applied 0.
Neighbor reads (grades 4 and 6 and the rest of the computer science reads): no item crosses into grade 5.

## Applied

- **Expert 1** (days.csv days 20, 22, 23; frame.md Devices bullet and unit 4 session 3): the paper path's pretend
  model is a partner or card procedure that may look only at the training cards and labels each test card by the
  training card it matches most closely on stated features (size, number of corners, line thickness, tilt), never by
  knowing the shape. Day 20's hook gets a printed result card of that model's wrong answers on the paper path; day 23's
  paper path adds the chosen training cards and recounts. The .md Devices bullet and unit 4 arc say so.
- **Expert 2** (days.csv day 16; frame.md unit 3 session 6; .md unit 3 arc): day 16 opens with a worked timer
  component, its inline comment and a three-line project note, read in the text view and placed by its note (about 6
  minutes); the movement component is a partly finished shell its student modifies before making.
- **Expert 3** (days.csv days 17, 23; .md units 3 and 4): `assess` blanked on days 17 and 23; each note now says the
  record is scored there and carried into the following check, which is the unit's end-of-unit assessment. "Marked
  `end`, part 1" deleted from the .md; old For the lead 1 deleted.
- **Expert 4** (days.csv days 4, 18, 27, 31; frame.md Units table units 1 and 5, mid-year checks row): day 31
  E5-SYS-IM-15 asks culture or living and work, each a help or hindrance; E5-SOC-HI-16 asks what changed in how the
  tool was made and for its users (day 27 too); day 4 E5-SYS-SE-13 asks at least one threat per side with why the side
  matters, E5-SYS-HW-12 the hardware and software for each of the four operations; day 18's trace item holds store,
  compare and modify.
- **Expert 5** (.md Shorter path; days.csv days 11, 13 notes): folds 2 and 3 end with a self-check against a posted key
  on two items, the error-letter reteach becomes the next session's five-minute opening, day 10's flowchart fixes go
  to day 11's opening trace; fold 1 keeps only the score program on day 11 and moves the countdown and password
  programs into day 13's buggy set.
- **Expert 6** (days.csv): no-device paths named on days 16 and 17 (printed block strips into a team sheet, tester as
  the computer), 19 (paper version of the missed device item), 21 (printed ramp times sorted by hand), 25 (paper form
  and hand-sorted table); driver and navigator switch at the halfway signal named on days 11, 13, 14, 15, 17, 20, 22,
  23; .md Devices bullet says so.
- **Expert 7** (days.csv day 27; frame.md unit 5 session 1; .md unit 5 arc): two cases taught whole (name form,
  captions), three by pair jigsaw, each pair placing one card and reporting one line; the programming language card's
  second view (in English words, it left out people who did not read English).
- **Expert 8** (days.csv days 19, 26, 28; .md Devices): day 19 drops g5-team-project from skills; day 26 adds
  E5-ALG-ML-02 to codes; device minutes stated as about 300 of 726 once the trainer exists and about 245 now (a
  third), check and respond device minutes about 32 more; the "Unsure" line deleted; day 28's teacher source line
  names the two Bureau of Labor Statistics handbook pages with their modified dates as the case's two views (also in
  frame.md unit 5 session 2).
- **Settled rows 1 to 12**: each applied as above.
- **Lead call 1**: days 17 and 23 cleared (expert 3); no other teaching day carried `end` only for the old gate (days
  4, 9 and 31 are real check sittings and keep `end`).
- **Lead call 2**: no source-map.csv in data/plans/computer-science-grade-5/ (already moved to the scratch folder);
  the .md's leaning-days line now points to the frame's Source map, "waits on L149".
- **Lead call 4** (frame.md): year-end checks row now asks E5-DAT-IM-11 in two sentence frames, not a
  benefit-risk-chart a week after session 5's (the scope's old For the lead 4, now deleted); the paper-path ML-02
  wording and the device share ("a little over 40 percent once the trainer exists, about a third until then")
  corrected.
- **Lead call 5** (frame.md Day kinds bullet): rewritten to GLOSSARY: first teaching of a row or method, and predict and
  watch, are Understanding (unit 2 sessions 1 and 3, unit 3 sessions 1, 3 to 6, unit 4 sessions 1 to 3 and 5, unit 5
  sessions 1 to 4); Fluency is modify on a taught row; Application is unit 2 session 2 and unit 3 session 7. The
  scope's old For the lead 2 is deleted and its Kinds line says the frame now matches.
- **Lead call 7**: 11 defect rows logged (`plan.py defect --status=fixed --made-at=scope`), one per expert finding
  (finding 4 as one row) plus one frame.md wording row.
- **Lead call 11**: frame lines the read changed (unit 3 session 6, unit 4 session 3, unit 5 sessions 1 and 2, the
  end-of-unit cells, both check rows) reworded to the read's settled fix.
- **Own 1** (.md unit 1 Assessments line): the day 4 paper's summary now names a threat per side and the four
  operations, matching days.csv.
- **Own 2** (.md For the lead): renumbered to one item (L107, six ids not on a course-level check, met by naming per
  the read); the codes-not-sampled paragraph points to it.

Rule 2 lists re-run: every assumed row is grade 4, last used the year before, retrieval (unchanged); each check's
sampled codes, Collect once (days 17 and 23 records reused, never collected again), each part of each code (now
asked, expert 4), end days (4, 9, 31 plus the two checks standing for units 3 and 4) and our words: no new gap.

## Not applied

None. Lead calls 3, 6, 8, 9, 10 and 12 do not touch this course beyond what is above (frame.py check was already 0
failures; no Specialty id or begun id here; "Open Government Licence" stays as spelled, the known lint exception).

## Settled (for DIGEST)

| Judgment | Reuse |
|---|---|
| A paper "pretend model" is a partner or card procedure that labels a test card only by the closest training card on stated features | Any grade whose model trainer is not built yet |
| A team build day opens with a worked component, comment and note; an untraced component is given as a shell to modify | Team project days |
| A shorter-year fold into a paper day ends with a self-check on a posted key; the error-letter reteach is the next opening | Every fold of a respond day |
| Device minutes are stated both with and without a tool that is queued but not built | Any device-share line |

## For the structure pass

- data/plans/frames.csv and calendar.csv: no change (units, day counts and check weeks 18 and 25 unchanged).
- docs/courses/computer-science/APPROACH.md kinds table ("society day" as Application): could follow GLOSSARY as this
  frame's Day kinds bullet now does (row: society day, old "Application", new "Understanding when it first teaches a
  row"). Lead's call.
- Unchanged from the read: the week 18 overlap with other specials stays for the lead's calendar pass (frame For the
  lead 1).

## For Cory

None.

## Gates

- `python -X utf8 scripts/sequence.py check computer-science-grade-5`: 0 failures.
- `python -X utf8 scripts/frame.py check`: 0 failures in every frame; this course 5 units, 32 days.
- `python -X utf8 scripts/frame.py calendar`: grade 5 computer science weeks 18 and 25, unchanged; as a K to 5 special
  it does not count against the stagger rule; no break.
- `python -X utf8 scripts/gate.py --course computer-science-grade-5`: 0 failing findings against the baseline (the
  one standing line is the known "Open Government Licence" UK spelling hit; index-reports' non-zero exit is
  math-kindergarten orphans, not this course).

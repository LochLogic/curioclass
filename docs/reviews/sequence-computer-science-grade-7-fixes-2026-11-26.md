# Fixes: scope and sequence of computer-science-grade-7, 2026-11-26

Job: build/scope-writes/CS-FIX.md over docs/pipeline/briefs/sequence-fix.md. One read so far: the Claude expert read
docs/reviews/sequence-computer-science-grade-7-2026-11-26.md (the Codex read waits for Codex's reset after 2026-11-30).

Counts: applied 18 (expert 16, lead calls 2 beyond the expert's overlap, own 1; band items 0 apply), not applied 0.
Every applied finding is logged with `plan.py defect --status=fixed --made-at=scope` (17 rows: 16 expert, 1 writer).

## Applied

- **Expert 1** (days.csv day 50; frame unit 5 session 50; .md unit 5): day 50 sets the NTIA survey beside the
  Federal Communications Commission's 2025-09-30 vote (2 to 1) to end E-Rate support for library and school hotspot
  lending and school bus Wi-Fi; majority order and dissent are the two dated views; "programs named as of the day
  read; the teacher page checks each is still running", an ended program said to have ended.
- **Expert 2** (days.csv days 9, 21; .md unit 1 and 2 bullets, Shorter path; frame unit 1 end-of-unit): day 9 about
  17 and 18 minutes, its new program fifteen lines; day 21 about 8, 7 and 20; Shorter path: "a sitting keeps every
  id's item and cuts one read item per id (about 30 minutes)".
- **Expert 3 / lead call 1** (days.csv days 30, 61, 31, 62; .md units 3 and 6): `end` cleared on days 30 and 61; the
  brief and the claim are kept work the teacher reads, unscored; the "Marked end" lines and For the lead 1 dropped.
- **Expert 4** (days.csv day 39; frame unit 4 session 39, its Sensitive cell and Sensitivity reads; .md unit 4): the
  cases worded as the studies found them (2020 speech study: Black speakers' words misheard about twice as often;
  NISTIR 8280, December 2019: more false matches for some groups in most systems, by very different amounts); source
  lines named; "accent" became "dialect" in the sensitivity flag.
- **Expert 5** (days.csv day 5; frame unit 1 session 5; .md unit 1): one planted bug found with the four-step routine,
  unscored, the routine printed on the day 7 build sheet.
- **Expert 6** (days.csv days 14, 16; frame unit 2 session 14; .md unit 2): day 14 opens with a worked lookup, then a
  changed call, then one alone, with one worked error-guide lookup; day 16 looks each bug up in the guide.
- **Expert 7** (days.csv days 17 to 20; .md unit 2): paper paths named; MS-PRO-TR-19 met in full on paper, MS-PRO-PD-13
  part met without a device.
- **Expert 8** (days.csv days 6, 7; frame unit 1 session 6; .md unit 1): the worked design is changed for one new
  requirement and retraced before the student's own; day 7's first minutes finish the design.
- **Expert 9** (days.csv day 28; frame unit 3 session 28; .md unit 3): the two views sit on a choice inside the case,
  never on whether the nation may govern its data; the nation's own account is one of the two sources.
- **Expert 10** (days.csv days 55, 56; frame unit 6 anchor and sessions 55, 56; .md unit 6): the anchor is the move to
  computer-controlled exchanges, no company name, the date confirmed from a museum or government source before use;
  day 56's environment half follows the phones the network made common, EPA page as of the day read.
- **Expert 11** (days.csv days 48, 59; frame sessions 48, 59; .md units 5 and 6): day 48 adds the agency's Office of
  the Inspector General reporting as the second dated source and the guard "what was taken and the effect on people,
  not who is said to have done it"; day 59 from a dated source, rechecked each year.
- **Expert 12** (days.csv `retrieves`): day 8 g7-analyze-code, day 41 g7-design-with-variables (pseudocode trace),
  day 45 g7-lists (list loop), day 50 g7-test-refine (test-table); notes say so. Seams retrievals untouched.
- **Expert 13a** (days.csv): "Pair roles: driver and navigator, switching at the halfway signal" on days 2, 5, 12 to
  14, 16, 18 to 20, 23, 25, 36 to 38 and 46.
- **Expert 13b** (.md Shorter path fold 1): the written account is three lines at the end of day 7, never a home task.
- **Expert 13c** (.md): For the lead 2 kept as is, with the expert's reason stated in the checks section; item dropped.
- **Expert 13d / lead call 5** (frame Day kinds; .md Kinds): the frame's bullet follows GLOSSARY: session 6
  Understanding (and predict-and-watch sessions), Application lists unit 1 sessions 7 and 8 and unit 5 session 48.
- **Lead call 2** (.md For the lead): the source-map item is now "waits on L149", the placement list kept.
- **Lead call 6** (.md Shorter path): bar C1 stated on the shorter path: 2 of 46 teaching days outside the standards
  (about 4 percent), 2 of 45 with the fifth fold-in; no rebalance needed.
- **Own** (days.csv day 46): its retrieval moved from g7-lists to g7-analyze-code (a unit 1 program) so days 45 and 46
  do not open on one row, the repeat finding 12 named. Rule 2 lists re-run (earlier rows and last use, each check's
  sampled codes, Collect once, each part of each code, end days, our words): nothing else found.
- **Frame source list** (frame For the lead 6, lead call 4): OPM inspector general reporting, Route Fifty October
  2025, the American Library Association hotspot FAQ added.

## Not applied

None. Lead calls 3 (no frame.py failures here), 9, 10 and 12 do not touch this course beyond the known "Open
Government Licence" lint hit, which stays. No cross-grade item in the neighboring grades' reads (6, 8, 11) asks a
change of grade 7.

## Settled (for DIGEST)

| Choice | Reason |
|---|---|
| A unit closed by a course-level check has no `end` day; its last brief or claim is kept work, unscored | The check is the unit's end (lead call 1) |
| A day whose help program can end names programs "as of the day read", teacher page checks each | Bar item 4, real and current cases |
| Bias cases are worded at the size their study found, with the study and date on the day | Society with evidence |
| Sovereignty cases put the two views on a choice inside the case, never on the nation's authority | CARE Principles, frame guard |
| A sitting fits 35 teaching minutes; the 40-minute path cuts one read item per id | Frame minutes |

## For the structure pass

- docs/APPROACH-SOURCES.md: add the Route Fifty October 2025 FCC hotspot vote page
  (route-fifty.com/digital-government/2025/10/fcc-ends-federal-funding-wi-fi-hotspots-access-buses/408519), the ALA
  E-Rate hotspot FAQ (ala.org/advocacy/federal-resources/broadband-policy/erate/hotspot-FAQ) and the OPM Office of
  the Inspector General reporting on the 2015 breach (to be located and dated by the lead).
- Browser check: none. The OPM inspector general report and the speech-study wording are from the expert's memory; the
  teacher page checks them before use (day notes say so).
- Calendar: no change; check weeks stay 16, 31 and 32.

## For Cory

Nothing.

## Gates

- `scripts/sequence.py check computer-science-grade-7`: 0 failures.
- `scripts/frame.py check`: 0 failures for every frame; computer-science-grade-7 "6 units, 64 days (58 in units, 6
  for checks and respond days)".
- `scripts/frame.py calendar`: grade 7 computer science weeks 16, 31, 32; no stagger break.
- `scripts/gate.py --course computer-science-grade-7`: 0 failing findings against the baseline; the one standing lint
  line is the "Open Government Licence" proper name (lead call 12); index-reports exits non-zero as at baseline.

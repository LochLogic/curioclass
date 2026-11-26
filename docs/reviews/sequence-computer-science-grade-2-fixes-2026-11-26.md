# Fixes: scope and sequence of computer-science-grade-2, 2026-11-26

Fix pass after the Claude expert read docs/reviews/sequence-computer-science-grade-2-2026-11-26.md, per
build/scope-writes/CS-FIX.md and docs/pipeline/briefs/sequence-fix.md. The Codex read waits for Codex's usage reset
(after 2026-11-30) and gets its own small fix pass then.

Counts: applied 14 (expert findings 10, expert settled-table row 1, lead calls 3: call 2, call 5, and calls 4 with 8
together; lead call 1 is the same item as expert 3; own 0 new); not applied 1 (expert 11, a no-change item under lead call 12). Band items: none touch this course
(grade 1 finding 4 and grade 3 findings 3 and 4 are their own courses' days; their shapes match what this pass did here).
Each finding is logged with `plan.py defect` (15 rows, made-at scope).

## Applied

- **Expert 1** (days.csv days 13 to 20, scope Device days paragraph, frame Days, Devices, Paper path, Safety, Costs,
  unit 3 cell): the paper path is a printed desk mat per pair with a paper token for movement programs; dance programs
  are acted out by the partner at the desk, seated or standing in place. The taped floor grid is the teacher's alone at
  the front (day 13 anchor, day 16 worked bug, day 19 sample act-outs). Put-away stays four minutes, cards and mats into
  the pair envelope. Costs unit 3: one roll of tape plus 15 printed mats in place of two rolls, still $12.
- **Expert 2** (days.csv days 5, 11, 19, 26, 31; scope Course-level checks and Shorter path; frame Evidence bullet and
  both check rows): each assessment day runs paper items read aloud together first (about 10 minutes, collected), then
  the five spoken groups (about 15 minutes) while the class does a quiet unscored picture task; 28 of 30 minutes with
  retrieval, which stays only while the paper part keeps to 10 minutes. Day 26 drops the sampled E2-SYS-SE-12 item
  (codes and skills; day 27's skills too); the frame's year-end row says so. The 25-minute period: retrieval dropped,
  10 paper plus 15 spoken.
- **Expert 3 / lead call 1** (days.csv day 9; scope unit 2 Assessment, For the lead 1): day 9's placeholder `observe`
  cleared and its note sentence removed; day 25 keeps `observe` (a real record). For the lead 1 now reads "Resolved".
- **Expert 4** (days.csv days 3, 4, 23, 24, 25, 26; scope units 1 and 4 Assessment; frame unit 4 cell and year-end row):
  days 3 and 4 goals name the E2-SYS-HW-11 task (each child explains one new action card, about 6 minutes, fifteen
  children). E2-DAT-DI-09 is heard on days 23 (last 5 minutes) and 25 (last 7 minutes), fifteen children each; day 24
  drops the code and carries no look-for; day 26 reuses "days 23 and 25".
- **Expert 5** (days.csv days 29, 31; scope unit 5; frame unit 5 cell): E2-SOC-HI-14's "express ideas" part asked:
  what problem each tool solved or what idea it helped people record or share. Braille and khipu carry the ideas part,
  the abacus the problem part.
- **Expert 6** (days.csv days 29, 31; scope unit 5; frame unit 5 cell, under lead call 4 as a claim the source does
  not support): each case card is a span from the earliest documented use to today where the source says it is still
  used. Abacus the longest span (its page gives no origin date); khipu as the NMAI page words it (browser check);
  braille from the 1820s.
- **Expert 7** (days.csv days 9, 17; scope units 2 and 3): three-line by-exception product look-for, unscored, no
  `assess` mark, used by the respond days; day 19 stays the scored code item.
- **Expert 8** (days.csv days 14 to 17; scope unit 3 Practices): navigator reads and lays the cards, driver (or robot
  on the paper path) runs them, switch at the halfway signal (IC5).
- **Expert 9** (days.csv days 14, 18; frame unit 3 cell and Models carried): day 14's paper-path score is a labeled cup
  "score" the teacher updates after each run (labeled, not coded); day 18's goal reads "Telling (device day; the program
  open on screen, or on its block cards on the paper path)".
- **Expert 10** (scope Shorter path): each fold-in replaces the host day's three-minute retrieval and takes about five
  minutes; the checks keep weeks 11 and 26, and a lost week moves teaching days, never a check.
- **Expert settled table, day 12** (days.csv day 12): retrieval is now one input-output action laid on the
  system-diagram (`retrieves` g2-io-parts), so day 14 no longer repeats day 12's event-block task. g1-code-sequence
  still opens as retrieval on day 14, its first-use day.
- **Lead call 2** (scope For the lead 3): no source-map.csv; the item now says it waits on L149.
- **Lead call 5** (frame Day kinds bullet): reworded to GLOSSARY: Understanding is the first explicit teaching of
  anything new (a construct, idea, model or method such as debugging), traced or predicted and watched included. The
  scope's kinds already followed GLOSSARY; no day's kind changed.
- **Lead calls 4 and 8**: the frame wording items above (Paper path, Safety, Costs, Evidence, check rows, unit 4 and 5
  cells) were applied here as wording; no unit, day count or owned row moved.
- **Rule 2 lists re-run (own)**: every grade 1 row still opens as retrieval on the day that first uses its grade 2 row;
  each check day lists only the codes it samples (day 26 now lists six codes); E2-DAT-DI-09 collected once (days
  23 and 25) and reused on day 26; each part of E2-SOC-HI-14 now asked; end days unchanged; goals and notes in our own
  words. Nothing new found.

## Not applied

- **Expert 11** (frame Base text "Open Government Licence"): a proper name, kept as spelled (lead call 12); the lint
  hit stays a known exception. Logged as rejected.
- Lead calls 3, 6, 9, 10, 11: nothing to do in this course (frame.py check had no failures; no Specialty id or begun id
  here; grade 9 only; grade 3's day 20 is grade 3's).

## Settled (for DIGEST)

| Judgment | Reason | Where |
|---|---|---|
| K to 2 paper-path programs run on a desk mat per pair; a taped floor grid is the teacher's demonstration only | One grid cannot serve 15 pairs in a 30-minute special | days 13 to 20; frame Paper path |
| Assessment days with a read-aloud and spoken groups run in sequence: paper read aloud first (10), then groups (15) with a quiet unscored task | One teacher cannot read aloud and hear a group at once | days 5, 11, 19, 26, 31; frame Evidence |
| A spoken look-for spread over teaching days skips the day a new model is first taught | Keeps that day's teaching whole | days 23 to 25 |
| Timeline cards are spans from the earliest documented use to today, never points | Sources often give no origin date | days 29, 31 |
| A make product gets an unscored three-line look-for for the respond day, no `assess` mark | Bar item 8 projects with criteria, without a second score | days 9, 17 |

## For the structure pass

- docs/APPROACH-SOURCES.md (or the lead's source list): Computer History Museum abacus page opened 2026-11-26 (no
  origin date; dated objects 1878, 1879, 1946); NMAI khipu page and Britannica "quipu" both 403 on 2026-11-26, status
  "browser check" (as the expert read lists).
- Lint allow list (scripts' UK-spelling check): add "Open Government Licence" as a proper name, or keep the baseline
  line (lead call 12).
- data/plans/calendar.csv: no change needed; check weeks stay 11 and 26 and school_day is unchanged.

## For Cory

None.

## Gates

- `python -X utf8 scripts/sequence.py check computer-science-grade-2`: 0 failures.
- `python -X utf8 scripts/frame.py check` (all frames, this course included): 0 failures for computer-science-grade-2.
- `python -X utf8 scripts/frame.py calendar`: grade 2 computer science weeks 11 and 26; no stagger break (a special,
  CALENDAR.md rule 1); no frame change here moved a week.
- `python -X utf8 scripts/gate.py --course computer-science-grade-2`: exit 0, 0 failing findings against the
  baseline; the one standing line is the frame's "Licence" lint hit (expert 11). The shared index-reports gate exits
  non-zero, as it did before this pass.

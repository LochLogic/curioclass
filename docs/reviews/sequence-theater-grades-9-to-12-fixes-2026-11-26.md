# Fixes: scope and sequence of theater-grades-9-to-12, 2026-11-26

Fix pass per docs/pipeline/briefs/sequence-fix.md with build/scope-writes/ARTS-FIX.md. One read so far: the Claude
expert read docs/reviews/sequence-theater-grades-9-to-12-2026-11-26.md. The Codex read waits for Codex's usage reset
(after 2026-11-30) and gets its own small fix pass then; the brief's Codex and 2026-11-15 lead-call items are skipped.
days.csv was rewritten with Python's csv module from scripts kept in the session scratchpad.

Counts: applied 12 of 12 expert findings and every row of "Settled by the expert" (three specific day picks inside
findings 1 and 10 adjusted, with the reason below); 9 ARTS-FIX lead calls applied or confirmed (1, 2, 3, 5, 6, 7, 8,
9 applied; 4 needs no change); 0 band items (none touch this course); 4 own. Not applied: 0 findings; 3 day picks
adjusted (finding 1 unit 16 map and day 500, finding 10 unit 17 days); frame cells go to the structure pass.

## Applied

- **Expert 1** (80-day merge map). Every merge re-mapped by rules (a) to (c), written in the .md Shorter path section.
  (a) Each first-taught owned id merged on the short path now pairs with one kept Understanding day of its thread that
  takes nothing else: 50 into 48, 54 into 52, 86 into 84, 120 into 118, 205 into 203, 209 into 207, 242 into 240, 365
  into 363, 369 into 367, 402 into 400, 588 into 585, 594 into 592, 617 into 612, 628 into 623. (b) Work sessions merge
  into a later kept critique, revision, final rehearsal or Application day, at most two a day; Fluency days fold into a
  later kept day's warm-up, at most two a day. (c) No revision, critique, check or respond day takes or loses a merge:
  598 kept; 500 into 505, 538 into 543. Unit 3 matches the expert's map exactly (51 and 55 into 60, 56 and 58 into 61,
  59 into 63; 69 into 74, 72 into 75, 73 into 77). Unit 5: day 132 kept and 120 merged (count still 19) so the first
  half fits two a day. Level 4 kept sets rebuilt: 16 and 17 keep every run's peer feedback session; 18 keeps 568, 19
  keeps the revision session 598, 20 keeps the folio, defense and tech peer sessions (610, 616, 627) and day 607 (the
  retrieval day, kept off the hook). The .md "Short path" lines of units 5 and 16 to 20 list the new kept days. Script
  check: max two work sessions and two warm-ups into any kept day, no merge into a merged, check or respond day, no
  cross-unit merge, kept counts per unit unchanged (80 a level).
- **Expert 2** (Level 4 company model). With lead call 9: the .md states the model once under the Level 4 heading;
  frame.md's Level 4 bullet ("The course in brief", Units) adds it; days 606, 607, 628, 636 (goal and note) and 637
  reworded (companies of about five, one company in a small class, one 5-minute piece per company built from members'
  plays, six pieces on day 636 in about 36 minutes, each student leading one role and running the element they
  design; folios and defenses for the student's own play, on paper). Unit 20's Assessment line matches.
- **Expert 3** (baseline looks). The 16 fold-ins moved off the baseline days (15 to 19, 49 to 53, 85 to 89, 119 to
  123, 169 to 173, 186 to 190, 204 to 208, 221 to 225, 241 to 245, 276 to 280, 329 to 333, 346 to 350, 364 to 368, 381
  to 385, 401 to 405, 436 to 440); fold-in table updated. Every merged baseline day's note adds "the baseline look
  moves to day n". Level 4 baselines added on 483, 521, 561, 586, 608 (in conferences). Logic model outputs reworded.
- **Expert 4** (check goals). Goals of days 159, 237, 397, 479, 557 rewritten as settled, and the .md check lines
  match. Day 479 also keeps TH:Re9.1.IIIa (one choice backed or judged from a given history and culture page), which
  the settled wording had dropped (own 1).
- **Expert 5** (unit 20 senior fold). Fold days now 609, 611, 614, 615, 618, 619, 625, 626, 630, 634; notes and the
  .md table updated, with the line that each Level 4 run keeps its first session and its peer feedback round.
- **Expert 6** (same-level retrieval). retrieves column and notes: 48 th-g9-story, 84 th-g9-notice, 203 th-g10-story,
  240 th-g10-notice, 363 th-g11-imagine, 400 th-g11-actor (ten minutes split five and five); five-minute design
  retrieval at the start of 146 (th-g9-design), 303 (th-g10-design), 463 (th-g11-design). Readiness table adds a row.
- **Expert 7** (placement sitting). Days 162 and 322 notes: a student new to the level sits a parallel form of the
  previous year-end check in the first 35 minutes; days 161 and 321 notes carry it on the short path. Units 6 and 11
  Arc lines say the same.
- **Expert 8** (Fluency). 150 to 152, 307 to 312, 467 to 472 relabeled Application ("Rehearsal with choice"); 123 and
  132 rewritten as Application work on the dramaturgy page and discussion note; every Level 4 Fluency day has a second
  round. Counts kept (113 Fluency days); the reason and a pick are For the lead item 7.
- **Expert 9** (text). 133 (final work session on the page and note), 134 (kept discussion note, fishbowl in two
  rounds of fifteen; .md unit 5 line too), 281, 490, 503, 601 fixed; revision days of written threads (41, 75, 97, 111,
  131, 196, 231, 252, 268, 356, 391, 412, 428) name the journal or the product's revision line instead of the rehearsal
  log.
- **Expert 10** (process table). Units 17 to 20 Connecting cells name real days; unit 19 Performing marked presenting.
- **Expert 11.** Day 79 goal and unit 3 Assessment line: "mid-unit marks standing unless reworked".
- **Expert 12.** Shorter path section: 80-day weeks (kept day k in week ceil(k / 5); mid-year on kept day 41, 38, 38
  or 39 by level; year-end on kept days 79 and 80, week 16). Course-level checks section names both finals weeks.
- **Lead call 1.** Confirmed: ten course days a level (no other reading in the file); heading says so.
- **Lead call 2.** The four-processes intro rewritten (each level all four; a unit claims what the frame names; practice
  claims no id; no code outside the unit's owned rows). The table's stretched hook-day claims replaced (expert 10).
- **Lead call 3.** Not-sampled list kept with its reason and a line citing the lead call.
- **Lead call 5.** school_day stays blank and counts inside each level; the .md says so.
- **Lead call 6.** For the lead item 2 replaced by the settled rule; check days 81, 159, 237, 319, 397, 479, 557, 639
  carry the rule 2 note; the checks section says it once.
- **Lead call 7.** Checked: no check re-asks items a unit gave one to three days before (each samples a unit ended at
  least five weeks earlier, or units 2 to 4, 7 to 9, 12 to 14). Stated in the .md. Frame cells: structure pass.
- **Lead call 8.** Formula stated once ((n - 1) mod 160 + 1, week (school_day - 1) // 5 + 1); all units and checks
  checked against the frame's weeks; not re-counted to calendar.csv.
- **Lead call 9.** See expert 2 (the coordinator's update: the expert's company model as written).
- **Own 1** (rule 2, each part). Day 479 restores TH:Re9.1.IIIa (above).
- **Own 2** (rule 2, each part). Day 81 adds "or culture" and the analysis (TH:Cr2.1.Ia); 319 adds purpose
  (TH:Re9.1.IIc); 639 adds defend (TH:Re7.1.IIIa) and compare (TH:Re9.1.IIIc); 237 asks the choices that keep the scene
  believable and consistent (TH:Pr4.1.IIa); 397 adds the research page (TH:Pr4.1.IIIa). The .md check lines match.
- **Own 3** (rule 2 re-run). Earlier-grade rows: grade 8 readiness on day 1, one-level-back retrieval on day 2 of each
  unit, now with the same-level rows; unchanged otherwise. Sampled codes: 81 (Pr4.1.Ia, Cn11.2.Ib, Cr2.1.Ia), 159
  (Cr1.1.Ia, Re8.1.Ia, Re9.1.Ia, Re9.1.Ic), 237 (Pr4.1.IIa, Cn11.2.IIb, Cr1.1.IIa), 319 (Cr1.1.IIa, Re8.1.IIa,
  Re9.1.IIc), 397 (Pr4.1.IIIa, Cn11.2.IIIa, Cr1.1.IIIa), 479 (Cr2.1.IIIa, Re8.1.IIIa, Re9.1.IIIa, Re9.1.IIIc), 557
  (Cn11.2.IIIb, Cn10.1.IIIa), 639 (Re7.1.IIIa, Re9.1.IIIc); each part now asked. Collect once and end days hold. Our
  words: new goals and notes written fresh.
- **Own 4** (short path, retrieval). The first unit 20 re-map put the retrieval day 607 into the hook; changed so 607
  stays kept and 628 merges into 623 instead. No other retrieval day merges into a hook (units 6 and 11 excepted: the
  review is itself retrieval, on the frame's three-day path).

## Not applied (as written), with the reason

- **Expert 1, unit 16 map** ("keep 489 and 495, merge 509 and 510 into 508 and 511") and **"merge 500 into 506"**.
  On the files, that map merges all five peer feedback sessions (485, 492, 497, 505, 510), which the same finding's
  rule (c) and its "keep the session with the peer feedback round" forbid. Kept instead: 485, 492, 497, 505, 510, so
  both writing runs keep a session (the map's aim) and reading drops from four sessions to one plus its mini-lesson.
  506 is then merged, so 500 merges into 505.
- **Expert 1, "swap 598 to kept and merge ... 601"**: 598 kept; 601 was already merged. The count is held by merging
  the mini-lesson 594 into 592 (rule a).
- **Expert 10, unit 17 Connecting "526 to 531 and 536"**: on the files, 526 to 531 are the forms and technology run
  (TH:Cr1.1.IIIa); the credited traditions are 532 to 535 and 538, checked on 536. The cell names 532 to 536 and 538.
- **Frame cells** (expert 4's checks table, expert 2's unit 20 row): frame.md edited only in the Level 4 bullet (lead
  call 9); the rest is under "For the structure pass".

## Settled

| Judgment | Reuse |
|---|---|
| Fluency merges do not count against the two-a-day cap for work sessions; they have their own cap of two warm-ups a day, and never go into a day that took a first-taught day | Any arts short path that folds Fluency into warm-ups |
| In Level 4 and production halves, a kept mini-lesson that took no first-taught day may take the one work session after it | Short paths of project-phase units |
| A peer feedback round that a unit's kept count cannot hold merges only into the unit's trios critique day | Level 4 or any self-directed unit with fixed short-path counts |
| A retrieval day (unit day 2) never merges into the hook on the short path | Every short path |
| A fold-in never sits on a baseline-look day | Every short year table |

## For the structure pass

- **docs/courses/theater-grades-9-to-12/frame.md, checks table** (lines 325 to 332): replace each row's sampled-item
  wording with the scope's check goals:
  - Level 1 mid-year: "one way the play's history would change a first concept idea (TH:Cr2.1.Ia)" to "one way the
    play's history or culture would change a given first concept idea, with the analysis (TH:Cr2.1.Ia)".
  - Level 1 year-end: "a short critique with criteria and purpose (TH:Re9.1.Ia, TH:Re9.1.Ic, unit 4)" to "a short
    critique of an unseen described scene with one criterion, one piece of evidence and one link each to another art,
    history and culture (TH:Re9.1.Ia), and its purpose and intended audience (TH:Re9.1.Ic, unit 4)".
  - Level 2 mid-year: "(distinctive choices, TH:Pr4.1.IIa; a bias check on a given research note, TH:Cn11.2.IIb;" to
    "(which distinctive choices would keep it believable and consistent from start to end, TH:Pr4.1.IIa; one belief of
    the student's own that could skew how they read a given research note and how they would test it, TH:Cn11.2.IIb;".
  - Level 2 year-end: "how an unseen scene reaches its audience (TH:Re9.1.IIc)" to "how an unseen scene communicates
    to its intended audience and serves its purpose (TH:Re9.1.IIc)".
  - Level 3 mid-year: "a directing concept traced to a style, TH:Pr4.1.IIIa; a source judged sound or not,
    TH:Cn11.2.IIIa;" to "a directing concept traced to a style from a given research page, TH:Pr4.1.IIIa; one
    production choice defended by judging a given source sound or not, TH:Cn11.2.IIIa;".
  - Level 3 year-end: the sampled items to "a revision of a given scene from proof and a standard and an
    interpretation of a given classmate's choice with its evidence (TH:Re8.1.IIIa); an original concept from a given
    research page drawing one western and one non-western tradition, each credited (TH:Cr2.1.IIIa); one of an unseen
    production's choices backed or judged from a given page of its history and culture (TH:Re9.1.IIIa); that
    production's tie to a current issue argued from two sides and compared (TH:Re9.1.IIIc)".
  - Level 4 mid-year: "(TH:Cn11.2.IIIb, the play's social and historical meaning, and TH:Cn10.1.IIIa, its viewpoints on
    the issue)" to "(TH:Cn10.1.IIIa, the play's personal, local and cultural viewpoints on the issue, and TH:Cn11.2.IIIb,
    its social and historical meaning defended from one critically read source)".
  - Level 4 year-end: "organizing a response by its history and culture and debating its tie to a current issue" to
    "organizing a response by its history and culture and defending it, and comparing and debating its tie to a
    current issue from two sides".
- **frame.md, Units table row 20**: "Works: the student's own production" to "Works: the company's piece, built from
  its members' plays"; "TH:Pr6.1.IIIa (owned in unit 15) in the production for a chosen audience" to "... in the
  company's piece for the audience the company chooses, each student leading one creative role and its research";
  "Showing: the student-led production (staged or recorded)" to "Showing: the company pieces (staged or recorded),
  about 5 minutes each".
- **frame.md, Units table rows 1, 6, 11**: add "end slot: the readiness or placement record" (writer's For the lead
  item 1, agreed by the expert).
- **frame.md, the Fluency line** (line 88 area, "Fluency: short repeated practice"): if the lead takes For the lead
  item 7's first pick, "one or two fluency days a unit" to "one or two fluency days a technique".
- **docs/agents/decisions/DESK-ANSWERS.md**: one entry for lead call 6 as an arts 9 to 12 rule (the expert read asks
  for it so later reads do not raise the check form again).
- **data/plans/calendar.csv**: regenerate at commit (lead call 8); `frame.py calendar` was run here as the brief asks.

## For Cory

- Unchanged from the frame: the supplies ceiling (frame For the lead item 5, $150 a class a level, free path kept).
  Nothing in this pass changes scope, money, people or audience.

## Gates

- `python -X utf8 scripts/sequence.py check theater-grades-9-to-12`: 0 failures (notes only: units 1, 6, 11 and
  16 to 20 own no id, as the frame sets).
- `python -X utf8 scripts/frame.py check theater-grades-9-to-12`: 0 failures.
- `python -X utf8 scripts/frame.py calendar`: runs clean; 9 to 12 is under the finals-week rule, so no stagger break;
  no frame change here moves a check.
- `python -X utf8 scripts/stale.py check`: 121 files, 0 failures.

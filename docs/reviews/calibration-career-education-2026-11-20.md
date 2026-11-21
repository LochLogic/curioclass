# Calibration: Career and technical education, expert reader, run 1, 2026-11-20

Per-subject calibration at stage 1 (docs/pipeline/CALIBRATION.md, "Per subject, at stage 1"; line approved by Cory
on Desk q-prework-open-2). A set built correct from this subject's pages, then 10 major and 2 minor faults planted,
kept outside the repository at `S:/CurioClass-sources/_calibration/subjects/career-education/` (`set/` and `key/faults.csv`).
One fresh expert agent read `set/` cold with the career-education lens and docs/pipeline/briefs/prework-codex-read.md (as it stood
before the 2026-11-20 additions), and returned a report. Scored by the lead against the key; `key/NOTES.md` was used
to tell planted faults from findings on the page as it really is.

## Verdict

Run 2 result: docs/reviews/calibration-career-education-run2-2026-11-20.md.

Under the line on ranking: 8 of 10 majors and no false alarm, but the top finding was the planted minor K11 (a practice dropped from a list, which the reader rightly treated as a missing standard; the builder had marked it minor). Held to the line as written, as the core run held its frame piece: a fresh set (`subjects/career-education-run2/`) is read again with the changed brief.

## Scoring (fault ids from the key; #n is the reader's finding number)

- caught majors: K1(#11, ranked minor) K2(#7) K3(#3) K5(#6) K6(#8) K7(#4) K8(#5) K10(#2) = 8/10. missed: K4 (no ~ carry of practices in Pathways), K9 (teacher note sent to student job card).
- minors: K11 (#1, ranked MAJOR, top finding), K12 (#6) = 2/2.
- false major alarms: 0. real-page findings: #9 lean targets not ids (CS data strand rows unnamed, library/SEL no progression), #10 grade 7 placement leans, #12 field task count, #13 courses.csv typical_grade blank.
- top finding = K11, planted as minor. Strict line: top finding must be a planted major -> FAILS ranking. Scorer view: K11 drops a whole practice from the list a writer maps units to, which meets the set's own major definition (a writer would build wrong days); the key's severity was the builder's error. Recorded as pass with the regrade stated.

Findings marked real-page are true of the subject's real pages, not planted: they are not false alarms, and they go
to the stage 1 fix pass with the Codex read's findings (data/plans/later.csv L96).

## Pattern across the nine subjects

Every reader missed the planted "plan field sent to the wrong place" fault (nine of nine), and five missed the
"handoff that skips a grade" fault. Both point at the read brief, which checked that plan fields exist but not where
they sit, and did not ask for handoffs to be walked pair by pair. The brief now does both, and also asks that each
owner row teach every part of its ids and that each sensitive place keep its teacher note (2026-11-20). The Codex
half reads these same sets with the changed brief from 2026-11-23.

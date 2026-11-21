# Calibration: Physical education, expert reader, run 1, 2026-11-20

Per-subject calibration at stage 1 (docs/pipeline/CALIBRATION.md, "Per subject, at stage 1"; line approved by Cory
on Desk q-prework-open-2). A set built correct from this subject's pages, then 10 major and 2 minor faults planted,
kept outside the repository at `S:/CurioClass-sources/_calibration/subjects/physical-education/` (`set/` and `key/faults.csv`).
One fresh expert agent read `set/` cold with the physical-education lens and docs/pipeline/briefs/prework-codex-read.md (as it stood
before the 2026-11-20 additions), and returned a report. Scored by the lead against the key; `key/NOTES.md` was used
to tell planted faults from findings on the page as it really is.

## Verdict

Run 2 result: docs/reviews/calibration-physical-education-run2-2026-11-20.md.

Under the line (7 of 10 majors). Not used alone: the read brief was changed (2026-11-20, below) and a fresh set (`subjects/physical-education-run2/`) is read again.

## Scoring (fault ids from the key; #n is the reader's finding number)

- caught majors: PE1(#1) PE3(#2) PE5(#9, ranked minor) PE6(#13, ranked minor) PE7(#5) PE8(#3) PE9(#4) = 7/10. missed: PE2 (S3.5.1 dropped from g4-team-roles notes), PE4 (g4-attack-ideas hands on to g6, g5-defend assumes g3), PE10 (space and equipment sent to unit field 10).
- minors: PE11(#10) PE12(#16) = 2/2. false major alarms: 0 (#6 PECAT rule 3 tension, #7 S2.2.2 owner in K-2, #8 no sensitive-ground section: checked, the real APPROACH has none). 
- top finding #1 = PE1 planted major. FAILS the catch line (7 of 10).

Findings marked real-page are true of the subject's real pages, not planted: they are not false alarms, and they go
to the stage 1 fix pass with the Codex read's findings (data/plans/later.csv L96).

## Pattern across the nine subjects

Every reader missed the planted "plan field sent to the wrong place" fault (nine of nine), and five missed the
"handoff that skips a grade" fault. Both point at the read brief, which checked that plan fields exist but not where
they sit, and did not ask for handoffs to be walked pair by pair. The brief now does both, and also asks that each
owner row teach every part of its ids and that each sensitive place keep its teacher note (2026-11-20). The Codex
half reads these same sets with the changed brief from 2026-11-23.

# Calibration: Computer science, expert reader, run 1, 2026-11-20

Per-subject calibration at stage 1 (docs/pipeline/CALIBRATION.md, "Per subject, at stage 1"; line approved by Cory
on Desk q-prework-open-2). A set built correct from this subject's pages, then 10 major and 2 minor faults planted,
kept outside the repository at `S:/CurioClass-sources/_calibration/subjects/computer-science/` (`set/` and `key/faults.csv`).
One fresh expert agent read `set/` cold with the computer-science lens and docs/pipeline/briefs/prework-codex-read.md (as it stood
before the 2026-11-20 additions), and returned a report. Scored by the lead against the key; `key/NOTES.md` was used
to tell planted faults from findings on the page as it really is.

## Verdict

Passes the line: at least 8 of 10 majors, no false major alarm, top finding a planted major. The expert reader may be trusted for this subject at stage 1; the Codex half is owed (data/plans/later.csv L88).

## Scoring (fault ids from the key; #n is the reader's finding number)

- caught majors: C1(#1) C2(#3) C3(#2) C5(#12, ranked minor) C6(#13, ranked minor) C7(#7) C8(#4) C10(#5) = 8/10. missed: C4 (g5-systematic-debug hands on to g7, g6-verify-algorithm no longer assumes it), C9 (device versions sent to section fields 4 and 9, not 5 and 10).
- minors: C11(#9) = 1/2; C12 missed. false major alarms: 0 (#6 depth store vs one-line statement, #8 rotating third vs weekly read: both in the real pages).
- top finding #1 = C1 planted major. PASS.

Findings marked real-page are true of the subject's real pages, not planted: they are not false alarms, and they go
to the stage 1 fix pass with the Codex read's findings (data/plans/later.csv L96).

## Pattern across the nine subjects

Every reader missed the planted "plan field sent to the wrong place" fault (nine of nine), and five missed the
"handoff that skips a grade" fault. Both point at the read brief, which checked that plan fields exist but not where
they sit, and did not ask for handoffs to be walked pair by pair. The brief now does both, and also asks that each
owner row teach every part of its ids and that each sensitive place keep its teacher note (2026-11-20). The Codex
half reads these same sets with the changed brief from 2026-11-23.

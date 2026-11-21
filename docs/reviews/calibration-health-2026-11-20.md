# Calibration: Health, expert reader, run 1, 2026-11-20

Per-subject calibration at stage 1 (docs/pipeline/CALIBRATION.md, "Per subject, at stage 1"; line approved by Cory
on Desk q-prework-open-2). A set built correct from this subject's pages, then 10 major and 2 minor faults planted,
kept outside the repository at `S:/CurioClass-sources/_calibration/subjects/health/` (`set/` and `key/faults.csv`).
One fresh expert agent read `set/` cold with the health lens and docs/pipeline/briefs/prework-codex-read.md (as it stood
before the 2026-11-20 additions), and returned a report. Scored by the lead against the key; `key/NOTES.md` was used
to tell planted faults from findings on the page as it really is.

## Verdict

Passes the line: at least 8 of 10 majors, no false major alarm, top finding a planted major. The expert reader may be trusted for this subject at stage 1; the Codex half is owed (data/plans/later.csv L88).

## Scoring (fault ids from the key; #n is the reader's finding number)

- caught majors: H1(#2) H2(#11) H3(#1) H5(#5) H6(#14, ranked minor) H7(#3) H8(#10) H10(#4) = 8/10. missed: H4 (g5 health-information assumes g3 not g4; g4 hands_on skips to g6), H9 (unit field 2 "facts that matter" dropped).
- minors: H11(#16) H12(#7, in part) = 2/2.
- false major alarms: 0 found. Real-page findings (major as filed): #7 map cites PHW 13 and FN 13 in 9-12 (file has 12 each; checked in the real STANDARD line 74-75), PA 8, S 9, T 6 to check; #6 general help-seeking HBO6 sits only in sensitive units; #8 "alternate years" vs "each year"; #9 science lean for puberty and germs has no science rows; #13 national survey figure for grades 4-5 does not exist; #12 child calls 911 (judgment). Minor real: #15 one health row in courses.csv, #17 "bottom" (Cory chose this word 2026-11-21: not a fault), #18-#22.
- top finding #1 = H3 planted major. PASS.

Findings marked real-page are true of the subject's real pages, not planted: they are not false alarms, and they go
to the stage 1 fix pass with the Codex read's findings (data/plans/later.csv L96).

## Pattern across the nine subjects

Every reader missed the planted "plan field sent to the wrong place" fault (nine of nine), and five missed the
"handoff that skips a grade" fault. Both point at the read brief, which checked that plan fields exist but not where
they sit, and did not ask for handoffs to be walked pair by pair. The brief now does both, and also asks that each
owner row teach every part of its ids and that each sensitive place keep its teacher note (2026-11-20). The Codex
half reads these same sets with the changed brief from 2026-11-23.

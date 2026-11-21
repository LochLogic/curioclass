# Calibration: Physical education, expert reader, run 2, 2026-11-20

Run 1 (docs/reviews/calibration-physical-education-2026-11-20.md) was under the line. As CALIBRATION.md asks, the read brief
(docs/pipeline/briefs/prework-codex-read.md) was changed first: it now checks where each plan field sits against
docs/courses/UNIT-PLAN.md, walks every handoff pair in both directions, checks that each owner row teaches every part of
its ids, and checks each sensitive place keeps its teacher note. A fresh set with new plantings, none at a run 1
location, was built at `S:/CurioClass-sources/_calibration/subjects/physical-education-run2/` and read cold by a fresh expert agent
with the physical-education lens and the changed brief. Scored by the lead against `key/faults.csv` and `key/NOTES.md`.

## Verdict

Passes the line: 10 of 10 majors, no false major alarm, top finding a planted major. With the changed brief the expert reader may be trusted for physical education at stage 1; the Codex half is owed (data/plans/later.csv L88).

## Scoring (fault ids from the key; #n is the reader's finding number)

- caught majors: PF1(#5) PF2(#6) PF3(#4) PF4(#7) PF5(#2) PF6(#13) PF7(#8) PF8(#3) PF9(#9) PF10(#1) = 10/10.
- minors: PF11 and PF12 missed = 0/2 (not counted toward the line).
- false major alarms: 0. #7 also lists the real page's skips that carry a written reason (key NOTES: real, allowed by the gate); the brief's new handoff check said "no grade skipped" without the gate's exception, so the brief now says a skip with a written reason in the row is allowed. #10 no per-band session defaults, #11 one pe row in courses.csv, #12 S4 "carries" vs owns: real-page.
- top finding #1 = PF10 planted major. PASS.

Findings marked real-page go to the stage 1 fix pass (data/plans/later.csv L96).

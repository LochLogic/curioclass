# Calibration: Career and technical education, expert reader, run 2, 2026-11-20

Run 1 (docs/reviews/calibration-career-education-2026-11-20.md) was under the line. As CALIBRATION.md asks, the read brief
(docs/pipeline/briefs/prework-codex-read.md) was changed first: it now checks where each plan field sits against
docs/courses/UNIT-PLAN.md, walks every handoff pair in both directions, checks that each owner row teaches every part of
its ids, and checks each sensitive place keeps its teacher note. A fresh set with new plantings, none at a run 1
location, was built at `S:/CurioClass-sources/_calibration/subjects/career-education-run2/` and read cold by a fresh expert agent
with the career-education lens and the changed brief. Scored by the lead against `key/faults.csv` and `key/NOTES.md`.

## Verdict

9 of 10 majors and no false major alarm: the catch and false-alarm lines pass, and the changed brief caught the plan-field fault every run 1 reader missed. The top finding is not a planted fault but a real major already on the record (later.csv L94), ranked above every planted minor. The line as written asks for a planted major on top, so whether this passes is put to Cory (Desk q-calibration-1). Pending(docs/agents/decisions/DESK-ANSWERS.md#q-calibration-subjects-1)

## Scoring (fault ids from the key; #n is the reader's finding number)

- caught majors: KF1(#13, ranked minor) KF2(#2) KF3(#3) KF5(#7) KF6(#10) KF7(#5) KF8(#6) KF9(#8) KF10(#4) = 9/10. missed: KF4 (unit field 3: Pathways starts a new plan and the Exploration plan is not picked up; #15 names the grade 8 to 10 gap but not the plan).
- minors: KF11 and KF12 (#18) = 2/2. false major alarms: 0 (#9 plan scored with no feedback round, #11 learner goals ownership, #12 Pathways owns sub-clusters few students meet: real-page).
- top finding #1 is not planted: progression.py codes() collapses every CTE id to "CTE.Career", the known real defect already logged as data/plans/later.csv L94. A real major, confirmed. Every planted major is ranked above both planted minors. Literal line ("the top finding is a planted major") not met; its purpose (majors ranked above minors) met.

Findings marked real-page go to the stage 1 fix pass (data/plans/later.csv L96).

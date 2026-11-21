# Calibration: World languages, second-model reader (Gemini 4 Neon, medium), 2026-11-20

Per-subject calibration at stage 1 (docs/pipeline/CALIBRATION.md, "Per subject, at stage 1"). The second-model half:
Gemini 4 Neon at medium effort in Antigravity, pasted by Cory in a new conversation (prompt
`S:/CurioClass-gemini/09-calibration-world-languages.txt`), read the same set as the expert
(`S:/CurioClass-sources/_calibration/subjects/world-languages/set/`) cold with the world languages lens. Its report is
kept at `S:/CurioClass-gemini/reports/calibration-world-languages.md`. Scored by the lead against `key/faults.csv`, with
`key/NOTES.md` used to tell planted faults from the page as it really is.

## Verdict

Passes the line: 10 of 10 majors, no false major alarm, top finding a planted major. Gemini may be trusted as the
second reader for world languages at stage 1, so its real-page read (prompt 18) counts.

## Scoring (fault ids from the key; #n is the reader's finding number)

- caught majors: W1(#1) W2(#2) W3(#9) W4(#10) W5(#7) W6(#8) W7(#6) W8(#4) W9(#3) W10(#5) = 10/10. missed: none. The
  expert missed W9; between them the two readers caught all ten.
- minors: W11(#13) W12(#14) = 2/2.
- false major alarms: 0. Real-page findings (major):
  - #11 (with #7's second part): STANDARD.md line 128 settles Option D (four levels plus an early-years companion, 12
    courses), but APPROACH.md line 192 still says "a K to 5 learner has the same course at the same dose", STANDARD.md
    line 234 still asks the early-start question, and courses.csv lines 36, 37 and 45 hold one all-level row per
    language. The reader's claim that the split is unsettled is wrong; the clash between the pages is real.
  - #12: APPROACH.md puts the frame withdrawal day in unit field 7 (line 63) though section field 5 holds it (line
    76), and section field 2 opens with "the task goal" (line 73); its other slot points (unit field 8, section fields
    1, 3 and 5) are checked against UNIT-PLAN.md in the fix pass.
- Minor real-page: #15 the gate notes give no lean-timing rule for level-keyed subjects; #16 the not-endorsed note on
  every public page (STANDARD.md line 75), the "before you teach" block in English and Spanish (APPROACH.md line 15),
  the person-read line pairing a Spanish-speaking teacher with ASL (line 174), and graphics-only ASL against the bar's
  "materials are video" (the expert raised the last one too).
- top finding #1 = W1 planted major. PASS.

Real-page findings go to the stage 1 fix pass (data/plans/later.csv L96).

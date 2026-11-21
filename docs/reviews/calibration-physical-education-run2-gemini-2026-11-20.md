# Calibration: Physical education, second-model reader (Gemini 4 Neon, medium), 2026-11-20

Per-subject calibration at stage 1 (docs/pipeline/CALIBRATION.md, "Per subject, at stage 1"). The second-model half:
Gemini 4 Neon at medium effort in Antigravity, pasted by Cory in a new conversation (prompt
`S:/CurioClass-gemini/02-calibration-physical-education.txt`), read the run 2 set
(`S:/CurioClass-sources/_calibration/subjects/physical-education-run2/set/`) cold with the physical education lens. Its
report is kept at `S:/CurioClass-gemini/reports/calibration-physical-education-run2.md`. Scored by the lead against
`key/faults.csv`, with `key/NOTES.md` used to tell planted faults from the page as it really is.

## Verdict

Passes the line: 10 of 10 majors (one ranked minor), no false major alarm, top finding a planted major. Gemini may be
trusted as the second reader for physical education at stage 1, so its real-page read (prompt 11) counts.

## Scoring (fault ids from the key; #n is the reader's finding number)

- caught majors: PF1(#6) PF2(#8) PF3(#7) PF4(#10, ranked minor) PF5(#4) PF6(#9) PF7(#3) PF8(#2) PF9(#5) PF10(#1)
  = 10/10. missed: none. #10 names the grade 6 to 8 fitness handoff and the grade 4 and 5 assumes in both grade 7
  rows; its fix offers routing through the grade 7 row, which repairs it. The expert also caught all ten.
- minors: PF11 and PF12 missed = 0/2 (#12 quotes the planted "7 and 8" count as correct).
- false major alarms: 0. No real-page major findings.
- Minor real-page: #10 also lists skips whose reason sits only on the receiving row (g7-rest to g10-rest,
  physical-education.csv line 130; the reason is on line 178) and the empty hands_on on g7-dance-ideas (key notes:
  real); #11 no per-band session default (APPROACH.md line 89) and "four courses" against one pe row in courses.csv
  (STANDARD.md line 5); #12 APPROACH.md line 121 says only the K to 5 and standard 1 PECAT tables were read, while
  STANDARD.md section 3 reports the 6 to 8 and 9 to 12 tables; #13 APPROACH.md has no unit field 7 override for
  hands-up self-marking and no sensitive-ground section (the second already known, key notes).
- top finding #1 = PF10 planted major. PASS.

Real-page findings go to the stage 1 fix pass (data/plans/later.csv L96).

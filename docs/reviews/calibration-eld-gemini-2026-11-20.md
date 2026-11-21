# Calibration: ELD, second-model reader (Gemini 4 Neon, medium), 2026-11-20

Per-subject calibration at stage 1 (docs/pipeline/CALIBRATION.md, "Per subject, at stage 1"). The second-model half:
Gemini 4 Neon at medium effort in Antigravity, pasted by Cory in a new conversation (prompt
`S:/CurioClass-gemini/07-calibration-eld.txt`), read the same set as the expert
(`S:/CurioClass-sources/_calibration/subjects/eld/set/`) cold with the ELD lens. Its report is kept at
`S:/CurioClass-gemini/reports/calibration-eld.md`. Scored by the lead against `key/faults.csv`, with `key/NOTES.md` used
to tell planted faults from the page as it really is.

## Verdict

Passes the line: 10 of 10 majors, no false major alarm, top finding a planted major. Gemini may be trusted as the
second reader for ELD at stage 1, so its real-page read (prompt 16) counts.

## Scoring (fault ids from the key; #n is the reader's finding number)

- caught majors: E1(#4) E2(#6) E3(#5) E4(#3) E5(#10) E6(#7) E7(#1) E8(#8) E9(#9) E10(#2) = 10/10. missed: none. #5
  names the grade 4 gap and its fix has grade 4 carry SI 4-12, so it is counted; but it moves the owner to grade 12,
  and its second point (grade 5 breaks the last-grade rule) leans on text the key notes keep as real (the real owner is
  grade 4, by design): neutral, and the fix pass keeps grade 4. The expert missed E3 and E9; between them the two
  readers caught all ten.
- minors: E11(#12) E12(#13) = 2/2.
- false major alarms: 0. No real-page major findings.
- Minor real-page: #11 "one owned row per id ... 104 in all" against rows that pair the two modes (STANDARD.md line
  71; the expert raised it too), and scripts/progression.py has no eld entry yet; #13 "e10 to e12 seminar" for
  e10-sl-seminar, e11-seminar and e12-seminar (STANDARD.md line 134); #14 English learners with disabilities left out
  of the named-notes lines (STANDARD.md line 97, APPROACH.md line 18). #12's point on the unchecked state minutes is on
  text the real page marks as unchecked (APPROACH.md line 125): a fair note for the fix pass, not counted.
- top finding #1 = E7 planted major. PASS.

Real-page findings go to the stage 1 fix pass (data/plans/later.csv L96).

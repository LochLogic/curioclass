# Calibration: Career education, second-model reader (Gemini 4 Neon, medium), 2026-11-20

Per-subject calibration at stage 1 (docs/pipeline/CALIBRATION.md, "Per subject, at stage 1"). The second-model half:
Gemini 4 Neon at medium effort in Antigravity, pasted by Cory in a new conversation (prompt
`S:/CurioClass-gemini/08-calibration-career-education.txt`), read the run 2 set
(`S:/CurioClass-sources/_calibration/subjects/career-education-run2/set/`) cold with the career education lens. Its
report is kept at `S:/CurioClass-gemini/reports/calibration-career-education-run2.md`. Scored by the lead against
`key/faults.csv`, with `key/NOTES.md` used to tell planted faults from the page as it really is.

## Verdict

Passes the line: 10 of 10 majors, no false major alarm, top finding a planted major. Gemini may be trusted as the
second reader for career education at stage 1, so its real-page read (prompt 17) counts.

## Scoring (fault ids from the key; #n is the reader's finding number)

- caught majors: KF1(#8) KF2(#5) KF3(#7) KF4(#11) KF5(#6) KF6(#9) KF7(#1) KF8(#2) KF9(#4) KF10(#3) = 10/10. missed:
  none. The expert missed KF4; between them the two readers caught all ten.
- minors: KF11(#14) KF12(#15) = 2/2.
- false major alarms: 0. Real-page finding (major): #10, "Financial Services (left to Economics)" in the sensitive
  ground list (STANDARD.md line 130) reads as handing a whole career cluster to Economics, though Ownership gives all 14
  clusters to the two courses (lines 79 to 80); the line needs to say only consumer personal finance is Economics'.
- Minor real-page: #12 section field 2 uses unit field 3's "builds on and leads to" (APPROACH.md line 56); #13 section
  field 1 asks for "the verb" though cluster codes are nouns and the practice text may not be quoted (APPROACH.md line
  53); #16 the read's community slot names Judicial Systems but not Public Safety (STANDARD.md lines 129 and 137 to
  139; may be shorthand for one sub-cluster); #17 unit field 7 and section field 3 slots, no reason line for the grade 8
  to 10 step, and "the grade's economics rows" with no row id (STANDARD.md line 152; known, key notes).
- top finding #1 = KF7 planted major. PASS.

Real-page findings go to the stage 1 fix pass (data/plans/later.csv L96).

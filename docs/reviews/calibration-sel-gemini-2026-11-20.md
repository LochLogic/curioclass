# Calibration: SEL, second-model reader (Gemini 4 Neon, medium), 2026-11-20

Per-subject calibration at stage 1 (docs/pipeline/CALIBRATION.md, "Per subject, at stage 1"). The second-model half:
Gemini 4 Neon at medium effort in Antigravity, pasted by Cory in a new conversation (prompt
`S:/CurioClass-gemini/05-calibration-sel.txt`), read the same set as the expert
(`S:/CurioClass-sources/_calibration/subjects/sel/set/`) cold with the SEL lens. Its report is kept at
`S:/CurioClass-gemini/reports/calibration-sel.md`. Scored by the lead against `key/faults.csv`, with `key/NOTES.md` used
to tell planted faults from the page as it really is.

## Verdict

Passes the line: 10 of 10 majors (one ranked minor), no false major alarm, top finding a planted major. Gemini may be
trusted as the second reader for SEL at stage 1, so its real-page read (prompt 14) counts.

## Scoring (fault ids from the key; #n is the reader's finding number)

- caught majors: S1(#6) S2(#7) S3(#4) S4(#5) S5(#11, ranked minor) S6(#8) S7(#10) S8(#1) S9(#3) S10(#2) = 10/10.
  missed: none. The expert missed S7 and S9; between them the two readers caught all ten.
- minors: S11(#12) = 1/2. missed: S12 ("not seen" for "not yet" in unit field 7).
- false major alarms: 0. Real-page findings (major): #9 the short path drops "the second Application session in each
  unit", which takes 6 sessions off 64, not 32 (STANDARD.md line 62; the expert raised it too). #4's added point that
  scripts/progression.py has no band-scoped ownership rule for sel is a gate gap, checked in the fix pass.
- Minor real-page: #13 the depth ladder has three rungs but the 9 to 12 band has four years (STANDARD.md lines 84 to
  85); #14 K to 2 "three or four pictured words" against "one or two pictured steps" (APPROACH.md line 81, STANDARD.md
  line 79); #15 the student-voice placement sits in unit field 10 and section field 2 uses unit field 3's labels
  (APPROACH.md lines 70 and 74); #16 "In K to 5 a new skill is taught before it is tried" (APPROACH.md line 83); #17 no
  private student self-check per unit named for C8 (to be checked in the fix pass).
- top finding #1 = S8 planted major. PASS.

Real-page findings go to the stage 1 fix pass (data/plans/later.csv L96).

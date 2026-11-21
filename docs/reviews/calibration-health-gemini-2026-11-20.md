# Calibration: Health, second-model reader (Gemini 4 Neon, medium), 2026-11-20

Per-subject calibration at stage 1 (docs/pipeline/CALIBRATION.md, "Per subject, at stage 1"). The second-model half:
Gemini 4 Neon at medium effort in Antigravity, pasted by Cory in a new conversation (prompt
`S:/CurioClass-gemini/01-calibration-health.txt`), read the same set as the expert
(`S:/CurioClass-sources/_calibration/subjects/health/set/`) cold with the health lens and the read brief as changed on
2026-11-20. Its report is kept at `S:/CurioClass-gemini/reports/calibration-health.md`. Scored by the lead against
`key/faults.csv`, with `key/NOTES.md` used to tell planted faults from the page as it really is.

## Verdict

Passes the line: 9 of 10 majors, no false major alarm, top finding a planted major. Gemini may be trusted as the
second reader for health at stage 1, so its real-page read (prompt 10) counts.

## Scoring (fault ids from the key; #n is the reader's finding number)

- caught majors: H1(#1) H2(#3) H3(#2) H4(#7) H5(#10) H6(#6) H7(#5) H8(#9) H10(#4) = 9/10. missed: H9 (unit field 2
  "the facts that matter for the decision" dropped). The expert missed H9 too; between them the two readers caught
  all ten.
- minors: H11(#12) H12(#11) = 2/2.
- false major alarms: 0. #8 is real-page: the live STANDARD.md coverage map (lines 74 to 80) cites PHW 13, FN 13,
  PA 8, S 9 and T 6, none of which exist (hecat-topics.txt has PHW 12, FN 12, PA 7, S 8, T 5), and the K to 2 PHW cell
  omits 10 although the key says care-seeking (PHW 10 and 11) starts in K to 2. The parts of #5 on
  g5-sh-consent-and-health and g5-v-body-safety, and the grade 4 to 6 jumps in #7, are on text the key notes keep as in
  the real file; they are checked in the fix pass, not counted against the reader.
- Minor real-page: #13 STANDARD section 1 calls nhes-2024.txt "ids only" but the file carries one line per id; #14 the
  K to 2 violence cell names V 8 and not V 9; #15 the family note is unit field 9, not a section field.
- top finding #1 = H1 planted major. PASS.

Real-page findings go to the stage 1 fix pass (data/plans/later.csv L96).

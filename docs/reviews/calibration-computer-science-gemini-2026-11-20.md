# Calibration: Computer science, second-model reader (Gemini 4 Neon, medium), 2026-11-20

Per-subject calibration at stage 1 (docs/pipeline/CALIBRATION.md, "Per subject, at stage 1"). The second-model half:
Gemini 4 Neon at medium effort in Antigravity, pasted by Cory in a new conversation (prompt
`S:/CurioClass-gemini/04-calibration-computer-science.txt`), read the same set as the expert
(`S:/CurioClass-sources/_calibration/subjects/computer-science/set/`) cold with the computer science lens. Its report is
kept at `S:/CurioClass-gemini/reports/calibration-computer-science.md`. Scored by the lead against `key/faults.csv`, with
`key/NOTES.md` used to tell planted faults from the page as it really is.

## Verdict

Passes the line: 9 of 10 majors, no false major alarm, top finding a planted major. Gemini may be trusted as the
second reader for computer science at stage 1, so its real-page read (prompt 13) counts.

## Scoring (fault ids from the key; #n is the reader's finding number)

- caught majors: C1(#4) C2(#7) C3(#5) C4(#8) C6(#6) C7(#10) C8(#1) C9(#3) C10(#2) = 9/10. missed: C5 (#9 flags the
  pacing source as unread but its fix keeps the wrong one third and one fifth; the real figures are two thirds and
  about half). The expert missed C4 and C9 and caught C5; between them the two readers caught all ten.
- minors: C11(#11) C12(#15) = 2/2.
- false major alarms: 0. Real-page findings (major), both inside #10:
  - neither real page names computer science's sensitive ground or when a sensitivity read is due (no such section in
    STANDARD.md or APPROACH.md);
  - the real g5-who-included owns E5-SOC-HI-16 ("inclusion or exclusion") but teaches only exclusion, with cases
    "from memory, to be checked" and no two views (computer-science.csv line 89).
- Minor real-page: #12 courses.csv line 35 still gives the 2017 CSTA bands for cs-k12; #13 no minutes a session in
  STANDARD.md line 68 (APPROACH.md line 104 leaves them to the frames); #14 section field 1 repeats the error register
  and unit field 8 has no TOOL-ASKS.md link (APPROACH.md plan field list; to be checked in the fix pass); #15 the real
  g5-visual-algorithm never names events, which E5-ALG-PS-01 asks for (line 79).
- top finding #1 = C8 planted major. PASS.

Real-page findings go to the stage 1 fix pass (data/plans/later.csv L96).

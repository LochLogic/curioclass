# Calibration: Library, second-model reader (Gemini 4 Neon, medium), 2026-11-20

Per-subject calibration at stage 1 (docs/pipeline/CALIBRATION.md, "Per subject, at stage 1"). The second-model half:
Gemini 4 Neon at medium effort in Antigravity, pasted by Cory in a new conversation (prompt
`S:/CurioClass-gemini/06-calibration-library.txt`), read the same set as the expert
(`S:/CurioClass-sources/_calibration/subjects/library/set/`) cold with the library lens. Its report is kept at
`S:/CurioClass-gemini/reports/calibration-library.md`. Scored by the lead against `key/faults.csv`, with `key/NOTES.md`
used to tell planted faults from the page as it really is.

## Verdict

Passes the line: 10 of 10 majors, no false major alarm, top finding a planted major. Gemini may be trusted as the
second reader for library at stage 1, so its real-page read (prompt 15) counts.

## Scoring (fault ids from the key; #n is the reader's finding number)

- caught majors: L1(#7) L2(#4) L3(#5) L4(#9) L5(#10) L6(#6) L7(#3) L8(#1) L9(#8) L10(#2) = 10/10. missed: none. #7
  hedges on which III.D id replaces III.D.3 and #10 offers both doses, each including the right one, so both are
  counted. The expert missed L9; between them the two readers caught all ten.
- minors: L11(#12) L12(#11) = 2/2.
- false major alarms: 0. Real-page finding (major): #5 part 2, STANDARD.md line 74 tells writers to put the ELA or
  social studies row a library row builds on in `assumes`, but scripts/progression.py (lines 300 to 307) accepts only
  rows of the same file there; those leans belong in `cross_subject`, as section 5 (line 120) says.
- Minor real-page: #11 courses.csv line 50 holds one K to 12 library row, not the eight courses; #13 the research
  range starts at e1-shared-research, not ek-shared-research (STANDARD.md line 112), section field 2 uses unit field
  3's labels (APPROACH.md line 54), the print path sits in section field 6, not 5 (line 62), and section field 9
  names no check accommodations (line 66, to be checked in the fix pass).
- top finding #1 = L8 planted major. PASS.

Real-page findings go to the stage 1 fix pass (data/plans/later.csv L96).

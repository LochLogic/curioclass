# Calibration: Arts, second-model reader (Gemini 4 Neon, medium), 2026-11-20

Per-subject calibration at stage 1 (docs/pipeline/CALIBRATION.md, "Per subject, at stage 1"). The second-model half:
Gemini 4 Neon at medium effort in Antigravity, pasted by Cory in a new conversation (prompt
`S:/CurioClass-gemini/03-calibration-arts.txt`), read the same set as the expert
(`S:/CurioClass-sources/_calibration/subjects/arts/set/`) cold with the arts lens. Its report is kept at
`S:/CurioClass-gemini/reports/calibration-arts.md`. Scored by the lead against `key/faults.csv`, with `key/NOTES.md`
used to tell planted faults from the page as it really is.

## Verdict

Passes the line: 9 of 10 majors, no false major alarm, top finding a planted major. Gemini may be trusted as the
second reader for arts at stage 1, so its real-page read (prompt 12) counts.

## Scoring (fault ids from the key; #n is the reader's finding number)

- caught majors: A1(#3) A2(#4) A3(#5) A4(#7) A5(#10) A6(#6) A7(#2) A8(#1) A10(#8) = 9/10. missed: A9 (rights line
  moved off the unit plan to the day page). #5 keeps MU:Pr4.2.5c in mu-g5-read and drops it from mu-g5-respond, the
  real owner; that still leaves one owner, so it is counted, and the fix pass keeps it in respond. The expert missed A9
  too; neither reader caught it.
- minors: A11(#13) A12(#15) = 2/2.
- false major alarms: 0. Real-page findings (major):
  - #5 parts 2 and 3: the real mu-g5-respond notes never teach MU:Cn11.1.5a (music and other arts, subjects and daily
    life) and drop "citing music-element evidence for setting fit" from MU:Re9.1.5a (arts.csv line 149).
  - #9: STANDARD.md lines 110 to 112 count the Level 1 bridge unit, which teaches grade 8 ids, as inside the standards
    for the 10 percent limit; on the 80-day path 12 days is 15 percent. This rests on Desk q-prework-arts-1, so the fix
    pass weighs it with Cory.
  - #11: APPROACH.md line 78 makes teaching first the default only in grades 2 to 5, leaving out K and 1 (the expert
    raised it too).
  - #12: APPROACH.md puts safe use under section field 9 (line 160) and has no slot for the error register (unit
    field 6) or expected errors (section field 4) and leaves fields 8 and 9 unmarked as section fields (lines 133 and
    138). Its point on a missing Evidence and sources section is on the excerpt only (the real page has it, line 192):
    neutral.
- Minor real-page: #14 the levels to grade column mapping for the gate and the unloaded MU .C. ids (STANDARD.md
  section 3.2 and 3.3); #15 mu-g4-perform and mu-g5-perform drop the solo-or-doubled teacher note (arts.csv lines 139
  and 147) and mu-g5-revise drops "explain how it shows intent" (line 144); #16 "20 courses" against five K to 12 rows
  in courses.csv; #17 the leans in STANDARD.md section 6 name no codes.
- top finding #1 = A8 planted major. PASS.

Real-page findings go to the stage 1 fix pass (data/plans/later.csv L96).

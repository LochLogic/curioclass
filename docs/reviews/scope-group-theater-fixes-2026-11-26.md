# Scope group fix pass: theater, K to 12 (2026-11-26)

Brief: build/scope-writes/GROUP-FIX.md. Read applied: docs/reviews/scope-group-theater-2026-11-26.md (8 scope,
2 frame, 0 structure, 0 Cory). Courses: theater-grades-k-to-2, theater-grades-3-to-5, theater-grades-6-to-8,
theater-grades-9-to-12. Also read: build/scope-writes/GROUP-READ.md and ARTS-FIX.md (lead calls 1 to 9 still hold).
The days.csv edits were made with a Python csv script that kept the files' quoting and CRLF line endings. Each
finding is logged in the defect ledger (made at scope, found by expert), one row per course touched.

## Applied

1. **Seam: stage areas and blocking (scope; lead call: the read's pick).** Theater 6 to 8 day 23 now teaches stage
   areas (stage left, downstage) and blocking in steps on a taped stage-areas floor card during the walking-pace run,
   each move written on the script as it is set. Its note says this is the first teaching and that Theater, grades 9
   to 12 day 1 checks it as a grade 8 technique. Day 164's venue plan names its playing areas by stage area and marks
   one blocking move for each problem. Both days carry "Words: stage left, downstage, blocking". The unit 2 and
   unit 11 arc lines in the .md say the same. No day count, unit or code changed. 9 to 12 day 1 stays as written.
2. **Models "first used" (scope).** 6 to 8 notes on days 1, 3, 22, 36, 37, 39 and 50 now read "returns from Theater,
   grades 3 to 5 unit n; here ...". The units are 2 (audience journal, character map), 1 (what-if list), 3 (prop
   sketch, two-ties), 11 (cue sheet) and 4 (criteria card), and each note says what grows, taken from the frame's
   Models table. Script markup (day 20) and reason-because (day 39) still say "first used".
3. **Written-day load (scope).** All twelve 6 to 8 written days (17, 31, 47, 61, 81, 95, 111, 125, 145, 159, 175,
   189) now carry "a student may answer aloud at the table, marked the same". TH:Cr3.1.6b (body and voice traits that
   work) moved from day 17 to day 16's showing as a live look-for. Day 16's goal and codes, day 17's goal, codes and
   note, and the unit 1 Assessments line were updated. Day 17 now holds three items, and no written day sets more
   than three (checked by script). The .md End-of-unit bullet states the spoken option.
4. **Once-a-week path (frame; lead call: 6 to 8 drops its mid-year check as 3 to 5 does, frame wording only).**
   The 6 to 8 frame's once-a-week bullet now keeps only the year-end check (week 31, respond in week 32) and drops
   the mid-year check, for the 3 to 5 reasons. The two freed sessions go to the design unit (3, 7, 11), so each year
   runs units of 9, 7, 8 and 6 sessions. The design unit's split is study 1, a making session alone 1, then
   rehearsal, critique and revision 3, then showing, written and respond. It runs in weeks 17 to 24. For the lead
   item 1 in the frame was reworded to match.
5. **Floor rule drift (scope).** All 12 floor lines in 3 to 5 now add "no lifts, no falls, no contact stage fights".
   On day 1 the line reads "freezes held still, no falls, no lifts, no contact stage fights". The .md equipment
   bullet carries the frame's hazards line: no lifts, no falls rehearsed, no contact stage fights.
6. **Family content notes (frame; lead call: the read's pick as frame wording).** Each of the four frames gains a
   "Content notes to families" bullet after its Sensitivity reads bullet. A studied work gets a content note to
   families (to the student at 18 or over) when its subject includes violence against a person, a killing, sexual
   violence or drug use, even when only described. Other hard history is named plainly with no note. Each bullet
   names its band's cases:
   - 9 to 12 day 68 (Twilight: Los Angeles, 1992) now has the note, beside Sweat (224) and Sovereignty (417 to 432).
   - 6 to 8 day 179 (Woza Albert!) now has the note.
   - 6 to 8 days 73 and 118 and 3 to 5 day 165 stay named plainly with no note.
   - K to 2 and 3 to 5 have no work that meets the line.
7. **Unnamed revisits (scope).** Three notes now name the revisit and its new job:
   - 9 to 12 day 167: noh's own form, after 3 to 5 day 17's kyogen.
   - 9 to 12 day 328: kabuki as a borrowed tradition, after 6 to 8 unit 7 (days 99 to 112).
   - 6 to 8 day 177: Boal's forum theater, after 3 to 5 unit 11 (days 165 and 169), the audience now stepping in.
8. **Shadow theater (scope).** Two notes now name the revisit:
   - 3 to 5 day 101 (tholu bommalata): a revisit of the year's wayang (day 71), with the lamp as a tech element
     serving a central idea as its new job.
   - K to 2 day 165 (Karagöz): a revisit of kindergarten's shadow day (day 42), with the light-and-sound cue as its
     new job.

   The read's optional swap of tholu bommalata for a non-shadow tradition is left to the unit 7 plan, as the read
   allows.
9. **Shared cards (scope, finding 10).** Three cards now keep their earlier lines as they grow:
   - Agreements card (3 to 5 frame Models table): "take turns, add on, freeze on the signal, join when ready, and
     from grade 3 keep the space safe".
   - Warm-up routine (9 to 12 day 2 goal and the frame's unit 1 row): "body, breath, voice and focus", as in 6 to 8.
   - Freeze (3 to 5 day 2): named as K to 2's freeze and melt, with the breathe step added.

   3 to 5 keeps "body, voice and thinking", as the read asks.

## Rejected

- **Finding 9 (K to 2 school_day to ceil(2.5 n)).** Rejected. Arts lead call 8 is settled: keep the scope's own
  school_day formula, never re-count to match calendar.csv or frame.py's spread, and the lead regenerates
  calendar.csv at commit. K to 2's formula already counts across the band (lead call 5), puts every unit and check
  in the frame's weeks, and is stated once in its .md. The read's goal of one rule across the group is a calendar
  matter for the lead's pass, not this fix.

10. **6 to 8 once-a-week wording in the scope (finding 4 follow-on, at the lead's request after the first report).**
    Wording only; no days.csv row or count changed. The once-a-week paragraph in the 6 to 8 scope now reads 9, 7, 8,
    6 sessions a year plus the year-end check (week 31) and its respond session (week 32), with the mid-year check
    dropped on that path. The session table now gives units 3, 7 and 11 eight sessions each, with day order kept:
    - Unit 3: S2 38, 39; S3 40 (making alone); S4 41, 43; S5 44, 45; S6 to S8 for the showing, written and respond.
    - Unit 7: S2 102, 103; S3 104 (making alone); S4 105, 107; S5 108, 109.
    - Unit 11: S2 167, 168; S3 169 (making alone); S4 170, 172; S5 173.

    The paragraph under the table no longer calls the split a lead's call. The scope's For the lead item 1 is marked
    closed.

## For the structure pass and the lead

- **APPROACH.md line (finding 6).** The content-note threshold is now in each theater frame. The read's pick also
  puts it once in docs/courses/arts/APPROACH.md "Sensitive ground", a shared arts file outside this job.
- No structure or Cory findings were raised by the read.

## Checks

- `scripts/sequence.py check`: theater-grades-k-to-2, 3-to-5, 6-to-8 and 9-to-12 each show 0 failures.
- `scripts/frame.py check`: all four show 0 failures. Both checks were rerun on theater-grades-6-to-8 after item 10:
  0 failures each. Notes only: day counts unchanged (192, 192, 192, 640). On
  9 to 12, units 18 to 20 report "standard None is on no day", a note that was there before this pass.

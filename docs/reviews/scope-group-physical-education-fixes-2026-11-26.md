# Scope group fixes: physical education, 2026-11-26

Fix pass for docs/reviews/scope-group-physical-education-2026-11-26.md, by build/scope-writes/GROUP-FIX.md, over
physical-education-grades-k-to-2, -grades-3-to-5, -grades-6-to-8 and -grades-9-to-12. All nine findings were tagged
scope; all nine are applied, three with a correction to the read (below). One extra scope fix came from the lead:
docs/reviews/scope-group-dance-2026-11-26.md finding 8 (PE 6 to 8 day 276). No unit moved, no day count or owned row
changed. Health, SEL and dance files were read only, never edited. Each fix is logged with `plan.py defect`.

## Applied

1. **Team talk quotes health's conflict steps.** The words come from health's scopes as they stand today:
   - Grade 2 form, "stop, say what happened, listen, find a fair way, and an adult helps when words do not work",
     from health K to 2 day 72. Health K to 2's scope-and-sequence.md names the day but does not word the steps;
     the day's goal in its days.csv does.
   - Grade 5 and 6 to 8 form, "stop, calm down, each says their side, find a fair way, or walk away and get help",
     from health 6 to 8's scope-and-sequence.md "Health's own cards" (taught on health 6 to 8 day 51). The same words
     are on health 3 to 5 day 77 (unit 18, grade 5 week 17).

   Changes by course:
   - 3 to 5: days 49, 103 and 181 now print the grade 2 form. Day 203 (grade 5 week 18, after health day 77) prints
     the grade 5 form. Day 49 keeps SEL's talk turn card as a listening card and says it is not team talk. The other
     uses (51, 106, 110, 112, 185, 187, 190) say "team talk" and take the form in force on their day.
   - 3 to 5 .md: the Shared cards bullet, the unit 5 and unit 18 arcs and the leave-out bridge now say the same.
   - 3 to 5 frame: the two cross-subject rows that said "in SEL's words" and "PE uses SEL's talk turn card" now match.
   - 6 to 8: days 1, 39, 45 and 135 print the steps. 9 to 12: days 8, 47, 50 and 285 print them. Each .md Shared
     cards bullet names them.
2. **Grade 9's first readiness check.** On 9 to 12 day 1, `assess` is cleared and the note says why: both rows were
   last used in grade 8, on PE 6 to 8 day 194. Day 2 retrieves g7-effort-aerobic and g7-fitt-principles. The .md
   unit 1 paragraph, the .md "The day" bullet and the frame's unit 1 cell are reworded to match.
3. **Water units.**
   - K to 2: the cue is "shout for a grown-up, then reach or throw, don't go" on days 230, 231, 237 and 238. Day 230
     carries the Palm Beach County "Reach, Throw, Don't Go" source line.
   - Reach base, following the cited page (lying on the stomach only): 3 to 5 "a lying or kneeling base" becomes
     "lying on the stomach" (days 226, 227, .md). 6 to 8 day 268 and 9 to 12 day 137 change "lying flat" to "lying
     on your stomach", and so does the 6 to 8 .md.
   - Each band's .md water paragraph and family card now name what that band adds:
     - K to 2: fastening, plus a grown-up called first.
     - 3 to 5: the buddy rule, and floating and strokes shown on the floor.
     - 6 to 8: choosing reach or throw for a scene, and cold water.
     - 9 to 12: currents and hypothermia. Day 137 now retrieves 6 to 8's cold-water rule rather than teaching it new.
4. **Records picked up.**
   - 3 to 5 day 2: the K to 2 record, where kept, sets the first groups.
   - 6 to 8 day 2: each student reads the grade 5 skill sheet and circles one cue.
   - 9 to 12 day 2: the grade 8 record and private fitness plot, where kept, open the private log.
   - Each adds "where a student has no record, nothing changes". The 3 to 5 assessment bullet and the 6 to 8 unit 1
     paragraph say so too.
5. **Family game case.** 9 to 12 day 112, the .md unit 9 paragraph and the frame's unit 9 Candidate cell now use the
   unit 22 rule: only where its source says the game is open to be taught, no sacred or ceremonial game, and the
   teacher reads the source with the student. The 3 to 5 drop stands. K to 2 and 6 to 8 are unchanged.
6. **Sepak takraw.** The 9 to 12 .md Sensitivity bullet now says the rules are sourced to ActiveSG (opened
   2026-11-26) and that sepak takraw stays a candidate until the sensitivity read. The "Sources not loaded" bullet
   names the ActiveSG page as opened.
7. **Heart rate count.**
   - From grade 6 on, the count is fifteen seconds times four.
   - 9 to 12 retrieves it, and a ten-second count is shown as a quicker option between intervals.
   - The neck caution, still "from memory" for the safety agent, is added to 6 to 8 day 25 and 9 to 12 day 5.
   - The 9 to 12 .md unit 1 arc and the frame's unit 1 cell match.
8. **Reduced paths.**
   - 3 to 5 adds "A shorter period" (25 to 30 minutes). Its fold-ins are now counted as 5 sessions (175 minutes) a
     year.
   - 9 to 12 adds "A shorter period" (35 to 40 minutes, in 6 to 8's split; the one-check-day units are 11, 15, 18, 21
     and 24).
   - In 9 to 12, a 10-day loss now folds the first five named days of each year (225 minutes a year). The other five
     are kept for a 20-day loss, and the 20 day notes say so.
9. **Conduct codes.** A conduct review outside its owning unit now writes the reviewed S3 id with `~` in the codes
   column on the day that marks it:
   - 3 to 5: 18 check days (20, 31, 41, 61, 71, 79, 89, 99, 121, 133, 141, 152, 159, 172, 201, 221, 231, 239). Day
     41's S3.5.3 is a begun id (owned in unit 5).
   - 6 to 8: 15 days (22, 33, 62, 76, 90, 117, 129, 158, 171, 186, 214, 227, 252, 264, 283).
   - 9 to 12: 24 days (28, 33, 35, 47, 50, 62, 75, 87, 89, 104, 140, 155, 185, 214, 221, 225, 233, 236, 244, 252, 267,
     302, 305, 319).
   - Each .md says so once.
10. **Lead item, dance group read finding 8.** The PE 6 to 8 day 276 note now says: a student who took dance 6 to 8
    retrieves its unit 8 capoeira history; every other student, and every student where the school has no dance
    course, gets the history from the case card first. The 6 to 8 .md unit 22 paragraph, its leans bullet and the
    frame's lean row are reworded to match.

## Rejected or corrected

None rejected outright. Three parts of the read were corrected:
- **Finding 7:** 9 to 12 teaches heart rate on day 5, not in "unit 1 (days 1 to 3)" or on day 1. The fix went on
  day 5.
- **Finding 3:** the read names "planning an outing's water safety" as new in 9 to 12. No 9 to 12 day teaches that,
  so the .md names only what the days teach: currents, hypothermia and the open-water scenes. Adding outing planning
  would be new content.
- **Finding 9:** the read says 3 to 5 "codes none" and marks conduct "with no S3 id". In fact the 3 to 5 notes name
  the id ("Conduct is SHAPE.S3.5.x in review"), but the codes column did not carry it. The fix (the `~` code)
  applies all the same.

## For the structure pass

None. No finding needed a unit, day count, owned row or progression change.

## For the lead

- **SEL 9 to 12 frame, stale "For the lead" item.** SEL 9 to 12 frame.md "For the lead" item 5 calls PE 9 to 12 day
  296's citation of "SEL 9 to 12 unit 22's balanced week" wrong. It is right: SEL day 229 designs one. Its other two
  PE points are also stale: PE day 66 now cites unit 1, and the PE frame names data/plans/calendar.csv. I did not edit
  the SEL file, as the brief says.
- **Health K to 2's scope page** names the short conflict steps on day 72 without wording them. PE quotes them from
  health's days.csv goal for that day. A health pass may want the words on the .md.

## For Cory

None.

## Check results

- `sequence.py check`: 0 failures in all four courses. K to 2 keeps its three "Fluency, first day for ~S3" notes,
  which were there before this pass. 9 to 12 keeps the "standard None is on no day" notes for units 13 to 24, which
  lead call 12 leaves alone.
- `frame.py check`: 0 failures in all four courses.

# Scope group fixes: visual arts, 2026-11-26

Courses: visual-arts-grades-k-to-2, visual-arts-grades-3-to-5, visual-arts-grades-6-to-8, visual-arts-grades-9-to-12.
Brief: build/scope-writes/GROUP-FIX.md, applying docs/reviews/scope-group-visual-arts-2026-11-26.md, with the
ARTS-FIX.md lead calls kept. Only scope-and-sequence.md and days.csv changed (days.csv by csv module script, CRLF
and quoting kept, round trip checked before editing). No unit moved, no day count, owned row, code or `assess`
value changed. No frame.md and no progression row changed. Each finding is logged with `plan.py defect`.

## Applied

1. **Printmaking ladder (scope).** 9 to 12 day 169 now teaches collagraph in named steps as the Level 2 step,
   naming the grade 3 one-color foam print (3 to 5 days 4, 5) and the grade 8 two-color print (6 to 8 days 134 to
   136) as known, with the one-color foam step card kept as the reteach for a student new to visual arts; hazard
   line adds glue labeled non-toxic and card torn or cut by an adult, no blades. Day 168 lists "collagraph print" as
   the medium. Day 332's print group is a multi-plate collagraph printed in register, named one step past grade 8.
   I chose multi-plate over reduction (the read offered either): a reduction print needs plate cutting, which the
   blade rule bars. Scope unit 7 order line updated.
2. **Washes (scope).** 6 to 8 day 66: grade 5's flat, graded and wet-into-wet washes come back as a five-minute
   strip (retaught in full for a student new to the band), and the new step is controlled layers; day 67 drops wet
   into wet (grade 5 work) and keeps dry brush and Fan Kuan's layering. 9 to 12 day 170: value planned in three
   layers over a dried ground, the step past grade 7; day 332: glazing at a larger scale over a full series, past
   Level 2. Scope unit 5 arc updated.
3. **Contour and the color wheel (scope).** The read's first option: 6 to 8 day 7 opens with blind and modified
   contour, first taught there, drilled on day 10 (the drill already folds into day 11 on the short year, so the
   short path is unchanged). 9 to 12 day 5 says "taught in grade 6, retaught here"; day 8 and the unit 1 text say the
   full mixed wheel is first built in the bridge. Unit 1 text no longer calls everything "grade 8 work".
4. **Critique routine (scope).** One name in all four courses, "the critique routine (describe, ask, suggest)".
   K to 2 day 15 (and scope Kinds line) adds turn-taking pictures and both rules; day 150 "critique routine card".
   3 to 5 day 13 adds the suggestion tied to a look-for and both rules; day 28 is "the critique routine's partner
   talk (not a new card)"; days 30, 82 follow; day 89 is grade 4's additions (roles, the artist's planned change);
   days 103, 146 and the unit 2 and 6 order lines follow. 6 to 8 day 11: the routine returns, grade 6 adds criteria,
   both rules. 9 to 12 day 10 and the unit shape bullet: the K to 12 routine, the band adds vision and named
   standards, both rules. Work card fields: 3 to 5 day 54 now "maker, place, date, purpose"; 6 to 8 day 1 adds the
   rights line from grade 6. Value scale: 6 to 8 day 2 is nine steps, matching the bridge.
5. **Leave-out (scope).** Followed each frame's Leave-out bullet: the leave-out is a community's choice of a work
   or a unit, never a time cut, and swapping a work keeps the unit, its showing and every id. 3 to 5: the four
   time-cut sentences are gone (units 4, 8, 12 and the short-year bullet, which now says the fold-ins are the only
   short-year route). Each named unit's line now gives the frame's reason and the ids not claimed if the whole unit
   is left out: K to 2 units 8, 12; 3 to 5 units 4, 8, 12; 6 to 8 units 5, 8, 11, 12 (new bullets); 9 to 12 units
   5, 14, 15 (with the 18-and-over choice).
6. **Two levels, "pending" (scope).** 9 to 12 section retitled "Two levels in one room (Cory, 2026-11-26, Desk
   q-frames-arts-1)"; it states the Levels 1 and 2 rule and that the unit plans mark the shared days. The Levels 2
   and 3 pairing is kept as a separate paragraph marked pending Cory (finding 7); For the lead 4 says the same.
8. **Returning works (scope).** 9 to 12 day 1 (Dürer from grade 1, van Gogh from grade 4), day 13 (Migration
   Series met in grade 3 without the panels of violence; Level 1 adds them, named in the family note; Lawrence also
   opened grade 6), day 280 (Persian or Mughal painting from grade 7, new task), day 363 (Smith from grade 7), day
   445 (Rivera from grade 5), day 481 (Monet from grade 2). 6 to 8 day 86 names the Level 2 return.
9. **Task forms (scope).** 6 to 8 day 168: grade 4's grid and color plan known, new steps edge marks and squaring to
   mural scale (unit 11 arc too). 3 to 5 day 168: grade 3's map with a key known, new step labels in art and design
   words (unit 11 order line too).
10. **Portfolio (scope).** 9 to 12 unit shape bullet: the portfolio or a photo record stays at school across levels;
   a placed student uses the brought work of the placement checklist on days 203 and 237 (both notes say so) and
   writes a first reaction on day 329. 6 to 8 unit 12 Why here: the year's kept work with earlier pieces as
   photographs.
11. **Writing ramp (scope).** 9 to 12 day 413: the competing readings and the defended one as a multi-paragraph
   argument of about 500 words; day 418's mid goal and the unit 14 scope text say "argument". Day 608: Level 4
   labels at 80 words, matching Level 3.

## Rejected

12. **K to 8 weekdays (scope).** Not applied. ARTS-FIX lead call 8, which this brief says still holds, tells each
   course to keep its own school_day formula, and weeks already agree (frame.py and CALENDAR.md pass). Moving 3 to 5
   to the third and fifth days rewrites 192 school_day cells and needs the lead to regenerate calendar.csv; if the
   lead wants one weekday pattern across the band, it is the lead's change, not a fixer's.

## For the structure pass

- None of the findings needed a unit, row or day count moved.
- Frame wording the lead may align at the next frame edit (not a frame finding, so left): visual-arts-grades-3-to-5
  frame.md "Picked up from" table still says "work card (who, where, when, what for)" (line 253) and "inside the
  critique protocol" (line 248).

## For Cory

7. **May Levels 2 and 3 share a room?** Not asked in Desk q-frames-arts-1, which named Levels 1 and 2 only.
   Options: (a) yes, by the same rule (own units and ids, shared opening look and critique days); (b) no, only
   Levels 1 and 2, and the scope drops the Levels 2 and 3 paragraph. The read's pick: **(a)**, since the days already
   line up and a small high school is as likely to combine second- and third-year students. Not applied; the scope
   keeps the pairing marked pending.

## Browser check

Kept as the read left them: https://americanindian.si.edu/nationtonation/ (403) and
https://www.metmuseum.org/art/collection/search/45434 (429), both "browser check" for the lead.

## Checks

`sequence.py check` and `frame.py check`, run after the edits on all four courses: 0 failures each
(visual-arts-grades-k-to-2, -3-to-5, -6-to-8, -9-to-12). No em dashes in any touched file.

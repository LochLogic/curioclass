# Scope group fixes: social and emotional learning, K to 12 (2026-11-26)

Applied docs/reviews/scope-group-sel-2026-11-26.md with the AFTERCORE-FIX.md lead calls, under
build/scope-writes/GROUP-FIX.md. Courses touched: social-and-emotional-learning-grades-k-to-2, -3-to-5, -6-to-8 and
-9-to-12. No unit moved, no day count changed, no owned row changed. Health, PE, STANDARD and scripts were not edited.
days.csv files were edited with the Python csv module, keeping each file's quoting and line endings (3 to 5 LF, the
others CRLF). 29 defect rows logged (status fixed, made at scope).

## Applied

1. **First day of a band (sequence).**
   - 6 to 8: day 1's readiness check is gone. The day now opens with one three-part retrieval item on
     g5-sm-plan-and-tidy, g5-sm-stay-on-task and g5-sa-i-can-try. A class without SEL 3 to 5 gets the grade 5 card
     forms in the first ten minutes, claiming nothing, as 3 to 5 day 1 does. Day 5 lost its "where day 1's card showed
     it" clause. The scope's Readiness and unit 1 bullets and the frame's Days, Seams and Leave-out text match.
   - 9 to 12: the day 1 Given: item on the grade 8 card became the same bridge (the grade 8 card forms, claiming nothing;
     STANDARD 5.6 keeps Given: for a left-out unit). The scope's Readiness and Candidate bullets match, and the frame's
     Candidate cell is marked settled.
2. **Carriers on the days (missing).**
   - 6 to 8:
     - Each unit's first day has its carry-out cue.
     - Each Respond day has the family note line and the family activity. Units 3, 6, 9, 12, 15 and 18 use the
       course-level Respond days 31, 64, 95, 128, 160 and 192.
     - Day 99 names health units 3 (grade 6) and 11 (grade 7). Grade 7 health has no stress unit.
     - The scope has a carriers bullet.
   - 3 to 5:
     - The disclosure line is on days 12, 54, 65, 75, 85, 117, 139, 149, 170 and 182.
     - Day 46 carries the core link math:m3-scaled-graphs.
     - The scope's Respond line names the carriers.
   - K to 2:
     - Core links added: day 23 (social-studies:ssk-story-characters), day 57 (math:mk-sort-count), day 124
       (math:m1-data-three-categories) and day 164 (ela:e2-discussion).
     - Day 182 already named its math lean, so I changed it to the Core link form.
   - 9 to 12:
     - The disclosure line (health's steps, APPROACH.md) is on days 22, 43, 54, 65, 85, 96, 118, 150, 160, 182, 193, 214
       and 224.
     - Day 75 names health 9 to 12 unit 7 and says health owns mental health.
     - The scope has a Students 18 or over bullet (Desk q-prog-sel-1) and a carriers bullet.
3. **Refusal card (wording, missing).** This follows the lead call: health's "a reason or none" and the full steps
   "say it, say it again, move away, tell".
   - 3 to 5:
     - Day 43's card now reads "give a reason or none" and keeps the second push ("if it comes again: say it, say it
       again, move away, tell").
     - The second push is rehearsed on days 43, 51, 112, 114, 165 and 167.
     - Day 112's health note says "same words".
     - The progression row g3-rel-say-no was reworded. I spliced back that one row only and checked it with a diff.
     - The frame rows (line 12, Models carried, the health table, For the lead 4) and the scope's Refusal steps line
       match.
   - 6 to 8:
     - The second push is rehearsed on days 38, 40, 76, 79, 145 and 147.
     - The scope's unit 4 Order bullet and the frame's Models carried row carry the full card.
   - 9 to 12:
     - Day 35 now treats the second push as carried from grades 3 to 8, retrieved and not new, in the full words.
     - Frame lines 13, 139 and 148 match.
4. **3 to 5 leave-out bridges (wording).** Twelve bridge notes (days 12, 22, 33, 43, 60, 65, 75, 79, 95, 98, 109 and
   112) now model the one-step form, "the card named, its first step modeled once". The frame's Leave-out bullet and the
   scope's Leave-out section match.
6. **Unit titles (wording).** The 9 to 12 frame's Picked up table now uses the SEL 6 to 8 titles, 40 replacements:
   - Deciding under pressure
   - Values that cost
   - Heavy weeks
   - Other views, fair norms
   - Hard talks and fair deals
   - Improving our school
7. **Repeated projects (sequence).**
   - 6 to 8: day 54 names the step up from grade 5, and day 56's audience is a grade team or the principal. The scope's
     unit 6 bullet and the frame's unit 6 safety text match.
   - 9 to 12: unit 23's default community fix is a printed guide for new ninth graders, made inside school (days 241 and
     243, scope, frame lines 23 and 167). Day 244's hidden term is now in a job offer letter, a different document from
     grade 11's offer sheet on day 152. The scope's Candidate bullet matches.
8. **Settled cases (source).**
   - Day 43 now reads "a federal appeals court upheld in 1947".
   - Day 85 names Mendez as the year-before case whose arguments were later used in Brown (U.S. Courts).
   - The scope's Settled cases bullet names the arc: schools, then travel, then public places.
9. **Cultural picks (wording).** All four frames' Sensitivity bullets now say: a place already used in any SEL band (and
   in that grade's PE and arts) is not used again, and the unit plan lists the places used so far. The K to 2 bullet
   names Ampe and acchi muite hoi.
10. **Begun AASL ids (alignment).**
    - 44 `~AASL` codes were dropped from grades 9 to 11 rows (days 1 to 192, C rows included). The notes still name the
      ids.
    - The frame says this once.
    - 9 to 12 scope For the lead 4 is closed.
11. **Owned codes off the checks (alignment), frame part.** Each frame's Course-level paragraph now says: an owned code
    not sampled on a course-level check is assessed by its own unit's end-of-unit assessment, which is rule 3's named
    reason, and the two-sample cap stays. 3 to 5 scope For the lead 1 and 9 to 12 scope For the lead 2 are marked
    settled.
12. **Short-path check weeks (timing).**
    - K to 2, scope and frame: grade 1 unit 7 and grade 2 unit 13 run in 4 sessions, and units 12 and 18 run in 6.
      Check weeks: kindergarten weeks 11 and 26, grades 1 and 2 weeks 10 and 26. All are clear of health's weeks (K 12
      and 27, grades 1 and 2 11 and 27).
    - 6 to 8, scope: check weeks are grade 6 weeks 17 and 32, grade 7 weeks 17 and 32, and grade 8 weeks 16 and 32. Week
      17 also holds health's grade 6 and 7 mid-year checks. CALENDAR rule 3 counts days, so the school puts the SEL
      session on a different day, and the scope says so.
- **Lead extra (9 to 12 frame For the lead 5).** The item said PE unit 23's citation of "SEL 9 to 12 unit 22's balanced
  week" was wrong. It is marked settled: SEL day 229, in unit 22, has each student design a balanced week. The item's
  other two PE points stay open.

## Rejected

None. Two parts were close calls:
- Finding 2 in K to 2 unit 18 was partly a false gap: day 182 already named its math lean. I only normalized it to the
  Core link form.
- Finding 3 asked health to match. Health is handled by the health fix pass running now, so no health file was edited
  here.

## Structure pass (for the lead)

- **Finding 13: unit_skeleton.py's SUBJECTS has no SEL.** Because of this, sequence.py prints no rule 2 notes for SEL.
  The read's fix is to add SEL and the other after-core subjects to SUBJECTS. Pick: do it. Finding 1 is the kind of miss
  the tool would catch. Scripts were not edited here.
- **STANDARD parts (owner lead), not applied:**
  - Section 7, refusal row (finding 3): the 3 to 5 and other band rows should read "a reason or none" plus "say it, say
    it again, move away, tell".
  - Section 7, 3 to 5 rows (finding 5): add the talk turn, calm-down, goal steps and refusal rows. State that goal
    steps keeps four steps through 6 to 8 and grows only in 9 to 12.
  - Section 7, grade 2 talk line (finding 5): either add "I hear ___; I think ___ because ___" to section 7, or name it
    in K to 2 as a separate disagree frame. Pick: name it in K to 2 as a disagree frame, since the card stays smaller.
  - Section 3 (finding 6): either say once that frame titles win, or take the 6 to 8 titles. The section also still
    lists "Stress and strong feelings" and "Under pressure". Pick: take the 6 to 8 titles.
  - Section 5 (finding 9): add the cultural-places line that is now in each frame.
  - Section 2 (finding 11): add the owned-code reason that is now in each frame.
- The 6 to 8 frame's Units table still uses STANDARD's titles, not the scope's. This goes with the section 3 call.

## Cory

None of the findings needs Cory.

## Check results

| Course | sequence.py check | frame.py check |
|---|---|---|
| K to 2 | 0 failures | 0 failures |
| 3 to 5 | 0 failures | 0 failures |
| 6 to 8 | 0 failures | 0 failures |
| 9 to 12 | 0 failures | 0 failures |

progression.py check sel: 520 rows, 0 failures.

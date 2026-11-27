# Scope group fix pass: career education, 2026-11-26

Brief: build/scope-writes/GROUP-FIX.md. Read applied: docs/reviews/scope-group-career-2026-11-26.md. Courses:
career-exploration-grades-6-to-8 and career-pathways-grades-9-to-12. The AFTERCORE-FIX.md lead calls still hold. Two
extra files were in scope for this group only, by the lead's prompt: docs/courses/career-education/APPROACH.md
("Pacing") and the DIGEST line that recorded the first-job source rule. No library course was edited.

## Applied

1. **Lateral reading, one card (scope).** Lead note followed over the read's split fix: both career days quote
   library 9 to 12's routine card words, the band's end form (stop, investigate the source, look for better coverage,
   trace the claim to its original), not library 6 to 8's grade 6 words, which a library fix pass may still reword.
   - Exploration day 9: goal and note teach that card (library g9-lateral-method named as its source) in place of the
     course's own three steps; the opening retrieval of g6-lateral-reading stays. Scope's retrieval table row matches.
   - Pathways day 84: the steps are that card, retrieval for a student who took library 9 to 12, taught from the card
     for one who did not; `retrieves` = g9-lateral-method. Day 80's readiness drops library g6-lateral-reading (now
     named as retrieval on day 84). Scope: the readiness lead-in drops library g6-lateral-reading; the bridge sentence
     names only ELA grade 10 and computer science as later, and SEL 9 to 12 and library 9 to 12 grade 9 rows as the
     year before (retrieval for a student who took them); the day 84 bullet names the card. Frame Models carried,
     lateral-reading row: library `g9-lateral-method` behind it.
2. **First job's hour and task limits (scope).** Exploration day 90 and Pathways day 72 cite the Wage and Hour
   Division's Fact Sheet #43 (https://www.dol.gov/agencies/whd/fact-sheets/43-child-labor-non-agriculture) for the
   figures, keep YouthRules as the student-facing page and the young workers page for a safe workplace and who to ask,
   and keep "a stricter state law applies where there is one". The child labor page is no longer cited. Matching
   wording: Exploration scope Sources bullet and frame unit 7 Units cell; Pathways scope unit 5 source line. DIGEST
   line: the "Settled (for DIGEST)" row in docs/reviews/sequence-career-exploration-grades-6-to-8-fixes-2026-11-26.md
   (not yet copied into docs/reviews/DIGEST.md, which has no career line) now records Fact Sheet #43 and why.
3. **Pathways readiness checks (scope).** Days 1, 12, 43, 54, 67 and 80 now name the two APPROACH items plus at most
   two more (about two minutes each), and list every other assumed row as "taught again in context" with its day
   (found with a script from cte.csv `assumes` against the days' skills). Day 12's two: a job on the cluster map and a
   wage against a training cost; day 54's: a route's dated cost and a trade-off, as the read named. Days 14 and 23's
   Retail lean now says m7-compare-populations is taught again there with one worked example. The scope's readiness
   table now has "Items sampled" and "Taught again in context" columns; the frame's Readiness and retrieval bullet
   says the same (frame wording). Every id stays in each note, so sequence.py's rule 2 counting is unchanged.
4. **Production line safety (scope).** Exploration days 33 and 34's safety words and supplies (scrap paper, school
   scissors counted out and back in, cut away from the body, seated, five minutes of clean-up) added to Pathways days
   14 and 23 (session 1 of each shared block) and 32 (packet day 2, the session-1 step), where Advanced Manufacturing
   is the cluster. The read named packet days 31 and 34; 31 is the explore day and 34 the session-3 step, so 32 is the
   right packet day. Scope: the "Every day" safety bullet adds the production line; the slot table note says session 1
   is the grade 8 first-look task at higher demand and its task sheet names what is new; the safety line names the
   production line. Frame safety read list adds it.
5. **Sensitive sub-cluster list (scope).** Pathways day 19 and the scope's sensitive list drop Water Systems; it keeps
   the views line (no verdict, a view never graded) with no leave-out. Resource Extraction follows STANDARD.md section
   6 in both courses (the read's pick): Exploration day 51's health-steps sentence removed; the scope's Sensitivity
   bullet and the frame's Sensitive ground line now name the four sub-clusters section 6 lists, with Resource
   Extraction under the views rule.
6. **Desk answers that had not reached (scope).** Exploration day 86's "Pending Cory" line now states the call (day 86
   stays in unit 7; a school whose deadline is earlier teaches it in its registration week). APPROACH.md Pacing: the
   short path is set by each frame, Exploration 66 sessions, about 50 hours (30 fold), Pathways 64 sessions, 48 hours
   (32 fold), with Desk q-career-scope-1 named.
7. **Pathways unit 6 short row (frame).** The Shorter path table's unit 6 row now states the lighter applied project:
   one option weighed and tested, the second try on paper, the effects map one line; scored codes unchanged.

No unit, day count, owned row or school_day moved.

## Rejected

None. Finding 4's packet day numbers (31 and 34) were corrected to 32 as above, not rejected.

## For the structure pass (not applied)

- **Finding 3: career's decision and goal cards beside SEL's.** Career's six-step decision steps card and near and far
  goal lines run in the same years as SEL 6 to 8's stop-think-choose and goal steps cards and SEL 9 to 12's six-step
  card and dated plan page (Exploration days 4 and 11; Pathways days 2 and 8). The read's fix: the lead extends SEL
  STANDARD section 7's goal steps card to career (career adds near and far and the dated check) and states once how the
  decision steps card relates to stop-think-choose (same first steps, career adds "gather facts" from dated sources
  and "check later"); then cte.csv g8-cd2-2-decision-steps model text and those four days are reworded. Read's pick:
  do it before the unit plans write the cards. It changes a progression's model words, so it waits for the lead. Logged
  as one open defect row on Exploration days.csv.
- docs/APPROACH-SOURCES.md line 554 still lists YouthRules as the source for "minors' hours and barred tasks"; it
  should add Fact Sheet #43 for the figures. Outside this pass's files.
- Note: Pathways days 2 and 8 still say SEL 9 to 12's goal and careful-thinking rows "come later", while the read says
  SEL grade 9 ran the six-step card the year before. That wording belongs to finding 3, so it waits with it.

## For Cory

None.

## Checks

- `python -X utf8 scripts/sequence.py check career-exploration-grades-6-to-8`: 0 failures.
- `python -X utf8 scripts/frame.py check career-exploration-grades-6-to-8`: 0 failures (note: 7 units, 96 days).
- `python -X utf8 scripts/sequence.py check career-pathways-grades-9-to-12`: 0 failures.
- `python -X utf8 scripts/frame.py check career-pathways-grades-9-to-12`: 0 failures (note: 6 units, 96 days).
- Defects logged with scripts/plan.py: 10 fixed rows (findings 1, 2 and 6 one per course; 4, 5 and 8 Pathways; 7
  Exploration) and 1 open row for finding 3.

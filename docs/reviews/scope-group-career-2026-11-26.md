# Scope group read: career education, 2026-11-26

Group: career. Courses: career-exploration-grades-6-to-8 (grade 8) and career-pathways-grades-9-to-12 (grade 10). The
single-course reads and fix passes are not repeated here; the 2026-11-26 Desk answers (q-career-scope-1: 66 sessions on
the 6 to 8 two-session path, day 86 stays in unit 7, the lighter unit 6 project on the 9 to 12 64-session path) are taken
as applied and checked only for where they did not reach.

## What I read

- AGENTS.md; docs/agents/EXPERT.md; docs/pipeline/briefs/sequence-read.md; build/scope-writes/AFTERCORE-BRIEF.md.
- docs/agents/lenses/career-education.md; data/progressions/cte.csv (read with a script), cte-edges.md, cte-excluded.csv;
  docs/courses/career-education/STANDARD.md (sections 3, 5, 6) and APPROACH.md (Pacing).
- Both courses: frame.md (course in brief, Shorter path table, Seams, Models carried, For the lead), scope-and-sequence.md
  in full, days.csv (read with scripts in build/scope-writes/scratch/group-career/: every skill and code placed, every
  g10 row's `assumes` matched to the Exploration days that teach it, school_day against the formula, every cross-subject
  lean matched to the other course's days.csv). Both -fixes reports and the expert reads' finding lists.
- docs/courses/CALENDAR.md (target week table); DESK-ANSWERS.md entries of 2026-11-26 (after-core frame fix-pass rules,
  frame calls, scope lead calls, q-career-scope-1).
- For the cross-subject cards: SEL STANDARD section 7 ("Shared steps"); the SEL 6 to 8 and 9 to 12 frames;
  data/progressions/sel.csv and library.csv lateral and goal rows; library 6 to 8 and 9 to 12 days.csv.

What the scripts showed holds: all 85 grade 8 rows and all 143 grade 10 rows are taught by a day (none only begun); all
66 Exploration indicators are scored in Exploration and carried as `~` codes in Pathways, and no Pathways-owned code
appears in Exploration; every school_day matches ceil(n x 160 / 96) in both files; every Pathways readiness list names
exactly the grade 8 rows its unit's rows assume; every "Exploration unit N, days a to b" in the Pathways frame's Seams
table matches the Exploration days that teach the row.

## Findings

1. **Lateral reading is taught with three different step lists, and Pathways misreads library 9 to 12 as later.**
   Exploration day 9 teaches "its own three steps (open a new tab, see who stands behind the source, compare two
   others)"; Pathways day 84 says "the same three steps run on a live browser". Library teaches one routine with other
   words: library 6 to 8 day 6 (grade 6) "leave the page, see what others say about its maker and claim, go upstream to
   the original, and judge"; library 9 to 12 day 3 (grade 9) the routine card "stop, investigate the source, look for
   better coverage, trace the claim to its original", and day 30 (grade 10, school day 107) the same on machine-made
   text. Library 9 to 12 runs from a host class period, so most grade 10 students have it. Pathways day 84's note does
   treat library 9 to 12 as retrieval, but day 80's readiness check still lists library `g6-lateral-reading` (grade 6,
   counted four grades back), and the scope's "Earlier-grade rows" section calls library 9 to 12 and SEL 9 to 12
   "courses that come later than this one", when their grade 9 year comes the year before and their grade 10 year runs
   beside it. The Exploration fix pass settled that a lean used one hop later is retrieval; Pathways applies it on day
   84 and not on day 80. Why it matters: a student meets two step lists for one check in the same year, and the career
   page competes with the card library has just taught. Fix: Exploration day 9 teaches library 6 to 8's grade 6 words
   (leave the page, what others say about its maker and claim, upstream to the original, judge) instead of its own
   three; Pathways day 84 names library 9 to 12's card (stop, investigate the source, look for better coverage, trace
   the claim) as the steps, retrieval for a student who took it and taught from the same card for one who did not;
   day 80 drops `g6-lateral-reading` from the readiness list and day 84's `retrieves` names `g9-lateral-method`; the
   scope's bridge sentence names only ELA grade 10 and computer science as later, and says SEL 9 to 12 and library 9
   to 12 grade 9 rows are the year before (retrieval for a student who took them). Pathways frame, Models carried,
   lateral-reading row: name library `g9-lateral-method` behind it. **scope**

2. **The first job's hour and task limits are cited to pages that do not hold them.** Exploration day 90 and Pathways
   day 72 (teacher pages) cite the Wage and Hour Division's YouthRules page and child labor page for "the hours and task
   limits under 16 and under 18"; the Exploration fix pass recorded this as settled for both courses. Opened
   2026-11-26: the YouthRules page links to resources ("What hours can I work?", "Dangerous Jobs") and the child labor
   page says some jobs are off-limits under 18 and links onward; neither states the limits. Fact Sheet #43 (Child Labor
   Provisions of the FLSA for Nonagricultural Occupations) states them: for 14 and 15 year olds 3 hours on a school day,
   8 on a non-school day, 18 a school week, 40 otherwise, between 7 a.m. and 7 p.m. (9 p.m. June 1 to Labor Day), and
   the 17 hazardous occupations orders under 18. Why it matters: a teacher who opens the cited page for a figure will
   not find one; this is the same fault the Exploration read found with the safety page. Fix: both days cite Fact
   Sheet #43 for the figures, keep YouthRules as the student-facing page and the young workers page for a safe
   workplace and who to ask, and keep "a stricter state law applies where there is one". The DIGEST line from the
   Exploration fix pass should be corrected in the lead's next digest. **scope**

3. **Career runs its own decision and goal cards beside SEL's in the same years.** Career's decision steps card has six
   steps (name the choice, list options, gather facts, weigh, choose, check later; cte.csv g8-cd2-2-decision-steps);
   SEL 6 to 8 carries a five-step stop-think-choose card all band and SEL 9 to 12 a six-step one (g9 and g10
   careful-thinking rows). Exploration day 11 says SEL careful thinking is taught first "so the day names its steps
   briefly and runs its own decision steps card"; Pathways day 8 teaches "both decision methods" because SEL grade 10
   comes later, though SEL grade 9 ran the six-step card the year before. Goals the same way: Exploration day 4 writes
   "the course's own" near and far goals (SEL 6 to 8's goal steps card, goal, steps, block and plan, check, has been on
   the band's cards since grade 6); Pathways day 2 teaches "dated goal steps ... as a career task" while SEL 9 to 12 day
   1 grows the grade 8 goal steps card into its own plan page (goal, dated steps, trade-off accepted, check date,
   verdict). Why it matters: the reason behind the settled shared-card rule (one card a child meets in every course)
   applies here, and a grade 10 student now keeps two plan pages with different goal lines. The shared-card rule names
   SEL, health and PE only, so this is not a breach, but it is drift a teacher will see. Fix: the lead extends SEL
   STANDARD section 7's goal steps card to career (the plan page's goal lines use the band's card words, career adding
   near and far and the dated check), and states once how the career decision steps card relates to stop-think-choose
   (the same first steps, career adding "gather facts" from dated sources and "check later"), then cte.csv's
   decision-steps model text, Exploration days 4 and 11 and Pathways days 2 and 8 are reworded to match. It changes a
   progression's model words, so it is a structure change for the lead; my pick is to do it before the unit plans
   write the cards. **structure**

4. **Pathways' readiness checks list far more rows than ten minutes can sample.** Exploration's readiness checks hold
   the two APPROACH items (days 1, 16, 30, 47, 58, 68, 84). Pathways' hold the two items and then name 9 rows (day 1),
   38 rows (day 12: the 14 cluster rows, the 14 first-look sub-cluster rows, ten more and three math rows and
   ss8-public-budget), 10 (day 43), 15 (day 54), 7 (day 67) and 12 (day 80), each "sampled" in the same ten minutes.
   The frame says each check "samples the grade 8 rows its unit's rows assume", and every grade 8 part is taught again
   in context because Exploration is optional. Why it matters: the jump from two items in grade 8 to a check that
   claims 38 rows in grade 10 cannot be built as written; a unit plan writer will either cut silently or overfill the
   last ten minutes of a respond day. Fix: each Pathways readiness note names its items (the two APPROACH items plus
   at most two more, about two minutes each: day 12 a job placed on the cluster map and a wage set against a training
   cost; day 54 a route's dated cost and a trade-off), and lists the other assumed rows as "taught again in context on
   day N" with the day, not as sampled. No row, unit or day count moves. **scope**

5. **Pathways' production line has no safety line, and the first-look repeats are not named.** Pathways' session 1 in
   Advanced Manufacturing is Production and Automation, which cte.csv sets as "a longer paper production line with a
   quality check", the grade 8 task (Exploration days 33 and 34) at higher demand. Exploration's version needs school
   scissors, counted out and back in, with five minutes of clean-up. Pathways day 14 (session 1) names no supplies or
   safety for it, its scope says "the only hands-on test is card and school coins", and its frame's safety read list
   names the card-and-coin bracket but not the line. More widely, Pathways' session 1 in every cluster is that
   cluster's Exploration first-look task at higher demand (the menu for 20 becomes 100 with allergen labels; the stand
   becomes a one-page service plan; the five-minute lesson becomes fifteen), which the progression notes say but
   neither scope does. Why it matters: a hands-on day loses its safety words between grades, and a teacher who sees
   the menu task again cannot tell from the scope what is new. Fix: Pathways day 14 and packet days 31 and 34 (where
   Advanced Manufacturing is the cluster) carry Exploration day 33's safety words and supplies; the scope's "Every day"
   safety bullet adds the production line; the slot table note says session 1 is the grade 8 first-look task at higher
   demand and that the task sheet names what is new for a student who did it in grade 8. The frame's safety read list
   adding the line is a one-line frame fix the same pass may make. **scope**

6. **The sensitive sub-cluster list differs between the two courses.** STANDARD section 5 names six sensitive
   sub-clusters (Military and National Security, Behavioral and Mental Health, Emergency Response, Judicial Systems,
   Public Safety, Resource Extraction). Pathways' scope (unit 2) and day 19 add Water Systems, with a leave-out swap
   and "its id named as not claimed"; Pathways' frame treats Water Systems only as a live public dispute under the
   views rule, as STANDARD section 6 does for Environmental Protection. Exploration day 51 puts health's "If a student
   tells you something" steps on the Resource Extraction section (its frame's line 23 covers it); Pathways day 19 does
   not, and its frame's health-steps line names only the four violence and mental health sub-clusters. Why it matters:
   a leave-out list is Cory's (Desk q-fix-career-1); widening it in one course makes a school tell families a
   different list in grade 10 than in grade 8, and the health steps should follow the same topics in both. Fix:
   Pathways' scope and day 19 drop Water Systems from the sensitive list and keep its views line (no verdict, views
   never graded) with no leave-out; on Resource Extraction, follow STANDARD section 6 in both courses (the views rule,
   no health steps required), so Exploration day 51's health-steps sentence goes, or, if the lead wants it kept, add it
   to Pathways day 19 and to STANDARD section 6 so both match. My pick: follow STANDARD and drop it from day 51.
   **scope**

7. **The 2026-11-26 Desk answers did not reach every place.** Exploration days.csv day 86 still ends "Pending Cory:
   whether the course choices fall before the school's registration deadline", though the scope and frame item 8 state
   the call (day 86 stays in unit 7, taught in the school's registration week where it comes earlier). APPROACH.md
   "Pacing" still says the two-session path is "64 sessions or 48 hours" and that the scope "names the 32 sessions the
   short path drops"; Exploration's is now 66 sessions (30 folds), Pathways' 64 (32). Why it matters: a unit plan
   writer reads the day note and the subject page, not the Desk log. Fix: day 86's note states the call in one line;
   APPROACH Pacing says each frame sets its short path (Exploration 66 sessions, about 50 hours; Pathways 64, 48
   hours), with the Desk entry named. APPROACH.md is the lead's file. **scope**

8. **The Pathways frame's unit 6 short row predates the lighter project.** The frame's "Shorter path, unit by unit" row
   for unit 6 still lists "options weighed and tested", "effects mapped" and "the second try and the evidence check" as
   on the full path; the call (one option tested, its second try on paper, the effects map one line) sits only in For
   the lead item 4 and the scope's Shorter path. Why it matters: the table is what the unit plan for the short path
   will be built from. Fix: reword the unit 6 row to the settled lighter project, every scored code kept. **frame**

## What holds

- The seam is complete and exact: every grade 10 row's `assumes` is a grade 8 row taught on a named Exploration day,
  every Pathways readiness list matches its unit's assumed rows, and the Seams table's unit and day ranges agree with
  Exploration's days.csv.
- Ownership is clean: 66 indicators owned and scored in grade 8, carried as `~` codes in grade 10; 64 owned in grade
  10; the 5 adult-only indicators out with reasons.
- The ramp is named and real: one field task per cluster and two packet days in grade 8 grow to six field task sessions
  per cluster, an 11-day packet and the five-minute fix in grade 10; the device turn grows from three minutes and a
  sort to five minutes and a chart; the resume line and spoken answer grow to the full resume and mock interview.
- The same rules hold in both: family note in English and Spanish with the trusted-adult route (and the 18 and over
  rule in grade 10), the plan private and scored on reasoning, no task on family income or status, the military as
  one route with the recruiter-policy line, dated figures with "check these figures this school year", the privacy
  step at the shared device, the pay-gap unit's health steps.
- Calendar: both run 96 sessions at three a week on the same formula; checks in weeks 16 and 32 (grade 8) and 14 and 32
  (grade 10), as CALENDAR.md's table gives them.

## Sources

- https://www.bls.gov/cps/cpsaat11.htm, opened 2026-11-26: "Employed people by detailed occupation, sex, race, and
  Hispanic or Latino ethnicity", 2025; 2025 annual figures are 11-month averages without October; sex given as percent
  women. Agrees with Exploration day 75's note.
- https://www.bls.gov/cps/cpsaat39.htm, opened 2026-11-26: median weekly earnings by detailed occupation and sex, 2025.
- https://www.dol.gov/agencies/whd/youthrules, opened 2026-11-26: links to hours and jobs resources; no limits stated.
- https://www.dol.gov/agencies/whd/child-labor, opened 2026-11-26: says some jobs are off-limits under 18; links to the
  list; no hour limits stated.
- https://www.dol.gov/agencies/whd/fact-sheets/43-child-labor-non-agriculture, opened 2026-11-26: Fact Sheet #43, hour
  limits for 14 and 15 year olds and the hazardous occupations orders under 18 (for the source list).
- https://www.osha.gov/young-workers, opened 2026-11-26: young worker safety and rights; no hour limits.
- https://www.eeoc.gov/laws/guidance/enforcement-guidance-preemployment-disability-related-questions-and-medical,
  opened 2026-11-26: before a conditional offer, no disability-related questions; may ask whether the applicant can
  perform job functions with or without reasonable accommodation. Agrees with Pathways day 75.
- https://www.cdc.gov/niosh/talkingsafety/, opened 2026-11-26: the Talking Safety young worker curriculum page.

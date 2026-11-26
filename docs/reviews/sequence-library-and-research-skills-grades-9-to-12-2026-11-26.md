# Expert read: scope and sequence, Library and Research Skills, grades 9 to 12 (2026-11-26)

Course `library-and-research-skills-grades-9-to-12`. A cold read by the curriculum expert (PRODUCTION-PATH step 3),
per docs/pipeline/briefs/sequence-read.md and build/scope-writes/AFTERCORE-READ.md. I did not write the scope. I read it
as a high school librarian who co-teaches with ELA and history, as a district curriculum lead, and as a reader of the
lateral reading research.

## What I read

- docs/agents/EXPERT.md; docs/agents/lenses/library.md; docs/ADOPTION-BAR-SUBJECTS.md part 11 (items 1 to 6 and
  "Fails if"); docs/courses/library/STANDARD.md and APPROACH.md in full.
- build/scope-writes/AFTERCORE-BRIEF.md (how the writer applied sequence-write.md here).
- The scope under review: docs/courses/library-and-research-skills-grades-9-to-12/scope-and-sequence.md and
  data/plans/library-and-research-skills-grades-9-to-12/days.csv (72 rows), in full.
- Beside them: the frame (docs/courses/library-and-research-skills-grades-9-to-12/frame.md, in full); the grade 8 to 12
  rows of data/progressions/library.csv and library-edges.md; docs/courses/CALENDAR.md (rule 4 and the grade 9 to 12
  table rows); the grade 9 to 12 ELA, science and social studies unit rows of data/plans/calendar.csv; the ELA grade 9
  and grade 12 frames' unit 6 rows; data/plans/later.csv L149.
- Earlier reads for REPEAT: docs/reviews/sequence-library-and-research-skills-grade-4-2026-11-26.md and grade-5 (their
  finding lists).
- Gates: `python -X utf8 scripts/plan.py check` (this course: 0 failures; notes "day 66: Fluency, first day in the course
  for ~AASL.IV.D.3" and "unit 5: standard None is on no day"); `python -X utf8 scripts/frame.py calendar` (K to 8 only;
  no 9 to 12 lines, as the frame says); `scripts/sequence.py check` 0 failures; `scripts/frame.py check` 0 failures
  (8 units, 72 days, 14 unit days a year); `scripts/stale.py check` 0 failures.
- Outside: the Stanford news release on the 2022 field study and the search summary of the paper; the US Copyright
  Office fair use index (opened).

## Verdict

The scope is sound in its skeleton. All 72 school days land in the weeks the frame and CALENDAR.md give, every owned id
sits on a day and reaches its year's check (unit 8's two on day 70, as the frame designs), lateral reading is taught
as leaving the page, and every unit has a host and a stand-alone question. The biggest risk is that in two units an
owned move is only ever modeled by the teacher: no day has the grade 9 student design their own question (I.D.2), and
no day has the grade 12 student choose their capstone decision and map its communities (II.D.3), yet both are scored.
Fix those two days first. Then make six check items ask the whole of the id they claim and repair the shorter period's
lateral-minute arithmetic.

## Findings, most serious first

### 1. Two owned moves are modeled but never done by the student before they are scored (serious; LAYER sequence; REPEAT yes, grade 4 finding 7's kind)

**What is wrong.** Unit 1: day 1 is the teacher designing a research question (its last ten minutes are the readiness
check, and it has no exit ticket); day 2 is databases; day 3 lateral; day 4 "starts the source log on their own
question". No day has the student write and narrow their own question, yet check 1 (day 8) scores "a too-broad question
made researchable", and AASL.I.D.2 (owned) rests on the student holding that question for three rounds. Unit 8: day 63
is a show-me in which "the teacher chooses a capstone decision, maps the communities it touches ... and says where they
stand". Day 64 runs "search rounds ... on the capstone question" as if each student already had one. No day names the
student choosing their decision, drawing their own communities map, or writing their "where I stand and what follows"
line. Days 65 and 69 carry AASL.II.D.3 in `codes`, but their goals do not say what the student does for it. Day 70 then
scores "where they stand and what follows".

**Why it matters.** A day writer works from the goal column. They will build unit 1 without a student question-writing
step, and unit 8 without the map, and two owned ids will be scored with no student try (the frame's "No score from a day
a move is first taught" breaks in spirit).

**Fix.** Day 2: the exit ticket becomes "your own question on the teacher-set topic, narrowed, with one operator string
for it" (the operator-string exit moves into day 4's last five minutes, where the frame already puts a string). The
teacher returns the question with a line before day 4. Day 64: the first 10 minutes, after the card is withdrawn, are
each student naming their decision and drafting their own communities map. Day 65's draft carries the "where I stand
and what follows" paragraph. Day 67's fixes include the map. Write each of these into the goal column.

### 2. Six check items ask only part of the id or row they claim (moderate; LAYER sequence; REPEAT yes, grade 4 finding 3 and grade 5 finding 2)

| Day | Row or id | The part not asked | Fix (one prompt) |
|---|---|---|---|
| 17 | AASL.VI.C.1, g9-open-licenses | "credit as the license asks": the item asks what three works allow and a permission request, never a credit line | Add: write the credit line one of the three licenses asks for |
| 26 | AASL.II.A.3, g10-own-lens | the after half ("after it say whether that happened"): the item asks only how a starting point *could* shape a reading | Give an invented reader's before note and their findings; ask whether the starting point shaped the reading and how you can tell. Or score the day 25 after-note, with the private path kept |
| 53 | AASL.VI.D.2, g11-honesty-review | "sources represented fairly": the unseen project has quotes out of context, missing credit and a missing disclosure line, but no unfairly represented source | Plant one source summarized against its own conclusion in the unseen project |
| 61 | AASL.VI.D.3, g12-help-others | "within the law": the sample guide is fixed for one unsafe and one dishonest step | Add a third fault: the guide reuses an all-rights-reserved image without permission |
| 8 and 17 | ~AASL.IV.B.1, g9-databases-operators | the row's "compare it with the open web for the same question" and the search across kinds | The operator-string item adds one line: database or open web for this question, and why |
| 42 | ~AASL.IV.D.1, g11-lateral-news | "rechecking their source log" (claimed on day 42) | One prompt: after the fourth capture, which log entry changes and why |

### 3. Check 8 repeats day 70's task within two weeks and does not draw unit 8's skill from earlier units (moderate; LAYER sequence; REPEAT new)

**What is wrong.** Day 70 (school day 143, week 29) is unit 8's end-of-unit assessment: "one claim traced upstream, an
unseen source audited". Day 71 (school day 152, week 31), the course-level check right after it, opens with "a source
checked laterally with one claim traced upstream (units 1 and 8)". That is the same task form nine school days later,
which breaks the scope's own "No task form repeats one given in the two weeks before". It also breaks the brief's rule
for a check right after an end-of-unit assessment: its items for that unit's skills come from earlier units' content,
and the scope says the opposite ("it does not repeat day 70").

**Fix.** Drop the upstream trace from day 70's sitting. Day 70 keeps the unseen source audited and "where I stand and
what follows", and the capstone carries its own traces from day 66's audit. Day 71's first case is written on unit 1's
or unit 4's content (a street-trees or night-sky page, or a captured summary), labeled "units 1 and 4", and the scope's
check paragraph says so.

### 4. The shorter period breaks the lateral-minute floor the scope promises to keep (moderate; LAYER sequence; REPEAT yes, grade 4 finding 2 and grade 5 finding 1)

**What is wrong.** On the 40-minute path there are 34 working minutes, and "the nine lateral sessions keep their lateral
minutes". Days 3 and 30 hold 39 lateral minutes, which cannot fit in 34. At most the total is 7 x 34 + 2 x 29 = 296
minutes, under the "at least the six 50-minute lessons" (300) the scope and frame hold. The 10-days-short fold of day
21 also removes unit 3's only practice day, so the pairs stage of the card disappears. It puts a chain try into "day
20's last 8 minutes", which is also day 20's exit ticket, and the missing-view try into "day 23's 10 non-lateral
minutes", which already hold the log line, card withdrawal and interview logistics.

**Fix.** On the 40-minute path, days 3 and 30 run 34 lateral minutes. Days 7 and 23 move their non-lateral work to the
host period: day 7's findings note and self-check, and day 23's "why it was missing" log line, written as homework in
the notebook. Each then runs 34 lateral minutes: 9 x 34 = 306. State the sum in the Shorter path section. For the short
year, fold day 22 instead of day 21: its unscored rehearsal turns go into day 24's first 8 minutes, and its ground-rule
modeling into day 21's last 8 minutes in place of the exit ticket. Unit 3 keeps its practice day and card stages, and
nothing assessed is cut. Or keep day 21 and say how the card's pair stage survives.

**On how the minutes are counted (judgment call).** Days 5, 6, 23 and 32 count 29 to 34 minutes of an inquiry session
in which students also search, log and draft. The field study's lessons were taught lessons, not lateral checks
folded into project time. The margin over 300 is 6 minutes. The day plans should show the lateral move as the session's
main activity, with the other work named in minutes. The scope already says "a day plan that cuts one below its figure
moves the other work". Keep that line, and have the unit plan show the split.

### 5. Unit 6 scores the interview report with no feedback round, and day 49 first-teaches two owned rows (moderate; LAYER sequence; REPEAT new)

**What is wrong.** AASL.II.D.1's product, the interview or first-person report, is first written on day 52. That same
day also holds publishing to the audience and the self-check, and the report is scored on day 53. The frame's evidence
rule wants a scored product "after a draft day, written feedback and a revision counted in the unit's days". The method
note gets that (48 to 50), but the report does not. Day 49 shows choosing a published form (VI.C.2) and models the
honesty review (VI.D.2), with a pair try, in about 34 minutes after the retrieval: two owned rows first taught in one
session.

**Fix.** Day 48 also drafts the interview report as one paragraph ("what I expected, what the person's experience
showed, what changed"), so the teacher's written feedback covers it. Day 50 revises it, and day 52 only finalizes and
shares it. Day 49 splits its minutes in the note: about 12 for choosing a form, about 20 for the honesty review model
and pair try. Choosing a form can be cut to a sort of the four format cards, since ELA grade 11 unit 4 taught
presenting before this unit.

### 6. Day 56 sends a practice day to open search on real program pages (moderate; LAYER sequence; REPEAT new)

**What is wrong.** Day 56 is Fluency. Each student runs "one search they choose on a next step after school, a
training, a program or a job", and the note carries the boilerplate "Open search only on a teacher-guided inquiry day".
That contradicts the day's own kind. APPROACH.md ("Sites, search and real cases") says practice pages use invented
sites, and only inquiry days may use the real web. Real training and program pages are where students meet paid
placements and recruiting claims, which is exactly what the stand-alone question asks them to check.

**Fix.** Day 56's next-step search runs on the closed invented set of program pages (the unit 7 stand-alone set,
including one page whose promises fail a lateral check). A student may repeat it on the real web at day 60 or at home,
with the stop rule and the home note. Remove the open-search boilerplate from day 56, or replace it with "closed set
only".

### 7. Day 33 uses the grade 7 citation style with no readiness check (moderate; LAYER sequence; REPEAT yes, rule 2 kind)

**What is wrong.** Day 33 models point-of-use credits "in the grade 7 style" (g10-label-own-work's note: "Credits follow
the grade 7 citation style (g7-citation-style)"). That row is three grades back, in an optional course the frame says no
grade 9 student is assumed to have taken, and nothing in grades 9 or 10 teaches or retrieves a citation style (unit 2
credits "as the license asks", and the full style is unit 6). Rule 2 calls for a readiness check.

**Fix.** Day 27 (check 3's respond day, between units 3 and 4): the last ten minutes are a readiness item, one source
cited in a set style. Students who miss it get a ten-minute reteach on day 28 or day 29, never on day 33's show-me.
Where ELA grade 9 unit 4 or grade 10 taught a standard citation format, name that style as the one used, and the day 27
item checks it. Drop "No readiness check before unit 4" from day 27's note.

### 8. Codes tagged in years that do not own them, and one id tagged on days that do not teach it (minor; LAYER sequence; REPEAT yes, grade 5 finding 2)

- The scope says "A `~` code in days.csv is an id owned in an earlier grade and revisited", but later years' checks
  carry earlier-owned ids bare: day 26 (AASL.IV.D.1, AASL.VI.C.1, owned grade 9), day 35 (AASL.II.B.3), day 42
  (AASL.IV.D.2, AASL.VI.B.3), day 61 (AASL.IV.D.3, AASL.VI.D.2) and day 71 (AASL.II.B.3, AASL.IV.D.2, AASL.IV.D.3,
  AASL.VI.C.1). Marked bare, a one-item sample reads as a claim on the whole id (see finding 2). **Fix:** prefix `~` on
  each of those.
- AASL.II.C.2 (the seminar: add to a talk where views differ) is in `codes` on days 20, 21 and 23. None of those goals
  has talk in it (database pages, reference chains, a search). **Fix:** remove II.C.2 from days 20, 21 and 23. Keep it on
  22, 24, 25 and the check.

### 9. Day 23 allows an interview with no lead time for consent or teacher-checked questions (minor; LAYER sequence; REPEAT new)

Day 23 offers "a source or an interview under the interview rules". The rules (APPROACH.md item 8) need questions
checked by the teacher and a parent's consent under 18, and grade 10 has no planning day for them: the interview plan is
taught in grade 11, day 45. **Fix:** in day 23's note, an interview needs its questions checked and the consent note
sent home by day 20. Otherwise the student uses a missing-view source or the first-person set. The source path is the
default.

### 10. Unit 4's labeled "product" is never named (minor; LAYER frame; REPEAT new)

Days 33 and 34 place point-of-use credits "beside a quotation, a paraphrase and a visual" in "the finished labeled
product shared with another class". The only products unit 4 makes are the matrix and map, which hold no quotations or
visuals to credit. A writer cannot tell what is labeled. **Fix:** name it in the scope: a one-page synthesis summary
written from the map between days 32 and 34 in the host course or the notebook, labeled and shared on day 34. If that is
more than the unit can hold, label the map and put the credits on its source entries. Add a line to the scope's For the
lead section so the frame's unit 4 row says which.

### 11. In-step hosts exist that the scope does not name, and one "beside" claim is wrong (minor; LAYER sequence and frame; REPEAT yes, grade 4 finding 5)

- Unit 2 (weeks 18 to 29) names World History I unit 3 and ELA grade 9 unit 1, both over before it starts. In the
  calendar, ELA grade 9 unit 6, "Should school start later? Teen sleep, data and argument" (weeks 20 to 24,
  e9-ri-argument-evaluate, e9-w-argument), is a neutral school decision argued on both sides with data, in the same
  weeks as days 13 to 16. It is a natural host for the decision memo.
- Unit 8 (weeks 16 to 29): ELA grade 12 unit 6, "Public words and a public decision" (weeks 18 to 21, a town zoning
  decision, e12-info-multiple-sources), runs beside days 63 to 65. It can host under its own frame's guards (the topic
  is contested, so the evenness rule applies).
- Unit 1's arc says days 3 to 7 are "placed in weeks 6 to 13 beside World History I's source checks". World History I
  unit 1 (the named host) ends in week 3. **Fix:** say "after".

**Fix:** add the two in-step hosts as optional hosts in the units' Host lines, with the stand-alone kept. Put a For the
lead line asking the frame to list them.

### 12. Small fixes (minor; LAYER sequence; REPEAT yes)

- Day 19: g10-own-lens assumes g9-fair-sides, but day 19 retrieves g9-research-question-design, and g9-fair-sides first
  returns on day 22, after the row is taught. Retrieve g9-fair-sides on day 19 (whose view leads this paragraph?).
  g9-research-question-design returns on day 28, where unit 4 assumes it.
- Day 1 has no `retrieves` entry, although its readiness item retrieves g8-test-assumptions and g8-research-product,
  the only grade 8 rows with no retrieval anywhere. Add them to day 1's `retrieves`.
- Day 37 carries the hook, the compelling question, a 5-minute retrieval and five shown moves (reports, data sets,
  primary-and-news contrast, sponsored placement, saved search). Write the minute split in the note, or move the
  saved search to day 38 as a practiced step after a 2-minute model.
- Unit 1: name round 1 (the search behind day 4's log start), so "rounds 2 and 3" on days 5 and 6 read correctly.
- Day 12 practices licenses but not the permission request that check 2 scores. Add one request to the practice, or
  require one on day 14 for a case-set work marked all rights reserved.
- Day 9 gives g8-multiple-views-gather a second readiness check after day 1's and two retrievals. One is enough: drop it
  from day 9.

## Checked and right (do not touch)

- school_day formula (9n, then 9n - 1, then 160) and every value in days.csv. Checks fall in weeks 15/31, 15/31, 11/31
  and 13/31, none in a core check week of their grade (calendar.csv), none in week 32.
- Readiness placement: unit 1 in day 1's last ten minutes after the hook, unit 2 on check 1's respond day, no other
  unit's first day touched. Keeping grade 8 rows as readiness plus retrieval is the frame's deliberate call (optional
  course) and is stated (For the lead 2). I agree with it.
- Lateral reading taught as leaving the page, with dated captures and "other tabs" sheets on the paper path. No paid
  database, no real site, no product name. No claim that the method raises scores.
- The 2022 field study's figures (about 500 students, six 50-minute lessons, government classes) match the Stanford
  release and the paper's record. The scope rightly calls it background.
- The fair use wording (four questions weighed, never ruled lawful). The US Copyright Office fair use index opens at the
  frame's address and lists the four factors.
- Sensitivity handling: privacy of the "where I start" note, strengths and goal notes kept private, interview rules
  with 18-or-over consent, honest use fixed privately, the ELA grade 11 unit 8 guard (Riis's stereotypes, no immigrant
  family story asked) carried onto day 47, the rehearsal partner who plays a cooperative learner only (day 59), and
  neutral stand-alone questions.
- Unit 8 ending in its own assessment in week 29, with the senior-leaving fold.
- The `~` convention, skill card stages and self-checks in every unit.

## Lens checklist (scope and sequence layer)

| Line | Verdict |
|---|---|
| Host task from another course named | Met in every unit; in step weakly in units 1, 2 and 8 (finding 11) |
| Source judging not a page checklist | Met |
| No citation unit without research to cite | Met; unit 4's product unclear (finding 10) |
| End-of-unit assessment not recall of terms | Met |
| No AASL text copied, no alignment claim | Met |
| Live web page relied on with no dated capture | Met, except day 56 (finding 6) |
| No paid database or library | Met |
| No product or company name | Met |
| No claim of raised scores | Met |
| Bar 1 to 6 (cycle, priority skills with checks, lateral, real tasks, honest use, product shared) | Met; unit 5's "product" is a partner share, thin but adequate |

## Stale notes

stale.py: 0 failures. The L149 note (sources not loaded) is current: later.csv L149 is open and
S:\CurioClass-sources\library holds only the 2026-11-21 AASL folder. No stale lines found by hand.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Day 2 exit ticket = the student's own question narrowed plus one operator string | The owned I.D.2 move gets a student try before day 8 | days.csv, scope unit 1 |
| Day 64 opens with each student's decision and communities map; day 65 drafts "where I stand" | II.D.3 owned, otherwise only modeled | days.csv, scope unit 8 |
| The six item additions in finding 2 | Each item asks the whole of its id | days.csv (8, 17, 26, 42, 53, 61), frame check text via lead |
| Upstream trace removed from day 70; day 71 case 1 on unit 1 or 4 content | No repeated form in two weeks; check-after-end rule | days.csv, scope checks |
| 40-minute path: days 3 and 30 at 34; days 7 and 23 move non-lateral work to the host | Keeps 306 lateral minutes | scope Shorter path |
| Short year folds day 22, not day 21 | Unit 3 keeps its practice day | scope Shorter path, days.csv notes |
| Interview report drafted day 48, revised day 50 | Draft-feedback-revise for a scored product | days.csv 48, 50, 52 |
| Day 56 search on the closed program set | Practice pages use invented sites (APPROACH) | days.csv 56 |
| Day 27 readiness item on a citation style | Rule 2, three grades back in an optional course | days.csv 27, scope table |
| `~` added on days 26, 35, 42, 61, 71; II.C.2 removed from days 20, 21, 23 | Tagging matches ownership and teaching | days.csv |
| Day 19 retrieves g9-fair-sides; day 1 `retrieves` lists the two g8 rows; day 9 drops the repeat g8 item | Retrieval before use and recorded | days.csv |

## For the lead (frame and process)

- The frame's unit 4 row should name what is labeled (finding 10) and could list ELA grade 9 unit 6 and ELA grade 12
  unit 6 as in-step hosts (finding 11).
- The frame's check 2, 3, 6 and 7 texts need the added prompts in finding 2, so the unit plans do not copy the shorter
  items back.
- g10-label-own-work's note points at g7-citation-style, which is in an optional course. Consider pointing it at ELA's
  standard citation format row instead (progression note).

## For Cory

None. Every finding is item-level or a frame note.

## Confidence

Findings 1, 2, 3, 7 and 8: firm (read against the rows, the frame rule and the days). Finding 4's arithmetic: firm.
Its minute-counting note: a judgment call. Findings 5, 6, 9 and 10: likely. Finding 11: a judgment call about which host
fits best.

## What I could not judge

The online-reasoning lessons and the web-literacy book are not loaded (L149), so whether days 3 to 7, 30 to 32 and 37 to
40 match their open lessons waits for the source map. I did not open the continuum 9 to 12 band file again; the
frame's cell-by-cell read stands.

## Sources

- [Stanford news release, "It doesn't take long to learn how to spot misinformation online"](https://ed.stanford.edu/news/it-doesn-t-take-long-learn-how-spot-misinformation-online-stanford-study-finds): the study's size and dose (via search summary).
- Wineburg and others, "Lateral reading on the open Internet: A district-wide field study in high school government classes", Journal of Educational Psychology, 2022, doi 10.1037/edu0000740 (record and supplemental materials listing only; article not read).
- [US Copyright Office, Fair Use Index](https://www.copyright.gov/fair-use/): opened; confirms the four factors the days use.

## For the source list

- The supplemental materials for the 2022 field study, with a sample lesson plan: https://supp.apa.org/psycarticles/supplemental/edu0000740/EDU_2020_0630_Supplemental_Materials.pdf (not opened; worth reading when L149 loads the lessons).
- The US Copyright Office fair use index opened without a block on 2026-11-26 (frame For the lead item 6).

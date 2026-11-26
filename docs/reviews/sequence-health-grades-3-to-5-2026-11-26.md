# Expert read: scope and sequence, Health, grades 3 to 5 (2026-11-26)

Reader: Curio Class curriculum expert agent (fresh, cold read; did not write the scope). Brief:
docs/pipeline/briefs/sequence-read.md with build/scope-writes/AFTERCORE-READ.md and AFTERCORE-BRIEF.md.

## What I read

- Under review: docs/courses/health-grades-3-to-5/scope-and-sequence.md and data/plans/health-grades-3-to-5/days.csv
  (90 rows), every row and note.
- Beside it: the frame (Units table, Course-level checks, Cross-subject, For the lead), data/progressions/health.csv
  rows for grades 2 to 5, data/standards/nhes-2024.txt (3-5 indicators), docs/courses/CALENDAR.md (grade 3 to 5
  rows), data/plans/calendar.csv (SEL 3 to 5 and PE 3 to 5 rows), docs/courses/sel/STANDARD.md section 7, the SEL
  3 to 5 frame's shared-card lines, docs/agents/EXPERT.md, docs/agents/lenses/health.md, the bar's "3. Health"
  section, data/plans/course-list.csv (pins 60:300, 75:370).
- Gates: `plan.py check` (health 3 to 5 not listed), `sequence.py check` 0 failures (notes "standard None is on no
  day" for the six sensitive units, expected), `frame.py check` 0 failures, `frame.py calendar` no stagger break for
  grades 3 to 5 (health weeks 15/29, 14/29, 14/28), `stale.py check` nothing for this course.
- Sources opened: CDC physical activity guidelines for children (page dated 2025-12-04); CDC youth tobacco data
  (NYTS 2024, page dated 2024-10-17); CDC "About bullying" (page dated 2024-10-28). Browser check:
  stopbullying.gov "What is bullying" (403); Monitoring the Future annual reports (403; a second source, the federal
  drug-abuse institute's MTF results page, returned 404).

## Verdict

The scope is sound in its structure: every owned NHES 3-5 indicator sits on a teaching day and an end-of-unit
check in its own year, all six course-level checks sit on CALENDAR.md's weeks off each grade's core and SEL check
weeks, the SEL, PE and ELA leans match calendar.csv, and the sensitive units keep the frame's notes, opt-out,
disclosure steps and private routes. The biggest risk is in the check items: several end-of-unit and course-level
checks list a code but ask only part of it, or none of it (NHES.S8.5.2, S1.5.5 and S1.5.1 have no item on their unit
check), although the .md says every half holds a prompt. The one change that matters most is to write one item per
part on those check days; after it, fix the two shorter-path folds that cut a part and move the three family notes
that ride on removable units.

## Findings, most serious first

### 1. Check items do not ask every part of the codes they list (sequence; REPEAT yes)

The .md's "Each part of each code" says the teaching day and the check each hold a prompt for every half. The check
rows do not:

| Day | Code | What the item asks | Missing |
|---|---|---|---|
| 24 (unit 5 end) | S1.5.1 (explain how to grow a strength) | goal sentence, reason, alone-or-together, a sort item | no strength item at all (only the year-end check, day 29, asks it) |
| 69 (unit 16 end), 75 | S1.5.5 (how knowing how to find and use information helps wellness) | source check on a claim and how it could hurt | that is S3.5.3 and S3.5.4; no item asks how finding information helps a choice |
| 54 (unit 12 end), 59 | S8.5.2 (describe how teamwork and communication make advocacy stronger) | boundary steps, refusal, a speak-up plan | no item asks the teamwork and communication description |
| 49 (unit 11 end), 59 | S2.5.2 (own and others') and S2.5.3 (people and communities, and why) | one item: "how one influence affects two characters and why" | S2.5.3's community half and its "why" (circumstance) have no prompt; the two codes share one item |
| 49, 59 | S3.5.3 (facts, products and services) | "the source check on a new claim" | products and services (day 48 teaches all three) |
| 44 (grade 4 mid-year) | S4.5.3 (ask and give help) | the ask only | the giving half (day 43 asks it; day 44 does not) |
| 79 (unit 18 end), 88 | S4.5.6 (stay out of, handle, settle) | "the conflict steps for a character" | a prompt per part |
| 39, 44 | S1.5.3 (illness and injury) | "an illness or injury" | "and": one prompt each |
| 39, 44 | S5.5.2 (whether a decision needs help or teamwork) | "who should help" | the "whether" (a case that needs no help) |
| 74, 88 | S5.5.5 (for them and others) | "a look-back on a character's choice" | both halves named |
| 75, 88 | S1.5.7 (when, and the reasons) | "when a character should get care" | the reason (day 69 has it) |

Why it matters: an end-of-unit or course-level judgment on a code that was only half asked is not evidence of the
code, and the unit planners write items from these goal lines. Fix: rewrite each listed goal so it names one item per
part (see Settled 1). Where the frame's check table carries the same wording (days 44, 59, 75, 88), the scope's day
wins and the frame line goes to the lead.

### 2. Two shorter-path folds cut a part or a row (sequence; REPEAT yes)

- Grade 4, day 41 folds into days 40 and 42 as "a five-minute ask rehearsal in each". Day 41 is the only day that
  teaches S4.5.3's giving half (being the one who listens when a friend asks). The fold as written drops it.
- Grade 5, day 70 folds into day 71. Day 70 is the whole of g5-aod-refuse-alcohol-drugs (alcohol and drug facts,
  medicine misuse, the norm, the refusal with the card), and day 74 assesses its refusal for a group offer. Day 71
  already holds two rows (online safety and S2.5.4) and a two-row retrieval; it cannot take a third.

Fix: day 41's fold keeps the listening reply: a five-minute ask rehearsal on day 40 and a five-minute listening-reply
rehearsal on day 42. Grade 5 keeps day 70 whole and folds the respond day 76 instead (Settled 2). Respond days are
not assessed and own nothing, and the scope already folds day 90 the same way.

### 3. Family notes for three sensitive units go home on a removable unit's day (sequence; REPEAT new)

The unit 7 note goes home on day 25 (unit 6), the unit 14 note on day 55 (unit 13) and the unit 21 note on day 84
(unit 20). A school that leaves out unit 6, 13 or 20 turns that day into practice on another unit, and the next
unit's note has no day. Why it matters: the bar's sensitive-topic rule and STANDARD.md section 5 need the note two
weeks before, every time. Fix: send both notes together on days 23, 53 and 82, two and four weeks ahead, or keep the
weeks and add to each of days 25, 55 and 84 "the unit 7 (14, 21) note goes home this week whether or not this unit
runs". Name it in the leave-out bridge.

### 4. Retrieval is missing on the sensitive days, and one row is used before its retrieval (sequence; REPEAT yes)

- The rule 2 table says the grade 2 sensitive rows (g2-v-body-safety, g2-sh-bodies-grow-respect) open "inside days 25
  and 27", but neither day's note or `retrieves` cell carries it. Grades 4 and 5 have the same gap and the table does
  not list them: day 55 (g3-v-body-safety), day 57 (g3-sh-respect-all-people), day 84 (g4-v-body-safety) and day 86
  (g4-sh-body-changes, and g4-v-limits-and-respect, a non-sensitive grade 4 unit 12 row).
- Day 61 uses g5-pa-habit-practice, whose assumed row g4-pa-warm-up is only retrieved on day 62.

Fix: add a five-minute retrieval to each of days 25, 27, 55, 57, 84 and 86, set in the `retrieves` cell, in the
leave-out bridge's form ("never a child's fault, telling works"; one respect scene; the plain body-change terms)
so the retrieval also serves a class whose earlier sensitive unit was left out. Add g4-pa-warm-up to day 61's
retrieval (one line: why warm up and drink water) and keep day 62's. Add the grade 4 and 5 rows to the table.

### 5. The response-time line contradicts itself and double-books the opener (sequence; REPEAT yes)

Every end-of-unit note says "response time is the same day (the teacher returns the marked steps next lesson in the
opener)". It cannot be both. The next lesson's five-minute opener is already the retrieval task on days 5, 10, 22,
35, 40, 46, 50, 65, 70, 77 and 80. After units 7, 14 and 21 the next lesson is a course-level check (days 29, 59, 88),
which has no opener. Fix: see Settled 3. The marked sheet comes back at the start of the next lesson and each
student redoes one "not yet" step as that lesson's exit ticket, counted once there. For units 7, 14 and 21 the sheet
comes back privately on the respond day (30, 60, 89).

### 6. Five days carry more than a 30-minute lesson holds (sequence; REPEAT new)

At 25 minutes after the opener:
- Day 80: four retrievals in a five-minute opener (team asks, refusal, comparing options, W.4.1), then two rows,
  approaches, audience and a snack-day plan.
- Day 86: a puberty review, everyday consent, HIV basics and a question box, on a sensitive day.
- Day 40: stress signs, the calm-down card, the modeled ask (four steps) and two retrievals.
- Day 46: two indicators (S2.5.2 and S2.5.3), each with its own case set.
- Day 70: alcohol and drug facts, medicine misuse, the norm, the refusal with the card and a label case.

Fix: on day 80, move the W.4.1 and comparing-options retrievals to day 81's opener, which retrieves one row. On day 86,
make the puberty review the day's retrieval (it also closes finding 4), collect question-box slips on day 86, and
answer them on day 87 before the check. Day 87 already holds the answers on the unit 14 pattern. For days 40, 46 and
70, the unit planners time the day; if it runs over, day 41's Fluency takes the second ask model, day 48 takes one
community case, and day 72 takes the medicine label case.

### 7. Practice-only codes are listed on check days whose items do not ask them (sequence, progression; REPEAT new)

Day 9 lists S1.5.2 (no item asks an action per part of wellness), day 58 lists S4.5.4, and day 85 lists S4.5.6 (a
telling-line check asks nothing about conflicts). The other sensitive checks (26, 28, 56, 87) also list codes the
frame says those units do not own. A gradebook that reads `codes` on `assess=end` rows would count these as
evidence. Fix: on assess rows, list only the codes an item asks in full. Drop S1.5.2 from day 9, S4.5.4 from day 58
and S4.5.6 from day 85, and add "practiced, not scored" to the sensitive checks' notes. For the progression owner:
g5-v-body-safety's ~NHES.S4.5.6 (conflict) is a weak fit for a signs-and-helpers row, and ~NHES.S3.5.1 or S4.5.3
would match the day.

### 8. Some step cards are never withdrawn before the check (sequence; REPEAT new)

The .md says each card "is withdrawn on the day the note says", but no day withdraws the help-steps card (unit 3),
the listening steps (unit 4), the decision-steps card (unit 9) or the refusal card (unit 12). Every check is taken
without its card, so students meet "no card" first on the check. Fix: withdraw help-steps on day 13 with the
decision card, the listening steps on day 20, the decision-steps card for day 38's last case, and the refusal card on
day 53's team ask. The speak-up plan stays held through day 53 and is first unaided at the check, which the .md
should say.

### 9. Shared card wording (sequence; REPEAT new)

The refusal card is quoted as "give a reason or none". The SEL 3 to 5 frame's grade 3 form is "stop and think, say
no clearly, give a reason, offer something else or walk away", and health adds "a reason is optional" separately, so
the scope both edits SEL's words and adds the addition. SEL STANDARD section 7 gives K to 2 and 6 to 12 forms only;
the 3 to 5 forms the scope uses (calm-down four steps, talk turn card, goal steps card) come from the SEL 3 to 5
frame. Fix: quote SEL's card word for word on days 51 and 70 and the .md, with health's line after it, and cite the
grades 3 to 5 forms as "SEL 3 to 5 frame, from STANDARD section 7". Day 18 should name SEL unit 4 (weeks 17 to 21) as
side by side for the talk turn card.

### 10. Facts and sources (sequence, frame; REPEAT new)

- Day 3 (and frame unit 1): the CDC guideline (page dated 2025-12-04, opened) also says vigorous activity on at least
  3 days a week. Add "some of it hard enough to breathe fast, at least three days" to the one line.
- Tobacco norms (days 8, 51) hold: NYTS 2024, middle school, 3.5% current e-cigarette use and 12.9% ever tried any
  tobacco product (CDC youth tobacco data, page dated 2024-10-17). Name that source and year in the notes.
- Day 70's alcohol and drug norm says "CDC pages", but CDC's national youth survey is high school. The nearest age
  group is the federally funded national survey of 8th graders (Monitoring the Future). Browser check: the MTF
  results page (403); the norm itself is very likely true, from memory.
- Day 19's bullying definition matches CDC's (unwanted aggression, observed or perceived power imbalance, repeated
  or highly likely to be repeated; page dated 2024-10-28). Add it to the .md's sources (stopbullying.gov: browser
  check).
- Day 41's "help line named in plain words" names no line. Name it by purpose (the national crisis line, call or
  text 988) so the unit planner does not guess.

### 11. "Its days extend unit 4" does not say how (frame; REPEAT new)

A left-out sensitive unit sits weeks after the unit it "extends" (unit 6 in weeks 25 and 26 extends unit 4, which
ended in week 21; unit 14 in weeks 27 and 28 extends unit 11, which ended in week 19). Fix: one line in the .md's
leave-out bullet: "the freed days stay in their weeks as practice days on that unit's cards, with no new items, so
no check moves".

### 12. Shorter period: "items the day before" lands on another check or on station days (sequence; REPEAT new)

Moving a check's facts-in-use and valuing items to "the last ten minutes of the day before" puts the grade 3
mid-year items on day 14 (unit 3's own check) and squeezes the hearing stations on days 20, 42, 52 and 77. Fix: for
course-level checks, give those items in the first ten minutes of the respond day before the re-rehearsal. For
unit checks after a station day, give them at the start of the check day and shorten its scenario set by one card.
Nothing is cut either way.

## What is right and should not be touched

- One lesson a week in weeks 1 to 30, the school_day formula, and every unit and check week match the frame,
  CALENDAR.md and the pins. Grade 5's doubled week 10 is the only way 14 unit days fit before the week 14 pin, and
  the .md says why.
- The non-repeating course-level checks: each check right after a unit sets that unit's item in an earlier unit's
  situation, and the .md says so.
- Getting help taught in non-sensitive units every year (3, 10, 16, 17), and the leave-out bridge.
- The coverage map, the eight standards in every year, the HBO tie on every day, and the norms worked on directly
  (bar criteria 1, 4, 5 and 10).
- The carried records (listening, routine, log, delivery) are never collected twice, and the reasons the five codes
  are not sampled on a course check are honest.

## Lens checklist (scope and sequence layer)

| Line | Status |
|---|---|
| All eight standards reached in the band | met (every year) |
| Each skill standard practiced in two or more topics | met (.md lists them) |
| Coverage map with units in each cell | met |
| No topic taught once with nothing after | met |
| Sensitive units removable, with a leave-out note | met, with finding 3 (family-note days) and 11 |
| Getting help not only inside a sensitive unit | met |
| Indicators claimed in the right span | met (all 3-5 indicators in grades 3 to 5); finding 7 on practice codes |

## Settled by the expert

| # | Choice | Reason | File |
|---|---|---|---|
| 1 | Rewrite the goal lines of days 24, 39, 44, 49, 54, 59, 69, 74, 75, 79 and 88 with one item per part, as in the finding 1 table (day 24 adds "how to grow a strength"; days 69 and 75 add "how finding this fact would change the character's choice"; days 54 and 59 add "why a team with a clear ask is heard more"; day 49 splits S2.5.2 and S2.5.3 and adds a product and a service to the claim) | the code is judged only on what is asked | days.csv |
| 2 | Shorter path: grade 4 day 41 fold keeps a five-minute listening-reply rehearsal on day 42; grade 5 keeps day 70 and folds respond day 76 into day 77's exit (five minutes) and day 78's opener (day 78's retrieval repeats day 77's), grouped by step from the record sheet | no owned part or assessed row cut | scope-and-sequence.md |
| 3 | Response time: the marked sheet returns at the start of the next lesson and each student redoes one "not yet" step as that lesson's exit ticket; for units 7, 14 and 21 the sheet returns privately on days 30, 60 and 89 | counted once, no double-booked opener | days.csv notes, scope-and-sequence.md |
| 4 | Unit 7, 14 and 21 family notes go home on days 23, 53 and 82 with the earlier notes | they no longer ride on a removable unit | days.csv, scope-and-sequence.md |
| 5 | Retrieval added on days 25, 27, 55, 57, 84, 86 (bridge form) and g4-pa-warm-up on day 61 | rule 2; it also serves a left-out earlier unit | days.csv, rule 2 table |
| 6 | Day 80's W.4.1 and comparing-options retrievals move to day 81; day 86's question box is answered on day 87 | load | days.csv |
| 7 | Card withdrawal days as in finding 8 | no first unaided use on a check | days.csv |
| 8 | Drop S1.5.2 (day 9), S4.5.4 (day 58) and S4.5.6 (day 85) from `codes`; sensitive checks note "practiced, not scored" | assess rows list only what is asked in full | days.csv |
| 9 | Refusal card quoted as SEL's grade 3 form, with health's line after it | word-for-word rule | days.csv day 51, 70; scope-and-sequence.md |
| 10 | Source lines: NYTS 2024 for days 8 and 51; the national 8th-grade survey for day 70 (browser check); CDC bullying page for day 19; the vigorous-days line on day 3; 988 named by purpose on day 41 | accuracy, figures with source and year | days.csv, scope-and-sequence.md |

## For Cory

None. Every finding is an item-level or wording choice inside the frame.

## For the lead

- Frame lines that match finding 1 (the check table's wording for the grade 4 mid-year, grade 4 year-end, grade 5
  mid-year and year-end items), finding 10 (unit 1's guideline line) and finding 11 (the leave-out wording) are the
  frame's. The progression owner should look at g5-v-body-safety's ~NHES.S4.5.6 (finding 7).
- Agree with the scope's For the lead 1 (SEL Cross-subject: unit 17 now weeks 10 to 13).
- Browser check: https://www.stopbullying.gov/bullying/what-is-bullying (403);
  https://monitoringthefuture.org/results/annual-reports/ (403).

## For the source list

- CDC, youth tobacco data (NYTS 2024 middle school figures): https://www.cdc.gov/tobacco/php/data-statistics/youth-data-tobacco/index.html
- CDC, About bullying (uniform definition): https://www.cdc.gov/youth-violence/about/about-bullying.html

Findings: 12 (none for Cory). Confidence: findings 1, 2, 3, 5 firm (read straight from the rows against the
indicator text); 4, 7, 8 firm; 6, 12 judgment calls; 9 likely; 10 firm where a page was opened, likely for the
alcohol norm.

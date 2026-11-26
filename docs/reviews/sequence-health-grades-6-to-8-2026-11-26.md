# Expert read: scope and sequence, Health, grades 6 to 8 (2026-11-26)

Reader: Curio Class curriculum expert agent (fresh, cold read; did not write the scope). Brief:
docs/pipeline/briefs/sequence-read.md through build/scope-writes/AFTERCORE-READ.md.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/health.md, build/scope-writes/AFTERCORE-BRIEF.md.
- The thing under review: docs/courses/health-grades-6-to-8/scope-and-sequence.md and
  data/plans/health-grades-6-to-8/days.csv (144 rows), both in full.
- Beside them: docs/courses/health-grades-6-to-8/frame.md (course in brief, Models carried, the full Units table, For
  the lead), data/progressions/health.csv (assumes for every row placed here), data/standards/nhes-2024.txt (6-8
  span, for the whole-of-id checks; ids and our own words only below), docs/courses/health/STANDARD.md section 4,
  docs/courses/sel/STANDARD.md section 7 (shared steps), docs/courses/CALENDAR.md rule 3 and the grade 6 to 8 table,
  data/plans/calendar.csv (SEL, PE, math, science and ELA units and every check in weeks 17 and 18), the ELA grade 8
  scope (unit 5), the SEL and PE 6 to 8 days.csv (SEL unit 1, PE unit 11), and the earlier health sequence read
  (docs/reviews/sequence-health-grades-k-to-2-2026-11-26.md) for the REPEAT tags.
- Gates, run first: `plan.py check` (this course 0 failures), `frame.py calendar` (health weeks 17 and 32 in grades
  6, 7 and 8; no school day 84 clash in any grade), `sequence.py check health-grades-6-to-8` (0 failures; notes on
  day 117's `~NHES.S4.8.5` and "standard None" for the nine units that own no indicator, both expected),
  `frame.py check` (0 failures), `stale.py check` (0 failures).
- **The .md and days.csv agree.** The writer reported an edit to the .md after its last write. I checked by script:
  every unit's days and weeks in the .md match days.csv; every "(day N, code)" in the .md is on that day's codes;
  every day kind the .md names matches; the six course-level check rows carry the same codes in both files; the
  readiness table, family-note days and supplies match; `school_day` is ceil(10n / 3) on all 144 rows. No drift found.
- Outside sources opened (see Sources).

## Verdict

The scope is sound and close to ready: the 46 owned indicators are each placed in their own year and all sampled
on a course-level check, the calendar holds (weeks 17 and 32, no school day 84 clash), the sensitive units are
removable with their family notes two weeks ahead, and the .md and days.csv agree. The biggest risk is in the end
checks: several ask only part of the code they claim (S1.8.1's one-person half, S6.8.3's link to health, S4.8.7 on
the unit 26 end), so a unit plan built from these rows would leave parts of owned indicators unassessed. The one
change that matters most is to rewrite those end-check goals with a prompt per part; the rest is day-kind relabels,
self-check placement and small wording.

Findings: 8 (0 serious, 4 moderate, 4 minor).

## Findings, most serious first

### 1. End checks ask only part of the code they claim (moderate; LAYER sequence; REPEAT yes)

A busy writer builds the end sitting from the day's goal. These goals leave a part out:

- **NHES.S1.8.1** (strengths raise wellness for one person or a whole group). Day 5 asks "name a strength that helps
  the group"; day 25 samples only S1.8.2 from unit 1; day 47's item is "strengths for a group". The one-person half
  is never assessed in the band. Fix, day 5 goal: "...write the habit chain, and name a strength that raises the
  character's own wellness and one that helps the group, with what each adds." Day 47 note: "strengths for one
  person and for a group".
- **NHES.S6.8.3** (write a goal and explain its link to health). Day 84 asks "rewrite an unseen character goal with
  a measure and a time, and write a plan with a backup"; no item asks the link to health. Day 95's item ("a goal
  rewritten with a measure and a backup plan") has the same gap. Fix both: add "and say how the goal links to the
  character's health".
- **NHES.S4.8.7** (work well with others in different settings). Day 129 lists the code, but its goal scores the
  team record and monitoring sheet on the goal-plan steps; no teamwork prompt. Fix, day 129: add "one unseen team
  scene in a different setting (a class group or a club): write what the character does to work well with the
  others", and score the teacher's day 123 to 127 record of each student's part on the teamwork steps.
- **NHES.S2.8.4** (put methods and tools into practice). Day 108 asks only "name a tool". Naming is not putting into
  practice, and the day 103 log is private, so it cannot be the evidence. Fix, day 108: "an unseen influence case:
  choose a tool and write how the character uses it this week"; note that the day 107 record (a taught strategy on
  an invented message) counts for S3.8.5 and, if the unit plan wants it, for S2.8.4 too.
- **NHES.S4.8.3** (seek support and give it), day 53: "write the support line" can be read as one side. Write
  "write a line asking for support and a line offering it".
- **NHES.S4.8.6** (prevent, handle and end conflict), day 53: "the conflict steps a character uses" reads as one
  moment. Write "how the character could have prevented it, handles it now and ends it".
- **NHES.S8.8.5 and NHES.S5.8.6**, day 135: "one unseen look-back case" for two codes. Write "one unseen case with
  two prompts: did the advocacy make health better and how we know; how the decision to run it worked out for the
  team and others".
- **NHES.S1.8.7** (explain the ways care services help keep a person healthy), day 101: "choose the service with its
  reason" is a choice, not an explanation of the ways. Add "and explain how that service helps keep the character
  healthy".
- **NHES.S2.8.2** (factors behind behaviors, results and fair health), day 80: "the five-level check" names
  factors only. Add "with one health result and one fairness point".

### 2. New ideas first taught on Application days (moderate; LAYER sequence and frame; REPEAT yes)

The frame's day-kind rule says first teaching is always an Understanding day, and the writer applied it to S4.8.2
(day 13) and S6.8.2 (day 39). It was not applied to these, where the owned idea appears first on an Application
day with no model:

- Day 30, NHES.S5.8.1 (how following a decision process affects health): day 29 rehearses the steps (S5.8.2), and
  the "how it affects health" explanation is new on day 30.
- Day 71, NHES.S7.8.2 (which habits improve personal and community wellness, by reach): new on day 71.
- Day 134, NHES.S8.8.5 and NHES.S5.8.6 (judging the advocacy's effect; how the decision worked out): both new.
- Day 128, NHES.S6.8.6 (how setting the goal affected health): new, but the team has three monitoring lessons
  behind it, so Application with a modeled write-up is defensible.

The frame's Units table carries the same labels for 30, 71 and 134, so this is partly a frame wording issue. Cost:
a day writer builds a "new case, apply it" day for an idea nobody has explained. Fix: relabel days 30, 71 and 134
Understanding and start each goal with the teacher modeling the idea on one case ("the teacher shows how the steps
change a result, then..."); keep day 128 Application with a note that the teacher models one effect write-up first.
Settled below; the lead may add the frame wording at the next frame pass.

### 3. Self-checks missing in units 5, 15 and 25, and lost on fold-in days (moderate; LAYER sequence; REPEAT yes)

The .md says every unit has two self-checks (bar criterion 8). Units 5, 15 and 25 have self-check 1 (days 22, 70,
116) but no self-check 2: their end-of-unit assessment is the mid-year check (days 25, 73, 121), and those notes do
not name it. Separately, five of the nine ten-days-short fold-in days carry a unit's self-check 1 (days 7, 50, 70,
99, 110), and day 70 also carries the asthma emergency plan candidate line; the Shorter path does not say where
these go when the day folds.

Fix: days 25, 73 and 121 notes add "Self-check 2 for unit 5 (15, 25) after the check". Shorter path adds one line:
"A folded day's self-check moves to the next day of its unit, and day 70's asthma plan line moves to day 69."

### 4. Readiness checks stacked on two heavy end days (moderate; LAYER sequence; REPEAT new)

Days 59 and 65 each hold a full end sitting (two or three scenarios, a facts-in-use item per unit fact, a valuing
item), self-check 2, and a ten-minute readiness check. Day 59's end asks for a refusal, a ride plan and a decision
form; day 65's asks for a trace, two ratings, a product and a service source and the instruction-to-outcome link.
That does not fit 45 minutes as written, and a writer will cut the readiness check or rush the end. The placement
itself is right (rule 2: the last ten minutes of the previous unit's last day). Fix: the notes of days 59 and 65 cap
the sitting at two short scenarios, 25 minutes, then self-check 2 (5 minutes) and the readiness check (10 minutes).

### 5. The e-cigarette norm is worded against a different measure, and two facts need care (minor; LAYER sequence; REPEAT new)

- Day 17 states "the share of middle school students who do not use e-cigarettes". The national youth tobacco
  survey reports current use (any use in the past 30 days); the CDC youth page, opened today, gives 3.5 percent of
  middle school students in 2024. "Do not use" overstates what the figure shows. Write "had not used an
  e-cigarette in the past 30 days" (about 96 in 100 in 2024; check at the expert read whether a 2025 edition has
  been released and use the latest). The frame's norm bullet has the same wording; the lead may align it.
- Day 2: grade 6 students are 11 or 12, which straddles the CDC sleep bands (9 to 12 hours for ages 6 to 12, 8 to
  10 for teens; page dated 2024-05-15). The day note should give both ranges, never one number for the class.
- The national survey of grade 8 students (days 54, 115): its federal summary page lists a 2025 survey released
  2025-12-17; the survey's own results site returned 403 (browser check). The national highway traffic safety
  agency pages (days 56, 118) stay browser check as the .md says. "Ride in the back seat until 13" matches the
  standing federal advice from memory; confirm at the safety read.

### 6. The 40-minute path does not add up (minor; LAYER sequence; REPEAT yes)

"Opening scenario to 3 minutes and cards set out before the bell" saves about 3 minutes of the 5 lost, and gives
nothing on the days that also hold a 10-minute retrieval or readiness task (days 1, 59, 65, 97). Fix: "the retrieval
task drops to 7 minutes and the opening scenario to 3; a readiness check keeps its 10 minutes and the end sitting
on that day keeps two scenarios".

### 7. Stale or loose lines in the .md and a few notes (minor; LAYER sequence; REPEAT yes)

- .md "The 45 minutes": "A unit's second or third day opens with a 10-minute retrieval task." days.csv puts most
  retrievals on the unit's first day, as the .md's own Readiness section says. Write "first or second day".
- .md "What every unit does": self-checks "on its application or first day". In days.csv self-check 1 sits on
  Understanding, Fluency and Application days alike. Write "on a practice day before the check".
- Day 51 note: "PE unit 11 (weeks 13 to 16)"; calendar.csv has PE unit 11 in weeks 12 to 15.
- Day 13 note quotes the listening card without the grades 6 to 8 first step ("choose how to talk"); the .md's card
  table and day 110 have it. Add it on day 13.
- Day 69 note: science grade 7 unit 3 ends in week 14, the week unit 15 opens; "comes first" holds only within the
  week. Write "ends the week unit 15 opens".
- Coverage: "AOD 8 (units 5, 12, 25)" and the other leading numbers do not match STANDARD.md section 4's 6 to 8
  column (alcohol and other drugs there is outcomes 1 to 4, 6 and 8, six outcomes). I checked every unit's HBO list
  in days.csv against that column: every outcome in it is served (personal health 1 to 12, food 1 to 9, 11, 12,
  mental health 1 to 9, physical activity 1, 2, 5, 7, safety 1 to 8, violence 1 to 3, 5 to 7 plus 4, 8 to 10 in
  sensitive units, tobacco 1 to 5, alcohol and drugs 1 to 4, 6, 8, sexual health 1 to 10). Replace the leading
  counts with the outcome numbers, topic by topic, each with its units.

### 8. Two sensitive-unit lines from the frame are not carried (minor; LAYER sequence; REPEAT new)

- The frame says each sensitive unit's leave-in note tells a school that keeps the unit it may add one practice day
  before its check. Neither the .md's "Sensitivity and leave-out" nor the first-day notes of units 9, 10, 19, 20, 21,
  28, 29 and 30 say so. Add one sentence to each.
- Day 118 (impaired driving) handles the topic well ("the teacher reads the room") but names no flag; the brief asks
  the flag to be named in the note. Add "Sensitivity (safety and harm; substances):".

Everything else on safety and sensitivity holds: scenarios only, no student plays a person who pressures or harms,
the disclosure route on every sensitive first day, 988 named by purpose with a counselor told ahead on days 89 and
138, no method detail, no weighing or calorie talk, no real products, helmet shown on a stand only, and getting help
taught in a non-sensitive unit every year (units 2, 11, 24 and unit 22's services).

## What is right and should not be touched

- Owned rows: all 46 placed in their own year, each on at least one day and on at least one course-level check; no
  sensitive unit owns or is sampled; every year touches all eight standards in its non-sensitive units.
- Calendar: course days fall on ceil(10n / 3); every unit and check sits on the frame's weeks; mid-year checks on
  school day 84 clash with nothing in grades 6 to 8; same-year leans checked against calendar.csv (math 6 unit 2
  before unit 6, math 6 unit 8 and math 7 unit 8 after, ELA 7 unit 4 before unit 18, ELA 7 unit 6 after unit 13, ELA 8
  unit 2 beside unit 23 and before unit 27, ELA 8 unit 5 holds the formal talk, SEL and PE units as cited) all hold.
- Readiness and retrieval: every assumed row was checked against the progression. Year-before rows open as
  retrievals inside the unit; the three two-grades-back sets get readiness checks on days 59, 65 and 97.
- Shared cards: the .md quotes SEL STANDARD section 7's grades 6 to 8 words exactly.
- Leave-out targets match the frame (9 to 7, 10 to 1, 19 and 21 to 11, 20 to 14, 28 and 29 to 24, 30 to 27), and all
  eight family notes go home ten school days ahead.
- Unit order within each unit builds day on day; product units (18, 26, 27) count draft, feedback and revision.

## Lens checklist (scope and sequence layer)

| Line | Result |
|---|---|
| Band reaches all eight standards; skill standards in two topics | Met (frame counts with sensitive rows out) |
| Coverage map whose cells name units | Met in substance; numbers wrong (finding 7) |
| Topic taught once with nothing after | Met (tobacco 4, 18, 23; alcohol and drugs 5, 12, 25; food 6, 16, 27) |
| Sensitive unit removable, no skill only there, leave-out note | Met; leave-in line missing (finding 8) |
| Getting help not only in a sensitive unit | Met (units 2, 11, 24, 22) |
| Indicators in the right span | Met (6-8 span only) |

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Unit 22's readiness check stays on day 97 (last ten minutes, after the hook), `assess` blank | Day 96 is the grade 7 year's last day, months before grade 8; a check there is far more than a few days ahead. Agree with For the lead 1 | days.csv day 97 (no change) |
| g6-phw-adult-or-professional keeps a readiness check on day 97, not a retrieval | The progression governs: no grade 7 row assumes it; day 50's retrieval does not change that | days.csv day 97 (no change) |
| Relabel days 30, 71 and 134 Understanding, each opening with a teacher model | First teaching of an owned idea | days.csv days 30, 71, 134 |
| Days 59 and 65: two short scenarios, 25 minutes, then self-check 2 and the readiness check | Fits 45 minutes | days.csv days 59, 65 |
| Day 17 norm worded "had not used an e-cigarette in the past 30 days" | Matches the survey measure | days.csv day 17; .md unit 4 |
| Day 2 gives both CDC sleep ranges | Grade 6 straddles two age bands | days.csv day 2 |
| For the lead 6: sensitive-unit end checks stay unseen written scenarios, at most two short ones, telling and refusal lines, read aloud on request | Same form as every unit keeps the routine predictable; the length, not the form, is the load | .md For the lead 6 |
| For the lead 3 and 5: agree ("units 1 and 3"; "a fifth check") | Frame slips | frame.md at the next frame pass |

## For Cory

None. Every finding is inside the frame's units, rows and dose.

## What I could not judge

- The survey figures themselves (entered at the unit plan's expert read) and the national highway traffic safety
  agency pages (browser check).
- Whether three days hold the HECAT Sexual Health 6-8 outcomes for unit 30 (the frame defers it to the unit plan).

## Sources

- CDC, youth e-cigarette page, https://www.cdc.gov/tobacco/e-cigarettes/youth.html (opened 2026-11-26): 2024
  national youth tobacco survey, current middle school use 3.5 percent; used for finding 5.
- CDC, sleep basics, https://www.cdc.gov/sleep/about/index.html (opened 2026-11-26, page dated 2024-05-15): hours by
  age; finding 5.
- National drug abuse institute, Monitoring the Future summary,
  https://nida.nih.gov/research-topics/trends-statistics/monitoring-future (opened 2026-11-26): latest survey 2025,
  released 2025-12-17; finding 5.
- Monitoring the Future results site, https://monitoringthefuture.org/results/annual-reports/: 403, browser check.
- From memory: back seat until 13 (federal child passenger advice), 988 as the national crisis line.

## For the source list

- The CDC youth e-cigarette page above opens to automated reads and gives the national youth tobacco survey's
  latest middle school figure; the Monitoring the Future results site refuses automated reads (403), and the
  federal summary page above opens and names the latest year.

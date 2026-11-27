# Scope group read: health, 2026-11-26

Courses: health-grades-k-to-2, health-grades-3-to-5, health-grades-6-to-8, health-grades-9-to-12.

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/pipeline/briefs/sequence-read.md, build/scope-writes/AFTERCORE-BRIEF.md,
  build/scope-writes/GROUP-READ.md.
- data/progressions/health.csv and its edges file, the health section of docs/ADOPTION-BAR-SUBJECTS.md, health
  STANDARD.md and APPROACH.md, docs/agents/lenses/health.md.
- For each of the four courses: frame.md, scope-and-sequence.md, and data/plans/<course>/days.csv, read with Python
  scripts. They checked each progression row's `assumes` against its first use and the `retrieves` column, every
  `~ID` against a plain owner, NHES ownership across the band, and the card wording on every day that names a shared
  card. I also skimmed the four sequence reads and their -fixes reports from 2026-11-26.
- docs/courses/CALENDAR.md, data/plans/calendar.csv, and DESK-ANSWERS.md entries that name health, above all
  2026-11-26.
- SEL STANDARD section 7 (Shared steps) and the SEL frames and scopes at K to 2 and 3 to 5. I also read the PE K to 2
  and 3 to 5 scopes for the shared cards and the lean weeks.

## Findings

### 1. Family-structure content: health opts it out, SEL teaches it the same weeks (Cory)

Two health units treat this content as sensitive and removable, each with a family note and a leave-out bridge:

- Health K to 2 unit 11, days 53 and 54 (grade 1, weeks 25 to 26). These days hold the read-aloud on families of
  many structures.
- Health 3 to 5 unit 7, days 27 and 28, which teach that families differ.

SEL teaches the same content as ordinary model content, with no opt-out:

- SEL K to 2, kindergarten unit 1 model pages: two moms, two dads, one parent, grandparents, foster families.
- SEL K to 2, grade 1 unit 11 (weeks 21 to 26, day 105): "families of every kind in the models, LGBTQ families
  included".
- SEL 3 to 5 model webs: "families of every kind".

The health K to 2 fixes report (For the structure pass) asked SEL to confirm it has no family-structure content in
unit 11, so that health's opt-out holds. It does have that content, so the condition fails. As written, a family that
opts out of health unit 11 meets the same content in SEL in the same weeks. That breaks the promise the family note
makes. It also makes the sensitive flag look arbitrary to a reviewer who reads both courses.

Options:

- (a) Keep health's units sensitive, and have the family note say plainly that SEL's models show families of every
  kind all year and are not removable.
- (b) Make health's family-respect days ordinary, matching SEL. Keep the leave-out only for any body or
  relationship-history content.
- (c) SEL removes family structures from its models.

My pick is (b). Showing many kinds of families as part of respect is how SEL already handles it across two bands. An
opt-out that cannot actually keep the content away misleads families. If Cory wants an opt-out kept, (a) is the honest
fallback. I advise against (c): it cuts content from a course that has already passed its own read.

### 2. Boundary steps are worded three ways across the band (scope)

The same steps read differently from course to course:

- Health K to 2, day 71 (also the K to 2 frame and SEL K to 2): "say it, say stop again, move away, tell".
- Health 3 to 5, day 20, and health 6 to 8, days 33 and 67: "say it, repeat it, leave, tell". No frame and no SEL
  card uses this wording.
- Health 9 to 12, day 37: "say it, say it again, move away, tell". This matches the SEL STANDARD section 7 refusal
  second push, which names health's boundary steps as "say it again, move away, tell".

SEL's refusal card points to health's boundary steps by name, so the words need to be the same. A student who learns
"repeat it, leave" in grades 3 to 8 then meets "say it again, move away" in SEL and in grade 9. Every one of those
cards is meant to be the same card.

Fix: health 3 to 5 day 20 and health 6 to 8 days 33 and 67 (and the .md "Shared cards" lines) take SEL's words: "say
it, say it again, move away, tell". K to 2 keeps "say stop again" as its young form and says that it grows into "say
it again". No unit or day moves.

### 3. No line for a student new to Curio Class health at the 6 to 8 and 9 to 12 band entries (scope)

Health 3 to 5 carries "a student new to Curio Class health shows any gap here and the teacher reteaches that step on
the card the same day" on 41 days, including its year-one openers. Health 6 to 8 does not carry it on its grade 6
openers (from day 1, where cards from grade 5 are retrieved), and health 9 to 12 does not carry it on day 1 or on its
grade 8 retrievals. Day 1 of health 9 to 12 even assumes grade 8 logs.

Middle school and high school are where students most often change schools. Those are exactly the seams where the line
matters.

Fix: add the 3 to 5 sentence, or one pointing to the scope's band-entry paragraph, to health 6 to 8 days 1, 10, 12, 19
and 21. Add it to health 9 to 12 day 1 and to each day that retrieves a grade 8 row. Health 9 to 12 day 1 should say
what replaces the grade 8 log when there is none (for example, a one-minute self-rating).

### 4. NYTS figures cite the 2024 edition after the 2025 edition is out (scope)

- Health 3 to 5, days 8 and 51, cite NYTS 2024 for middle school: 12.9% had ever tried an e-cigarette, and 3.5% were
  current users.
- Health 6 to 8, day 17, cites 2024: 3.5% current users, "about 96 in 100" did not use. The scope says a later edition
  replaces it once released.
- The FDA NYTS results page (opened 2026-11-26) gives 2025 results: 2.6% of middle school students and 7.1% of high
  school students were current users.
- The CDC youth e-cigarette page (opened 2026-11-26) still shows 2024 figures.
- Health 9 to 12 already uses 2025, so the band now holds two editions.

STANDARD section 6 treats a figure older than its source's latest edition as a finding. A norm figure also carries the
lesson's message, so it should be the current one.

Fix: health 6 to 8 day 17 becomes 2.6%, "about 97 in 100" (past 30 days, following the 6 to 8 settled norm wording).
Health 3 to 5 days 8 and 51 take the same current-use figure. The "ever tried" figure is rechecked against the 2025
release. If 2025 does not report it, the note says "the latest edition that reports it" with its year, as the 9 to 12
settled judgment does.

### 5. The speak-up plan changes name and steps at grade 9 with no link to grade 8 (scope)

The plan's form through the band:

- Health 3 to 5, day 52, teaches the speak-up plan as "notice, who, say, ask". Health 6 to 8 keeps those steps.
- Health 6 to 8 day 85 adds a grade 7 form, "a first step added before notice", but never names the step.
- Health 6 to 8 day 130 gives a grade 8 form, "fitted to the audience".
- Health 9 to 12 day 21 calls its counter line "the speak-up plan's first use in the course".
- Health 9 to 12 day 61 gives the plan as "issue, audience, ask, evidence, deliver, judge the result". It does not
  retrieve the grade 8 card or say how this form grew from it.

A card that changes its steps without a named growth looks like a new card. Students then lose the transfer the band is
built on.

Fix:

- Health 6 to 8 day 85 names the added step.
- Health 9 to 12 day 21 retrieves the grade 8 form (health 6 to 8 day 130).
- Health 9 to 12 day 61 says each new step is added to the grade 8 card: "issue" grows from notice, "audience" from
  who, "evidence" is new, and "judge the result" is the look-back.

### 6. Help steps and decision steps drift between 6 to 8 and 9 to 12 (scope)

Help steps:

- Health 6 to 8: "know your helpers, pick the right one, say who, what happened, that it matters, keep telling".
- Health 9 to 12 day 12 drops "pick the right one" and says nothing about the change.

Decision steps:

- Health 6 to 8: "notice a careful choice, ask if it needs help, name options and results, pick the one that supports
  health, look back".
- Health 9 to 12 day 42: "notice the choice, is it a careful one, options, priorities and results, pick, plan, look
  back". This adds priorities and a plan, with no growth named.

Conflict steps:

- Health 9 to 12 day 39 models the conflict card but never states its words.
- Health 3 to 5 day 77 and health 6 to 8 day 51 both read "stop, calm down, each says their side, find a fair way, or
  walk away and get help". Health 3 to 5 day 19 retrieves the grade 2 form, so that change is named and holds.

Fix:

- Health 9 to 12 day 12 keeps "pick the right one", or says why it drops.
- Health 9 to 12 day 42 says that priorities and plan are added to the grade 8 card.
- Health 9 to 12 day 39 quotes its conflict card, in the 6 to 8 words or a named grown form.

### 7. Codes on sensitive-unit days are recorded four ways (scope)

- Health K to 2: the codes column is empty except for one `~` preview.
- Health 3 to 5: plain codes with "practiced, not scored" (for example, day 25 S3.5.1; days 55 and 56 S4.5.4 and
  S4.5.3; day 86 S1.5.7).
- Health 6 to 8: `~` codes.
- Health 9 to 12: plain codes with no "practiced, not scored" (days 69 to 78: S4.12.4, S3.12.1, S4.12.3, S4.12.10).

The sensitive units own nothing, so a removable unit must not look like a scored owner. A reader of 9 to 12 days 69 to
78 sees plain codes and could take them as owned evidence. The 3 to 5 settled judgment ("on assess rows `codes` lists
only codes an item asks in full; sensitive checks add 'practiced, not scored'") is applied there and not in the other
three courses.

Fix: apply the 3 to 5 judgment across the band. Health 9 to 12 days 69 to 78 add "practiced, not scored". Health 6 to
8 keeps its `~` codes, or moves to plain codes with the same note. Health K to 2 states in its scope that its sensitive
days carry no codes.

### 8. Sensitivity flags and private routes on ordinary days are uneven (scope)

- Health 9 to 12 has 33 days that carry "Sensitivity flag: <area>" with the private route. The route says the cases are
  characters', any student may take another case, and a student can talk privately with the nurse or counselor.
- Health 6 to 8 writes "Sensitivity (topic):" and gives no private route.
- Health 3 to 5 gives only "Sensitivity read: X". Some days that need a flag carry none, such as unit 17 day 70
  (alcohol).
- Health K to 2 carries "Sensitivity flag" on days 3, 6 and 60.
- The health 6 to 8 scope says units 14 (safety and harm) and 26 (body) are flagged. Yet no day in unit 14 (days 66 to
  68) or unit 26 (days 123 to 129) carries a sensitivity note.

The after-core brief asks for private routes on the day they apply, with the flag named. The 9 to 12 settled judgment
("a sensitivity flag names its area and the private route in the note itself") was applied in one course only.

Fix: health 6 to 8 and 3 to 5 take the 9 to 12 form, with a private route suited to their grade (in 3 to 5, "talk to
the teacher or the counselor"). Health 6 to 8 days 66 to 68 and 123 to 129 gain their flags. Health 3 to 5 day 70
gains a flag.

### 9. The 6 to 8 frame's seam sentence contradicts its own table (frame)

Health 6 to 8 frame line 190 calls g4-meh-calm-stress and g4-phw-prevent-illness-injury "two grade 4 rows two grades
back (readiness checks)". The same frame's pick-up table (rows 202 and 207) and the 6 to 8 scope (days 10 and 21) treat
them as retrievals. The table and scope are right: health 3 to 5 retrieves both rows in grade 5 (days 61, 78 and 72),
so their last use is one grade back.

Fix: line 190 reads "two grade 4 rows last used in grade 5 (retrieval)".

### 10. The asthma case runs as a main case in four grades (scope)

The asthma case is a main case in:

- Health 3 to 5, day 36 (grade 4).
- Health 6 to 8, day 69 (grade 7).
- Health 6 to 8, day 97 hook (grade 8, asthma and air quality).
- Health 9 to 12, day 17.

Health 9 to 12 names its reason, which is the return to living with conditions. Health 6 to 8 names none for either
grade 7 or grade 8. A student who meets the same case three years running sees nothing new in it.

Fix: health 6 to 8 day 69 or day 97 swaps to another chronic condition (for example, type 1 diabetes or a food
allergy), or the note names what is new this time (the grade 8 environment and community factor).

## What holds

- Every row in health.csv for these grades is taught. Every `~` id is finished by a plain owner in its course. All 172
  NHES ids have exactly one owner across the band.
- The seams match both frames' tables. The readiness checks sit where rule 2 puts them: health 6 to 8 days 59, 65 and
  97, and health 9 to 12 days 36 and 51. Two retrievals come one day after the first use, which is harmless: health 6
  to 8 day 44 retrieves g5-sh on day 45, and health 9 to 12 day 16 retrieves g7-living on day 17.
- The check weeks match CALENDAR.md: K to 2 weeks 12 and 27 (K) and 11 and 27; 3 to 5 weeks 15 and 29, 14 and 29, and
  14 and 28; 6 to 8 weeks 17 and 32; 9 to 12 weeks 7 and 16. The K to 2 SEL and PE lean weeks match calendar.csv. The
  load ramp (28, 30, 48 and 80 lessons a year) is the one Cory accepted.
- 988 is named by purpose in an ordinary unit in each band from grade 4 (health 3 to 5 day 41, 6 to 8 day 6, 9 to 12
  day 29). The 988 site confirms call or text.
- The I-statement and calm-down wordings match SEL in every band. The refusal card is played by a card, not a partner,
  in every band (Desk 2026-11-26). K to 2's conflict steps match PE K to 2 day 183.
- Family notes go home two weeks ahead in every band. Health 9 to 12 carries the 18-or-over rule. The K to 2 adult
  tobacco figure (19.8%, 2022) holds.
- The tobacco-free advocacy case comes back in 3 to 5 day 80, 6 to 8 day 86 and 9 to 12 day 67, each time in a
  different task form (one line, a campaign, a coalition). That is a named climb, not a repeat.

## Sources

- https://www.fda.gov/tobacco-products/youth-and-tobacco/results-annual-national-youth-tobacco-survey-nyts, opened
  2026-11-26 (the 2025 NYTS figures).
- https://www.cdc.gov/tobacco/e-cigarettes/youth.html, opened 2026-11-26 (still shows 2024).
- https://988lifeline.org/, opened 2026-11-26.
- Browser check, carried from the course scopes and not reopened here: the national highway traffic safety agency
  pages, Poison Help, https://www.stopbullying.gov/bullying/what-is-bullying, the Monitoring the Future pages,
  https://library.samhsa.gov/product/preventing-suicide-toolkit-high-schools/sma12-4669, and the NIH dietary
  supplement page.

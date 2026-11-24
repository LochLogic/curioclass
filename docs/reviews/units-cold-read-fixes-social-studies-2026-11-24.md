# Cold read fixes, social studies unit plans, 2026-11-24

Fix pass on docs/reviews/units-cold-read-social-studies-2026-11-24.md. Kindergarten to grade 3 have every day
written (courses/social-studies-*), so a fix that changes one of their days is a defect row in
data/plans/defects.csv (found_by "cold-read fix 2026-11-24"), not an edit to the day. Grades 4, 5 and the high
school courses touched here have no written days, so their plans and days.csv notes were edited directly.

Outcomes by finding: 5 fixed (1, 3, 5, 6, 7), 1 defect rows only (2), 1 fixed in the plans with one defect row for
a written day (4); 0 for Cory, 0 no change. Defect rows added: 4.

## Findings

### 1. Reused rows labeled "owned" (fixed earlier)

Fixed in scripts/unit_skeleton.py and pushed before this pass (commit 8dd354eed). Checked in grade 2 s05, grade 3
s05, grade 5 s05 and World History I s09: each now lists only the frame's owned rows as owned, the reused rows on
their own "Earlier rows used again (review, not owned)" line, and Builds on carries earlier-grade rows only (grade 3
s05 no longer lists ss1-leaders). Reads right. No further edit.

### 2. Grade 2 exits ask less than grade 1's (defect rows)

Every grade 2 day is written, so no day and no Goal map row was edited (the Goal map row changes with the day). Three
day-layer defect rows, kind level, one per unit, name the days whose goal is choose, read, source or distinguish and
whose exit should add a spoken reason ("circle it, then say why"):
- unit 1: days 1, 5, 7, 8, 9, 10, 11 (days 2, 3, 4, 6 are identify, count or answer and keep recognise);
- unit 2: days 21, 22 (locate and identify days 17 to 19 and 23 keep recognise);
- unit 3: days 34, 35, 38 (match and identify days 37 and 39 to 42 keep recognise).
Unit 4's Goal map has no recognise exit. Outside the finding's scope and not logged: unit 5 day 62 ("pick and
trace") and unit 7 days 82 to 84 (choose and pick, token exits) have the same shape; the day fixer may weigh them.

### 3. Grade 5 unit 1 never checks ss4-native-nations-sites (fixed)

social-studies-grade-5/s01.md field 4: a day 1 retrieval row (a preserved place such as Cahokia or Mesa Verde, the
living nations who count its builders as ancestors, what it shows about who lived and governed here before the
colonies), with a ten-minute repair inside day 2 beside the New England nations' own pages. days.csv day 1 note
names the task. Item-level choice: the prompt follows the row as written (preserved sites and the nations tied to
them), not the cold read's suggested eastern woodlands map task, which belongs to ss5-colonial-encounters itself.

### 4. Six more assumed rows with no retrieval (4 fixed, 1 fixed with a defect row, 1 label fix)

- Grade 1 unit 3, ssk-i-think-because: the written day 20 already asks "I think ___ because ___"; only the label
  missed it. Field 4 row and days.csv day 20 note now name the row. No defect needed.
- Grade 3 unit 5, ss2-nation-of-immigrants: field 4 row on day 98 (who chose to come, who was here first, who was
  forced to come; no family histories asked), handoffs line updated, days.csv day 98 note added. Day 98 is written:
  defect row (day, handoff) to add the task to it.
- Grade 4 unit 2, ss3-biography: field 4 row and days.csv note on day 18 (where the grade 3 facts came from, how
  notes were kept), before kinds of sources are named.
- Grade 4 unit 6, ss3-home-region: field 4 row and days.csv note on day 108 (find our state, its region and two
  other states), rechecked on day 113. ss3-state-constitution stays inside day 126, as the cold read accepted.
- Grade 5 unit 5, ss4-states-and-statehood: field 4 row and days.csv note on day 61 (what a state gains), set just
  before the state-size debate it feeds.

### 5. World Geography and Ancient Civilizations I field 4 labels (fixed)

- s01: day 2 retrieval of the grade 5 source log (ss5-civil-rights-research) on an Ur tablet card, and day 3
  retrieval of a grade 5 cause chain (ss5-revolution-causes) before the worked investigation; the field 4 lead line
  now names days 2, 3 and 4; days.csv notes for days 2 and 3 added.
- s08: "Given: none" replaced by a "Retrieval only:" line pointing at day 105's in-day check.

### 6. US History II leans on other courses' checks (fixed)

s07 and s10 field 4 each gain one line: a student who did not sit the other course's check (Government unit 2,
Economics unit 1) takes the unit's retrieval task (day 86, day 130) as readiness evidence, scored as readiness, with
the same repair. Item-level, so decided here.

### 7. High school goal verbs barely climb (fixed where it belongs)

No unit plan edit, as the cold read says. Passed to section and day work as one line in the social studies lens
(docs/agents/lenses/social-studies.md, "Errors reviewers catch", Day): a high school exit that asks for a weighed
judgment names that verb (evaluate, argue, defend) in its Goal map row, not "explain".

## For Cory

Nothing. No finding turned on scope, money, people or audience.

## Gates

- `python -X utf8 scripts/unitplan.py check`: no FAIL.
- `python -X utf8 scripts/sequence.py check <course>`: 0 failures for social-studies-grade-1, grade-3, grade-4,
  grade-5, world-geography-and-ancient-civilizations-i and us-history-ii.
- Goalmap audit: not run; no brief named it and no Goal map row was edited.
- `plan.py check` (not a gate for this pass) still reports earlier FAILs in grades 1 and 3 items.csv (one-ask
  stems, missing exit items); none comes from these edits.

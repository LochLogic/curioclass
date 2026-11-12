# What a unit costs

Started 2026-11-12. One row for each piece of each pilot unit, filled in as the piece is made, not afterwards.
This is the base of the plan with sizes and dates for all 105 courses (ROADMAP), so a guess is worse than a
blank: leave a cell empty if it was not measured, and say "estimate" if it is one.

- **Tokens:** from the agent's own usage figure at the end of its run. Include the cold read and the revision.
- **Wall hours:** start to pushed.
- **Owner minutes:** Cory's or Sara's time reading, answering or fixing.
- **Defects:** from `python -X utf8 scripts/plan.py defects`, counted by the read that found them.

## Grade 4 math, unit 11.1 (area and perimeter, days 89 to 93)

| Piece | Tokens | Wall hours | Owner minutes | Defects found, by read | Notes |
|---|---|---|---|---|---|
| Stretch sheet and unit plan (s11.md) | not measured | not measured | not measured | 15, expert cold read | Written three times over two days before costs were kept; do not use as a base |
| Plan as data (parts, days, items, wrongs, errors) | not measured | | | 0 by the script after revision | |
| Lesson-day template (LESSON-DAY.md), with scripts/lesson.py | Cold read 200,829 (the expert's run); writing and revision not measured | | | 13, expert cold read, shared with day 90 (9 fixed, 4 open for the taught run) | Once only, not a unit cost. Draft 2 waits on Cory's yes |
| Day 89 lesson | 129,028 by its agent (23 tool uses), plus about 4,000 merge (estimate) | 0.07 for the agent (4.4 min); merge and push same evening | 0 | 0 by the scripts at merge; 10 by the expert cold read | One agent per day from one shared brief, in its own worktree. Teacher 878 words, student 210, two sides |
| Day 90 lesson | Not measured apart from the template | | | Counted with the template row | Draft 2: teacher 898 words, student 247, two sides; not ready (tool, opener, facts sheet, record sheet missing) |
| Day 91 lesson | 132,830 by its agent (27 tool uses), plus about 4,000 merge (estimate) | 0.08 for the agent (5.1 min) | 0 | 0 by the scripts at merge; 14 by the expert cold read | Teacher 895, student 176, two sides. Needed the generator sheet (row below) |
| Day 92 lesson | 136,815 by its agent (25 tool uses), plus about 4,000 merge (estimate) | 0.10 for the agent (5.8 min) | 0 | 0 by the scripts at merge; 14 by the expert cold read | Teacher 898, student 280, two sides |
| Day 93 check and respond | 127,977 by its agent (29 tool uses), plus about 4,000 merge (estimate) | 0.06 for the agent (3.8 min) | 0 | 0 by the scripts; the agent found 5 builder gaps for check days; 12 by the expert cold read | Teacher 500, student 202, two sides. Fixing the check-day builders in lesson.py (display, key order, look-fors) took about 25,000 more (estimate); a once-only tooling cost, not a day cost |
| Expert cold reads, days 89, 91, 92, 93 | 167,177 / 180,499 / 167,661 / 166,847 (34 / 37 / 29 / 27 tool uses) | 0.13 / 0.15 / 0.13 / 0.14 (8.0 / 9.1 / 7.6 / 8.1 min), run in parallel | 0 | 50 in all (10 / 14 / 14 / 12); about 7 in 10 in the process layer (template, generator, scripts), not the day; none needed Cory | Reports in docs/reviews/day-0NN-2026-11-12.md. Fixes applied by one agent: 129,337 tokens, 121 tool uses, 22.7 min; 47 fixed, 3 open, 13 new gates |
| Generator sheet | not measured (made in the main session) | | 0 | 0 by check_generators | A new skill in measure-shapes, a preset row, sheet-d091.md, and plan.py reserve so it never repeats the unit's numbers |
| Readiness check and end check, print and keys | not measured (main session) | | 0 | 0 by the scripts | Readiness is a piece file; the end check is day 93's student page. Also the two facts-check sheets (unit 1.1) |
| Record sheet | not measured (main session) | | 0 | 0 by the scripts | One landscape side, 22 rows |
| Family note (English, Spanish) | not measured (main session) | | 0 | | Spanish waits for a qualified reader. Also made: the anchor chart and a family game (Fence or Floor) |
| Community Plot Planner: eight asks | | | | | Queued 2026-11-12 as the first build in the Codex queue (scripts/codex_queue.py PILOT), with an owner note pointing at d090.md |
| Teacher read | | | | | A person; see README.md |
| Taught run | | | | | A person |
| Three timed students | | | | | People |

**For estimates (the four days).** A lesson day written by one agent from a shared brief cost 128,000 to 137,000
tokens, mean 131,700, plus about 4,000 to merge (estimate). Add a cold read before using the figure as a full day
cost: the four expert day reads cost 167,000 to 180,000, mean 170,500, so a day with a full expert read is about
306,000 tokens, more than half of it the read. That is why the read is the first cost to shrink once its findings
stop repeating (docs/pilots/REVIEW-CADENCE.md). The agents read the same plan pack, so most of each figure is
reading, not writing.

## Grade 4 math, stretch 10 (multiplicative comparison, days 80 to 88), the second unit

Built 2026-11-12, after the four 11.1 day reads were folded in. Full expert read on every day still to come
(REVIEW-CADENCE.md step 2).

| Piece | Tokens | Wall hours | Owner minutes | Defects found, by read | Notes |
|---|---|---|---|---|---|
| Plan as data (s10.md and u10 files into the five CSVs) | 81,149 by one agent (46 tool uses) | 0.26 (15.5 min) | 0 | 0 by the script after | Prose plan existed (written before costs were kept); plan.py gained unit-file tables and multi-part cells |
| Day 80 lesson | 158,163 by its agent (21 tool uses) | 0.11 (6.8 min), all nine in parallel | 0 | 0 by the scripts at merge | One agent per day from one shared brief (with the four 11.1 reads folded in), in its own worktree |
| Day 81 lesson | 169,947 by its agent (29 tool uses) | 0.12 (7.3 min), all nine in parallel | 0 | 0 by the scripts at merge | One agent per day from one shared brief (with the four 11.1 reads folded in), in its own worktree |
| Day 82 lesson | 179,863 by its agent (32 tool uses) | 0.14 (8.3 min), all nine in parallel | 0 | 0 by the scripts at merge | One agent per day from one shared brief (with the four 11.1 reads folded in), in its own worktree |
| Day 83 lesson | 170,049 by its agent (28 tool uses) | 0.12 (7.5 min), all nine in parallel | 0 | 0 by the scripts at merge | One agent per day from one shared brief (with the four 11.1 reads folded in), in its own worktree |
| Day 84 lesson | 166,148 by its agent (41 tool uses) | 0.16 (9.6 min), all nine in parallel | 0 | 0 by the scripts at merge | One agent per day from one shared brief (with the four 11.1 reads folded in), in its own worktree |
| Day 85 lesson | 171,024 by its agent (32 tool uses) | 0.14 (8.3 min), all nine in parallel | 0 | 0 by the scripts at merge | One agent per day from one shared brief (with the four 11.1 reads folded in), in its own worktree |
| Day 86 lesson | 184,931 by its agent (35 tool uses) | 0.13 (8.1 min), all nine in parallel | 0 | 0 by the scripts at merge | One agent per day from one shared brief (with the four 11.1 reads folded in), in its own worktree |
| Day 87 lesson | 182,060 by its agent (38 tool uses) | 0.14 (8.5 min), all nine in parallel | 0 | 0 by the scripts at merge | One agent per day from one shared brief (with the four 11.1 reads folded in), in its own worktree |
| Day 88 lesson | 140,555 by its agent (22 tool uses) | 0.07 (4.1 min), all nine in parallel | 0 | 0 by the scripts at merge | One agent per day from one shared brief (with the four 11.1 reads folded in), in its own worktree |
| Shared pieces (readiness, three openers, record, strip sheet, family note) | 165,181 by one agent (63 tool uses) | 0.17 (10.2 min) | 0 | 0 by the scripts | Run alongside the nine days |
| Merge of the nine days | not measured (main session, small) | | 0 | 2 duplicate wrong-answer rows, removed | |
| Writer-flagged fix pass (lesson.py byte-stable PDFs, sketch gate, check screen, and others) | 96,200 by one agent (97 tool uses) | 0.27 (15.9 min) | 0 | 13 fixed, found by the day writers | Before the expert reads |
| Expert cold reads, days 80 to 88 | 173,197 / 164,160 / 197,136 / 184,064 / 160,803 / 178,123 / 158,824 / 175,657 / 211,259; mean 178,100 | 0.09 to 0.12 each (5.2 to 7.1 min), run in parallel | 0 | 87 in all (10 / 7 / 12 / 10 / 7 / 9 / 10 / 11 / 11); 56% process layer; 61 repeat an 11.1 kind; none for Cory | Reports in docs/reviews/day-080 to 088-2026-11-12.md; analysis in REVIEW-CADENCE.md |
| Expert fix pass | 216,916 by one agent (264 tool uses) | 0.55 (33.1 min) | 0 | 85 of 87 fixed, 2 open (a tool ask; one judgment left for the taught run); about 10 new gates | Also touched stretch 11 days 89 to 93 where a stretch 10 promise reached them |

**For estimates.** Nine days cost 140,555 to 184,931 tokens each, mean 169,200, up from 131,700 in unit 11.1: the brief now carries
the 11.1 lessons and the gates are stricter, so agents spend more turns passing them. A stretch's shared pieces cost
about 165,000 once, and putting a prose plan into data about 81,000.

## Grade 4 math, stretches 1 and 9, the third and fourth units

Started 2026-11-12. Stretch 1 is factors and multiples (days 1 to 6); stretch 9 is adding and subtracting to a
million (days 72 to 79; day 78 is Check 2, which waits on stretches 6 to 8).

| Piece | Tokens | Wall hours | Owner minutes | Defects found, by read | Notes |
|---|---|---|---|---|---|
| Stretch 1 plan as data | 250,696 by one agent (68 tool uses) | 0.17 (10.2 min) | 0 | 0 by the script after | Prose plan existed |
| Stretch 9 plan as data | 217,505 by one agent (42 tool uses) | 0.17 (10.3 min) | 0 | 0 by the script after | plan.py: check-2 and respond-2 units |
| Merge of both into main | not measured (main session) | | 0 | 1 stale duplicate day row; 2 hand-backs at the door moved to pencils down | The new tool-rows gate flags days 2 to 5 and 77 until their writers add T rows |

## Grade 6 ELA, stretch 2, five pilot days

Not started. Planning pieces so far (rubric page, approach page, rights list): tokens not measured.

## Science pilot

Not started.

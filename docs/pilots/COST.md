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
| Day 89 lesson | 129,028 by its agent (23 tool uses), plus about 4,000 merge (estimate) | 0.07 for the agent (4.4 min); merge and push same evening | 0 | 0 by the scripts at merge; no cold read yet | One agent per day from one shared brief, in its own worktree. Teacher 878 words, student 210, two sides |
| Day 90 lesson | Not measured apart from the template | | | Counted with the template row | Draft 2: teacher 898 words, student 247, two sides; not ready (tool, opener, facts sheet, record sheet missing) |
| Day 91 lesson | 132,830 by its agent (27 tool uses), plus about 4,000 merge (estimate) | 0.08 for the agent (5.1 min) | 0 | 0 by the scripts at merge; no cold read yet | Teacher 895, student 176, two sides. Needed the generator sheet (row below) |
| Day 92 lesson | 136,815 by its agent (25 tool uses), plus about 4,000 merge (estimate) | 0.10 for the agent (5.8 min) | 0 | 0 by the scripts at merge; no cold read yet | Teacher 898, student 280, two sides |
| Day 93 check and respond | 127,977 by its agent (29 tool uses), plus about 4,000 merge (estimate) | 0.06 for the agent (3.8 min) | 0 | 0 by the scripts; the agent found 5 builder gaps for check days | Teacher 500, student 202, two sides. Fixing the check-day builders in lesson.py (display, key order, look-fors) took about 25,000 more (estimate); a once-only tooling cost, not a day cost |
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
cost: the day 90 cold read was 200,829 on its own. The agents read the same plan pack, so most of each figure is
reading, not writing.

## Grade 6 ELA, stretch 2, five pilot days

Not started. Planning pieces so far (rubric page, approach page, rights list): tokens not measured.

## Science pilot

Not started.

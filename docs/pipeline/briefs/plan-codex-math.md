# Job: write unit {unit} plan of {course} (Codex, math)

**Open for the lead (calls not found in docs/agents/decisions/DESK-ANSWERS.md or the frames; follow the stated default and list any use under "For the lead"):**
- Numeric balance of understanding, fluency and application per unit: no rule on file; the frame's day counts decide. State the balance you chose.
- Whether a unit below the major-work line (65 percent for grades 3 to 8, 75 percent for K to 2) is acceptable when the course total clears it: not decided. Report the unit's own share and do not pad.
- High school math (clusters marked "wap", no 65 percent rule): no unit-level standard of rigor on file. Follow the frame and say so.

[COURSE] = {course}. You fill in the plan for unit {unit} of the math course {course}: docs/courses/{course}/s{uu}.md only; other units are written in their own runs, one after another. Where an earlier unit plan of this course exists, read it first, keep its shape and voice, and keep or change its carried list. The file already exists as a skeleton made by scripts/unit_skeleton.py: the mechanical fields are filled and correct; replace every `TODO(writer)` line with the content it asks for, as the curriculum expert (docs/agents/EXPERT.md), following docs/pipeline/briefs/plan.md and docs/courses/UNIT-PLAN.md, to the bar: docs/RUBRIC-MATH-K8.md (three gateways: focus and coherence, rigor and the eight practices, supports) for kindergarten to grade 8, with the math lens in docs/pipeline/briefs and the course's frame; the wording of every owned code from data/standards/ccss-math-standards.txt. Where a `TODO(writer)` line names missing data, do the work with what is on file, say what was missing under "For the lead", and do not invent it. Change a mechanical field only if it is wrong, and then say so under "For the lead". Then run `python -X utf8 scripts/unitplan.py check {course}` until s{uu}.md passes (later units may still be skeletons; ignore their failures).

Style: a teacher reads this quickly. Write plain full sentences. No slash chains (write "map and photograph", not "map/photograph"), no telegraphic shorthand, no abbreviations a teacher would have to decode. Keep within the word cap by choosing less, not by compressing words.

Settled by the social studies plan reads (2026-11-14; apply where they fit this subject):
- Write the file as UTF-8 with LF line endings. Never let an apostrophe, quote or accented letter turn into "?"; the gate fails it.
- An exit ticket is one question with at most two parts; any invented case is printed "invented for practice". Kindergarten to grade 2: every child marks a picture on paper while the teacher reads the prompt aloud, and the spoken reason is heard from a rotating group of about six a day.
- Give each assessment item its minutes and keep the total inside the day's real minutes; a part made earlier on a product day comes off the sitting. No reteaching on an assessment day.
- Check days.csv before naming a day in prose; a day number in the plan matches days.csv.
- No pipeline notes in the plan (skeleton, gate, run or reviewer remarks); they go in your last message.
- A fact that can change (a living institution or leader, a renamed place, a court ruling, a current figure) gets a dated teacher background line ("As of November 2026: ...") with its source, after a news search of the last 24 months, deaths included.

Math settled by the frames and the Desk:
- Base text: Illustrative Mathematics (CC BY 4.0). Adapt in its order; each lesson used gets one short credit line on its day and nowhere else. The skeleton lists data/plans/{course}/source-map.csv rows in field 10: keep, change or drop each with a reason.
- The cluster weight line in the skeleton header states major, supporting or additional per cluster from data/standards/ccss-math-focus.csv. Keep it as written (the gate checks it). Supporting work is used to practise major work, and the unit says where.
- The major-work line is at least 65 percent for grades 3 to 8 and 75 percent for K to 2, counted by units, lessons and time (docs/RUBRIC-MATH-K8.md). State the unit's own share.
- Each of the eight practices the frame names for this unit is developed on a named day through a named task, not just listed.
- Understanding, fluency and application each appear where the standards call for them; the skeleton marks days by kind. Fluency days are fluency, not new content.
- Every assessment item names its standard. The answer-key read solves every item cold (BASELINE rule 27), so write keys that can be solved: sample answers, what each wrong answer shows, what to do next.
- A paper path for every task; calculators only after estimating; manipulatives true to the mathematics; household or no-kit supplies named in field 8.
- Personal finance is light touches only where a day already fits.

Settled (do not raise): the readiness check is given before the unit opens, in the last ten minutes of the previous unit's last day or the respond day between the units, a few days ahead at most; unit 1's check, where unit 1 has readiness rows, takes the last ten minutes of day 1 after the hook, and days.csv marks day 1 `readiness` (lead rule 2026-11-14; unit 1's plan defines what it asks and how the teacher uses it); day 1 opens on the hook and the compelling question. Periods are 50 minutes; no timers shown to students; K to 2 assume at most one shared classroom device, always with a paper path. No qualified outside readers exist: agent reads take their place (the answer-key read that solves every item cold, the safety read against published school guidance, the expert's text read, and the sensitivity agent, docs/pipeline/briefs/sensitivity-read.md); name, per unit, what each must study, and for sensitive content the community's own sources first. No day added beyond the frame's totals.

You own only docs/courses/{course}/s*.md (and TOOL-ASKS.md, DEFAULTS.md in that folder if the template asks). Edit no other file. Rules: no em dashes; "Curio Class" in full; no company names in student, teacher or family copy. Blind rule: do not open docs/courses/ela-6/, docs/courses/ela-6-spine.md, docs/courses/math-4/, docs/courses/math-4-spine.md, docs/courses/math-3-5-progression*.md, docs/courses/science-4-spine.md, docs/courses/NEXT-SPINES.md, data/plans/math-4/, data/units.csv, courses/, im-g4-draft-map.csv, or docs/reviews/*reconcile*, *math-4*, *ela-6*, science-4-spine*. No git. Leave no stray files.

Last message (under 250 words): the unit written, decisions the expert should look at, For the lead items.

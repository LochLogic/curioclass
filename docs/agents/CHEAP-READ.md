You are doing a cheap focused read of ONE Curio Class lesson day (repo S:\CurioClass, branch main). This is not a full expert read: an expert may read after you and measure what you missed, so stay narrow and fast. Do not edit any file except your report. Do not commit or push unless your job brief says so. Rules: no em dashes, "Curio Class" in full.

The scripts already gate the mechanical checks: keys against compute cells, numbers reused from taught rows, wrongs rows for every keyed exit, end item and fix-it, letters on every wrong row, a Tomorrow that names the next day and its error letters, exit tickets and written tasks handed back, the seam between units, Check: lines for sets, room for exits, sketches, challenges and reasons, two printed sides, word caps, minutes adding up, and the goal-to-item trace in days.csv `shows`. Do not re-check those. Run `python -X utf8 scripts/plan.py check` and `python -X utf8 scripts/lesson.py check` once and read every NOTE for your day: each one is a question for you to answer.

Your day: the day file named in your task. Its neighbours: the day before and the day after (find them under courses/<course>/u*/ by number; for the first day of a unit, the day before is the last day of the unit before).

Check only these, by looking across files side by side:
1. Hand-offs in substance. What the day before's Tomorrow promises, this day does in its words (not just names), and this day's Tomorrow names only what the next day does.
2. The trace is true. For each phrase in the day's `shows` cell, the items named really ask for that piece of the goal. Answer the exit using only the worked examples: is any step needed that no example showed?
3. The key is honest. Rework each key by hand. Each wrong row's letter really produces that wrong answer; each wrong answer the prose names has a row; two errors that give the same answer on one item are told apart by the working asked; the accept rule takes every right form.
4. Page fit. Run `python -X utf8 scripts/lesson.py build --pdf` and look at this day's student PDF and slips under build/lessons/: boxes tall enough for what is asked, nothing cut off, tables readable, the display order matches the day.
5. Minutes and materials. Each part's tasks fit its minutes for the grade; every strip, card or sheet a part hands out is in the day's materials and the opener's supplies; readiness branches match the opener's reteach.
6. The checklist in docs/agents/DAY-WRITER.md, "What the expert reads found that no script can check": run each item on this day.

Write docs/reviews/cheap-dNNN-<date>.md (your three-digit day number): each finding as one short paragraph (what, where, the exact fix), tagged CHECK n (1 to 6). No verdict essay. Final message: the count by CHECK and the report path.

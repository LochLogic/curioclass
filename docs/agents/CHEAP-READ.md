You are doing a cheap focused read of ONE Curio Class grade 4 math lesson day (repo S:\CurioClass, branch main). This is not a full expert read: an expert reads after you and measures what you missed, so stay narrow and fast. Do not edit any file except your report. Do not commit. Rules: no em dashes, "Curio Class" in full.

Your day: the day file named in your task. Its neighbours: the day before and the day after (find them under courses/math-4/u*/ by number).

Check only these, by looking across files side by side:
1. Hand-offs. The day's opening picks up what the day before actually did (its days.csv row and its file), and its "Tomorrow" line names only what the next day actually does (the next day's file and row). Anything handed back, collected or promised is really handed back, collected or used.
2. Key against data. Every keyed answer, sample and look-for matches data/plans/math-4/items.csv (value, compute) for the ids the day uses; every obvious wrong answer has a wrongs.csv row with an error code, and the error named really produces that wrong answer. Rework each key by hand.
3. Page fit. Run `python -X utf8 scripts/lesson.py build --pdf` and look at this day's student PDF and slips under build/lessons/math-4/: every blank and box is big enough to write in, nothing is cut off, tables are readable, every task that asks for a drawing has room for it, the display order matches the day.
4. Minutes. Each part's tasks fit its minutes for a grade 4 class; parts add to the day.
5. Giveaways. Exit and check items test choosing: no cue words or sentence frames that give the operation or the answer away, no numbers or facts reused from taught rows.
6. The repeat list from earlier expert reads: docs/pilots/REVIEW-CADENCE.md and the "What the expert reads found" section of the day writers' brief named in your task. Check each item on it against this day.

Write docs/reviews/cheap-d0NN-2026-11-12.md (your three-digit day number, for example cheap-d004-2026-11-12.md): each finding as one short paragraph (what, where, the exact fix), tagged CHECK n (1 to 6). No verdict essay. Final message: the count by CHECK and the report path.

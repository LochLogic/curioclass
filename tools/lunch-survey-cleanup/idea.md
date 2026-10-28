# Lunch Survey Cleanup (idea card)

- Module: computer-science-6-8-cleaning-data-honestly, grade 6-8. Codes: MS-DAT-DC-24, MS-DAT-DI-27
- Format / family: data / data-desk. Fit: good, because each cleaning choice changes the table, the chart and who is counted.
- One idea: A middle school's lunch survey (412 rows) arrives with blanks, mixed spellings and doubled rows; pick a fix for each problem (drop, reformat or keep) and watch the result, and the group of students quietly removed by your fixes, change, then write a short report that names your choices and their limits.
- How it plays (solo student by default):
  - First screen: the cafeteria manager's question, "Should we add a hot vegetarian option?", and the raw table.
  - Core loop: a problem list (38 blank answers, "veg", "vegetarian" and "Vegetarian" as three answers, 21 doubled rows from a double-tap). For each, choose drop, reformat or keep; the chart and a "who's in the data" panel update.
  - The catch: most blanks came from the paper version handed out in the English learners' class, whose second page was missing; dropping blanks cuts their voice almost to zero and flips the answer.
  - Report: fill a short report frame (what we fixed, what we dropped, who that removed, what we still can't say).
  - The aha or the end state: cleaning is a set of choices with effects, and an honest report says what the choices did.
- Standards, one line per code:
  - MS-DAT-DC-24: choose a fix for each data quality problem and see its effect.
  - MS-DAT-DI-27: report the result with its biases and limits stated.
- Not like: fair-survey-kit (grade 3-5 planning and simple fixes); catalog-column-rules (grade 9-12 data dictionaries); misleading-charts (grade 6-8 chart honesty).
- Art: drawn in code (table and charts, data-desk engine) with a generated cafeteria header.
- Proposed title: keep
- Proposed concept line: keep
- Flags: overlap risk (fair-survey-kit; kept apart by grade, choices with trade-offs and the written report)

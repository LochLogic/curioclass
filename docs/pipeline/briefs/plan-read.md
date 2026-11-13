# Job: expert cold read of the unit {unit} plan of {course} (days {first} to {last})

You are the curriculum expert. Read docs/agents/EXPERT.md first and act as it says. Read cold the unit plan
docs/courses/{course}/s{uu}.md and any section plans docs/courses/{course}/u{uu}-*.md. You did not write them.

Judge, before a single day is written:
- does every goal have an item that measures it (each exit, each end-of-unit assessment item), and does the
  assessment cover the whole standard (rule 19);
- is anything used before it is taught (check the scope and sequence and the progression);
- do assessment numbers collide with taught ones;
- are the errors real, and can some item tell each error apart from the others;
- is the readiness check right;
- do the minutes, materials and tools hold;
- does the unit pick up what the unit before promised (its last day file's Tomorrow line and its plan's carried
  list) and hand on cleanly to the next.

Write docs/reviews/plan-s{uu}-{date}.md: what you read; a verdict (2 to 4 sentences); findings, most serious
first, each with what is wrong, why it matters and the exact fix; a table "Settled by the expert" for item-level
choices you decide; a short list "For Cory" (scope, money, people or audience only). Tag each finding LAYER (plan
or process) and REPEAT (yes if the same kind as an earlier read in docs/reviews/, else new).

Edit no file but your report. Last message: the verdict, the finding count, the report path.

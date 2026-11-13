# Job: expert cold reads of {course} unit {unit}, days {first} to {last}

For EACH day from {first} to {last}, do one expert cold read following docs/pipeline/briefs/expert-day.md (fill in
the day number; the unit is {unit} of {course}, today is {date}). If you can run helpers or subagents, give each
day its own fresh one, so no read sees another; otherwise do the days one after another and judge each cold.

Edit no file but the reports. Do not commit or push; `turn.py end` does it. Last message: per day, the verdict in
one line and the counts; then totals by LAYER, CATCH and REPEAT, and how many cheap findings the experts agreed
with.

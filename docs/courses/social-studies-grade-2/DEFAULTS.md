# Grade 2 social studies: what holds every day

Generated 2026-11-18 by scripts/defaults.py (later.csv L76) from its band and subject blocks; edit any line that differs for this course and it is kept. A section plan or day writes only what differs from this.

- **The day.** 30 to 40 minutes (frames.csv); teacher prose at most 15 words a minute of the day's own length (600 at 40 minutes).
- **Student page:** at most 150 words a student reads, everything printed included (ours, untested).
- **Children read little or not at all.** The student page is pictures, boxes to draw in and short labels; a line on the teacher page says what to read aloud (in English, the text the day teaches children to read is printed for them). 18 point type.
- **Stems are spoken.** An exit or end item asks one thing, aloud, in a child's words; three asks in one stem are three items. Exit and end items have `path` spoken in items.csv unless the plan names a drawing or a written word the child can make.
- **Turns are counted.** A part where each child takes a turn is children times turn length. The teacher hears a rotating six a day and the record sheet has a column naming who was heard.
- **One marking scale:** shown, shown with help, not yet seen.
- **Stories:** one actor per scene, so a child can say who did what; practice cases are invented and the teacher says so aloud.
- **At home.** 15 to 30 minutes, one grown-up or older child, any day skippable; the exit is asked aloud.
- **Sources are free and checked once for the course** at plan data (status `checked: <date>`); a passage that cannot be checked is cut. A reserved source is never named before its day.
- **Sensitive topics** follow the frame's lines; no student reports on home, family, money, bodies or religion.
- **Repair slots fit what is routed to them.** Every hand-back lands in a named part of its day (handbacks.csv `where`) that holds its minutes; a warm-up holds one repair of at most 5 minutes (plan.py checks).
- **Exits ask a transfer:** a new case that needs the day's idea, not the worked example in new numbers.
- **Talk.** Every student may pass in public talk; no one is the example of a mistake.

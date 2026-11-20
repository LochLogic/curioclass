# Kindergarten science: what holds every day

Generated 2026-11-18 by scripts/defaults.py (later.csv L76) from its band and subject blocks; edit any line that differs for this course and it is kept. A section plan or day writes only what differs from this.

- **The day.** 30 minutes (frames.csv); at most 450 words of teacher prose (15 a minute of the day).
- **Student page:** at most 60 words a student reads, everything printed included (ours, untested).
- **Children read little or not at all.** The student page is pictures, boxes to draw in and short labels; a line on the teacher page says what to read aloud (in English, the text the day teaches children to read is printed for them). 18 point type.
- **Stems are spoken.** An exit or end item asks one thing, aloud, in a child's words; three asks in one stem are three items. Exit and end items have `path` spoken in items.csv unless the plan names a drawing or a written word the child can make.
- **Turns are counted.** A part where each child takes a turn is children times turn length. The teacher hears a rotating six a day and the record sheet has a column naming who was heard.
- **One marking scale:** shown, shown with help, not yet seen.
- **Stories:** one actor per scene, so a child can say who did what; practice cases are invented and the teacher says so aloud.
- **At home.** 25 to 30 minutes on a teaching day, 30 to 40 on an assessment day (the course day's length, as lesson.py checks it), one grown-up or older child, any day skippable; the exit is asked aloud.
- **Shared equipment fits the minutes.** Groups times minutes a turn fits inside the part, or the reading is a demonstration with readings shared. Field 8 of the unit plan sets supply and safety limits; a task they forbid is not written.
- **Real readings, with a fallback.** The class measures where it can; an invented record is the named fallback, said aloud to be invented, and the plan says what happens when a reading fails. Safety notes name the equipment actually used. A reading sits inside the instrument's step (a 1 g scale cannot show 0.7 g), and clean-up (goggle cleaning, handwashing) has its supplies and minutes.
- **Set-ups for later units** take at most 5 minutes of a day and are named as set-ups.
- **Repair slots fit what is routed to them.** Every hand-back lands in a named part of its day (handbacks.csv `where`) that holds its minutes; a warm-up holds one repair of at most 5 minutes (plan.py checks).
- **Exits ask a transfer:** a new case that needs the day's idea, not the worked example in new numbers.
- **Talk.** Every student may pass in public talk; no one is the example of a mistake.

# Grade 2 English: what holds every day

Generated 2026-11-18 by scripts/defaults.py (later.csv L76) from its band and subject blocks; edit any line that differs for this course and it is kept. A section plan or day writes only what differs from this.

- **The day.** 120 minutes (frames.csv); at most 1,800 words of teacher prose (15 a minute of the day).
- **Student page:** at most 150 words a student reads, everything printed included (ours, untested).
- **Children read little or not at all.** The student page is pictures, boxes to draw in and short labels; a line on the teacher page says what to read aloud (in English, the text the day teaches children to read is printed for them). 18 point type.
- **Stems are spoken.** An exit or end item asks one thing, aloud, in a child's words; three asks in one stem are three items. Exit and end items have `path` spoken in items.csv unless the plan names a drawing or a written word the child can make.
- **Turns are counted.** A part where each child takes a turn is children times turn length. The teacher hears a rotating six a day and the record sheet has a column naming who was heard.
- **One marking scale:** shown, shown with help, not yet seen.
- **Stories:** one actor per scene, so a child can say who did what; practice cases are invented and the teacher says so aloud.
- **At home.** 15 to 30 minutes, one grown-up or older child, any day skippable; the exit is asked aloud.
- **Core texts are written or checked before days.** A text still "to write" stops the day skeleton; the day writer never writes one.
- **A cold check reads a new text,** not one taught, and does not restate the taught text's central idea.
- **Reading fits the minutes:** about 120 words a minute in class alongside the day's other parts; more goes to a read-aloud or home reading, named. Content notes name what the texts contain, not only the topic.
- **Repair slots fit what is routed to them.** Every hand-back lands in a named part of its day (handbacks.csv `where`) that holds its minutes; a warm-up holds one repair of at most 5 minutes (plan.py checks).
- **Exits ask a transfer on the day's text:** a reserved passage or an unread part of the unit's own texts that needs the day's idea, never a card invented for the exit and never the worked passage. A Goal map's "new passage" or "fresh passage" means such a passage, unless the plan names a cold assessment text in ela-texts.csv. An item on an invented card has needs_text no (cold-read fix 2026-11-24).
- **Talk.** Every student may pass in public talk; no one is the example of a mistake.

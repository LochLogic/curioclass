# Job: write the section plans of unit {unit} of {course}

Written 2026-11-17 for the kindergarten social studies probe (PRODUCTION-PATH step 7, "How section plans are
authored", with a Sonnet writer while Codex is out of quota). One run writes every section of one unit, so the
shared context is loaded once and the handoffs between sections are seen together.

## Read, in this order

1. AGENTS.md (the rules for every worker), then docs/GLOSSARY.md only for a word you are unsure of.
2. docs/courses/UNIT-PLAN.md: "The rules", "The section plan: fields, in order", "Length" and "Blank copy: section
   plan". These are the rules card; nothing else defines a section plan.
3. The unit plan docs/courses/{course}/s{uu}.md, whole.
4. The skeletons docs/courses/{course}/section-skeletons/u{uu}-*.md. Every line between `<!-- skel -->` markers is
   data: copy it into the plan as it stands (it does not count toward the cap). Every `TODO(writer)` is yours.
5. For shape only, one finished section plan from another course: docs/courses/world-history-i/u03-4.md. Do not
   copy its content or its length; it is a high school section.
6. The course frame docs/courses/{course}/frame.md: only the row and notes for unit {unit}, and its Sensitive
   topics lines.

Do not open: anything under .claude/, docs/Return/, S:\CurioClass-spec2, data/closet/words, closet/words,
data/media-manifest.txt, courses/math-4/, docs/courses/math-4/, docs/courses/ela-6/, data/plans/math-4/,
*-spine.md, data/units.csv, or any file with math-4 or ela-6 in its name.

## Write

One file per section, docs/courses/{course}/u{uu}-{n}.md, in the fields of the blank copy, every TODO filled.

- **Defaults first.** docs/courses/{course}/DEFAULTS.md says what holds every day (minutes, caps, type size, exits,
  At home). A section plan writes only what differs from it.
- **Kindergarten first.** Children do not read yet. Evidence is spoken, drawn, pointed to, sorted or acted out and
  seen by the teacher; an "exit question" is asked aloud with picture cards, and its wrong answers are what a
  five-year-old actually says. Days are 20 to 30 minutes; the `- **N min. Part.**` lines must add up inside that.
- **Read-alouds are ours.** The unit plan names original picture read-alouds and picture sequences (field 10).
  Name them as it does; never name, quote or depend on a copyrighted picture book. A public-domain folktale may be
  named with its source.
- **Sensitivity.** Homes, families, money, bodies, religion and names differ. No child is asked to report on home,
  share about themselves in public, or be the example of a mistake. Follow the frame's Sensitive topics lines.
- **Rule 4:** no taught case, number or picture reappears in an exit or check.

## Rules from the probes (2026-11-18; each one a fault found in every subject so far)

1. **A repair slot fits what is routed to it.** Every hand-back, retry and error repair sent to a day lands in a
   named part of that day (handbacks.csv `where` is a word of the part's name) whose minutes hold all of it. A
   warm-up holds one repair of at most 5 minutes; more gets its own "Return and repair" part. When the receiving
   day is in the next section, give that day the slot too. An error letter's `if_many` minutes fit the slot it
   names. `plan.py check` fails a planned day whose part cannot hold its hand-backs.
2. **Shared equipment fits the minutes.** Count it: groups times minutes a turn must fit inside the part. One scale
   for six groups in 11 minutes does not; add stations, make it a demonstration with readings shared, or widen the
   part. The same holds for one reading per child (a shadow stick, a turn at a tool) and for a teacher who must hear
   each child.
3. **Real readings, with a fallback.** Where the class can measure, it measures. An invented record is the named
   fallback, said aloud to be invented, and the plan says what happens when a reading fails (no gain on a
   whole-gram scale, a cloudy day). Safety notes name the equipment actually used.
4. **Notation and terms are taught before they are tested.** No exit, check or At home asks for a symbol, rule
   form or term before the day that teaches it, across section edges too.
5. **Exits ask a transfer.** An exit is a new case that needs the day's idea, not the worked example again in new
   numbers.
6. **Set-ups for later units** (soil to dry, a plant to grow, a monthly reading) take at most 5 minutes of a day
   and are named as set-ups, so the day's own storyline holds. Start one only as early as its lead time needs.

Added after the confirm probe (L78, docs/reviews/probe-confirm-2026-11-18.md):

- Rule 3 also means **a reading inside the instrument's step**: a 1 g scale cannot show a 0.7 g change. Name the
  instrument's step beside each planned reading; where it cannot resolve the change, the reading is a demonstration
  on a finer instrument or the invented record is the plan, said so.
- Rule 2 also covers **clean-up**: goggle cleaning, handwashing and spills have supplies named and minutes counted
  (thirty students at two sinks is not two minutes).

English, in addition:

11. **Content notes name what the texts contain** (death, execution, violence, slavery, racism, religion, abuse,
    addiction, slurs left out), not only the topic the unit is about.
12. **Reading fits the minutes:** about 120 words a minute read in class, alongside the day's other parts. More goes
    to a teacher read-aloud or home reading, named.
13. **One word, one sense at a time:** a word the day checks in one sense, which a text the class reads uses in
    another, gets a line saying so.
14. **A passage used on several days keeps its terms:** states, implies and suggests mean the same on every day.

Kindergarten to grade 2, in addition (kindergarten probe, L74):

7. **Stems are spoken.** An exit or end item asks one thing, aloud, in a child's words; three asks in one stem are
   three items or one.
8. **Minutes are counted as turns.** A part where each child takes a turn is children times turn length; "five
   groups of six, two minutes a group" in a 10-minute part does not fit. Hear a rotating six a day, with a record
   column naming who was heard.
9. **One marking scale** per record: shown, shown with help, not yet seen. Do not mix it with points or
   "insufficient evidence".
10. **One actor per story scene,** so a child can say who did what; a puppet speaks one line at a time.
- **One wrong answer, one letter.** Each wrong answer is tagged with exactly one error letter from the unit's register.
- **Caps:** 1,600 words per section plan, not counting fields 3, 4 and 6 (UNIT-PLAN "Length"; cut in its order).
- No em dashes. Write "Curio Class" in full if you name it. No company or product names in teacher-facing text.
- Where the unit plan is wrong or silent, decide, write it in the section plan, and list it in your report under
  "Plan points". Do not edit the unit plan, days.csv or any other file.

## Gates

`python -X utf8 scripts/unitplan.py check {course}` must pass for your files (the caps and the letter gate).
Search your files for "TODO(writer)" and for the em dash character: none may remain.

Do not commit or push. Last message (under 250 words): files written with word counts; plan points you decided;
anything a reader should look at first.

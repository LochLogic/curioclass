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

- **Kindergarten first.** Children do not read yet. Evidence is spoken, drawn, pointed to, sorted or acted out and
  seen by the teacher; an "exit question" is asked aloud with picture cards, and its wrong answers are what a
  five-year-old actually says. Days are 20 to 30 minutes; the `- **N min. Part.**` lines must add up inside that.
- **Read-alouds are ours.** The unit plan names original picture read-alouds and picture sequences (field 10).
  Name them as it does; never name, quote or depend on a copyrighted picture book. A public-domain folktale may be
  named with its source.
- **Sensitivity.** Homes, families, money, bodies, religion and names differ. No child is asked to report on home,
  share about themselves in public, or be the example of a mistake. Follow the frame's Sensitive topics lines.
- **Rule 4:** no taught case, number or picture reappears in an exit or check.
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

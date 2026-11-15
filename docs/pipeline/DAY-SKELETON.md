# The day skeleton: a design note (2026-11-15, not built)

One page, written while the unit skeletons ran. No code yet. The day skeleton is built after social studies has
section plans (PRODUCTION-PATH step 7), and it is proven on social studies first, as the unit skeleton was.

## What it is for

The unit skeleton (scripts/unit_skeleton.py) fills every mechanical field of a unit plan and marks every judgment
field, so a writer spends its tokens on judgment. A day skeleton does the same for one teaching day
(docs/courses/LESSON-DAY.md): it writes the parts of `courses/<course>/u<unit>-<section>/d<day>.md` that the data
already decides, and leaves marked holes for the rest.

## Filled from data (never by a writer)

- **The header block:** day, course, unit, section, kind, version ("draft, not yet taught"), the codes and the parts
  of each code the day owes (days.csv and the section plan), `materials` and `print` (tools and supplies columns),
  `leans_on` (the tool, the section opener, sheets from other units, by path, with "when it exists:" for pieces not
  built yet), and `credit` (source-map.csv: the base lesson adapted, if any; nothing when the day is "ours").
- **The time frame:** one `### N min.` heading per part of the section plan's row for the day; the minutes add up
  to the day (LESSON-DAY rule 2) before a writer sees it.
- **Earlier rows:** the retrieval or readiness line for each earlier-grade row the day touches, counted exactly as the
  unit skeleton and the scope gate count it (one-hop "used"), with the row id named.
- **Assessment days:** the codes sampled and the parts, the record each check reuses from the last ten days (Collect
  once), and which task forms the last two weeks already gave.
- **Words and supports:** the section plan's key words with their Word Wall ids; access notes the section names.
- **Fixed blocks:** Other rooms (only when a tool or projector is named), At home (heading and the word cap), Shorter
  or longer, Tomorrow (the next day's goal is printed beside it), and a science safety line from the safety column.
- **Question ids:** an `[[id]]` placeholder for each items.csv row that already exists for the day.

## Left to the writer (marked, never guessed)

The teaching moves, the goal in student words, the worked examples and their numbers, every question row with its
computed key, the At home block itself, what to cut and the extension, what the exit tells the teacher, how a
sensitive topic is handled, and any timer (only with a grounded purpose).

## Lessons from the unit skeleton round (carry over)

1. **Gate the data before the skeleton reads it.** 21 source maps in 21 layouts crashed the first run; the fix was
   one layout, gated by sequence.py. The day skeleton reads parts.csv and items.csv only after plan.py passes them.
2. **One shared core, a small adapter per subject,** and the first subject's output frozen: every change is diffed
   byte for byte against the social studies baseline.
3. **Clear data errors, never tracebacks**: the message names the file, the line and what is wrong.
4. **A self-test on synthetic data** (`--data-dir`), so test rows never sit in data/plans.
5. **Count the same thing in one place.** The scope gate, the unit skeleton and the day skeleton share one rule 2
   function; a second copy drifts.
6. **Never overwrite** a written file without `--force`; a change to the script reaches new skeletons only.
7. **Pilot one course, then run the rest.** The skeleton exposes faults the reads miss; it should meet them on one
   course, not 37.

## Open until it is built

- Whether the skeleton fills the day file itself or a sidecar the writer copies from (the day file holds prose the
  writer owns; a sidecar keeps regeneration safe).
- How a day already written learns of a section plan change (most likely a check that lists stale days, not a
  rewrite).

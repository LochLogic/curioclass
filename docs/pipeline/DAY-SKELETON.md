# The day skeleton: a design note (2026-11-15, draft built)

One page, written while the unit skeletons ran. A living draft, scripts/day_skeleton.py, was built the same day (Cory:
a file that exists early gathers improvements before its first real need). It is not yet a production step: it is
proven on social studies once section plans exist (PRODUCTION-PATH step 7), then frozen there, as the unit skeleton was.
Each run, review or new lesson that touches day writing adds a line under "Draft log" below and, where it is a rule,
a change to the script.

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

## Draft log

- 2026-11-15, draft v0: writes a sidecar, docs/courses/<course>/day-skeletons/d<nnn>.md, never the day file (decided:
  regeneration stays safe and the writer's prose is never touched). Fills the header (day, unit and section, frame
  title and question, kind, assessment, minutes, calendar, tools, supplies, safety, leans_on, credit from source-map
  rows), the goal and note, skills marked own or earlier-grade review, codes in our words with the `~` mark kept, an
  Assessment block (taught-before days and Collect once, the unit skeleton's own functions), the nine teacher-page
  parts in LESSON-DAY order with the next day's goal under Tomorrow, and items.csv or parts.csv rows when a section
  plan has them. Self-test: 8 checks. Tried on us-history-i day 71 and science-grade-4 day 36.
- 2026-11-15, Cory on long day notes (ELA kindergarten to grade 2 most of all): a days.csv note may run long, since it
  is the writer's input; the teacher page does not. The day writer turns the note into the page's parts and keeps only
  what the teacher needs in the room, unless a length has a real need (a safety step, a station rotation). The
  sidecar prints the note for the writer only; the teacher page never copies it.
- 2026-11-15, from the template flattening: parts are `#### N min.` under `### The day` and At home is capped at 170
  words, as lesson.py reads them; the draft had `###` and 130. Lesson: read the script's constants, not prose.
- 2026-11-16, the nine findings built in (Cory: "integrate the findings we have into the code; we can repeat that step
  again later"). A **Before writing** block at the top lists STOPs (the day is not written until the data clears them;
  the command exits 1) and warnings. STOPs: an ELA core text still "to write"; a source on the day that is not
  checked or has no link (one we make needs no link); an item with no key, computed answer or samples; carried scored
  work with no written feedback day before it, or made on the first day its code is taught. Warnings: open `lead` rows
  of unit-rejections.csv; a days.csv note naming something "to write". A data error stops the build when an end or
  mid item in items.csv sits on a day days.csv gives no assessment, or a days.csv end day holds no end item. Printed:
  what the day kind means; unit field 8 (supply and safety limits) on science days and days with tools, supplies or a
  lab; the hook and worked example beside the exit, with "a new case, not this one in new numbers"; the cold-check
  rule on assessment days; each item's key and samples; the day's sources (link, rights, status) and the reserved
  sources it must not name; `endlooks` when end items are teacher-judged by look-fors; and the checks the written day
  must pass (prose cap at 15 words a minute, 500 on an assessment day unless it scores carried work; glosses; the
  respond-day line; a key per rotated form). Self-test 15 checks, the new ones on a copy of the World History I probe
  data with planted faults. Built every day of all 52 core courses to scratch: no crash.
- Lessons from that run: (1) materials.csv `per` counts copies (student or class), not authorship, so "made the same
  day it is scored" cannot be told apart from a handout; the rule covers carried work only (made on an earlier day).
  (2) The unit plans' field 5 tables are too varied to parse for scored days (item numbers and source years read as
  days); the scored-day check reads items.csv, which only section plans fill. (3) The all-courses run found a broken
  Algebra I source-map row (an unquoted comma from a hand edit that day) that `plan.py check` passed: sequence.py
  does not check a source map's cell count (later.csv L65). (4) ELA has a STOP on most days (core texts still to
  write, L58); ELA grade 11 has none.
- Lessons from the kindergarten probe (2026-11-18, docs/reviews/probe-social-studies-3-2026-11-18.md): (1) the
  skeleton STOPs on a source whose status is not "written" or checked, which our own read-alouds tripped until
  sources.csv said "written: <path>". (2) Spoken exits need `path` spoken, or the skeleton plans a paper ticket a
  five-year-old cannot read. (3) Another day's exit cannot be named as [[id]]; the skeleton should print it in words.
  (4) Skeleton minutes came from the frame minimum (20); kindergarten content needed 30, so minutes should come from
  the section plan's `## Day N` block. (5) "Scored from the work you handed in" and the write-nothing line belong on
  the teacher page only for grades whose children do not read (later.csv).
- Known gaps for the first real run: the student page and At home are bare TODOs; the readiness check on a unit's last
  day is not yet split out from the day's own assessment; no word list (Word Wall cards per day) is read yet; no check
  yet compares a written day against its sidecar.

## Findings to build in

Day-level lessons from the reads, for the skeleton to fill, print or check before a writer starts. Each review that
finds something about days adds a line here (the probe reports, the unit loop's sample reads).

All nine below were built in on 2026-11-16 (Draft log). A new finding is added here marked `(open)`, and marked
`(built in <date>)` once the script carries it.

- **Scored work** (built in 2026-11-16; both probes; unit loop known-fault test, 2026-11-16): for each scored part the Assessment block
  prints the day the work was made and the day of its written feedback and revision; a part made the same day it is
  scored, or on its first teaching day, fails the skeleton (UNIT-PLAN field 5).
- **Scored day agrees with days.csv** (built in 2026-11-16; sample read 2026-11-16, math grade 7 unit 5): the skeleton checks the section
  plan's scored day against days.csv and stops with a clear data error when they disagree.
- **Fresh exits and cold checks** (built in 2026-11-16; probe 2; sample read, ELA grade 8 unit 3): print the day's hook and worked example
  beside the exit hole, with the line "the exit is a new case, not this one in new numbers"; a cold check's text may
  not restate the taught text's central idea or reuse its key teaching words.
- **Day kinds** (built in 2026-11-16; sample read, math grade 2 unit 3): print what the kind means (a Fluency day practises, no new
  content; an Application day applies taught work), so a day is not quietly turned into an assessment.
- **Supplies and safety** (built in 2026-11-16; sample read, science grade 7 unit 2): print field 8's supply and safety limits beside each
  investigation or build, and the cost line; a task the limits forbid is a data error, not a writer's guess.
- **Texts not yet written** (built in 2026-11-16; sample read, ELA grade 4 unit 2 and grade 8 unit 3): a core text marked "to write" is a
  blocker printed at the top of the sidecar (later.csv L58), never a hole for the day writer to fill.
- **Keys, samples and source sheets** (built in 2026-11-16; probe 2: most unit-origin findings sat here, written at plan-data): the
  skeleton lists each item's key and sample with its source row, so the answer-key read after plan-data (L56) and
  the writer see the same thing; a sheet passage needs a sources.csv row with a link and a checked status.
- **Probe 2 check lines** (built in 2026-11-16; fix-u03-4): the teacher-prose cap per minute of the day, which an assessment day that
  scores earlier work takes from its teaching minutes; a reserved source never named before its day; `endlooks` on
  the record sheet; a key for each rotated form; glosses only for words the day uses; "Scored from the work you
  handed in" on a respond day.
- **Open lead items** (built in 2026-11-16; data/plans/unit-rejections.csv rows ruled `lead` and not applied): printed as warnings on every
  day of that unit until the calendar fix lands.

## Open until it is first used

- How a day already written learns of a section plan change (most likely a check that lists stale days, not a
  rewrite).
- 2026-11-15, first real run (us-history-i days 78 to 82, the social studies probe): parts.csv is the standards'
  parts (code, part, verb), not the day's timed parts, and items.csv keys rows by `item_id`, so v0 raised a DataError
  once real plan data existed. Fixed: the day's parts come from the section plan, docs/courses/<course>/u<uu>-<s>.md,
  the `- **N min. Name.**` lines under `## Day N`, with their sum checked against the frame's minutes; questions are
  listed by `item_id`; leans_on names the section plan and the section opener (courses/<course>/u<uu>-<s>/opener.md)
  when they exist; a day whose source-map rows are all `ours` gets the credit "all ours". Self-test still passes.

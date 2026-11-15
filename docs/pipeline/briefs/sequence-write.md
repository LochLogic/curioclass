# Job: write the scope and sequence of {course}

Added 2026-11-14 (PRODUCTION-PATH step 3; baseline 1 structure finding 2). A scope and sequence sets every course day
of a course in order, by unit: what each day is for, its kind, the skills and standards it carries, and where the
assessments fall. It starts from the course frame and changes none of the frame's units, owned rows or day counts.
It writes no items, answer keys, section plans or lessons: unit plans (step 4) and section plans (step 7) do. Social
studies goes first; the other subjects follow in step 5.

## Read first (in S:\CurioClass)
1. AGENTS.md; docs/PRODUCTION-PATH.md steps 2 to 4; docs/GLOSSARY.md (unit, course day, school day, week,
   course-level check, readiness check, retrieval task, mid-unit assessment, check set, lean, bridge).
2. The frame docs/courses/{course}/frame.md, all of it, and its row in data/plans/frames.csv.
3. The school calendar docs/courses/CALENDAR.md, and data/plans/calendar.csv for this course's grade (every
   subject's units and course-level checks, by week).
4. The progression rows the course owns and the rows of the grade before and after (data/progressions/{subject}.csv).
5. The subject lens docs/agents/lenses/{subject}.md and the subject's bar: {bar}
6. The frames of the other three subjects in the same grade: their Cross-subject sections and the units that teach
   what this course leans on.
7. The expert's read docs/pipeline/briefs/sequence-read.md: write to pass it.
8. {extra}

## The files
- `docs/courses/{course}/scope-and-sequence.md`: `# Scope and sequence: <title>`, one line (course id, grade,
  draft), then per unit a short section: the unit's days on the calendar (course days and weeks), its arc in a few
  sentences, why the days fall in this order, the readiness, mid-unit and end-of-unit assessment days and what each
  covers, and each "Candidate:" check-set cell settled (kept with its day cost inside the unit's days, or dropped
  with the reason). Then the course-level checks, with their weeks, and a "Shorter path" section (rule 10). Prose
  for judgment only; the days live in the CSV.
- `data/plans/{course}/days.csv`, one row per course day, columns in this order:
  `day,stretch,unit,kind,goal,skills,codes,assess,school_day,note`
  - **day**: 1 to the frame's total, in order, none skipped.
  - **stretch**: the unit number (the code name lags, GLOSSARY), or `C` for a course-level check day, its respond
    days and course-level review days.
  - **unit**: the section, as `<unit>.<n>` (`3.2`), where the scope and sequence already splits a unit into sections;
    otherwise `<unit>.1`. Blank on a `C` day.
  - **kind**: `Understanding`, `Fluency`, `Application`, `Check` or `Respond`, in every subject. The goal says the
    activity (an inquiry, a lab, a source reading, a discussion, a draft); there are no other kinds.
  - **goal**: what the day is for, in a short teacher sentence ("I can" lines come with the unit plan).
  - **skills**: the skill_ids the day teaches or assesses, `; `-separated. Every owned skill is on at least one day
    of its unit.
  - **codes**: the standard codes the day carries, lettered parts by their own code (RL.4.1a). Every owned code is on
    at least one day.
  - **assess**: `readiness`, `mid`, `end`, `course`, `observe` (K to 2 only, an observation task standing for the
    end-of-unit assessment) or blank. This reserves the slot and says its purpose; the unit plan writes the items.
  - **school_day**: blank for a course that meets every school day (course day n is school day n). A course meeting
    fewer days a week fills it, so its days sit on the weeks CALENDAR.md gives.
  - **note**: a bridge, a lean's timing, a sensitivity flag, a base-text lesson range.
  - **Optional columns after `note`, math and science only** (added 2026-11-14): `day,...,school_day,note,tools,supplies,safety`.
    Social studies and ELA files do not have them and are never checked for them. Each cell is a `; `-separated list
    ("ruler; protractor"), empty when there is none; no empty item, no trailing semicolon. They feed the unit plan's
    field 8 (UNIT-PLAN.md, tools and supplies across the unit) and the skeleton's tools and supplies lines.
    - **tools**: the digital or drawn tools the day uses, by the name the tools file uses (a simulation, an applet, a
      drawing or construction tool, a calculator). Physical objects go in supplies, not here. Math fills it on every
      day that uses a tool; a day with none leaves it empty.
    - **supplies**: the physical things students handle that day (counters, paper, a ruler, a beaker), each named
      once with its kind, and "household stand-in" or "no-kit" in the item where that is the plan. Math fills it on
      every day that needs more than pencil and paper; science fills it on every hands-on day.
    - **safety** (science fills; math leaves empty): for every day that names supplies, the hazard and its control
      ("hot plate: teacher-only; goggles on"), several hazards separated by semicolons, or the single lower-case word
      `none` when the day was weighed and has no hazard. Empty means not yet weighed, and the gate fails it on a day
      with supplies. Eye protection and teacher-only steps go here, in the words of the frame's safety column.
    - What the gate checks: the cells are well-formed lists; a science file with `supplies` also has `safety` (and the
      reverse); every science day with supplies has `safety` filled (`none` counts; any other case of the word `none`
      in a list fails). days.csv has no hands-on marker, so the gate cannot know a hands-on day with no supplies
      listed: it notes a science day whose goal or note reads like hands-on work (lab, investigate, build, heat) but
      names no supplies. A science file with none of the three columns gets a note, not a failure.

## The rules
1. **Units stay as the frame sets them.** Same order, same days, same owned rows. A unit that does not fit goes under
   "For the lead" with the fix, never quietly resized.
2. **Every unit closes with an end-of-unit assessment inside its days** (K to 2: an observation task over the unit's
   last lessons may stand for it), and the plan names its response time once: in the same day or on a respond day.
   **A unit over 25 days also holds a mid-unit assessment** inside its days (where a base text has its own, use it).
   **Readiness or retrieval** (settled 2026-11-14 for all 15 social studies courses; frame-write lesson 16 uses the
   same words): a row used the year before, or earlier the same year, opens as a retrieval task inside a day; every
   other earlier-grade row the unit assumes (last used two or more grades back) gets a readiness check. **When**
   (Cory, 2026-11-14, one timing in every course): before the unit opens, so its results shape day 1, in the last ten
   minutes of the previous unit's last day, or of the respond day or course-level check respond day where one sits
   between the two units; a few days ahead at most, never weeks. That day carries `assess` = `readiness`, or, if it
   already holds another assess value, keeps it and its note says "plus the next unit's readiness check (10
   minutes)". Unit 1's check, where unit 1 has readiness rows, takes the last ten minutes of day 1, after the hook,
   and day 1 carries `assess` = `readiness` (lead rule 2026-11-14; sequence.py accepts it). Every other unit's first
   day never holds a readiness check: it stays clean for the hook and the compelling question.
   The rows a readiness check samples for the next unit are named by id in that day's note, never in its `skills`
   column: `skills` holds only what the day's own unit works on (lead rule 2026-11-15; the skeleton reads an
   earlier-grade id in `skills` as a row of the day's own unit).
   **Count by grade number, and this rule wins over the frame's wording** (lead, 2026-11-14, after nine science
   reads found three readings): a row last used in grade g gets retrieval in grade g+1 and a readiness check in grade
   g+2 or later. "Idle two or more grades" in a frame means the same thing, never "two grades in between". A row
   counts as used only where a day of that grade's scope and sequence teaches or assesses it, not where it is
   "revisited" or "kept in use" in passing. One hop also counts (lead, 2026-11-15): a day that teaches a row whose
   progression `assumes` names the earlier row uses that row too, since it builds directly on it; a day noted as retrieval or
   readiness counts this way only where its kind is Understanding or Application. The skeleton (scripts/unit_skeleton.py) and the scope gate count it
   this way. List every earlier-grade row with its last-use grade and its treatment
   before you place a day.
   **End days:** where one end day would ask for full performances on two or more expectations, spread them over
   the unit's last days (no day added), and run whole-class performances in small groups where the day is short.
   In math a full performance is an extended task (multi-step with an explanation, or a modeling task); an end day
   holds at most one, plus short items for its other codes. Every year-end check samples each fluency standard
   directly, as a short independent station with no supplied work (not inside a critique). Source-map decisions use
   only keep, split (one base lesson over two or more days), merge, cut, ours.
   **Checks claim only what they sample:** a check day lists the codes it actually samples, never the whole unit
   or year, and a code is assessed only after a day teaches it. A retrieval opening is practice, never check evidence.
   **Collect once** (lead, 2026-11-15, after the same fault in all six ELA K to 5 courses): evidence gathered child
   by child (a one-to-one reading, a conference) is taken once per assessment window. A course-level check or end day
   within ten days of it reuses that record and says so; it never collects the same evidence again. A course-level
   check never repeats a task form given in the last two weeks.
   **Our words** (lead, 2026-11-15, after math grade 1 copied 140 base lesson purposes): every goal, note and
   source-map cell is written fresh in Curio Class words. Never copy or lightly edit a base text's lesson purpose,
   learning goal, title sentence or teacher note, even where its licence allows it. **Class size:** minute budgets for
   one-to-one or small-group evidence plan for 30 students.
   **Math leans in other subjects** (lead, 2026-11-15): students take math every year, so a lean on a math row opens
   with retrieval by default. It gets a readiness check only where a performance expectation rests on it and no math
   course uses the row after its grade; where a math course of the same year (Algebra II beside physics) checks or uses
   it first, the other subject retrieves it, and where the other subject uses it first, it gives the readiness check.
   **Each part of each code:** every observation, end-of-unit and check task asks about each part of each code it
   lists (a short prompt per part; no day added); a product or an observed performance may stand for a code where
   the day says so.
3. **Course-level checks** come from the frame's Course-level checks table: `C` days after the unit it names, each
   followed by at least one respond day, review days where the table has them. **A course-level check right after a
   unit's end-of-unit assessment draws its items for that unit's skills from earlier units**, so it does not repeat
   the assessment just given; the scope and sequence and the day's goal say so.
4. **The calendar and the stagger rule** (docs/courses/CALENDAR.md): place the course-level checks on the target
   weeks given there. K to 5: no week holds two subjects' check days. K to 2: the ELA and math one-to-one checks are
   at least five school days apart. 6 to 8: no school day holds two subjects' mid-year checks. If a target week
   cannot be met, use the tools in CALENDAR.md's order (meeting days, split review, the other side of a unit) and
   say so; never move a unit.
5. **Leans on the calendar.** Each same-year lean in the frame's Cross-subject section is checked against the other
   subject's days in data/plans/calendar.csv: where the other subject teaches it later, the day carries the bridge
   from the frame's "if later" line, and its time is inside the unit's days.
6. **Candidate cells are settled here**: each "Candidate:" check-set addition is kept (with the days it costs, inside
   its unit) or dropped (with the reason).
7. **Days by load.** Weigh each owned row's notes; a unit's teaching days follow its load, not equal shares.
8. **Base texts:** where the course has one, write data/plans/{course}/source-map.csv (one row per base lesson, the
   course unit and day it lands on, keep, split, merge, cut or ours, with the reason for a cut); a source-map row may
   name a unit before its sections exist. **One layout in every subject** (lead, 2026-11-15, after the reads found a
   different layout in each map; sequence.py gates it), columns in this order:
   `source,title,goals,standards,unit,days,decision,why,order_conflict,harms_learning`, then `url` if wanted.
   `source` is the base lesson's own id (IM G3 U2 L5, EL G4 M1 U1 L6, OSE 7.1 L3), or `ours` for a day with no base
   lesson; `title` is the base lesson's title, short; `goals` and `standards` are the base lesson's, in our own words;
   `unit` is the course unit (`3` or `3.2`); `days` the course days it lands on (`12`, `12-13`, `12; 14`), blank only
   on a cut; `decision` one of keep, split (one base lesson over two or more days), merge (two or more base lessons
   on one day), cut, ours; `why` the reason, required on a cut; `order_conflict` where our order differs from the
   base's, with `harms_learning` yes or no and why. Days that adapt no base lesson never carry "Base" in their goal
   or note.
9. **Sensitivity:** a day with content the frame flags names it in the note column; the sensitivity agent's read
   (docs/pipeline/briefs/sensitivity-read.md) comes with the unit plan.
10. **A shorter path.** The scope and sequence has a short "Shorter path" section (FOUNDATION section 5, adoption
    bar C2): how the days hold on a shorter period, and a year about 10 days short, by named fold-in days (days whose
    work folds into a neighbour, nothing assessed and no owned part cut). Each fold-in day names the minutes
    it saves, and the section states its total against the frame's day count (lead, 2026-11-15, one rule for every
    subject).
11. No em dashes; "Curio Class" in full; no company names. Edit only your files. No git.

## The gate
Run `python -X utf8 scripts/sequence.py check {course}` (also run by `python -X utf8 scripts/plan.py check`): days
numbered in order, the frame's total and each unit's days, `stretch` in 1 to the unit count or `C`, the five kinds,
an end-of-unit assessment per unit, a mid-unit assessment in units over 25 days, a respond day after each
course-level check, each `readiness` day on the previous unit's last day or a respond day at most 3 days before a
unit's first day and never on a first day except unit 1's day 1, every owned skill placed, every owned code placed (a note), the .md file present, not empty, with
its title and a section per unit, and a "Shorter path" section (a note). Then run
`python -X utf8 scripts/frame.py calendar` and say in your last message whether your course breaks the stagger rule.

Final message, short: units and days, the check weeks, the gate result, the Candidate cells settled, the "For the
lead" items, what you were unsure of.

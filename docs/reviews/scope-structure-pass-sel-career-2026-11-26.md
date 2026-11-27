# Structure pass: SEL STANDARD, career shared cards, rule 2 counting (lead, 2026-11-26)

The lead applied the structure picks left by docs/reviews/scope-group-sel-fixes-2026-11-26.md and
docs/reviews/scope-group-career-fixes-2026-11-26.md (finding 3), and SEL read finding 13. Rules: build/scope-writes/GROUP-FIX.md.
No unit moved, no day count or owned row changed, no id or row position changed. CSV files were edited with the csv
module, only the named rows spliced back, quoting and line endings kept (checked row by row against copies). Health and
PE files were not edited. No git.

## A. SEL STANDARD (docs/courses/sel/STANDARD.md)

- **Section 7, Shared steps.** Rewritten as one row per band, in the words the SEL courses now use:
  - K to 2: the calm-down, I-statement, talk turn (with grade 1's reply step) and goal steps rows as before; grade 2's
    "I hear ___; I think ___ because ___" is named as a separate disagree frame used beside the talk turn card, not a
    step of it; refusal as the course teaches it (say no with a reason, then offer something else; the second push says
    it again, moves away and tells, health's young boundary steps).
  - Grades 3 to 5 (new): calm-down four steps with three body tools; talk turn four steps; the I-statement with
    "because"; goal steps four steps from grade 3; refusal in health's words, "give a reason or none", and "if it comes
    again: say it, say it again, move away, tell".
  - Grades 6 to 8: the goal steps card keeps its four steps through 6 to 8 and grows only in 9 to 12; refusal's three
    options keep the second push.
  - Grades 9 to 12: the second push is carried from grades 3 to 8, retrieved, not added.
  - Career education (part B).
- **Section 3.** The grade 6, 7 and 8 rows take the SEL 6 to 8 scope's titles (sub-skill lists unchanged, checked by
  script); the health-adjacent list names "Calm and careful" and "Pressure and invitations"; grade 7's main year for
  SA6 and SO6 is "Fair and checked"; one line says the table's titles are the courses' own.
- **SEL 6 to 8 frame.** The Units table takes the same 18 titles, and its three "STANDARD section 3" citations match.
  The 3 to 5 frame's handed-on table names the 6 to 8 units by the new titles (6 cells).
- **Section 5.** Item 8, Cultural picks: the frames' line, with K to 2's two places.
- **Section 2.** A bullet: an owned code not sampled on a course-level check is assessed by its own unit's end-of-unit
  assessment, rule 3's named reason; the two-sample cap stays.
- **K to 2 course.** Days 131 and 135 (goal) and the scope's unit 15 line now say the disagree frame is used beside the
  talk turn card.

## B. Career shared cards (career read finding 3)

- **STANDARD section 7, Career education row.** Career's plan page writes its goals on the band's goal steps card
  (6 to 8 four steps, 9 to 12 the designed plan); career adds only the near and far pair and the dated check. The
  decision steps card is stop-think-choose grown for career choices, with the mapping: name the choice is the stop;
  list options, weigh and choose are the same steps, the reason written at choose; gather facts (dated sources) is
  career's added step; check later is SEL 9 to 12's look back. Where SEL ran, the career day retrieves the card and
  teaches only the added steps.
- **data/progressions/cte.csv**, g8-cd2-2-decision-steps notes (that row only): the card named as stop-think-choose
  grown, with the mapping.
- **Career exploration 6 to 8**: day 4 (the goal lines on the goal steps card, retrieval or taught from the card) and
  day 11 (retrieves stop-think-choose, teaches the decision steps card as its grown form). The frame's SEL seam cell
  no longer says the goal lines are the course's own.
- **Career pathways 9 to 12**: days 2 and 8 no longer say SEL 9 to 12's rows "come later": SEL grade 9, the year
  before, grew the goal steps plan page and ran the six-step stop-think-choose, so both are retrieval for a student who
  took it; the grade 10 rows still come later this year. The frame's SEL seam cell matches.
- **Defect row.** plan.py has no command to change a row's status, so the open row stays and a fixed row is logged
  that names it.

## C. Rule 2 counting (scripts/unit_skeleton.py, scripts/sequence.py)

- **SUBJECTS** now adds sel, health, physical-education, library, cte and eld. These are the frames.csv subject names,
  and each one names its progression file.
- **sequence.py** now takes the subject from frames.csv. course-list.csv has health and PE as `health-pe`, which names
  no progression file.
- **Band courses.** Adding the subjects alone counted nothing in a band course: its grade (k-2, 6-8) is not a number,
  so every row was set aside as "grade not a number", silently. earlier_rows now handles them like this:
  - It gives each unit its year: the highest progression grade among its skills. A course-level day takes the year of
    the unit day before it.
  - "This year" means that year's days only.
  - The band's earlier years count as earlier grades, as other courses' days already do. Earlier band courses count
    the same way.
  - Courses with a numeric grade (all core courses) take the old path unchanged.
- SUBJECT_STD is read with a default, so a skeleton for an after-core course does not fail on a missing key.
- `unit_skeleton.py --self-test`: all passed. No other test covers these scripts (goal_tests.py and test_voice.py do
  not).
- Arts and computer science were not added, since neither is after-core. Adding them is a one-line change.

### Result per subject: sequence.py check, 59 after-core, arts and CS courses, before and after

| Subject | Courses | Failures before | Failures after | New notes |
|---|---|---|---|---|
| SEL | 4 | 0 | 0 | none. 520 assumed rows counted, all retrieval the year before, all named |
| Career | 2 | 0 | 0 | Pathways unit 2: 14 rule 2 notes (below) |
| Physical education | 4 | 0 | 0 | 6 rule 2 notes in 3 to 5 (units 21, 22, 24), 6 to 8 (unit 19), 9 to 12 (units 7, 21) |
| Health | 4 | 0 | 0 | one "rule 2 check skipped" note per course (below) |
| Library | 8 | 0 | 0 | none |
| ELD | 4 | 0 | 0 | none |
| Music, visual arts, theater, dance, media arts | 20 | 0 | 0 | not in SUBJECTS, unchanged |
| Computer science | 13 | 0 | 0 | not in SUBJECTS, unchanged |

No course gained a failure, so every subject stays in SUBJECTS. `sequence.py check` over all 94 scope-stage courses
has 0 failures.

**For the owners (notes, not fixed here):**
- **Pathways unit 2.** The day 12 readiness check names the 14 g8-clu rows as a group ("the 14 g8-clu rows"), not by
  id, so the counter reads them as owed a readiness check that does not name them. The fix is to list the ids in day
  12's note.
- **Health.** data/progressions/health.csv row k-s-trusted-helpers (data line 9) has a broken quote, so the row reads
  as 13 cells against a header of 11. progression.py check does not catch it. Until the health owner fixes it, the
  counter skips health courses with a note.
- **PE.** The 6 PE notes are the counter's ordinary findings, for the PE owner.
- **sel.csv.** Its grade 6 to 8 notes still open with the old unit titles ("Unit 3, Stress and strong feelings", 120
  rows). This is plain wording that can be swept later. data/plans/calendar.csv carries the labels too, and the lead
  regenerates it at commit.

## Checks

| Course | sequence.py check | frame.py check |
|---|---|---|
| social-and-emotional-learning-grades-k-to-2 | 0 failures | 0 failures |
| social-and-emotional-learning-grades-3-to-5 | 0 failures | 0 failures |
| social-and-emotional-learning-grades-6-to-8 | 0 failures | 0 failures |
| social-and-emotional-learning-grades-9-to-12 | 0 failures | 0 failures |
| career-exploration-grades-6-to-8 | 0 failures | 0 failures |
| career-pathways-grades-9-to-12 | 0 failures | 0 failures |

- `progression.py check sel`: 520 rows, 0 failures.
- `progression.py check cte`: 228 rows, 0 failures.
- The gate on SEL K to 2, SEL 6 to 8, Exploration and Pathways shows 0 failing findings. Pathways has 14 new note
  lines, the rule 2 notes above.
- 6 defect rows were logged (fixed, made at scope).
- One decision line was added to docs/agents/decisions/DESK-ANSWERS.md.

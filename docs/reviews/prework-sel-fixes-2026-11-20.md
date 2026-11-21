# Social and emotional learning pre-work: stage 1 fix pass, 2026-11-21

Read for this pass: AGENTS.md, docs/agents/EXPERT.md, the SEL lens, docs/COURSE-RUN.md (stage 1) and
docs/courses/UNIT-PLAN.md (both field lists); the pages under fix (docs/courses/sel/STANDARD.md and APPROACH.md) and
data/standards/casel-5.txt; the findings in docs/reviews/prework-sel-gemini-2026-11-20.md, the real-page findings in
docs/reviews/calibration-sel-2026-11-20.md and calibration-sel-gemini-2026-11-20.md, the first read
(docs/reviews/prework-sel-read-2026-11-19.md, already fixed) and data/plans/later.csv L96; the settled calls in
DESK-ANSWERS (2026-11-15 L43, 2026-11-16 q-later-sel-eld, 2026-11-21 q-prework-open-1 and -2, q-fix-health-1,
q-fix-pe-1, q-fix-arts-1). Claims were checked against the files they cite: scripts/progression.py (STD_FILES,
ANCHOR, code_grades, codes, the ownership check at line 273), data/courses.csv (rows 62 to 65), the ELA discussion
ids in data/progressions/ela.csv, docs/pipeline/briefs/sensitivity-read.md ("When these reads run"),
docs/courses/health/APPROACH.md ("If a student tells you something", self-check, tools, pacing), the bar's C8 and
part 9, and the grade table (recounted: every grade teaches all 40 once, no unit over 8). The header lines of
casel-5.txt needed no change.

## Findings

| Source | What | Decision | Where |
|---|---|---|---|
| gemini #1; gemini calibration #4 (gate part); first read #1 | STANDARD says the gate needs only the codes() fix; progression.py also lacks sel in STD_FILES and ANCHOR, has no sel rule in code_grades, and fails any id owned by more than one grade (line 273), so all 40 ids would fail under the 160-row form | fixed (page) and follow-up | STANDARD section 3, "Ownership": the four changes named |
| gemini #2 and question 1; expert calibration #7, #8; gemini calibration #9; L96 | 64 sessions over 6 units is about ten a unit, not two a sub-skill for eight sub-skills; the short path "drops the second Application session in each unit" removes 6 sessions, not 32 | question for Cory (dose and what the short path cuts are choices); the false arithmetic is taken off the page and marked open | STANDARD sections 2 ("Sessions") and 3 (opening paragraph) |
| gemini #3.1; gemini calibration #15 | Student voice placed in unit field 10 (sources) | fixed | APPROACH kinds of day, Application row; removed from unit field 10, which now also names what is still to make |
| gemini #3.2 | Section field 1 drops the shared parts; "before you teach" is a unit teacher-page rule (bar item 13) but sits in a section field | fixed (wording): section field 1 is where the teacher page is explained, so every unit's teacher pages open with it; the shared parts are not a fault (next line) | APPROACH section field 1 |
| gemini #3.3; gemini calibration #15 | Section field 2 used unit field 3's labels (builds on, leads to), which UNIT-PLAN puts out of field 2 | fixed | APPROACH section field 2: the sections just before and after, and the field 4 retrieval items used |
| gemini #3.4, #3.5, #3.6 | Section fields 3, 5 and 7 omit their shared parts (owned item numbers; ideal instrument and a room with nothing; planned questions and the written task) | not a fault: the list adds what SEL fills and the shared parts stand; the page now says so in one line | APPROACH, line above the field list |
| gemini #4; gemini calibration #17 | No student self-check per unit (C8 fails if students never judge their own work) | fixed; item-level choice: once a unit, steps only, kept by the student (C8 asks for a page per unit; health's pattern) | APPROACH "Daily evidence" (section field 3) |
| gemini #5 | Unit field 4 ignores UNIT-PLAN's `Retrieval only:` rule (every SEL row was used the year before), and a ten-minute reteach fills half a K to 2 session | fixed | APPROACH unit field 4: `Retrieval only:` in the five-minute opening; `Given:` only after a left-out unit; kindergarten unit 1 `Start-of-year check:` |
| gemini #6.1 | The leave-out note is not in the family note | question for Cory (leave-out policy) | none |
| gemini #6.2 and question 2 | Disclosure steps cover the school only: no home route, no "do not promise secrecy" | fixed by the settled pattern (q-fix-pe-1 item 3, q-fix-arts-1 item 6): point to health's steps, not a second copy | STANDARD section 5, item 4 |
| gemini #6.3 | The health-handoff unit list misses units that teach SM2 or RS6 (grade 7 "Under pressure", grade 12 "Steady under change" and others) | fixed: the rule now names every grade 6 to 12 unit that teaches SM2 or RS6 first | STANDARD section 3, unit rules |
| gemini #6.4 | Sensitivity read said to be at the Finish check only | fixed: every unit plan and day and the Finish check, per the brief | STANDARD section 5, opening |
| gemini #7 and its settled choice; gemini calibration #13 | Depth ladder has three steps within a band; 9 to 12 has four years | fixed; item-level choice: grade 12 adds a setting past school (work, community, life after school), fitting its theme | STANDARD section 3, depth ladder |
| gemini #8.1 (section) | No standalone pacing section in APPROACH | not a fault: pacing is stated once, in STANDARD section 2, and the approach header points there | none |
| gemini #8.1 (benchmark) | No national dose figure stated | fixed in part: the criteria paper (read, p 25) asks that sessions be stated and sets no number; the reader's program-guide range and the primary guidance's "two 30-minute sessions" were found by web search only and are not used | STANDARD section 2, "Sessions" |
| gemini #8.2 | Tools: only what a tool may not do | fixed: what a tool may do, and that no tool stands in for rehearsal with people (bar item 5) | APPROACH unit field 8 |
| gemini #9 (status) | STANDARD still says DRAFT and "Draft for Cory's yes" | fixed | STANDARD header and owed-row table |
| gemini #9 (catalogue) | STANDARD says courses.csv has one `sel-k12` row and still "recommends" four | fixed (rows 62 to 65 checked: four band rows) | STANDARD section 2 |
| gemini #9 (ELA ids) | "e10-sl-seminar and on"; grades 11 and 12 are e11-seminar and e12-seminar | fixed (ids checked in ela.csv) | STANDARD section 7 |
| gemini #9 (SO6) | SO6 placement skips grade 2 | fixed: "K to 2" | STANDARD section 3, placement notes |
| gemini #9 (bar); first read #11 and #13 leftovers | ADOPTION-BAR-SUBJECTS part 9: items 9 to 13 tagged [I], "marked for a deeper review", SEL status row still owed the approach yes, sources row "pp 23 to 25; pp 21 to 27" | follow-up for the lead | none (not my page) |
| expert calibration #11; gemini calibration #14 | K to 2 step card "three or four pictured words" against the ladder's "one or two pictured steps"; "two to four steps" with no K to 2 line | fixed to the ladder (item-level) | APPROACH "What a good SEL session does" and section field 5 |
| gemini calibration #16 | "In K to 5 a new skill is taught before it is tried" | not a fault: the section order (Understanding first) holds in every band; the line only keeps K to 5 sessions from opening on a cold try | none |
| first read, all others | Fixed 2026-11-20 and settled 2026-11-21 (q-prework-open-1) | not reopened | none |

Counts: 17 fixed, 5 not a fault, 2 questions for Cory, 4 follow-ups for the lead.

## Questions for Cory

1. **SEL session arithmetic and the short path.** Settled: 64 sessions a year (two a week), six units, up to eight
   sub-skills first in a unit, and a 32-session short path that never drops a unit. That gives about ten sessions a
   unit, not the two a sub-skill the page claimed, and the stated short path cut (one Application session a unit)
   only removes 6. Recommended: keep 64 and 32; a unit groups its sub-skills into two or three sections of related
   sub-skills (each session still names one skill and rehearses it); the short path keeps each section's
   Understanding and one rehearsal, and puts the Check and Respond in one session, about five sessions a unit.
   Alternative: raise the full year to about 90 sessions (three a week).
2. **SEL family note and a left-out unit.** SEL lets a school leave out a unit, with the ids named to the school and
   on the course page. Arts (q-fix-arts-1) also names them in the family note. Recommended: SEL family notes do the
   same, so one rule holds in every subject.

## Follow-ups for the lead

1. scripts/progression.py, before the first SEL check: add `'sel': ['casel-5.txt']` to STD_FILES and `'sel':
   'casel-5.txt'` to ANCHOR; split codes() on the tab only; add a sel branch to code_grades (owners 2, 5, 8, 12, `~`
   in any grade); change the ownership check (line 273) so a sel id must be owned once in each of the four grades.
2. docs/ADOPTION-BAR-SUBJECTS.md part 9 and its tables: tag items 9 to 13 [O]; replace "marked for a deeper review"
   with the review's date and STANDARD section 4; update the SEL status row (line 569: approach approved
   2026-11-21, owed now the progression, the gate changes and this pass's two questions); set the CASEL criteria
   paper row (line 672) to "pp 1 to 3 and 20 to 35 in full".
3. docs/agents/lenses/sel.md, "SEL is not therapy" paragraph: the disclosure line names only the school's route and the
   counselor; point it to health's steps as STANDARD section 5, item 4 now does.
4. Before any SEL course page quotes a national dose figure, read the primary SEL guidance (Education Endowment
   Foundation) at source; the second read's "two 30-minute sessions a week" and "8 to 140 sessions" rest on web
   search only.

Lead, 2026-11-21: follow-up 3 done (the lens points to health's steps) and the SEL status row in follow-up 2 updated; the rest of 2, and 1 and 4, are on the lead's list. The two questions are on the Desk (q-fix-sel-1).

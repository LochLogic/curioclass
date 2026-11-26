# Fixes: scope and sequence of library-and-research-skills-grade-4, 2026-11-26

Fix pass per build/scope-writes/AFTERCORE-FIX.md on the expert read
docs/reviews/sequence-library-and-research-skills-grade-4-2026-11-26.md. The Codex read waits for Codex's usage reset
(after 2026-11-30). The other library expert reads (kindergarten, grades 1, 3 and 5) have no "Across" section; the
only item naming grade 4 (grade 5 read finding 5, "two grade 4 days carry" g3-safe-searching) still holds: days 2 to
4 carry ~AASL.VI.A.1 and day 2 retrieves g3-safe-searching.

Counts: applied 13 (expert 9 findings with every "Settled by the expert" row, lead calls 1, 4, 5 and 7); not applied
0. 13 defect rows logged as fixed (expert 1 to 9, four frame wording rows).

## Applied

- **Expert 1** (days.csv days 2, 3, 7 to 10 notes and `retrieves`; .md readiness line, unit 1 and unit 2 retrieval
  bullets): day 2 retrieves g3-key-words and g3-safe-searching before the three-way search; day 3 g3-research-questions
  before the narrowing practice; day 8 g3-source-kinds-and-makers; day 9 g3-source-list; day 10 g3-notes-in-boxes
  before the own-box notes round; day 7's model may start from a grade 3 key-word box inside the show-me.
- **Expert 2** (.md Shorter path): sitting papers on the desks before class, about 1 minute of opening setup, so
  days 12 and 29 fit 27 minutes; fold-in for day 10 dropped (unit 2 keeps its practice); two fold-ins (days 3 and 13),
  28 days; day 6 into day 15 only if a third session is lost.
- **Expert 3** (days.csv days 5, 14, 29; .md unit 1 assessment and check table): rubric line "the plan names what I
  still do not know, and each step fills one of those"; day 29's honest-use case fixed with a reason, inside the 27.
- **Expert 4** (days.csv day 18; .md unit 3 weather bullet): three set spots or the printed picture sequence when no
  rain falls or the ground is frozen; soil after rain stays the case.
- **Expert 5** (days.csv days 4, 11; .md unit 1 and unit 2 host lines): ELA unit 2 the in-step host for unit 2,
  science energy resources a finished question kept off policy; day 4 most often on the stand-alone Arctic question.
- **Expert 6** (days.csv days 4, 11, 12; .md unit 1 and 2): minutes named; day 12's second source as two printed
  sentences.
- **Expert 7** (days.csv day 20; .md unit 3 assessment): applied, though marked a judgment call for the lead, since it
  is a days.csv row I own and fits the minutes: the written part adds "for a new neutral question no source holds,
  which kind of plan would you use and what is its first step?" (about 2 minutes; written part about 10, day about
  28 of 29).
- **Expert 8** (.md Sources not loaded; days.csv days 1, 2, 10, 19, 24): band file on disk, read by the frame and
  checked by the expert, store entry waits on L149; no day leans on the presentation (sensitivity source only,
  browser check); day 2's projector page has the same-day check and printed swap.
- **Expert 9** (.md Owned codes and For the lead item 1): kept as written, reason named; the day 29 trade (two-page
  purpose sort plus one change-log line) is listed for the structure pass.
- **Lead call 1** (frame Placement paragraph and For the lead item 3; .md Calendar line): reworded as settled by
  CALENDAR.md rule 1; scope For the lead item 1 dropped.
- **Lead call 5** (frame Day kinds bullet): "practice half-day in units 2 and 3" replaced: days 9, 17 and 26 first
  teach a move and are Understanding days (GLOSSARY), as the scope has them; scope For the lead item 3 dropped.
- **Lead calls 4 and 7** (frame wording): seam table and unit 1 and 2 opening retrieval cells match the swap; unit 1
  evidence and both check cells ask the whole of AASL.I.B.2, the year-end cell fixes the honest-use case with a
  reason; unit 2 host and the science cross-subject row no longer claim energy resources runs in the same weeks; unit
  1 host notes the project's weeks 5 to 8; unit 3 evidence adds the new-question line (about 28 minutes) and the
  weather fallback.
- **Own re-run of rule 2:** every assumed grade 3 row is now retrieved on or before the day that builds on it; no
  readiness check owed; no `~` code or owned row changed; no task form repeats within two weeks.

## Not applied

None.

## Settled (for DIGEST)

| Judgment | Reason |
|---|---|
| A retrieval opens the day whose move needs it, not the day after | Retrieval wakes the earlier move before the new one is built on it |
| On a short session, sitting days have the papers on the desks before class (about 1 minute opening) | Lets a 27-minute sitting fit 26 to 27 working minutes |
| Never fold away a unit's only practice day; fold a respond day into the next check's respond day instead | Scoring needs a practiced day first |
| A plan rubric for AASL.I.B.2 carries "the plan names what I still do not know, and each step fills one" | The id's "what you still do not know" part |
| An observation planned for winter weeks names a weather fallback | No teacher can schedule rain |
| A group-plan id (AASL.V.C.2) is also checked on a new question, not only by explaining the group's plan | A student who rode along could describe it |

## For the structure pass

- data/progressions/library.csv, row g4-class-survey, note: "birds at a feeder for a week" to "the schoolyard soil
  after rain over a week (frost, puddles or snow at three set spots, or the printed picture sequence, as the
  fallback)", to match the frame and scope (expert finding 4).
- docs/courses/library-and-research-skills-grade-4/frame.md and days.csv day 29, at the next frame pass (expert
  finding 9): the lead may trade the three-page purpose sort for two pages (about 2 minutes) and add one change-log
  line for one piece of advice on a sample unit 2 note sheet, putting AASL.I.C.3 on the year-end check.
- docs/agents/lenses/library.md: "catalogues" to "catalogs", "licences" to "licenses", "judgement" to "judgment"
  (lead call 13), if not already applied from the grade 1 pass.
- data/plans/calendar.csv: no change from this pass (no week moved; checks stay in weeks 14 and 29).

## For Cory

None.

## Gates

- `python -X utf8 scripts/sequence.py check library-and-research-skills-grade-4`: 0 failures.
- `python -X utf8 scripts/frame.py check library-and-research-skills-grade-4`: 0 failures (4 units, 30 days, 26 in
  units, 4 for checks and respond days).
- `python -X utf8 scripts/frame.py calendar`: no failure or break line for this course. No unit, day count, owned row
  or week changed, so the stagger is as before (library is a K to 5 special, outside rule 1).

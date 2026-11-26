# Fixes: scope and sequence of career-pathways-grades-9-to-12, 2026-11-26

Fix pass after the Claude expert read (docs/reviews/sequence-career-pathways-grades-9-to-12-2026-11-26.md), run as
build/scope-writes/AFTERCORE-FIX.md asks. The Codex read waits for Codex's usage reset and gets its own pass.

Counts: applied 13 (expert 12, band item 1), plus frame wording under lead calls 4 and 11; not applied 1 (expert For
Cory item, waits on Cory). Defect ledger: 14 rows logged, all `fixed`, made at scope.

## Applied

- **Expert 1 (serious).** days.csv day 42: the CD3.R4 groupings prompt and the CD2.R2 "which method suited" prompt;
  day 95: six prompts, one per part (CD5.A3 plan line, CD4.R5 against an invented student's goal, CD4.R2 judged then
  revised, CD3.R1 update from a new dated figure, ALL2.R6 and A6, CD2.R9 how well the plan handles it); CD4.A2 dropped
  from day 95's codes. .md check sections rewritten to match; CD4.A2 added to the not-sampled list with its reason.
- **Expert 2.** days.csv days 66, 78, 91 to 93: the scored product named per claimed code. .md unit 4, 5 and 6 lines say
  so.
- **Expert 3.** days.csv: ALL1.R3 drafted on day 9 (skill and code added), CD1.R1 and CD2.R1 on day 64, ALL2.R3 and
  ALL1.R8 on day 87, ALL1.R6 on day 88 (skill and codes added); days 10, 65 and 90 now revise them from feedback. .md
  units 1, 4 and 6 match.
- **Expert 4.** .md made to agree with days.csv in the five places: day 87 (drafts), coin-test days 34 and 35 added,
  the frame's unit titles (Three clusters, broad to narrow; Who does which job, and why; One job, the full plan; Getting
  work; The applied project) in the calendar table and headings, each unit's compelling question with one line on why
  its days fall in that order, the reteach timing stated once, the non-repeat line in both check sections, CD4.K7 in the
  not-sampled list.
- **Expert 5.** days.csv day 13 opens with the compelling question; the reteach moves to day 14's first ten minutes while
  the class starts the field task; days 22 and 31 compare three figures (pay, training time and cost, outlook).
- **Expert 6.** .md 10-days-short fold 7 is now day 74 into day 70 (day 76 kept); the 64-session and grade 12 paths split
  the teacher's hearings over day 75's second half and day 77's first half. frame.md unit 5 short row says the same.
- **Expert 7.** days.csv day 12 and frame.md family-note bullet: the note names the sensitive sub-clusters of any shared
  cluster that holds one (Energy and Natural Resources included) and of each student's own cluster. .md unit 2 matches.
- **Expert 8.** .md 64-session path: unit 1's goals move to short session 2 with values; the two-cluster line (second
  shared cluster's rows not claimed, check 1 samples the one block). frame.md unit 1 short row, check 1 cell and For the
  lead item 4 updated (item 4 carries a Pending(Cory) marker). Unit 6: not applied, see For Cory; a one-line "Pending
  Cory" note is in the .md's Shorter path.
- **Expert 9.** days.csv day 89: a paired run-through of each defense's opening minute; CD4.A7 added. .md matches.
- **Expert 10.** days.csv day 75 and .md unit 5: the guidance's own terms (before a conditional job offer; the job's
  tasks with or without a reasonable change), page and date read.
- **Expert 11.** days.csv days 20 and 29: one shifted goal changed with its reason on the change log (CD1.R3 carried).
- **Expert 12.** .md fold 10: unit 4's reteach moves to day 57's first ten minutes; day 58's device turns run while the
  class works the route-steps line on paper.
- **Band item** (Exploration 6 to 8 read, finding 4 and "For the source list": "Career Pathways will need it too").
  days.csv day 72 and .md unit 5: the first job's teacher page cites the young workers page for a safe workplace and the
  Wage and Hour Division's YouthRules and child labor pages for hours and barred tasks, with a stricter state law where
  there is one.
- **Lead call 4/11 (frame wording).** frame.md check 1 and check 2 cells now ask each code whole, as the read settled.

## Not applied

- Expert 8, unit 6 part and the read's For Cory item: a lighter applied project on the 64-session path. Waits on Cory
  (lead note).

## Settled (for DIGEST)

| Choice | Reason |
|---|---|
| A reflection code is drafted in the last minutes of the day before the plan day and revised there | feedback before every score |
| A course-level item that claims a K-A-R code asks one prompt per part; a code whose whole is scored in its unit and asked only in part at the check is dropped from the check's codes and named in the not-sampled list | each item asks the whole of the id it claims |
| A unit's readiness reteach never takes the opening of its first day; it opens day 2 or runs after the hook | first day clean for the hook and compelling question |
| A fold never takes a feedback day; where a path folds it, its hearings split over the neighboring skill and plan days | the frame's no-fold rule |
| A first job's hours and barred tasks cite the Wage and Hour Division pages, not the young workers page | the safety page holds no hours or task limits |

## For the structure pass

- Source list: add https://www.eeoc.gov/laws/guidance/enforcement-guidance-preemployment-disability-related-questions-and-medical
  (the pre-offer rule and the job-functions question, unit 5's teacher page) and the Wage and Hour Division's YouthRules
  and child labor pages (already listed by the Exploration read) as used by this course too.
- data/plans/calendar.csv: unit titles for this course already match the frame; no check day moved, so no regeneration
  is needed for this course.
- Lens spellings (lead call 13): a search of docs/agents/lenses/career-education.md for common UK spellings found none.
- frame.md line 3 says "catalogue id"; scripts/frame.py and scripts/front_office_docs.py match that string, so a US
  spelling change ("catalog id") needs those scripts changed in the same pass. Left as is.

## For Cory

- **The 64-session path's applied project** (frame For the lead item 4, tested by the read): in 9 sessions unit 6 cannot
  hold a tested option, a second try, the evidence check and the portfolio as well as three panel days. The read's pick:
  a lighter project on that path (one option tested and its second try on paper, the effects map dropped to one line),
  with every scored code kept. Not applied; the .md's Shorter path and the frame's item 4 carry a Pending note.

## Gates

- `python -X utf8 scripts/sequence.py check career-pathways-grades-9-to-12`: 0 failures.
- `python -X utf8 scripts/frame.py check career-pathways-grades-9-to-12`: 0 failures (6 units, 96 days).
- `python -X utf8 scripts/frame.py calendar`: no break; grades 9 to 12 have the finals-week rule only, and no check day
  moved (check 1 days 42 and 43, weeks 14 and 15; check 2 days 95 and 96, week 32).

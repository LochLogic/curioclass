# Fixes: scope and sequence of computer-science-grade-12, 2026-11-26

Job: docs/pipeline/briefs/sequence-fix.md with build/scope-writes/CS-FIX.md. Read applied: the Claude expert read
docs/reviews/sequence-computer-science-grade-12-2026-11-26.md (the Codex read waits for Codex's reset, after
2026-11-30). No other grade's expert read has an "Across the grades" item that touches grade 12.

Counts: applied 18 (expert 8 findings and every "Settled by the expert" row; lead calls 1, 3, 4, 5, 6, 7; own 1);
not applied 0. Not used here: lead calls 2, 9, 10, 11, 12 (nothing in this course for them) and 8 (covered by call 4).

## Applied

- **Expert 1** (days.csv; frame.md; scope-and-sequence.md): a prompt per part. Day 10: HS-ALG-PS-05 accuracy, bias
  and harm; HS-SOC-HU-44 in three prompts (a difference, a consciousness claim as a claim people make, who is
  responsible on what ethical ground). Day 24: accuracy, bias and harm; HU-44 difference prompt plus one implication
  prompt, rotated. Day 55: HS-ALG-PS-05 item names its three prompts. Day 63: CE-45 prompts (a) team and its views,
  (b) computational thinking and a computing technology used to solve a problem, (c) an idea expressed, (d) barrier and
  opening the field; day 59's guide asks the same four. Frame's unit 1 and 5 evidence text and the check table cells
  (days 24, 55) reworded to match (lead call 4).
- **Expert 2** (days.csv; .md standards table; frame.md): day 53 codes add S1-SWD-UX-05 with one rubric line (the
  refinement judged against the intended users and setting stated on day 49); standards row reads taught 49 (and the
  user lens of 50 to 53), assessed product 53; 54. Scoring only, S1 count unchanged.
- **Expert 3 and lead call 6** (.md; frame.md): C1 recount corrected to about 4.77 day-equivalents, 9.2 percent of
  52. Short path rebalanced (my design, close to the expert's option (a), keeping all ten fold-ins and the lesson
  count): day 5 runs as a half lesson of S1 (both systems' sources in one combined sort; the other half writes and
  applies day 6's checklist), day 31 as a half lesson of S1 (branch and merge cards; clash card into day 32's opening;
  other half traces the starter module on paper). Short path S1 about 3.9 of 42, about 9.2 percent. Frame C1 paragraph
  updated (it also now counts the two five-minute parts on unit 3 days 4 and 5).
- **Expert 4 and lead call 1** (days.csv; .md): day 22's `assess` = end cleared and its note sentence replaced (check 1
  stands for unit 2; revised pieces are practice); unit 2's End-of-unit bullet rewritten; For the lead 1 dropped,
  remaining items renumbered.
- **Expert 5** (days.csv): days 33 to 39 openings named from their `retrieves` row (33 a test case against a short
  spec; 34 a list or key-value record picked and an item added; 35 a twenty-line sample traced; 36 a spec's edge case
  as a test-table row; 37 two modules traced; 38 a test case predicted pass or fail; 39 a saved generated function
  checked for its first wrong line). Item-level wordings for 36, 38 and 39 are mine.
- **Expert 6** (days.csv): driver and navigator switch added to days 41, 42, 48 and 53; days 50 and 52 name user-round
  roles (two users, one note-taker, one at the device, switched in round two).
- **Expert 7** (days.csv; .md; frame.md): days 10 and 45 read as 40-minute sittings, about 35 task minutes, with minutes
  per code; day 54's short program is a module from unit 3's worked project (day 27) and its screen unit 2's bus-route
  helper (frame check table too); no-device build step written once on day 32, referenced on days 33 to 43; day 8's
  candidate case "picked in the unit plan".
- **Expert 8** (days.csv; .md; frame.md): day 59 reads each account for the team the person worked in (Hopper's
  Harvard crew; Johnson's West Area Computing group and the flight-trajectory team), with the team's unit 3 log as the
  current case; the unit plan opens both pages at source and swaps in a NASA-published interview in Johnson's own words
  if the feature is a profile.
- **Lead call 3** (frame.md): `frame.py check` failed on unnamed leans `gov-policy-debates` (g12-law-policy,
  g12-data-policy-debate), which landed in the rows. Cross-subject now has a US Government and Politics table with a
  "by course order" bridge (unit 2 writes its own summaries, assumes no civics); frame For the lead 3 marked landed.
- **Lead call 5 and own finding** (days.csv; frame.md; .md): days 29 (first day of S1-SWD-PP-08), 50 (first day of
  HS-PRO-TR-20) and 60 (first day of HS-SOC-CE-46) relabeled Understanding per GLOSSARY, each with its worked example
  first; frame Day kinds bullet reworded to GLOSSARY's definition.
- **Lead call 7**: 11 defect rows logged (10 found_by expert, 1 writer), all fixed, made_at scope.
- **Rule 2 re-run (own)**: earlier-grade rows, check samples, Collect once, part coverage and end days rechecked
  after the edits; nothing else found.

## Not applied

None.

## Settled (for DIGEST)

| Judgment | Reuse |
|---|---|
| C1 on the short path is met by halving Specialty lessons in place, not by unfolding a fold-in | Any course whose fold-ins carry no S1 time |
| A standard's first day in the course is Understanding even when it is a design or user-round day; the worked example comes first | Every CS scope |
| A check right after a unit's end draws its items' material from earlier units (here unit 3's worked project and unit 2's bus-route program) | Year-end checks after the last scored unit |
| A rotated pair of implication prompts on a sample check is enough when the end-of-unit sitting asked all parts | Short sample items for multi-part codes |

## For the structure pass

- The defect ledger (plan.py defect): the Cross-subject lean row was logged found_by expert; it came from lead call 3 and
  frame.py, not the read. Change found_by to `script` if the ledger should keep that distinction.
- No shared file needs an edit from this pass. calendar.csv: no change (no unit, day count or week moved).

## For Cory

None.

## Gates

- `python -X utf8 scripts/sequence.py check computer-science-grade-12`: 0 failures.
- `python -X utf8 scripts/frame.py check computer-science-grade-12`: 0 failures (was 1, the gov-policy-debates lean);
  `frame.py check` across all frames: 0 FAIL lines.
- `python -X utf8 scripts/frame.py calendar`: no line for this course; no stagger break.
- `python -X utf8 scripts/gate.py --course computer-science-grade-12`: 0 failing findings against the baseline, 1 new
  note line (sequence 0 failures); plan gate's failing lines fell 1 to 0. The shared index-reports gate exits non-zero
  (not this course's).

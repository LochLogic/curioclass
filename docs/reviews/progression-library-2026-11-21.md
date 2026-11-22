# Library progression: expert cold read, 2026-11-21

Job: docs/pipeline/briefs/progression-read.md with subject library. Also the sensitivity read of the progression.

## What was read

- docs/agents/EXPERT.md, docs/agents/lenses/library.md, docs/ADOPTION-BAR-SUBJECTS.md ("The shared core" and part 11).
- docs/courses/library/STANDARD.md (173 lines) and APPROACH.md (157 lines), allowed by the brief because library has no
  earlier course pages.
- data/progressions/library.csv (98 rows: K 7, 1 8, 2 9, 3 9, 4 9, 5 9, 6 8, 7 8, 8 7, 9 7, 10 6, 11 6, 12 5),
  library-edges.md, library-excluded.csv (5 ids).
- data/standards/aasl-words.txt (68 ids); data/standards/aasl-2018.txt by id only.
- Every row named in a library `cross_subject` cell, in data/progressions/ela.csv, social-studies.csv and science.csv,
  plus every row in those files whose notes mention an interview or a survey.
- Gate: `python -X utf8 scripts/progression.py check library`: 98 rows, 0 failures. `scripts/stale.py check` on the
  progression and STANDARD.md: 0 failures.
- My own checks (scratch script, not kept): each of the 68 ids is owned once (63) or excluded (5); every `hands_on`
  lands in the next grade and is assumed back; every `assumes` is handed on; no model is used before the grade that
  introduces it (research-cycle K, citation 2, search-plan 3, lateral-reading 5); all 48 `cross_subject` leans name a
  real row at or before the leaning grade.
- Not opened: the continuum band files (kept outside the repo), earlier reviews of library (the brief forbids them).

## Verdict

The progression is sound: one owner per id, a full inquiry cycle every year, lateral reading owned by library before
social studies uses it, honest use in every band, and K to 5 cases kept neutral row by row. The biggest risk is one
accuracy fault a writer would build wrong days from: grade 8 teaches fair use as "a small part, for school, with
credit", which is a common myth, and grades 9 to 12 never teach fair use in depth. The one change that matters most
is that rewrite (finding 1); the rest are promises the grade notes make and no later row keeps, two-id rows whose
check reaches one id, and one interview and survey rule stated once instead of row by row.

## Findings, most serious first

REPEAT is "new" for all: this is the first library progression read, and earlier library reviews were not opened.

**1. Fair use is taught as a myth in grade 8, and not in depth in 9 to 12.** LAYER progression. Confidence firm (the
US Copyright Office's fair use index and the four statutory factors, from memory; the lens and bar both ask for fair
use "in depth" at 9 to 12).
Rows: `g8-fair-use-basics`, `g9-open-licenses`.
Problem: `g8-fair-use-basics` says fair use is "a small part used for teaching, comment or a school project with
credit, against copying a whole work", and students "decide whether a use ... is permitted". Credit does not make a
use fair, and "for school" is not a safe harbor; the row also asks students for the very verdict APPROACH "Sensitive
ground" item 6 forbids (no claim that a use is lawful). No 9 to 12 row teaches fair use beyond grade 8.
Fix, `g8-fair-use-basics` notes, replace the first two sentences with: "Students learn the basics of copyright and
fair use: a work is protected from the moment it is made; fair use weighs four questions (why the work is used, what
kind of work it is, how much is used, and whether the use takes the place of the original), and giving credit alone
does not make a use fair. For invented cases (an image, a clip, a quote in their product) students say which way each
question leans and pick the safer path: a public domain or openly licensed work, a smaller part, or asking
permission." Keep "Checked alone in grade 8" with: "the four questions applied to a new case and a safer path
chosen."
Fix, `g9-open-licenses` notes, add after the first sentence: "Fair use in depth: the four questions weighed on harder
cases (a remix, a parody, a clip inside a video), where reasonable people differ." Add `fair use` to its words.

**2. Grade 9 vs 10 and grade 11 vs 12 differences are promised and not kept.** LAYER progression. Confidence firm (the
rows themselves).
Rows: `g9-research-question-design`, `g10-synthesis-map`; `g11-publish-for-audience`, `g12-capstone-decision`.
Problem: STANDARD section 2 says the progression must state how 9 differs from 10 and 11 from 12, since the
continuum has one cell for each pair. Most rows do (databases, lateral reading, method note, advanced search). Two do
not: `g9-research-question-design` says "grade 10 sets its own topic", but no grade 10 row mentions a self-set topic
and I.D.2 is not carried in grade 10; `g11-publish-for-audience` says "grade 12 publishes the capstone", but
`g12-capstone-decision` names no audience or publishing and carries neither VI.C.2 nor I.C.4.
Fix: `g10-synthesis-map` standard `AASL.IV.D.2; ~AASL.I.D.2`, notes add: "Grade 10 sets its own topic and question for
the sustained project (grade 9 worked inside a topic the teacher set)." `g12-capstone-decision` standard
`AASL.I.D.3; ~AASL.I.D.2; ~AASL.VI.C.2`, notes add after the first sentence: "The capstone is published for the people
the decision affects, in the form grade 11 practiced."

**3. Grade 3 owns self-made note categories a year before ELA allows them.** LAYER progression. Confidence likely
(ela.csv `e3-short-research` and `e4-research` notes; STANDARD section 2's own grade 3 example, "simple
note-making").
Rows: `g3-notes-in-boxes`, `g4-evidence-notes`.
Problem: `g3-notes-in-boxes` owns IV.B.4 with "boxes ... they plan themselves", checked alone. ELA's grade 3 row sets
the limit "provided sources and provided categories; categorising on one's own and listing sources is grade 4
(W.4.8)". The same grade 3 child would be held to opposite rules in two courses, and the library check scores a skill
ELA places in grade 4.
Fix: `g3-notes-in-boxes` standard `~AASL.IV.B.4`; notes: boxes are "one box per research question the student wrote
(`g3-research-questions`) or the teacher's boxes"; drop the "Checked alone" sentence, end with "Grade 4 makes its own
categories." `g4-evidence-notes` standard `AASL.I.B.1; AASL.IV.B.4`; notes add: "Notes go into categories the student
makes and can explain. Checked alone in grade 4: notes on a new text that keep the answers (I.B.1), sorted into the
student's own labeled boxes with the plan said (IV.B.4)." Add `ela:e4-research (taking notes and sorting them into
categories the student makes)` to its cross_subject. Grade 3 then owns 7, grade 4 owns 9: still in step with the
neighbors.

**4. Two-id owner rows whose check reaches only one id.** LAYER progression. Confidence likely.
Rows and fixes (each row owns two ids; the brief asked for each to get a real checked task):
- `g3-gallery-feedback` (I.C.1, I.C.2) and `g3-research-team` (III.D.1, II.A.1): met; each check names both parts.
- `g6-team-product` (III.A.2, III.B.1): the check "explains ... the sharing choice" is talk, not doing. Fix: "Checked
  alone in grade 6: the team's sharing plan (which tool, why it fits, who holds what), scored on use over the unit
  (III.B.1), and each student explaining the team's new idea and where its parts came from (III.A.2)."
- `g7-feedback-loop` (III.C.1, V.D.3): "Checked alone in grade 7." states no check, and "takes sharp criticism calmly"
  scores a feeling. Fix: "Checked alone in grade 7: a response log that answers every comment (III.C.1), and at least
  one change made from a critical comment, with what changed and why (V.D.3). The check scores the use of criticism,
  never a student's mood."
- `g8-diverse-team` (II.B.1, III.B.2): the check says "a different view or the other class's work", so one id can
  pass alone. Fix: "Checked alone in grade 8: each student shows one change a teammate's different view made
  (II.B.1) and one change the other class's findings made (III.B.2)."
- `g10-others-views-in` (III.C.2, II.C.2): "Checked alone in grade 10. Owns both." states no check. Fix: "Checked alone
  in grade 10: a source from a missing perspective added to the source log with a line on why it was missing
  (III.C.2), and seminar turns on the record sheet that add evidence and say back another view first (II.C.2)."

**5. Interviews and surveys: the safeguards sit in four row notes, differ, and are missing in grade 10.** LAYER
progression (and APPROACH, see the fix). Confidence a judgment call on wording, firm that grade 10 lacks one.
Rows: `g2-group-research`, `g4-class-survey`, `g4-asking-others`, `g10-others-views-in`, `g11-learn-across-difference`.
Problem: `g10-others-views-in` asks for "a source or interview from a missing perspective" with no consent or
question check, a year before `g11-learn-across-difference` states one. Each row words its own rule, against the
"state each rule once" rule, and APPROACH "Sensitive ground" has no item for talking to people. `g4-class-survey`'s
example (which lunch fruit is picked most) touches school meals, which can expose who gets free meals. `g2-group-
research`'s "what a job involves" can expose a family member's work or lack of it.
Fix: add one item to APPROACH.md "Sensitive ground" (it restates practice already in social studies `ss2-family-
interviews`, `ss3-community-history`, `gov-policy-news` and career education's interview rule, so it tightens and
changes no scope): "8. **Asking people: interviews and surveys.** Questions stay on the topic and are checked by the
teacher before use; no one is asked about family history, beliefs, identity, health, money or immigration status
unless they raise it, and that is not recorded. Any trusted adult or a school staff member may stand in for a family
member, and a first-person source set may stand in for any interview. Interviews outside school are arranged through
the school or a family, in a public or supervised setting, with the person's consent (and a parent's, for anyone
under 18), recorded only with consent, and reported without a full name. No classmate is asked to speak for a group.
Surveys are of the class, on neutral things, with no names recorded. Read: every unit with an interview or survey."
Then each row's teacher note becomes "Teacher note: asking people follows APPROACH 'Sensitive ground' item 8" plus
only what is particular to it: g2 "a family interview is optional"; g4 survey example becomes "which of three
read-aloud books the class wants to hear again" (keep the bird-feeder observation); g11 "the difference is in
experience of the topic (a job, a place, an age, a way of living with it), never chosen by a group label; no group is
treated as one voice". `g10-others-views-in` gets the pointer. g2 "what a job involves" becomes "what a school job
involves" for the in-school path.

**6. Machine-made text rows do not say where the text comes from.** LAYER progression. Confidence likely (APPROACH
"What a tool may and may not do"; free, no accounts; most such tools set an age floor and need an account).
Rows: `g7-lateral-hard-cases`, `g10-lateral-machine-text`, `g11-honesty-review`.
Problem: `g10-lateral-machine-text` has students check "a machine-made summary" without saying who makes it; a writer
may send students to a tool. `g11-honesty-review` asks for a disclosure line "for any use", which is right, but should
not imply use is expected.
Fix: `g10-lateral-machine-text` notes add: "The summary is supplied by the teacher as a dated capture or an invented
copy; no student uses a tool or needs an account." `g7-lateral-hard-cases` add "(invented or a dated capture)" after
"machine-made text or images". `g11-honesty-review` change to "a disclosure line if a machine-made text tool was used
(using one is never required)".

**7. Continuum priority skills placed later than the continuum's band, with no note saying why.** LAYER progression.
Confidence likely (STANDARD section 2's own summary of the bold skills; the band files were not opened here).
Rows: `g2-catalog-lookup`, `g2-who-made-it`, `k-picture-book-labels`.
Problem: STANDARD section 2 says each grade is checked against the continuum's bold skills and "where the two differ,
the progression says why". No row records a difference. Three K to 2 bold skills named in section 2 (finding books by
label and shelf order, looking a book up by author, title or key word, naming who made a site) are carried with help
in K to 2 and first checked alone in grades 3 to 5, so K to 2 has priority skills with no check (bar part 11, item 2).
Fix: `g2-catalog-lookup` notes add: "Checked in grade 2 as the grade's priority skill: the child finds a named book
from a printed catalog entry by title or author and shelf order. The continuum lists key-word lookup in K to 2;
library leaves key words to grade 3, when children can type or spell them, and owns IV.B.1 at grade 4, where more than
one kind of source is searched." `g2-who-made-it` add: "The continuum lists naming a site's maker in K to 2; here it is
done with help on invented pages, and checked alone with the first lateral check in grade 5, because a K to 2 check of
a real site would need open search." `k-picture-book-labels` add "Checked in kindergarten: the child brings back a book
from a named bin." The lead may also ask the next writer to compare each grade's rows with the band files once, since
this read could not.

**8. The lateral reading time is stated in the field study's lesson length, not ours.** LAYER progression. Confidence
firm (APPROACH "Pacing and dose": 9 to 12 sessions are 45 minutes).
Row: `g9-lateral-method`.
Fix: "Grades 9 and 10 together hold at least 300 minutes of lateral reading (seven 45-minute sessions), the amount in
the one high school field study (six 50-minute lessons)."

**9. Grade 8 "mixed teams" and the partner class.** LAYER progression. Confidence a judgment call.
Row: `g8-diverse-team`.
Problem: "mixed teams on a question where they see things differently" does not say how teams are mixed, and a writer
may mix by background; the partner-class exchange has no stand-in for a school or home with one class (bar C14).
Fix: "Teams are mixed by each student's first answer to the question, written before research, never by background.
Where no partner class exists, the exchange is with another section, another grade, or a findings set left by an
earlier class."

**10. Grades 10 to 12 are not too thin by count; three content gaps sit there.** LAYER progression. Confidence likely.
Rows: `g11-method-note` (and findings 1 and 2).
Judgment: 6, 6 and 5 rows over 18 sessions a year is three sessions a row, a lighter load than 6 to 8 (8, 8, 7 rows at
the same dose) and K to 5 (7 to 9 rows over 30 sessions); 9 and 10 also hold seven sessions of lateral reading. The
count is right for the dose. What is thin is content the STANDARD section 3 cell names: fair use in depth (finding 1),
the self-set topic (finding 2), and "full citation", which no 9 to 12 row teaches.
Fix: `g11-method-note` notes add: "The annotated bibliography uses one full citation style for every kind of source
used, including a report, a data set, an interview and any machine-made text." Add `citation style` to its words.

**11. Same-grade leans do not say which subject comes first.** LAYER progression. Confidence likely (STANDARD section 5:
"the progression says which came first in each grade").
Rows: `g3-source-kinds-and-makers`, `g6-lateral-reading`, `g7-citation-style`, `g8-news-lateral`.
Problem: each meets an ELA or social studies row the same year without an order. The 6 to 8 course meets about once
every two weeks, so library cannot promise to go first.
Fix (one sentence per row): `g6-lateral-reading` "Either order works with ELA's grade 6 credibility work
(`e6-short-research`): if ELA's unit comes first, the show-me day reuses its weaker source as the invented case."
`g7-citation-style` "If ELA's citation format is not yet taught, the show-me day teaches it from the model; ELA's day
then retrieves it." `g3-source-kinds-and-makers` and `g8-news-lateral`: "Either order; the second course opens with
a retrieval task on the first."

**12. `g6-make-and-improve` does not break section 4; one word leans the wrong way.** LAYER progression. Confidence a
judgment call.
Judgment: section 4 places the design cycle (V.B.1) in science and keeps V.B.2, self-chosen making inside a research
product, in library, "leaning on" science. The row does exactly that: no problem with criteria and constraints, no
fair test, a version log of a research product, and the lean on `science:s5-design-test` is a real grade 5 row taught
before grade 6. The word `prototype` is engineering design's, and invites a writer to rebuild science's cycle.
Fix: words `draft; version; trial; improve`; notes end: "It uses the try-and-improve habit from science's grade 5
design cycle (`s5-design-test`), without its criteria, constraints or fair tests, which stay in science."

**13. Stale sentences in STANDARD.md.** LAYER process. Confidence firm (the repository).
Each sentence the writer saw, checked, with its fix (and two more found):
- Owed row "Progression gate support": stale. scripts/progression.py has the library entry (lines 69 to 83) and the
  gate passes; library-excluded.csv holds the five ids. Fix the State cell: "Done 2026-11-21: library entry in
  scripts/progression.py, data/progressions/library-excluded.csv (five ids), data/progressions/library.csv (98 rows,
  read cold 2026-11-21, docs/reviews/progression-library-2026-11-21.md)".
- Owed row "Catalogue": stale. scripts/course_status.py names no `library` id; its text (lines 7 to 8 and 217) already
  states one course per grade K to 5 and one each for 6 to 8 and 9 to 12. Fix: row name "Catalog", State "Done
  2026-11-21: eight course rows in data/courses.csv, grade_subjects.csv and modules.csv (Cory, 2026-11-21, Desk
  q-fix-library-1); scripts/course_status.py counts them".
- Section 2, "The result goes in a table here when the progression is drafted: ...": stale, and a table would copy the
  progression. Fix: "The per-grade priority skills, in our words, are the rows of data/progressions/library.csv; where
  a row places a continuum bold skill in a different grade, its note says why." (The notes come from finding 7.)
- Section 5, "Before the progression is drafted, the 3 to 5 and 6 to 8 emphasis cells above are re-read against ELA
  grades 4 to 7.": stale; done in this read (result below). Fix: "Re-read against ELA grades 3 to 7 on 2026-11-21
  (docs/reviews/progression-library-2026-11-21.md): no conflict in the emphasis cells; two ownership lines above were
  corrected and grade 3 note categories moved to grade 4."
- Section 5's ownership lines (found by the re-read): "the first source list (grade 4, `e4-research`)" and "locating
  print and digital sources with key words (grade 5, `e5-locate-sources`)" do not match the rows. Library writes a
  credit line in grade 2 and a short source list from a model in grade 3, and teaches key words from grade 3;
  `e5-locate-sources` is about finding answers quickly across sources and names no key words. Fix: "ELA owns ... the
  list of sources in research writing (grade 4, `e4-research`, which builds on library's grade 2 credit line and grade
  3 source list), finding answers quickly across several print and digital sources (grade 5, `e5-locate-sources`) ..."
- Section 3, table header "(ours, to be set at the progression)": stale. Fix: "(ours; set grade by grade in
  data/progressions/library.csv)".
- Section 3, Ownership: "The gate then needs library in scripts/progression.py: ..." : stale. Fix: "The gate's library
  entry in scripts/progression.py uses the standards file, the anchor, ids with no grade (any grade may own one; the
  one-owner check does the work) and data/progressions/library-excluded.csv for the ids section 4 places elsewhere."
- UK spellings (AGENTS.md: fix on next edit, which this is): line 19 "Catalogue" to "Catalog"; line 64 and 100
  "catalogue" to "catalog"; line 156 "catalogues" to "catalogs"; lines 66 and 102 "licences" to "licenses"; lines 69,
  106, 107 "licence" to "license"; line 115 "programmes" to "programs". Same on their next edit: aasl-words.txt
  VI.C.1 phrase "licence" to "license" (the header's "licence:" key may stay as a field name only if other words files
  use it); APPROACH.md "judgement" (5) and "licence" (1); the lens "catalogues", "licences", "judgement", "licence".

**14. A stale owed row outside the library pages.** LAYER process. Confidence firm.
Row: docs/ADOPTION-BAR-SUBJECTS.md, "Before a scope and sequence in this subject", Library (8): "Owed: the own-words
file, the PK to 2, 6 to 8 and 9 to 12 continuum bands, the gate entry and the excluded csv". All four exist. Fix: "Own
words written, all four continuum bands read, gate entry and excluded csv written (2026-11-21); progression
data/progressions/library.csv drafted and read cold 2026-11-21 (docs/reviews/progression-library-2026-11-21.md)."
(Not this read's file; the caller applies it.)

## The section 5 re-read: library 3 to 8 against ELA grades 3 to 7

| Library skill (row) | ELA row and grade | Result |
|---|---|---|
| Credit line, short source list (`g2-credit-line`, `g3-source-list`) | `e4-research`, list of sources, grade 4 | No conflict in teaching; STANDARD section 5 wording wrong (finding 13) |
| Notes in own boxes (`g3-notes-in-boxes`) | `e3-short-research` limit: given categories; own categories grade 4 | Conflict; finding 3 moves ownership to grade 4 |
| Key words, search across kinds (`g3-key-words`, `g4-search-more-kinds`, `g5-search-revise`) | `e5-locate-sources`, `e7-research-questions` (search terms) | No conflict: library owns searching and comes first; section 5 wording fixed |
| Primary and secondary, firsthand and secondhand (`g4-primary-secondary`) | `e4-firsthand-secondhand`, grade 4 | Same year, fits |
| Bibliography to a model (`g5-bibliography`) | `e5-research`, grade 5 | Same year, fits |
| First lateral check, lateral method (`g5-first-lateral-check`, `g6-lateral-reading`) | `e6-short-research`, credibility from a teacher-checked set | Fits; library gives the method ELA's judging uses; order line added (finding 11) |
| Quote and paraphrase (`g6-quote-paraphrase`) | `e6-short-research`, quoting or paraphrasing, basic bibliographic information | Same year, fits |
| One citation style (`g7-citation-style`) | `e7-research-questions`, standard format | Same year, fits; order line added |
| Machine-made text checks (`g7-lateral-hard-cases`) | none in ELA | Library's own |

The 3 to 5 and 6 to 8 emphasis cells in STANDARD section 3 need no change.

## Coverage, ownership and the lens checklist

- **Coverage:** all 68 ids are owned once (63) or placed in another subject (5, library-excluded.csv); the five
  receiving rows were confirmed for science (`sk-define-problem` names V.B.1). Every row names at least one id.
- **Ownership against the continuum emphasis:** sound except finding 3 (one grade early) and finding 7 (K to 2 checks).
  The heavy-owner grades are 3 and 4 (8 each, 7 and 9 after finding 3); K to 2 own 4 ids between them, which is the
  "with help" rule working, not a gap, once finding 7 adds the grade checks.
- **assumes, hands_on, models, words:** no gap, skip or early model (checks above). Words are taught at or before use
  and fit the grade.
- **cross_subject:** all 48 leans are real rows in time; the leaned-on rows teach what the lean says, with the two
  wording faults in finding 13.
- **Pace:** K 7, 1 8, then 9 a grade to 5, 8, 8, 7 in 6 to 8, 7, 6, 6, 5 in 9 to 12; no strand stops and restarts
  (lateral reading runs 5 to 12, citation 2 to 12, search 3 to 12). Count judgment in finding 10.

| Lens line (progression layer) | Mark |
|---|---|
| A one-off orientation instead of a year of spaced units | Met: rows every year K to 12 |
| A grade with no named priority skills | Met after finding 7 (K to 2 checks) |
| A skill owned twice at the same depth | Met (gate and own check) |
| A skill the continuum places two or more grades later, taught with no reason | Met: none found two grades early; one a grade early against ELA (finding 3) |
| Lateral reading owned by library and social studies with no line on who teaches first | Met: `g6-lateral-reading`, `g8-news-lateral` |
| Source judging as a page checklist | Met: lateral from grade 5, page features only as the maker's name in K to 4 |
| Honest use in every band, at the lens's depth | Part: fair use depth missing at 9 to 12 and wrong at 8 (finding 1) |
| No paid database or library assumed | Met: `g9-databases-operators`, `k-library-visit` |
| No product or company named | Met: kinds named generically throughout |
| No claim that the method raises scores | Met: `g9-lateral-method` cites an amount only |
| Scope and sequence, unit and day lines | Not applicable at this layer |

## Sensitivity read (progression layer)

- **K to 5 neutrality:** met row by row (`g2-two-books-differ`, `g4-own-question`, `g5-evidence-notes` carry the rule);
  the two examples in finding 5 (school meals, a family member's job) are the only slips.
- **Interviews, surveys, outside people:** finding 5.
- **Personal data:** met; names never typed (`g1-device-stop-rule`, `g3-safe-searching`), initials on public work
  (`g7-class-wiki`, `g10-label-own-work`, `g11-publish-for-audience`), self-disclosure optional (`g10-own-lens`,
  `g12-community-stand`).
- **Machine-made text:** finding 6; no row claims a tool is reliable or unreliable.
- **Honesty and copyright framing:** honest use without shaming in `g4-honest-use`, `g6-quote-paraphrase`,
  `g11-honesty-review`; copyright accuracy in finding 1.
- **Company and product names:** none.

## The writer's two questions

**(a) Grade 2 optional family-member interview (staff can stand in); grade 11 interview with someone whose life
differs, with consent and teacher-checked questions.** Within the pages' existing practice: social studies already
runs grade 2 family interviews about where a family came from (`ss2-family-interviews`, any trusted adult may stand
in), grade 3 interviews with family and neighbors, and grade 12 student interviews (`gov-policy-news`); library's grade
2 interview is milder (on the class topic) and optional. Grade 11 already has a no-interview path (first-person
sources). Expert view: keep both, with the tightened wording of finding 5 (topic not identity, no classmate as
spokesperson, supervised setting, parent consent under 18, no full names). No Cory call needed.

**(b) Grade 4 class survey (neutral questions, no names) owning V.C.2.** Right owner and within the rules: V.C.2 asks
for a new way to find something out, and a class survey or an observation plan is the plainest form a grade 4 child
can run and explain; science already does a schoolyard count in grade 2 (`s2-habitat-diversity`). Expert view: keep
it, swap the lunch example (finding 5). No Cory call needed.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Fair use taught as four questions, credit alone not enough, safer path chosen; depth in grade 9 | Accuracy, and APPROACH item 6 forbids a lawful/unlawful verdict | data/progressions/library.csv |
| IV.B.4 owner moves from grade 3 to grade 4 | ELA's grade 3 limit; same students in both courses | data/progressions/library.csv |
| Grade 10 self-set topic, grade 12 publishing stated | STANDARD section 2 asks for the 9/10 and 11/12 difference | data/progressions/library.csv |
| Two-id rows get a two-part check | Each owned id needs its own scored task | data/progressions/library.csv |
| Interview and survey rule stated once as APPROACH "Sensitive ground" item 8, rows point to it | One rule, one place; restates existing practice | docs/courses/library/APPROACH.md, library.csv |
| Survey example: which read-aloud to hear again | Avoids school meals | data/progressions/library.csv |
| Machine-made text supplied by the teacher; no tool use required | Free, no accounts, age floors | data/progressions/library.csv |
| K to 2 priority checks and continuum difference notes on three rows | Bar part 11 item 2; STANDARD section 2 | data/progressions/library.csv |
| Lateral reading time stated as 300 minutes (seven 45-minute sessions) | Our session length | data/progressions/library.csv |
| `prototype` replaced by `draft; version` in g6 | Keeps the design cycle in science | data/progressions/library.csv |
| Same-grade order lines (either order, second retrieves) | The 6 to 8 course cannot promise to go first | data/progressions/library.csv |
| STANDARD stale sentences, section 5 ownership wording, US spellings | The repository shows them done; AGENTS spelling rule | docs/courses/library/STANDARD.md |

## For Cory

None. Both of the writer's questions sit inside practice the social studies and career education pages already set
(see above). The APPROACH item in finding 5 adds no scope; if the lead counts any edit to an approved approach page as
needing Cory's yes, it is a one-line yes on that item.

## What this read could not judge

- Each grade's rows against the continuum's bold cells, cell by cell: the band files are outside the repo and were not
  opened. Finding 7 rests on STANDARD section 2's own summary.
- Whether the receiving SEL and ELA rows name V.D.1, V.D.2, III.D.2 and V.A.1 (only science's V.B.1 line was seen).

## Sources

- docs/courses/library/STANDARD.md and APPROACH.md, the lens and bar part 11 (what the progression must hold).
- data/progressions/ela.csv, social-studies.csv, science.csv (cross-subject leans, ELA grade limits, existing
  interview and survey practice).
- From memory: 17 U.S.C. section 107 (the four fair use factors) and the US Copyright Office fair use index
  (copyright.gov/fair-use), not re-read for this report.

## Fix pass (2026-11-21)

All 14 findings applied as their fixes say; none went to Cory. The lead settled the writer's two questions (grade 2
family interview and grade 11 interview; grade 4 survey) as within existing rules: keep all three, tightened per
finding 5.

1. `g8-fair-use-basics`: the myth sentence replaced by the four questions, "giving credit alone does not make a use
   fair", and a safer path (public domain or openly licensed work, a smaller part, a link instead of a copy, or asking
   permission; the link was added by the lead); check is the four questions applied to a new case and a safer path
   chosen; teacher note says students never rule a use permitted or lawful (APPROACH Sensitive ground 6).
   `g9-open-licenses`: fair use in depth sentence added; `fair use` added to words.
2. `g10-synthesis-map`: standard `AASL.IV.D.2; ~AASL.I.D.2`, self-set topic sentence added. `g12-capstone-decision`:
   standard `AASL.I.D.3; ~AASL.I.D.2; ~AASL.VI.C.2`, publishing sentence added after the first sentence.
3. `g3-notes-in-boxes`: standard `~AASL.IV.B.4`, boxes are the student's own research questions or the teacher's,
   "Checked alone" and "Owned here" dropped, ends "Grade 4 makes its own categories." `g4-evidence-notes`: standard
   `AASL.I.B.1; AASL.IV.B.4`, own-categories sentence and two-part check added, lean on `ela:e4-research` added.
4. Two-part checks written for `g6-team-product`, `g7-feedback-loop` (also "take sharp criticism calmly" replaced
   by "use critical comments to improve the product"), `g8-diverse-team` and `g10-others-views-in`.
5. APPROACH.md "Sensitive ground" item 8 written once (the fix's text, with home, food or meals and a family member's
   job added to the topics never asked about, per the lead). Rows point to it: `g2-group-research` (in-school example
   now "what a school job involves", family interview optional, staff can stand in), `g4-class-survey` (example now
   "which of three read-aloud books the class wants to hear again"; bird-feeder kept; note reads "survey rules"),
   `g4-asking-others`, `g10-others-views-in`, `g11-learn-across-difference` (group-label line added).
6. `g10-lateral-machine-text`: teacher-supplied summary, no tool or account. `g7-lateral-hard-cases`: "(invented or a
   dated capture)". `g11-honesty-review`: disclosure only if a tool was used, never required.
7. `g2-catalog-lookup`: grade 2 check and continuum difference note (also "or a subject word" dropped from the lookup
   so the row matches its own key-word line). `g2-who-made-it`: difference note. `k-picture-book-labels`: kindergarten
   check ("With help only" now "With help"). The band-file comparison remains for a later writer.
8. `g9-lateral-method`: 300 minutes (seven 45-minute sessions), the field study's six 50-minute lessons.
9. `g8-diverse-team`: teams mixed by first answers, never by background; stand-ins for a partner class.
10. `g11-method-note`: full citation sentence added; `citation style` added to words.
11. Order sentences added to `g6-lateral-reading`, `g7-citation-style`, `g3-source-kinds-and-makers`,
    `g8-news-lateral`.
12. `g6-make-and-improve`: words `draft; version; trial; improve`; notes end with the science design cycle line.
13. STANDARD.md: both owed rows (gate support, Catalog) done; section 2 table sentence now points to
    data/progressions/library.csv; section 3 header and gate sentence fixed; section 5 ownership lines (`e4-research`,
    `e5-locate-sources`) and the re-read sentence fixed; US spelling throughout (catalog, license, program).
    aasl-words.txt and the lens not edited (lead); APPROACH.md "judgement" and "licence" outside item 8 left for its
    next edit, since only item 8 was touched.
14. docs/ADOPTION-BAR-SUBJECTS.md library owed row replaced as the fix says ("relabelled" to "relabeled" in the same
    row).

Gate after the pass: `progression.py check library`, 98 rows, 0 failures.

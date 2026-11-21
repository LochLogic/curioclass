# World languages pre-work: stage 1 fix pass, 2026-11-21

World languages stay SHELVED (Cory, 2026-11-11; restated 2026-11-20); this pass fixes pre-work pages only and
unshelves nothing.

Read: AGENTS.md, docs/agents/EXPERT.md, the lens (docs/agents/lenses/world-languages.md), docs/COURSE-RUN.md stage 1,
docs/courses/UNIT-PLAN.md (rules and both field lists), the two pages (docs/courses/world-languages/STANDARD.md and
APPROACH.md) and data/standards/actfl-wrs.txt; the second-model read (docs/reviews/prework-world-languages-gemini-2026-11-20.md,
the main list), the real-page findings in both calibration reports (docs/reviews/calibration-world-languages-2026-11-20.md
and calibration-world-languages-gemini-2026-11-20.md, with the Gemini calibration report's findings 15 and 16 read
in S:/CurioClass-gemini/reports for their detail), the first read (docs/reviews/prework-world-languages-read-2026-11-20.md)
and later.csv rows L96, L92 and L93. Settled calls read first in DESK-ANSWERS: "After-core pre-work calls
(q-prework-open-1, q-prework-open-2)", "Health catalogue split (q-fix-health-1)", "PE fix pass calls (q-fix-pe-1)",
"Arts fix pass calls (q-fix-arts-1)", the can-do paraphrase call and "Ten Spanish tools". Checked at source, not taken
on trust: scripts/standards.py run against every id in actfl-wrs.txt (13 of 22 fail, as the reader said);
scripts/progression.py STD_FILES, ANCHOR, GRADES and lean_timing (keys are per subject; forward leans fail);
data/courses.csv (column is `subject`); ADOPTION-BAR-SUBJECTS part 6 item 9 and the owed row (still say video);
docs/FOUNDATION.md section 7 (Spanish and rights are agent reads); health APPROACH.md (the steps for when a student
tells you something); one web search on the 2024 guidelines (a search summary lists Distinguished; text not opened).
The reader's hours-to-proficiency figures (LTI, FSI) were not checked and nothing rests on them.

## Findings

| # | Source | What | Decision | Where |
|---|---|---|---|---|
| 1 | gemini #1 | STANDARD.md said scripts/standards.py accepts actfl-wrs.txt; 13 of 22 ids fail today | fixed (tested) | STANDARD.md section 1, "Validator"; actfl-wrs.txt header note; follow-up 1 |
| 2 | gemini #2; calibration gemini #11, expert #11 (part); L96 | Pages still written for one course per language after Option D: header table, section 2 French as an open question, section 5 "same course" and an Option B catalogue sentence, the questions record not marked answered, APPROACH pacing "settled by no one" and "a K to 5 learner has the same course" | fixed | STANDARD.md header table, sections 2, 3, 4, 5, "Questions for Cory (as asked)" opening line; APPROACH.md "Pacing and dose" |
| 3 | gemini #3; calibration gemini #12 | Plan fields placed against UNIT-PLAN.md: withdrawal day in unit field 7, room in unit field 8, task goal in section field 2, "who holds it" in section field 5, remedy in unit field 6; missing limits (unit 2), first-line token (unit 4), separate response time and the understand items' marking (unit 7), tools list (unit 8), codes, share and limits (section 1), owned item numbers (section 3), instruments and the room with nothing (section 5), who holds and tool by part (section 6) | fixed | APPROACH.md, "What world languages add to the unit and section plan fields"; "Error register in this subject" |
| 4 | gemini #3 | Judged marking at one minute a learner a task is about 50 minutes for 25 learners, over a 35-minute session | for when unshelved | below |
| 5 | gemini #3 | Rule 15 (quote the verb exactly) has no world languages override, though ACTFL wording may not be quoted | follow-up | follow-up 3; APPROACH.md unit field 2 points to STANDARD section 1 meanwhile |
| 6 | gemini #3 | "World-Readiness" named on a unit plan breaks the public-page rule | not a fault: unit plans are planning documents, and the public-page rule (STANDARD section 1) binds public pages; the line now says "world language standard" anyway | |
| 7 | gemini #3 | Level 1 Unit 1 assumes no earlier rows; which field 4 first line fits | for when unshelved | below |
| 8 | gemini #4.1 | No ownership line for the early-years companions | fixed: a companion targets the same level as its Level 1 or 2 course (Option D's own definition), so it uses that level's rows | STANDARD.md section 6, "Ownership for the gate" |
| 9 | gemini #4.2 | Page said one `world-languages` key in STD_FILES and ANCHOR, though each language is its own progression and the script keys by subject | fixed | STANDARD.md section 6, "What scripts/progression.py would need" |
| 10 | gemini #4.3; calibration gemini #15; first read #3 (still open) | The script fails forward leans by grade, and a level has no grade, so the page's lean rule could not be run | fixed: the gate needs list names the lean-timing change | STANDARD.md section 6; follow-up 4 |
| 11 | gemini #4.4 | Strand id files not on the owed table | fixed | STANDARD.md header table, new row |
| 12 | gemini #5.1; first read #1c (still open) | The depth ladder is named as the real progression but not written | fixed: the page says it is not written and is written with the progression once the 2024 guidelines are read at source (writing it now would rest on unread sources) | STANDARD.md section 6 |
| 13 | gemini #5.2 | "the level's stated length" points at a length no page states | fixed: the course frame states it (not set yet) | APPROACH.md "Supports" |
| 14 | gemini #5.3 | No own-words file for the 11 WRS ids, no check rule for Communities 5.1 and 5.2 | for when unshelved | below |
| 15 | gemini #6 | Level 4's Intermediate High exit looks out of reach at 63 hours a level | for when unshelved: Cory set the dose, the exit targets are marked ours and untested, and the page already says the hours are not shown to reach them | below |
| 16 | gemini #6; gemini question 2 (dose part) | No dose for the early-years companions | fixed: Cory's 3 sessions of 35 minutes covers them | APPROACH.md "Pacing and dose" |
| 17 | gemini #7.1; calibration gemini #16c | A Spanish-speaking teacher listed as a person read, tied to ASL, against FOUNDATION section 7 (Spanish is an agent read) | fixed | APPROACH.md "Sensitive ground", Reads |
| 18 | gemini #7.2 | No `rights` read for authentic texts, recordings and outside images | fixed (FOUNDATION section 7, rights agent) | APPROACH.md "Sensitive ground", Reads |
| 19 | gemini #7.3 | No steps for when a learner tells you something | fixed: points to health's steps, as PE and arts do | APPROACH.md "Sensitive ground"; section field 1 |
| 20 | gemini #7.3 | Leave-out not made honest | fixed: a left-out unit's ids are named as not claimed that year, the arts, PE and SEL pattern | APPROACH.md "Pacing and dose" |
| 21 | gemini #8.1 | Nothing helps tell a form gap from a missed task (C11) | fixed: one key line | APPROACH.md "Supports" |
| 22 | gemini #8.2 | A Spanish home table where the adult does not speak Spanish claimed an exchange (scripted) | fixed: the ASL caveat now covers both languages | APPROACH.md section field 10 |
| 23 | gemini #9.1; calibration expert #15, gemini #16d; L96 | ADOPTION-BAR part 6 item 9 "[O] Materials are video" and the owed row "decide the video source" stale against graphics only (Cory 2026-10-27) | follow-up | follow-up 2 |
| 24 | gemini #9.2 | courses.csv column called `track` | fixed (`subject`) | STANDARD.md section 2 |
| 25 | gemini #9.3 | Distinguished "not checked" for 2024 | fixed, marked as a search summary of the ISBE copy (text not opened) | STANDARD.md section 1; actfl-wrs.txt header note |
| 26 | gemini #9.4 | Second ASL scout missing from sources | fixed | APPROACH.md "Evidence and sources"; STANDARD.md header table |
| 27 | calibration expert #11 | courses.csv holds one all-level row per language | for when unshelved (catalogue rows); the page now says 12 rows are drawn then | STANDARD.md section 5 |
| 28 | calibration expert #12 | "A learner who is Deaf or hard of hearing is a signer first" assumes what the page says is never assumed | fixed | APPROACH.md ASL, "Access" |
| 29 | calibration expert #13 | Clerc structure stated as fact while marked not checked | fixed: given as the search summary's description | STANDARD.md section 4 |
| 30 | calibration expert #14 | Can-do and ASL check wording against L92 and L93 | fixed: section 3 points to Cory's note (L92); drawings and Reads point to the open L93 | STANDARD.md sections 3 and 4; APPROACH.md ASL and Reads |
| 31 | calibration gemini #16a | The paraphrase note names NCSSFL and ACTFL on public pages | not a fault: settled call (DESK-ANSWERS, "Can-do and ACTFL statements ship as paraphrases with the note"), and the licence asks for attribution | |
| 32 | calibration gemini #16b | The "before you teach" block in English and Spanish, while site-wide Spanish is parked (L60) | for when unshelved: the approach page was approved with it, and it touches nothing until a unit is written | below |
| 33 | gemini question 1 | Who reads ASL pages | not a fault: already open with Cory (L93); no new question | |
| 34 | gemini question 4 | The ASL scout's questions (Deaf co-author, Open Course Library files, a fingerspelling start, a credit) | for when unshelved | below |
| 35 | lens | The lens says "a Deaf signer checks them" as a rule while L93 is open | follow-up | follow-up 5 |
| 36 | first read #8b | One PDF address for the extracted text | not a fault: the header now names the actfl.org PDF and says the text was extracted from the Utah copy | |

Counts: fixed 22, not a fault 4, questions for Cory 0, follow-ups 5 (rows 1, 5, 10, 23, 35), notes for when it is
unshelved 7 (rows 4, 7, 14, 15, 27, 32, 34) plus the companion ids below.

## Questions for Cory

None. Nothing found blocks the pre-work from being correct; the one open people call (who reads ASL pages) is
already L93.

## For when it is unshelved

- Catalogue: the 12 Spanish and ASL rows under Option D (ids, grade ranges, which grades take a companion) and French's
  rows, drawn with Cory (rows 2 and 27; the reader suggested `spanish-k5-1` style ids and `k-5` and `6-12` ranges,
  not adopted).
- Marking time: judged exchange and presentation tasks at one minute a learner each do not fit a 35-minute Check day
  for a class of 25; the frame says how (two Check days, judging during partner rounds, or fewer judged tasks) (row 4).
- Field 4 for Level 1 Unit 1, which has no earlier rows: which first line (`Start-of-year check:` with a tiny task, or
  a gate exception) (row 7).
- An own-words file for the 11 WRS ids listing each standard's parts, so C1 can be checked, and a rule for how Level 1
  teaches and checks Communities 5.1 and 5.2 inside the room (row 14).
- Read the CASLS hours page and the 2024 guidelines before the frames, then bring the Level 4 exit against 63 hours a
  level to Cory with the reader's two ways through (lower the ladder, or a daily-period high school track) (row 15).
- Whether the "before you teach" block is bilingual or English only, given site-wide Spanish is parked (L60) (row 32).
- The ASL scout's four questions (docs/reviews/world-languages-asl-material-2026-11-21.md) go to the Desk with L93
  (row 34).

## Follow-ups for the lead

1. scripts/standards.py: add `('World-Readiness', 'actfl-wrs.txt')` to LISTED (13 of 22 ids fail validate() today:
   the 11 numbered WRS ids, ACTFL.Superior, ACTFL.Distinguished); keep the CLOSED patterns if any module row still uses
   a bare goal-area code. Now or at unshelving, the lead's call.
2. docs/ADOPTION-BAR-SUBJECTS.md part 6: item 9 "[O] Materials are video" and the owed row ("Decide the video source
   for American Sign Language, which may mean people on camera"; "Cory decides the split and the video") to say graphics
   only (Cory 2026-10-27) and that the split is Option D; "Two courses today, each all levels" stays until the pass
   opens if the lead reads Cory's French answer (bar wording corrected then) as covering it.
3. docs/courses/UNIT-PLAN.md rule 15: a world languages line like the arts and computer science ones (the standard's
   wording is not quoted; the unit plan states each part in our own words with the id).
4. scripts/progression.py, when the pass opens: `spanish` and `asl` keys in STD_FILES and ANCHOR, a level list for
   them, a code_grades rule for WRS ids, and a lean-timing rule for level-keyed rows (STANDARD.md section 6).
5. docs/agents/lenses/world-languages.md, ASL paragraph: "and a Deaf signer checks them" to say who checks is open
   (later.csv L93), matching APPROACH.md "Sensitive ground", Reads.

Lead, 2026-11-21: follow-up 5 done (the lens says who checks ASL pages is open, L93); 1 to 4 are filed in later.csv L97. No questions for Cory, so the pre: row is done; the subject stays shelved.

## Follow-up 1 done (2026-11-21)

scripts/standards.py now reads actfl-wrs.txt as a listed file (WRS ids as World-Readiness, levels as ACTFL): all 22 ids
pass, and an id not in the file still fails. STANDARD.md section 1 and the file's header note say so. The course stays
shelved.

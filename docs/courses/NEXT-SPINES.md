# Sara's work

**Redone 2026-11-11, night.** Cory accepted a cold review of the whole project
(docs/reviews/strategic-review-2026-11-11.md) and asked for this list to be rebuilt so you can start. Three things
changed for you:

- **Spec fixing has stopped.** No more batches in docs/spec-fixes/. A spec gets work only when a section plan names
  its tool.
- **One unit is being built all the way down first** (grade 4 math, unit 11). Until a teacher has read it, no
  new scopes and sequences, progression pages, unit plans or section plans are written. They came off this list. They are kept
  at the bottom under "On hold".
- **Small choices no longer go to Cory.** The curriculum expert settles them and they go in a weekly digest.
  Cory decides scope, audience, money, outside people, and anything that moves a standard between units.

The pieces are in order of what is waiting on them: the piece with the most waiting comes first. Core subjects
come first (BASELINE rule 24).

## Read first (once)

1. docs/HANDOFF.md, "Start here". It says what the main session is doing so you do not do the same thing.
2. docs/FOUNDATION.md. Nothing may contradict it. Section 7 changed: read it again.
3. docs/APPROACH.md and docs/reviews/approach-2026-11-11.md.
4. docs/agents/EXPERT.md (how the curriculum expert is run).
4a. data/plans/README.md. New 2026-11-11: check items and days are rows of data now, a script checks every answer
   key, and the tables in a plan are built from the rows. Short, and it changes pieces 1 and 4.
5. docs/RUBRIC-MATH-K8.md (the model for a rubric file).

## How every piece is made

1. **Gather.** Read what the piece rests on. For outside sources start from docs/APPROACH-SOURCES.md. No library
   access: a paywalled source stays unread and nothing may rest on it.
2. **Draft.** One file, in the place named. Plain words. A claim about a standard quotes its verb and code. A claim
   about how students learn names a source that was opened, and says how much of it was read.
3. **Expert read.** A fresh agent told to read docs/agents/EXPERT.md first and follow it, given the file and what
   will be built on it. Report in docs/reviews/<what>-<date>.md. **Every draft gets this read. You are never the
   only reviewer of your own draft.**
4. **Revise once** from the report. Item-level choices the expert settles are applied. Anything on Cory's list above
   goes to him as a question card on the Review Desk with a pick, and is marked in the draft "Proposed, waiting
   for Cory's yes".
5. **Record and push.** Tick the piece, add one dated line to docs/agents/decisions/DESK-ANSWERS.md, commit and
   push your own files.

**Your part, Sara.** You are the one human in the loop. Read each draft as the teacher who would have to use it,
and write what you see at the top of the review file under "Sara's read". The expert checks sources. You are the
one who can say "no one could teach this in a week" or "this order would lose my class".

## Where you are (2026-11-12)

Pieces 1 and 2 are done except your own read. **Next is piece 3 (science).** Your read is owed at the top of
four reports: unit-plan-s11-2026-11-12.md, rubric-ela-2026-11-11.md, approach-ela-2026-11-11.md and
rights-ela-6-s2-2026-11-11.md (all in docs/reviews/). The s11 one matters most: the pilot is built from it.

Cory answered the six ELA questions on 2026-11-12 (docs/HANDOFF.md, "Decided 2026-11-12"). All six went the
expert's way, with two additions: we find our own fallback hero text, and background text two carries a note
to upgrade to a free source later.

## The pieces

### 1. The pilot unit's plan: cold read, then your read

**Waiting on it: the pilot build, and through it the templates, the cost of a unit, and the plan with sizes and
dates for all 105 courses. Do this first. It is short.**

- [x] First run `python -X utf8 scripts/plan.py check`. It reworks every answer key and checks coverage, reused
      numbers and minutes, so the expert does not spend its read on those. It passes today.
- [x] Run the curriculum expert cold on `docs/courses/math-4/s11.md`, starting it from the reading pack
      (`python -X utf8 scripts/plan.py pack math-4 11`). Ask what the script cannot see: is each question a good
      question, are the six parts the right reading of the standard, does each day teach what its goal says
      and fit its minutes, are the wrong answers the ones children really give, could a lesson writer work from
      this. Also ask which sentences of prose only repeat a table, so they can be cut.
      Report: `docs/reviews/unit-plan-s11-<date>.md`. Revise once: a fact changes in `data/plans/math-4/`, then
      `scripts/plan.py tables`; only judgment changes in the prose.
- [x] Log each finding: `python -X utf8 scripts/plan.py defect math-4 s11.md plan expert <kind> "<what>"`. Your
      own findings use `sara` in place of `expert`.
- [ ] "Sara's read" at the top of that report: could you teach these five days? Where would a class get stuck?
- 2026-11-12: check run, expert read done (15 findings, none for Cory), plan revised once, findings logged.
  Only "Sara's read" is left.
- Tell the main session (or Cory) when it is done. The build waits for it.

### 2. English language arts: rubric file, approach page, and the rights list

**Waiting on it: the first ELA pilot (five days of grade 6, unit 2), which runs as soon as the math pilot has
been read, and behind it all 13 ELA courses. The rights work has the longest wait of anything here, so it starts
now.**

- [x] docs/RUBRIC-ELA.md (grades 3 to 8, and 6 to 12 where the guide differs). Shape of docs/RUBRIC-MATH-K8.md:
      what the rubric asks, indicator by indicator, in our own words, with a link. The source text is all rights
      reserved: link and summarise briefly, never copy, and keep it to structure.
- [x] docs/APPROACH-ELA.md. From docs/reviews/approach-2026-11-11.md, finding F1: the text is the unit; text
      complexity; text sets that build knowledge; volume of reading; the writing process and calendar; vocabulary
      from the texts; foundational skills in the lower grades; the daily question is about the text; modelled
      reading and writing; "fluency" means reading fluency. Sources: the ELA standards and appendices, the
      publishers' criteria, the federal practice guides on comprehension, foundational skills and writing.
- [x] The rights list for grade 6, unit 2 only (docs/courses/ela-6-spine.md): for each text, does it exist,
      where a free legal copy lives, its licence in the publisher's own words with the address, its level. Put
      it in docs/courses/ela-6/RIGHTS.md. **You gather; you do not rule.** A second reader checks every licence
      line before a text is taught (FOUNDATION section 7). Mark each row "found, not yet second-read".
- Changes to which texts are taught go to Cory as a card.
- 2026-11-11: all three drafted, read cold by the expert, revised once. Reports:
  docs/reviews/rubric-ela-2026-11-11.md, approach-ela-2026-11-11.md, rights-ela-6-s2-2026-11-11.md. "Sara's
  read" is owed on each. Six questions for Cory and the notes for the scope and sequence are in
  docs/reviews/piece-2-cards-for-cory-2026-11-11.md.
- 2026-11-12, main session: the six questions are on the Desk as card `q-ela-piece-2`; the scope and sequence edits are
  applied to docs/courses/ela-6-spine.md; the sources are on docs/APPROACH-SOURCES.md; the findings are in the
  defect ledger. What the expert settled is listed in docs/reviews/DIGEST.md. When the Desk cannot be opened
  from your session, keep writing cards to a file like this one; the main session places them. Every rights row is still "found, not yet second-read".

### 3. Science: rubric file, approach page, and the pilot unit's materials

**Waiting on it: the first science pilot, and behind it all 14 science courses.**

- [ ] docs/RUBRIC-SCIENCE-K5.md (and 6 to 8 if the same guide covers it). Same shape, same copying rule.
- [ ] docs/APPROACH-SCIENCE.md. From the same finding F1: a phenomenon or design problem comes first; three
      dimensions in every end task; investigation days and materials tiers; no daily exit question (the notebook
      and the class model are the daily evidence); worked examples for calculation and data work only; models
      are revised, not withdrawn. It must read at least one source on hands-on science teaching, which nobody has
      read yet. Sources: A Framework for K-12 Science Education, the NGSS appendices, the EQuIP rubric.
- [ ] Name one unit of the grade 4 science scope and sequence draft to be the pilot (your pick, with a reason, as a card for
      Cory), and list every material it needs with a household stand-in. A science teacher reads safety and
      materials before the course is called finished; for now mark what you are unsure of.

### 4. Grade 4 math: the start-of-year check and unit 4's readiness items

**Waiting on it: day 1 of the course cannot run without the check, and day 24 points at readiness items that do
not exist. This is the one piece of grade 4 planning that is not frozen. It is yours; the main session will not
do it.**

- [ ] The start-of-year check (day 1). It must carry unit 1's three readiness items
      (docs/courses/math-4/s01.md). Written to the check rules in docs/courses/UNIT-PLAN.md.
- [ ] Unit 4's readiness items only (not the unit plan, not its unit plans).
- Write the items straight into `data/plans/math-4/items.csv` and `wrongs.csv` (how: data/plans/README.md), with
  a compute cell for every answer, and run `scripts/plan.py check` until it passes. Use unit `0` for the
  start-of-year check and `4` for unit 4's readiness items. No table is typed by hand.

### 5. Social studies: the content standard options

**Waiting on it: all 14 social studies courses. No social studies scope and sequence can start before Cory decides. Nothing in
the first three pilots waits on it, which is why it is fifth.**

- [ ] docs/reviews/social-studies-content-standard-<date>.md, expert read, revised once, then a Desk card.
- Cory, 2026-11-11: only the C3 framework is loaded, and it names skills, not content. He asked for better than
  "pick one state": "this may require a unification of content standards or possibly a 'high watermark' method".
- Three options side by side: (a) one state's set; (b) a unified set built from several states; (c) high
  watermark: where states differ, take the more demanding expectation. For each: which states' standards are
  strong and freely usable, the cost to build and keep current, how a state reviewer would see it, what it does
  to the 135 topics tagged to C3, and what it means for the named high school courses.
- Beside it, the values question: Cory leans to "the higher quality or rigor" where state instruments conflict.
  Say what that rule would do in three real cases.
- This is a scope decision for 14 courses, so no recommendation is owed before the options are laid out, and the
  main session reads it with the expert before it goes to Cory.

### 6. When the pilot unit is built: read it, and perhaps teach it

**Waiting on it: every time figure in the course. This opens when the main session says unit 11 is built.**

- [ ] Read the five lesson days as a teacher against the five questions in docs/pilots/README.md, and file your
      notes there. You are not the grade 3 to 5 reader Cory is looking for, and your read does not replace
      theirs; it comes first and is cheaper.
- If Cory asks: teaching the five days to one child, with the minutes written down, is test 2 in that file.

### 7. Small owed fixes

**Waiting on them: nothing yet, but each is a known fault in a file others read.**

- [ ] Three description notes in data/modules.csv (docs/HANDOFF.md, "Owed, smaller").
- [ ] Footnoted limits in data/standards/ccss-math-standards.txt.
- [ ] The errors in the science sequence.csv.
- [ ] A header (source, version, date, licence) for data/standards/ccss-math-focus.csv.

## On hold until the pilot unit has been read

Do not start these. They will be written to a template the pilot is expected to change.

- Cold reads of grade 4 math units 3, 9 and 10, and of docs/ADOPTION-BAR-SUBJECTS.md. (Still owed. They move
  back up when the plan template is settled.)
- Math progression pages for kindergarten to grade 2 and grades 6 to 8. Note for later: the K to 2 rubric counts
  major work at 75 percent of days, not 65 (docs/RUBRIC-MATH-K8.md).
- Grade 4 math units 4 to 8 (unit plans and section plans).
- The grade 3 and grade 5 math scopes and sequences, and the six other math scopes and sequences.
- The full grade 6 ELA text plan beyond unit 2.

## Rules for all of it

- **Shared band topics (decided, Cory, 2026-11-11).** English language arts has topics that belong to a band, not
  a grade (for example "Narrators and Points of View", grades 3 to 5). The topic and its tools stay shared. Each
  grade's scope and sequence claims the skill on its own days, with that grade's standard code and that grade's texts, so every
  standard has an owner in a course. Do not split a band topic into one per grade.
- No rows go into data/units.csv, and no tool is specced, built or changed from these drafts. A scope and sequence becomes real
  only with Cory's yes.
- No licence or rights judgment is final on your word or one agent's. Gather it, quote it, and mark it for the
  second reader.
- Nothing is sent to an outside person and no money is spent without Cory's yes.
- Do not edit the grade 4 math scope and sequence or the approach pages. If a draft shows one of them is wrong, write the finding
  in your review file and on a Desk card.
- No em dashes anywhere. Always "Curio Class" in full. Never say Curio Class was reviewed by, meets or is endorsed
  by anyone. Public copy names no companies.
- Do not touch the Word Wall files (data/closet, closet/words, data/media-manifest.txt).
- Where you are unsure, say so on the page. A marked guess is useful; an unmarked one costs a unit.

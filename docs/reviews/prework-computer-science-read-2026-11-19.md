# Computer science pre-work: cold read, 2026-11-19

Read as the curriculum expert (docs/agents/EXPERT.md). I did not write these drafts. Nothing was edited but this file.
Confidence is Firm, Likely or Judgment call on each finding. Anything that rests on my memory is marked "from memory".
No outside source was opened (none was asked for), so no finding here rests on the CSTA PDF itself.

## What I read

AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/computer-science.md; docs/ADOPTION-BAR-SUBJECTS.md (pass rule,
C1 to C16, part 5, the computer science row of "Before a scope and sequence"); docs/courses/computer-science/STANDARD.md
and APPROACH.md; docs/APPROACH.md; docs/courses/UNIT-PLAN.md; docs/reviews/computer-science-open-material-2026-11-16.md;
docs/reviews/prework-physical-education-read-2026-11-19.md (format only); the three csta-2026 files in data/standards
(headers, then counted by script). For stale-note checks only: the CSTA and SPAN lines of scripts/standards.py and
scripts/progression.py, LICENSE-CONTENT.md rows, data/subjects.csv line 8, docs/PRODUCTION-PATH.md progression lines.

## Verdict

The standard is sound as a list: every id is real, countable and unique, the counts in STANDARD.md and the file headers
match what I counted, and all 331 statements match the two id files one for one. The risk is that it is not yet
usable for the 6 to 12 courses (no rule or gate says which grade owns each MS and HS id, and the depth the page says
governs, the boundary statement, is stored nowhere), and the approach page fills only about half of the subject slots,
with its field numbers 7 and 8 pointing at the wrong fields. The one change that matters most: replace the "What
computer science adds to the plan fields" block with a full eleven-field block (finding 1), and add the supports,
devices, opening and ownership text below before asking for Cory's yes.

## What I counted (so nobody has to again)

| Check | Result |
|---|---|
| Foundational ids | 196, no duplicates, all match the pattern band-concept-subconcept-number |
| By band | EK 16, E1 16, E2 16, E3 19, E4 19, E5 19, MS 45, HS 46 (matches the header and STANDARD.md) |
| By concept | ALG 40, PRO 45, DAT 35, SYS 38, SOC 38 (matches) |
| Band by concept, smallest cell | 3 (every band has at least 3 ids in every concept, so all five concepts are forced into every course) |
| Numbering | contiguous 01 to N inside each band; numbers are shared across concepts, and a K to 5 stem (for example ALG-IM-03) repeats in every grade with a new statement; MS and HS numbers do not match the E5 stems |
| Specialty ids | 135: S1 73, S2 62; per area AIN 14/10, CYB 15/12, DSC 14/15, GMD 9/8, PHY 8/8, SWD 8/9, XCS 5/0 (matches) |
| Statements | 331 lines, one per id, same id set as the two id files (diffed), none under 25 characters, none malformed |
| Licence lines | statements file: CC BY-NC-SA 4.0 with attribution and "not CC BY" in the header; LICENSE-CONTENT.md has a matching row; id files carry the licence and "ids only" |

## Findings, most serious first

### 1. The approach page's field list is wrong and half empty

- **Where:** APPROACH.md "What computer science adds to the plan fields"; UNIT-PLAN.md section plan fields 1 to 11.
- **What is wrong:** The page numbers section fields 7 and 8 as "pair roles" and "the device count; the paper path". In
  UNIT-PLAN, field 7 is Talk and writing and field 8 is Practice that returns. A writer who follows the page puts
  device counts where the warm-up goes and has no home for the written task. Fields 9 (supports and extension) and 10
  (two rooms) are not mentioned at all, so C10, C11 and the one-screen and one-parent answers have no slot filled. Unit
  field 2 asks what is carried through the unit; the page gives the concepts (already in every id) and the unplugged
  path, and says nothing of what is carried. How a day opens (field 6) is missing (finding 2). Tools are not given a
  job rule beyond the shared page.
- **Cost:** A planner writes 138 plans' worth of field-8 lines in the wrong place; C7, C10, C11, C14 and C15 each lose
  their slot. Those are door or scored criteria.
- **Fix (replace the whole block with this text):**

> ## What computer science adds to the plan fields
>
> **Unit plan.**
> - Field 2: each standard's parts by verb; the practice the unit teaches, named by its group; what is carried
>   through the unit: the anchor program, algorithm or dataset (its name, the day it is shown whole, the day it is
>   withdrawn, the day students first build alone); the unit's unplugged days, counted.
> - Field 8: each tool with its day, mark, job and verdict; devices needed per pair; the paper stand-in for every
>   device day; the few-device and one-screen versions (see "Devices and rooms").
>
> **Section plan.**
> - Field 1: the notional-machine point (what the computer does with each line, in order) or, in a unit with no
>   code, the adult-level background; the common bug and what it shows.
> - Field 3: each day's evidence in the form set under "The form of daily evidence".
> - Field 4: each expected error as a wrong example beside a right one: a wrong program for code, a wrong statement
>   for a systems, data or society idea.
> - Field 5: what is carried and what happens to it: the whole worked program, then the same program with blanks or
>   shuffled lines, then modified by students, then withdrawn; the key moments and the tool that serves each; what a
>   room with nothing does.
> - Field 6: one row a day: kind in this page's words; how the day opens and for how long; who holds the worked
>   program (teacher, pair, student); tool part, mark, job and minutes at the device; work away from the device; the
>   evidence number.
> - Field 7: two or three planned questions, at least one of the form "what will happen if"; one written or spoken
>   task ("what I tested and what I changed"); its look-fors. Pair roles (driver, navigator) and the time they switch
>   go here.
> - Field 8: practice that returns: a three-minute trace or debug of an earlier unit's construct, the unit named. No
>   fluency target.
> - Field 9: English learners, access, check accommodations, reading load and extension, as set under "Supports".
> - Field 10: one child at home; one screen in the room.

### 2. How a day opens is not set

- **Where:** APPROACH.md (absent); docs/APPROACH.md principle 4 and UNIT-PLAN rule 13.
- **What is wrong:** UNIT-PLAN field 6 asks how each day opens and for how long; the shared page limits an opening task
  to ten minutes in math and leaves other subjects to their page. Computer science's page is silent, so a writer will
  open with a blank editor ("try it and see"), which the lens calls a sign of trouble.
- **Fix (add as a section):**

> ## How a day opens
> Every day opens in its first five minutes with one of three things. (a) A retrieval trace: a short program or
> algorithm from an earlier unit, "what happens?", answered on paper, three minutes. (b) The wrong example from the
> last exit ticket, if more than a third missed it. (c) For a new idea, one short concrete moment, unplugged, that the
> teaching then names. Teaching first is the default for anything new: no blank editor, and no "try it" on a construct,
> before one worked example has been shown and traced. In grades 6 to 12 a day may open with a predict task on a short
> given program (ten minutes at most; ours, untested) when students have all they need to attempt it. The day row gives
> the opening and its minutes.

Confidence: Firm.

### 3. Nothing says which grade owns each MS and HS standard, and the gate has no computer science support

- **Where:** STANDARD.md section 2 (rows "grades 6, 7 and 8" and "grades 9 to 12"); scripts/progression.py (STD_FILES,
  SPAN, code_grades have no computer-science entry); docs/PRODUCTION-PATH.md (layer 4 decides one owner grade per skill).
- **What is wrong:** K to 5 is easy: E1 to E5 name their grade. For MS (45 ids) and HS (46 ids) STANDARD.md says the "6 to
  8 scope and sequence places each id in a year" and "each id is fully met by grade 8". That puts placement in the
  scope and sequence, which is layer 5; the production path puts "which grade owns each skill" in the progression
  (layer 4), and the progression script cannot read computer science at all. The text also gives no rule for what the
  other two grades of the band do with an id (teach it again? build on it?), the same fault I found in the physical
  education draft. Nothing says HS ids are met by grade 12.
- **Cost:** A progression writer must invent the rule. Two writers will place the same id twice or in no grade, and
  C1 (door) fails on any id with no lesson.
- **Fix (replace the "grades 6, 7 and 8" and "grades 9 to 12" Note cells and add this rule to section 2):**

> **Ownership of MS and HS ids.** Each MS and HS id has exactly one owner grade in the course progression (layer 4):
> the grade where students are first taught it to the depth its boundary statement sets and checked on it. Other
> grades of the band that use the id again carry it as `~ID` (used in a new setting). Every MS id is owned by grade 8
> at the latest; every HS id by grade 12. Starting split (ours, untested): grade 6 owns about 16 MS ids, grade 7 about
> 16, grade 8 about 13 (ALG 4/4/3, DAT 3/3/3, PRO 3/3/3, SOC 3/3/2, SYS 3/3/2); each HS year owns 11 or 12, with every
> concept in every year.

Also: add `computer-science` to STD_FILES, ANCHOR and a code_grades rule in scripts/progression.py (MS to grades 6 to 8,
HS to 9 to 12, E bands to their own grade), so an id outside its band fails. Confidence: Firm.

### 4. Devices: two different things are called "unplugged path", and few-device and one-screen rooms are missing

- **Where:** STANDARD.md section 5 ("Every unit has an unplugged path"); APPROACH.md field 8 ("the paper path for every
  tool day"); bar part 5 item 5 (unplugged work in every unit) and C14 (paper path for every tool day).
- **What is wrong:** Bar item 5 asks for unplugged teaching days (the idea taught with cards or movement). C14 asks
  for a stand-in when a tool day has no device. They are different. Neither page separates them, and neither says what a
  class with six devices for thirty students, or one projector and no student devices, does. Separately, a few ids
  name a tool and cannot be fully met on paper: E4-DAT-DC-09, E5-DAT-DC-09, E5-ALG-ML-02, MS-DAT-DC-23, MS-DAT-DI-25,
  MS-PRO-PD-13, MS-ALG-PS-05, HS-DAT-DC-21, HS-DAT-DC-23, HS-ALG-ML-08, HS-PRO-PD-12, HS-PRO-PD-13, HS-SYS-HW-30 (a
  physical or simulated device). Claiming them met with no device would break C1 and C16.
- **Cost:** C14 is a door criterion, and a school with few devices is the ordinary case.
- **Fix (add to STANDARD.md section 5 and point to it from APPROACH.md):**

> ## Devices and rooms
> Three things are kept apart. An unplugged day teaches an idea with cards, paper or movement; every unit has at least
> one (kind: understanding). A device day is a day where a tool does a named job. A stand-in is how a device day runs
> with fewer devices. Every device day is written four ways (section fields 5 and 10): (1) one device per pair, the
> default; (2) a few devices: three or four stations on a rotation, the other pairs at a paper station on the same
> idea, every pair taking the keyboard role at least once; (3) one screen: the class runs the program together,
> predicts and votes before each run, and a student at the device takes each step; (4) no device: the same idea on
> paper, with trace tables, "be the computer", programs written on paper and checked by a partner. An id whose
> standard asks students to use a computational tool, train a model, or use documentation and libraries is met only on
> a device. On the no-device path that day teaches the idea and the course record marks the id "part met without a
> device"; the course never says the id was met.

Confidence: Firm.

### 5. The supports slot is empty (English learners, access, reading load, extension, check accommodations)

- **Where:** APPROACH.md (absent); C10, C11, C15; UNIT-PLAN section field 9.
- **What is wrong:** Nothing on English learners (code keywords are English words with other meanings: run, loop, bug,
  sort, cloud, mouse), nothing on a student who cannot see the screen, use a mouse or drag blocks, nothing on a reading
  load for code, nothing on extension on the same standard. The lens says tools must be keyboard-only and colour-free
  playable; the page does not carry that into any rule.
- **Cost:** C10 and C11 have no answer. C15 fails if a tool fails keyboard-only or colour-free play.
- **Fix (add as a section):**

> ## Supports
> **English learners.** Each unit names five to eight words taught in depth (for example step, repeat, if, variable,
> bug), each with a picture or a traced example, and two sentence frames: "First the program ___, then it ___" and "I
> predict ___ because line ___ says ___". Words with an everyday meaning (run, loop, bug, sort, cloud, mouse) are
> taught as two meanings. A student may answer a trace in numbers, arrows or the home language. Each key says which
> wrong answers can come from reading the words rather than from the idea, so a language gap is not marked as a
> content gap.
> **Access.** Every tool works by keyboard alone, needs no colour to tell things apart (shape or label as well), enlarges
> text without breaking, has no flashing, and offers a typed or list choice wherever it offers drag and drop; every block
> program has a text view. For a student who cannot see the screen, the unplugged version uses cards and objects they
> can feel, and code is read aloud one line at a time. No tool task is timed.
> **Reading load.** Grades K to 2: no code read alone (icons, read aloud). Grades 3 to 5: up to ten lines. Grades 6 to
> 12: up to twenty lines (ours, untested). Error messages are plain words we write.
> **Check accommodations.** Read aloud, oral explanation, a scribe, extra time at the device, the paper version.
> **Extension.** On the same standard: a second bug, a new case the program must handle, an explanation of why a
> second solution is clearer. Never the next grade's construct.

Confidence: Firm.

### 6. The boundary statement sets the depth, and it is stored nowhere; the sub-concept codes are never explained

- **Where:** STANDARD.md section 1 ("the boundary statement, not the one-line statement, sets the depth"); statements
  file header ("boundary statements ... not stored").
- **What is wrong:** C1 fails if a standard is taught below its wording's depth. A planner has the one-line statement
  only, so cannot see what is excluded (for example, what "iteration" may and may not mean in grade 2). Plans must
  "restate the depth in our own words" with nothing to restate from. Separately, no page says what the two-letter
  sub-concept codes mean (PD, RD, TR, VD, PS, ML, IM, DC, DI, HW, SE, NT, HI, HU, CE, ET); a progression writer must
  guess that DAT-IM and ALG-IM are different strands.
- **Cost:** Two writers set two different depths. The lens's first error ("taught below its boundary statement") cannot
  be caught.
- **Fix:** Add `data/standards/csta-2026-boundaries.txt`, same header and same licence line as the statements file
  (planning only, never copied into a page), one line per Foundational id (196 lines first; Specialty on claim). Add
  to STANDARD.md section 1: "The sub-concept codes are listed in the PDF's concept pages; the key is in
  csta-2026-subconcepts.txt (code, name, our one-line meaning, ours not CSTA's)." Whoever holds the PDF fills the key;
  I will not guess it. Confidence: Firm that depth is unreachable now; the file form is a judgment call.

### 7. UNIT-PLAN rule 15 cannot be followed for computer science

- **Where:** UNIT-PLAN rules 15 and the blank unit plan (`**CODE:** "the standard's words"`); STANDARD.md section 1.
- **What is wrong:** The unit plan quotes the standard's words. STANDARD.md says no page ever copies a statement,
  because the statements are CC BY-NC-SA and our pages are CC BY. A writer must break one of them.
- **Fix (add to STANDARD.md section 1 and as a computer science line under UNIT-PLAN rule 15):**

> Computer science: a plan names each standard by its id and gives its action as one verb or a short phrase in our own
> words; the CSTA statement and boundary statement are never quoted. The id's statement lives in
> data/standards/csta-2026-statements.txt for the planner, not on the page.

Check whether scripts/unitplan.py tests for quoted words (I did not read it). Confidence: Firm.

### 8. "Real, dated cases" conflicts with "no company or product names"

- **Where:** lens ("real, dated cases"); bar part 5 item 4; APPROACH.md "Society days: a short claim with one piece of
  dated evidence"; AGENTS.md (no company or product names where a student, teacher or family reads).
- **What is wrong:** Most real cases in bias, privacy, data and security are known by a company or product name. The
  approach does not say how a case is told. A second fault: "one piece of dated evidence" is one view, and the lens
  wants more than one view with a source.
- **Fix (add to the society day line):**

> A real case is told by what happened, not by the company or product: "a company sold a face-matching system to
> police; a 2018 study found it wrong more often for darker-skinned women" (example only; check the facts before use).
> The teacher page gives the date and the source's title and publisher in a source line, which is a citation and not
> a promotion. If a case cannot be understood without the name, choose another case or use a court or government record's
> own description. A society day gives two views and one dated source for each.

Confidence: Firm that the rule needs stating; the example is mine, from memory, and unverified.

### 9. Three standards ask students to use a generated-text tool, which our no-account, no-network tool rule does not allow

- **Where:** MS-ALG-PS-05 ("Use an AI tool to generate outputs"), MS-PRO-RD-18, HS-PRO-RD-18, HS-ALG-PS-05 (evaluate
  generated output or code); STANDARD.md section 5 (nothing installed, no account); bar part 5 item 7.
- **What is wrong:** A student cannot "use" such a tool in a single-file offline page with no account and no network.
  A third-party tool means accounts for children, a product name, and data leaving the device. The evaluate-output
  ids (RD-18, HS-ALG-PS-05) can be met on supplied outputs; the "use" id (MS-ALG-PS-05) cannot be met honestly without
  a live tool.
- **Cost:** C15 and C3 on one side, C1 on the other.
- **Fix:** For the three evaluate ids, say: "Curio Class supplies saved outputs and code samples (some right, some
  flawed) and students judge them for accuracy and use." For MS-ALG-PS-05, see For Cory 2. Separately, the lens says
  these ideas sit in every band; if a rule bars the word AI in public copy (it was given to me for this read, I did
  not find it in the pages I read), public pages for these days say "machine learning" and "computers that learn from
  examples", and the plan states that. Confidence: Likely.

### 10. Student privacy, accounts and online safety have no rules

- **Where:** STANDARD.md section 5 (only "no account is made"); APPROACH.md (absent).
- **What is wrong:** Several ids put children near real data and real systems: EK-DAT-DI-09 and E5-DAT-DC-09 (collect
  data in students' environments), E1-SYS-SE-12 and E3-SYS-SE-13 (accounts, personal information), MS-SYS-SE-33 and
  HS-SYS-SE-33 (attacks, a flaw in a system). Nothing says what data students may collect, where a program is saved,
  how accounts are taught without making one, or that no live attack is ever run on a real system.
- **Fix (add as a section):**

> ## Privacy and safety
> No student's name, photo, voice, location or family detail goes into a program, a dataset or a tool. Class data is
> about things (weather, pets drawn from a list, shapes, snack types), tallied by hand or with counts, never about
> identifiable children, health or home. Accounts, passwords and personal information are taught with a pretend page
> or a paper account; no student makes an account. Online safety days use paper or an offline pretend site; any real web
> use is teacher-led on one screen. Security days use toy systems built into the page; no scanning, no attack and no test
> of a real school or home system, ever. A tool stores student work only on the device or in a file the student
> downloads or prints; it sends nothing off the device.

Confidence: Likely.

### 11. The daily-evidence form does not work for kindergarten to grade 2, and does not say where student work lives

- **Where:** APPROACH.md "The form of daily evidence".
- **What is wrong:** "Answered in writing" and "one line from the student" cannot be done by most kindergarten and grade
  1 students. "The program itself ... a minute per student" is thirty minutes of reading for one class, times five or
  six classes a week for a specials teacher. It does not say where the program is read (the device, a print, a download)
  without an account.
- **Fix (replace the first two bullets and add):**

> Grades K to 2: the answer is a pointing, sorting or ordering task, or said aloud to a partner and noted by the
> teacher by exception; a program is checked on the screen during the day. Grades 3 to 12: as written below. A tool
> checks the look-fors it can (does the program do these three things on the tests?) and shows the student a "yes" or
> "not yet" for each; the teacher reads the open part (what I tested and what I changed) for a rotating third of the
> class each day, so every student is read at least once a week and twice if the exit ticket shows a gap. Student work
> is read on the device, or on a printout the student hands in.

Confidence: Likely.

### 12. The check day names a build task with no rubric or samples

- **Where:** APPROACH.md "Check: ... plus a short build or debug task"; bar part 5 item 8; C8 and C9.
- **What is wrong:** Bar item 8 and C9 need a rubric and sample work at two levels for every open task. The page does
  not ask for either, and does not say how the build task is checked on the no-device path.
- **Fix (add to the Check row):**

> The end-of-unit build or debug task has look-fors and two sample programs, one that meets them and one that does not
> (UNIT-PLAN field 5), and a paper version for a class with no device, marked as in "Devices and rooms".

Confidence: Likely.

### 13. The non-specialist teacher is covered in one line

- **Where:** APPROACH.md field 1 (only the notional-machine point); bar part 5 item 9 and its fails-if.
- **What is wrong:** The lens lists what a non-specialist needs (adult-level content, common bugs and what each shows,
  never assuming the teacher can debug on the fly). The approach does not.
- **Fix (add as a line under the plan fields):**

> A teacher page for a unit with code carries: the idea at adult level; a finished, tested solution to every program
> students write; each common bug as a wrong program beside a right one with what it shows; the exact message the tool
> shows for each bug; and "if you are stuck" steps a teacher can follow without writing code. A teacher is never asked to
> debug a student's program on the fly.

Confidence: Likely.

### 14. Pacing: no session length, no days per course, and a lopsided load

- **Where:** STANDARD.md section 2 "Minutes"; APPROACH.md (absent); bar C2.
- **What is wrong:** Sessions a week are settled; session length and weeks a year are not stated in these pages, so a
  planner cannot test C2 or the 10 percent rule. By my arithmetic (assuming 36 weeks and 30 to 45 minute sessions; ours,
  untested): kindergarten to grade 2 meet about 36 sessions for 16 ids, grades 3 to 5 about 36 for 19, so roughly
  two sessions per id once a respond day and the checks are taken out, which is tight for a program an id says to
  "create". Grades 6 to 8 meet 72 to 108 sessions for about 15 ids, and grades 9 to 12 meet 72 to 108 for about 11.
  The ratio between devices and paper is also unset, and a once-a-week class has six days between sessions.
- **Fix (add as "Pacing" to APPROACH.md):**

> Each course frame states weeks, sessions a week and minutes a session. Because K to 5 meet once a week, every session
> opens with the three-minute retrieval trace and every unit ends with a respond day. Ours, untested: kindergarten to
> grade 2 spend about two thirds of the time away from a device; grades 3 to 5 about half; grades 6 to 12 at least one
> unplugged day in every unit. A K to 5 unit lets two or three ids share one anchor program so one id is not one
> session.

Confidence: Likely.

### 15. High school has far more days than standards, and the rule against lengthening units leaves two bad choices

- **Where:** STANDARD.md section 2 "Specialty standards"; bar C1 (more than 10 percent of days on content outside the
  standards fails).
- **What is wrong:** Four courses at 72 to 108 sessions each (my arithmetic above) is about 290 to 430 sessions for 46
  Foundational ids, 6 to 9 sessions per id. "No unit is lengthened to reach a Specialty id" and "a unit may claim an S1
  id only when its task already goes that far" mean the extra days either go to the Foundational ids at a depth
  their boundary statements may not ask for, or to outside content (the UK base's media-making units are outside CSTA
  2026, by the scout's own note), which counts against C1.
- **Fix:** See For Cory 1. Confidence: Judgment call.

### 16. No rule for blocks to text, or which text language

- **Where:** APPROACH.md and STANDARD.md (absent); lens "Middle school assumes text code when elementary taught only
  blocks, with no bridge".
- **What is wrong:** HS-PRO-VD-16 (data structures), HS-PRO-PD-12 (libraries) and HS-PRO-PD-13 (APIs) assume text code.
  Nothing says when the move happens, or that language names are allowed as subject terms in student copy.
- **Fix (add as a rule; ours, untested):**

> Kindergarten to grade 5: block code with a text view of the same program. Grade 6: blocks and text side by side. Grade
> 7: text for new programs, blocks as a stand-in. Grade 8 on: text. One text language for grades 7 to 12, named as a
> subject term on teacher pages, chosen so it runs in a common browser with nothing installed.

Confidence: Likely.

### 17. Practices: the twelve are never named, and the bar's four do not map to them

- **Where:** STANDARD.md sections 1 and 3; APPROACH.md "unit field 2: the practice taught"; bar part 5 item 2 (working
  together, testing and fixing, abstraction, explaining).
- **What is wrong:** Practices have no ids, so units "name the practice by its group", but the twelve practices and their
  four groups are not listed. The bar's four come from another rubric, and CSTA's groups do not match them; "explaining"
  and "abstraction" have no home. Section field 1's practices line (a day and a task for each) is not asked for.
- **Fix:** Add to STANDARD.md section 3 a table, one row per CSTA practice (name from the PDF's practice pages, our
  one-line meaning, ours not CSTA's), with a column "bar item 2" showing which of the bar's four it serves or "none".
  Ask for it in section field 1: "Practices: the practice, the day, the task."
  Confidence: Likely.

### 18. The approach cites nothing it rests on, and says nothing about effect

- **Where:** APPROACH.md throughout; lens "Sources" (PRIMM, use-modify-create, notional machine and Parsons problems
  marked "not re-read"); docs/APPROACH.md ("every claim about how students learn rests on a source opened and read"); C13
  and C16; bar part 5 "Unsupported".
- **What is wrong:** "Understanding before modify before make" and "worked program, modified then withdrawn" rest on
  sources nobody on the project re-read. The page has no sources table, no statement that the course has not been tried
  with children, no logic-model line, and no rule that no page claims coding improves general thinking.
- **Fix (add as a final section):**

> ## Honest limits
> The order of days (read and predict, then modify, then make) is ours and untested; it rests on published practice
> that has not been re-read for Curio Class. No page claims that learning to program improves thinking in general or
> school results. The course has not been tried with children. A one-page logic model is owed at course level. Sources
> read for this page: none yet; each one added is listed with how much of it was read.

Confidence: Likely.

### 19. What a progression writer would get wrong

- **Where:** the 196 and the statements.
- **What is wrong, and the fix (ordering inside a band, ours):**
  - MS: MS-PRO-VD-16 before MS-ALG-PS-01 and MS-PRO-RD-17; MS-PRO-PD-12 before MS-PRO-RD-17; MS-PRO-RD-17 before
    MS-PRO-RD-18; MS-DAT-DC-23 before MS-DAT-DI-25 to 27; MS-ALG-ML-06 before MS-ALG-ML-07 and 08, and the data-quality
    ids MS-DAT-DC-21 to 24 before ML-07; MS-SYS-NT-34 before NT-35. MS-DAT-DI-25 (relationships among variables, make a
    prediction) leans on scatter plots and association in math, which I place in grade 8 (from memory); own it in grade
    8 unless the math frame teaches it earlier.
  - HS: HS-PRO-VD-16 before HS-ALG-PS-01; HS-PRO-PD-12 before HS-PRO-RD-17; HS-ALG-ML-07 before HS-ALG-ML-08; HS-ALG-PS-03
    after PS-01 and 02; HS-SYS-SE-31 and 32 before SE-33; HS-SOC-ET-40 and 41 before ET-42; HS-DAT-IM-27 before IM-28.
  - Stems line up inside K to 5 only (E3-PRO-PD-04 follows E2-PRO-PD-04). MS and HS numbers do not match E5's, so a
    writer must not assume the same stem across E5 to MS.
  - EK is taught whole in kindergarten but E1 repeats many of the same constructs (sequence, debug, events); mark the
    K to 1 handoff weak in the progression rather than re-teach.
  - The same id is stated at a different depth in each band; a K to 5 course must not teach an id at its next band's
    depth.
- Confidence: Likely.

### 20. No gate stops a CSTA id turning up in the wrong grade or a Specialty id in a Foundational unit

- **Where:** scripts/standards.py lines 92 to 133 treat the two id files as one set; progression.py has nothing for
  computer science (finding 3).
- **What is wrong:** An E5 id in a grade 3 plan, or any S2 id, passes `plan.py check`. STANDARD.md's "no S2 id is
  claimed in a Foundational course" is a rule nothing enforces.
- **Fix:** A small check: band prefix to grade (EK to K, E1 to 1 ... E5 to 5, MS to 6 to 8, HS to 9 to 12); reject S2 ids;
  allow S1 ids only in grades 11 and 12 (or wherever Cory picks in For Cory 1). Confidence: Likely.

### 21. Stale or contradictory lines

- STANDARD.md, "One follow-up sits outside this subject's files: LICENSE-CONTENT.md ... needs a third-party line": that
  row is there now. Delete the paragraph; the header table's note on it goes too.
- csta-2026-specialty-ids.txt, last header note: "the checkers do not read this file yet" and "No module in
  data/modules.csv carries one yet". scripts/standards.py reads it (valid codes, line 92); "module" is not the glossary
  word. Replace with: "scripts/standards.py accepts these ids as valid codes (2026-11-11); no gate yet limits where one
  may be claimed. A unit may claim an S1 id only as STANDARD.md section 2 says."
- ADOPTION-BAR-SUBJECTS.md part 5, "Standards": "the 196 foundational codes ... with no header and no wording. The 135 ...
  are absent." Both are done (header 2026-11-11, wording and Specialty ids loaded). The same sentence then says they were
  loaded, so the paragraph argues with itself. Replace with: "Loaded (data/standards/): the 196 Foundational ids, the 135
  Specialty ids and the statements; see STANDARD.md."
- APPROACH.md: "Questions in this draft" holds only settled items; rename "Settled" or fold into the header. The header says
  "Short by design", which is no longer an excuse once findings 1 to 18 are in.
- docs/APPROACH.md, opening paragraph, lists approach pages for math and ELA and a short page for science and social
  studies; it does not mention the pages that now exist for other subjects, so a reader does not find computer science's.
- data/subjects.csv line 8 labels the standard "CSTA K-12"; the 2026 set is PK-12 (the K to 12 course list is still
  right).
- STANDARD.md says the 6 to 8 "scope and sequence" places each id (finding 3); the layer is the progression.
- Stated twice: "no account, nothing installed" in STANDARD.md section 5 and the bar; "an unplugged path" in both
  documents (finding 4). Keep the rule once, in STANDARD.md "Devices and rooms".

Confidence: Firm (each is checkable by reading the two lines side by side).

### 22. Licence soft spots

- **Where:** STANDARD.md section 1 ("Curio Class is free, so non-commercial is met"); the same page's "own words".
- **What is wrong:** Two things. (a) "Free" is not the test; the NonCommercial term turns on whether the use is mainly
  for commercial advantage. Curio Class's funding notes (from memory: a donation page and one philanthropy ask) probably
  keep it inside, but the sentence overstates. (b) A close paraphrase of a one-line statement may count as an adaptation,
  and ShareAlike would then ask for CC BY-NC-SA on that page. The page treats "our own words" as a way out without
  saying how far from the original the words must be.
- **Fix (replace the sentence):**

> Curio Class is free and sells nothing, which is the NonCommercial test as we read it; if a paid tier ever appears,
> this is rechecked. Our pages state what a standard asks in a new sentence, built from the plan's own task, never
> reworded line by line from the statement.

Confidence: Judgment call (not legal advice; no lawyer read this).

### 23. Four statements carry PDF line-break marks

- **Where:** csta-2026-statements.txt lines 129 (HS-DAT-IM-27, "large- scale"), 255 (S1-PHY-CI-04, "device- to-device"), 270
  (S1-SWD-UX-05, "human- centered") and 308 (S2-DSC-PP-13, "large- scale").
- **What is wrong:** The header says "unchanged except whitespace". These are spacing faults after a hyphen, so a
  planner searching "large-scale" misses them.
- **Fix:** Join each ("large-scale", "device-to-device", "human-centered", "large-scale") and add "four hyphen breaks
  after line-break repairs joined" to the header's fetch note. Confidence: Firm (mechanical).

## The bar and the approach, criterion by criterion

This rates whether the standard and approach pages give a planner what the criterion needs. It is not a rating of a
course (none exists). Pass = the line shows it; Part = something is there and a fails-if or a row is not answered; Fail = the page gives nothing.

### Part 5, computer science

| # | Verdict | Where, and what is lacking |
|---|---|---|
| 1 Coverage spans every concept | Pass | STANDARD 1 counts; the table above shows every band has at least 3 ids in each of the five concepts. Owed at the scope and sequence: a days share per concept |
| 2 Practices inside content | Part | STANDARD 3 names groups; APPROACH names pair roles and debugging. The twelve are never listed; bar's four unmapped (finding 17) |
| 3 Ordered ideas, band to band | Part | APPROACH "Order inside a unit". No ownership rule for MS and HS, no blocks to text bridge (findings 3, 16) |
| 4 Real, current cases | Part | APPROACH "society day ... dated evidence". Conflicts with no company names; one view (finding 8) |
| 5 Unplugged work in every unit | Part | STANDARD 5 asserts it; merged with the paper stand-in (finding 4) |
| 6 Technology built in, each tool has a purpose | Part | No tool job rule or tool kinds in the page beyond the shared rule 8; tools to build are not listed |
| 7 Common browser, nothing to install, notes for technical staff | Part | STANDARD 5 states browser and no install. No notes for technical staff |
| 8 Projects and code assessed, with rubrics | Part | "Check" names a build task; no rubric, no samples (finding 12) |
| 9 Teacher pages for a non-specialist | Part | One line (finding 13) |

Fails-if: "Block puzzles with no concepts named": Pass (unit field 2 names concepts; lens says goals name concepts, not
levels). "Nothing on data or society": Pass (forced by the id counts). "Install or account": Pass (STANDARD 5).
"No help for the non-specialist": Part (finding 13).

### Shared core rows that a layer 3 page answers

| Row | Verdict | Where, and what is lacking |
|---|---|---|
| C1 (door) Every standard named and taught in full | Part | Ids real and countable. Depth (boundary statement) not stored; MS and HS grade ownership unset (findings 3, 6) |
| C2 A year plan with reasons | Part | Not this page's layer, but session length and weeks are unstated (finding 14) |
| C3 (door) Nothing wrong, nothing sold | Part | No promotion in the pages. Cases conflict with no company names (finding 8) |
| C4 Each idea rests on the last | Part | Order inside a unit is stated; band handoffs, ownership and ordering constraints are not (findings 3, 19) |
| C5 Overview prepares the teacher | Part | Field 1 notional-machine point only (finding 13) |
| C7 Taught, then faded, returning | Part | "Modified then withdrawn" and "day students first build alone" are there. No fading ladder, no holder per day, no practice that returns (finding 1) |
| C8 Assessment system | Part | Daily evidence and check day are there; K to 2 form, rubric and samples are not (findings 11, 12) |
| C9 Teacher can score and act | Part | Error letters yes; rubrics and samples for the build task no (finding 12) |
| C10 Every learner on the content | Fail | No supports, extension, reading load or access (finding 5) |
| C11 English learners inside the lesson | Fail | Nothing (finding 5) |
| C12 Care and range | Part | Not addressed on the page; the values rule is named by the lens only. Sensitivity read owed per unit |
| C13 Approach explained, families told | Part | Draft page, no sources, no family note slot (finding 18) |
| C14 (door) Ordinary room | Part | Paper path stated; few-device, one-screen, class size and teacher knowledge not (findings 4, 13) |
| C15 Screens serve learning | Part | Browser, no install, no account stated. Keyboard-only, colour-free, and where work is stored are not (findings 5, 10) |
| C16 Honest about evidence | Part | Header says "ours, untested"; no effect ban, no logic model line (finding 18) |

Two doors (C1, C14) and C3 are Part, so the draft cannot go to a scope and sequence unfixed. C10 and C11 are Fail.

## Questions asked

- **Is the standard made usable?** For K to 5, yes. The 196 ids are real and countable; E1 to E5 name their own grade; the
  specialty ids are explicitly left out (no S2 in Foundational courses; S1 only where a unit already goes that far) but
  no S1 list, gate or day budget exists. The statements give each id a usable one-line meaning, and the reuse terms
  in the file headers are respected by both pages (no statement is copied; the credit line is given). Not yet usable
  for MS and HS (finding 3) and for depth (finding 6).
- **Devices and access:** findings 4, 5, 9, 10. No company or product names appear in the pages; the pressure is from the
  society cases and the tools (findings 8, 9).
- **Stale, contradictory, stated twice:** finding 21.

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Unplugged day (idea) and stand-in (fewer devices) are separate things | Bar item 5 and C14 ask for different things | STANDARD.md section 5 |
| A device-only id is marked "part met without a device" on the paper path | C1 and C16 forbid claiming it met | STANDARD.md section 5; course records |
| Day opens with a three-minute retrieval trace, a wrong example, or one concrete unplugged moment; no blank editor | Teaching first, lens | APPROACH.md |
| Starting split of MS ids 16/16/13 by concept; HS 11 or 12 a year | Even load with every concept in every year (ours, untested) | STANDARD.md section 2 |
| Ordering constraints listed in finding 19 | Each id leans on an earlier one | the progression |
| Blocks K to 5, side by side in 6, text from 7 or 8 (ours, untested) | Lens: no bridge is a fault | APPROACH.md |
| Reading load caps: none alone K to 2, ten lines 3 to 5, twenty lines 6 to 12 | A number, inside the standards' limits (ours, untested) | APPROACH.md |
| Four hyphen breaks joined in the statements file | Mechanical | csta-2026-statements.txt |
| One piece of dated evidence becomes two views and one dated source each | Lens: society with evidence | APPROACH.md |

## For Cory

1. **High school days and the Specialty standards (finding 15).** Four courses give far more days than 46 Foundational ids
   need. Do years 3 and 4 claim a short named list of S1 ids as in-course standards (taught and checked in full,
   counted so C1's 10 percent is not hit), or do the extra days go to deeper projects on the Foundational ids alone?
   Recommended: let grades 11 and 12 claim S1 ids, no new courses, and S2 stays out.
2. **The live generated-text tool (finding 9).** MS-ALG-PS-05 asks a student to use one. Recommended: no live tool in Curio
   Class; the day is teacher-run on one screen using a tool the school has already approved, with no student accounts,
   and the course marks the id "part met" where a school has none. The alternative is leaving the id out as unmet.
3. **Our own editor (the tools).** The UK base depends on named block-coding and board products, which our rules bar. Build
   one small browser editor of our own (blocks and a text view, with a step-through trace), single file, no
   account, starting with grades 3 to 5, rather than pointing teachers to a third-party tool. Recommended: build, small
   first. It also settles the text language for 7 to 12 (finding 16).
4. **Society cases without company names (finding 8).** Is it right to name government bodies and courts, but never companies,
   in student and teacher copy, with sources only in the teacher source line? Recommended: yes.
5. **The word AI in public copy (finding 9).** If the rule I was handed exists, say whether public pages use "machine
   learning" and "computers that learn from examples", and CSTA's own terms stay in internal docs. Recommended: yes.
6. **Your yes on the approach page**, once findings 1 to 14 are in. It stays a draft until then.

## What is right and should not be touched

- The id files and their headers (counts, contiguity, licence lines, "ids only").
- The statements file's one-line-per-id form and its licence header, and the LICENSE-CONTENT.md row.
- "Order inside a unit: understanding before modify before make", and the kinds-of-day table.
- Daily evidence for modify and make days ("look-fors plus what I tested and changed").
- Physical computing stays optional with a simulator or paper stand-in.
- The scout's verdict: partial base from the UK curriculum for K to 8, checked unit by unit, high school ours.
- The rule that no S2 id is claimed in a Foundational course.

## Not checked

- The CSTA PDF itself: I did not reopen it, so I did not check any statement, boundary statement, practice name or
  sub-concept meaning against it. The id and statement files were checked against each other only.
- scripts/unitplan.py and scripts/plan.py: whether they reject quoted statements or check computer science codes.
- docs/FOUNDATION.md, BASELINE rules and the "values rule" (the lens cites it; I did not read it), so the rule on society
  content is taken from the lens.
- Whether SPEC or tool specs already cover an editor, a trace stepper or a model trainer.
- The UK curriculum's licence and unit lists (the scout's report was read, not its sources).
- Anything about the math, science or social studies frames' timing that finding 19 leans on (grade 8 association in
  math is from memory).
- docs/HANDOFF.md, DESK-ANSWERS and later.csv for decisions about AI wording or tool building; if they exist they override
  the corresponding recommendation.
- data/units.csv, closet words, media manifest and other forbidden paths: not opened.
- Whether the repo's other pages copy any CSTA statement (no repo-wide search was run).

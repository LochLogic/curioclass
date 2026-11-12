# Cold read of the lesson-day template and its worked case, day 90 of grade 4 math

Read cold on 2026-11-11 for the files dated 2026-11-12, by the curriculum expert (docs/agents/EXPERT.md). Read
in full: EXPERT.md, docs/courses/LESSON-DAY.md, courses/math-4/u11-1/d090.md, the day 90 rows of items.csv and
wrongs.csv, errors.csv, the day 89 to 93 rows of days.csv, every built page in build/lessons/math-4/u11-1/ (the
student PDF rendered to images and looked at), scripts/lesson.py, the gate half of scripts/plan.py,
docs/courses/math-4/DEFAULTS.md, the parts of s11.md that day 90 rests on (U3, U5, U8, U9, the day table),
docs/reviews/unit-plan-s11-2026-11-12.md, the tool spec, the Community Plot Planner section of TOOL-ASKS.md,
recommendations 1 to 12 and risk 10 of the strategic review, RUBRIC-MATH-K8.md, ADOPTION-BAR.md, the shared core
(C1 to C16) of ADOPTION-BAR-SUBJECTS.md, the ELA rubric's parts table, APPROACH-ELA.md "What ELA adds", BASELINE
rules 20 to 28 and LICENSE-CONTENT.md.

Both gates pass: `lesson.py check` (teacher 880 words, student 98, 60 minutes, 0 failures) and `plan.py check`
(30 items, 38 wrong answers, 0 failures). I reworked every day 90 key by hand as well; all fourteen are right.

## Verdict

The template is sound in its bones (one source file, questions as rows with computed keys, fixed headings,
minutes tied to the plan, a paper path every day, no slides) and day 90 is correct mathematics in a sensible
order that would teach a grade 4 class to find a missing side. The biggest risk is that the template's promises
run ahead of what the build makes: the display page that replaces slides shows only question text, the tool's
exit items sit outside the data, and a day can pass every gate while leaning on pieces that do not exist, so
15,000 days would inherit a "ready to teach" that is not yet true. The one change that matters most: before
Cory's yes, make the display page carry the pictures and the worked steps from data, and put every question a
student answers on any path (the tool's "On your own" included) into items.csv.

## Before Cory is asked for his yes, and what can wait

**Must change before the yes** (they set the shape of every later day): findings 1 to 7.
**Can wait for the pilot's taught run** (they tune sizes or one day): findings 8 to 13, and the day 90 item
choices under "Settled by the expert", which the caller can apply at once.

## Findings, most serious first

### 1. The display page does not yet do the job that justifies "no slides"

- **What is wrong.** The template says the display page shows "the worked examples, the wrong answers to fix and
  the planned questions". The built d090-display.html shows the four stems as plain text, the two "Ask."
  questions and the two sentence frames. There is no rectangle, no labelled sides, no worked step, no right
  working. The teacher page says the fixes go "on the display beside the right working"; the display has none.
  Example 1 relies on "grid paper under the camera", which assumes a document camera that DEFAULTS.md never
  names.
- **Evidence.** The built file. Illustrative Mathematics K-5, grade 4, unit 5, lesson 17 (opened today) lists no
  slide deck either, but it posts its diagrams and shows one statement at a time; that is the bar a "display
  instead of slides" has to meet. EdReports gateway 3 design (3r to 3u, RUBRIC-MATH-K8.md) looks for a look that
  helps thinking.
- **Cost.** A teacher opening the display finds a page of sentences and makes slides by hand, which is the very
  copy the rule meant to avoid. In a room with a projector and no camera, Example 1 has nothing to show.
- **Change.** In LESSON-DAY.md, define the display page as: for each worked example, (1) the stem with a
  generated, labelled figure, (2) the steps revealed one screen at a time; for each fix, the wrong working and
  the right working side by side; one screen per planned question; one "check your answers" screen for any
  partner or self check. To make that possible, items.csv gains two optional columns: `figure` (for day 90, a
  rectangle spec such as `rect w=7 l=? A=63`) and `steps` (the steps as the teacher says them, separated by
  `|`). The teacher page's spoken steps then come from the same cell, so the teacher page and the display cannot
  drift. Add one line to DEFAULTS.md and to every day's materials: "no document camera: draw it on the board".
  The rule "no slides" stays.
- **Confidence.** Likely (one outside source plus the built file).

### 2. The tool's exit items are not rows, so the two exit paths are not the same evidence

- **What is wrong.** Rule 1 says every question a student answers on the day is a row. On the device path the
  exit is the tool's "On your own", four items that live only in the tool spec (56 ÷ 7, 9 × 6 = 54, 40 ÷ 2 − 12,
  2 × (9 + 6)). They are not in the day's key, the no-reuse gate never sees them, one of them (area with both
  sides known) is not the day's goal, and "Tomorrow" reads only the paper slip ("40 or 50 on the poster"). The
  record sheet column E90 therefore means different things in different rooms.
- **Evidence.** spec.md line 118; lesson.py builds the key only from `[[id]]` references; LESSON-DAY.md rule 1.
- **Cost.** The respond groups the next day are formed from two different tests, and a tool built later can
  quietly repeat a taught number.
- **Change.** Template rule 1 gains: "This includes the items a tool asks on its own. A tool's exit items are
  rows with `check` = `exit` and a new column `path` = `tool` (paper rows `path` = `paper`). Both paths ask the
  same parts with different numbers. 'Tomorrow' names the sign of each error on both paths." Day 90: add the
  tool's four items as rows (dropping or replacing 9 × 6 = 54, which tests nothing on day 90's goal), and add to
  "Tomorrow" what the end screen shows for errors C and D. TOOL-ASKS gets ask 9: the tool reads its "On your
  own" items from the rows.
- **Confidence.** Firm (the template's own rule, read against the spec and the build).

### 3. A day passes every gate while leaning on pieces that do not exist

- **What is wrong.** Day 90 needs the tool (spec only), the unit opener (it holds the reteach), the facts check
  part 2 sheet ("still to make") and the record sheet (not made). LESSON-DAY.md says so in "What day 90
  showed", item 5, but nothing in the template or the gate makes it visible on the day itself. The paper path
  for the 20-minute tool block, which is today the only teachable path, is three lines: it does not say how a
  student checks a note without the tool's feedback or what the teacher watches for on paper.
- **Evidence.** ADOPTION-BAR.md, "Ready to teach: a teacher writes nothing from scratch"; shared core C6 and
  C14 ("a tool day has no paper path" fails) in ADOPTION-BAR-SUBJECTS.md.
- **Cost.** Across 105 courses, many days will name tools and sheets that arrive later. A teacher printing day
  90 today meets a warm-up with no sheet and a reteach in a document that does not exist.
- **Change.** (a) Header field `leans_on`: every outside piece by path (`tools/community-plot-planner`,
  `courses/math-4/u11-1/opener.md`, the facts sheet, the record sheet). `lesson.py check` fails a day whose
  piece is missing unless the day's `version` says "not ready", and the build prints "Not ready to teach:
  <piece> missing" at the top of the teacher page. (b) Template, "Other rooms": "When the day's tool is
  planned but not built, the paper path is written as fully as the tool path: what students do, how they
  check, what to watch for." Day 90's paper path gains two sentences: students check each area note by
  multiplying back and each fence note by adding four sides; watch for a note solved by adding or subtracting
  the two numbers (error C) and for a fence answer not halved (error D).
- **Confidence.** Firm.

### 4. The credit rule is right in direction, with four holes

- **What is right.** Adapting only CC BY, CC0 and public domain material is correct for a CC BY 4.0 project:
  NonCommercial terms cannot pass through to a CC BY work, and ShareAlike would force the lesson to be BY-SA.
  Naming "informed by" sources is good practice.
- **What is wrong.** (a) The gate accepts "CC BY-ND": the text "cc by" matches and only NC and SA are refused.
  NoDerivatives forbids adaptation. (b) Credit is tied to the day, but adapted material lives in items.csv rows
  that the key, the display, the exit slip and later generators all print; only the student page gets the
  credit foot. (c) The rule lists source, author, licence and changes, but not the title or the licensor's
  requested form; Illustrative Mathematics asks for "© 2021 Illustrative Mathematics. Licensed under CC BY 4.0"
  and excludes its name and logo from the licence. (d) Nothing covers texts, images and data that are used but
  not adapted (an ELA passage under permission, a photo, a primary source), and nothing says a printed standard
  carries the Common Core notice.
- **Evidence.** CC BY 4.0 legal code, sections 2(a)(6), 2(b)(2) and 3(a) (read today): attribution keeps the
  creator, copyright notice, licence notice and a link, marks changes, may be met "in any reasonable manner",
  and may not suggest endorsement; trademark rights are not licensed. CC "Best practices for attribution" (read
  today): title, author, source, licence, and "adapted from" for derivatives; ND does not permit adaptation.
  IM lesson 17 footer (read today). LICENSE-CONTENT.md. Strategic review risk 10.
- **Change.** Rule 4 becomes: "Only CC BY (any version), CC0 or public domain material may be adapted; anything
  with NonCommercial, ShareAlike or NoDerivatives terms may be read to learn, never adapted, and 'informed by'
  means no wording, task sequence or problem context taken over. An adapted item carries its credit in a new
  items.csv column `source` (title, author, licence with link, what we changed, in the licensor's requested
  form), and every built piece that prints that item prints the credit at its foot. A name or logo the licence
  excludes appears only in the credit line. Texts, images and other material used but not adapted have their
  own rights record (texts.csv for ELA) and the first pilot in that subject sets its rule here." Gate: refuse
  `\bnd\b|noderivatives`, and fail any row with a non-empty `source` whose credit lacks a licence and a link.
- **Confidence.** Firm on (a) and (c); likely on (b) and (d).

### 5. The size caps measure the wrong thing for a student's reading

- **What is wrong.** The 250-word student cap leaves out the question stems. On day 90 the counted frame is 98
  words; the stems add 217, so a nine-year-old reads about 315 words. For ELA and science the stems and the
  passage are most of the reading. Type size is set for grades 3 to 12 only; kindergarten to grade 2 has none.
  The two-side rule is checked only by `lesson.py build --pdf`; `check`, the gate the template names, never
  counts sides.
- **Evidence.** words() and check_day() in lesson.py; my count of the day 90 stems; shared core C10 ("a reading
  load that fits the grade").
- **Cost.** A day can pass the cap with a page a struggling reader cannot get through, and the template will say
  nothing about it.
- **Change.** Template: "Words a student reads" counts everything printed for the student, stems included, and
  the gate reports stems and frame apart; cap per grade band in each course's DEFAULTS.md (grade 4 math: 350,
  ours, untested). Add a stem check: no sentence over 15 words in grades 3 to 5 (ours). Type: 18 point in
  kindergarten to grade 2, with a teacher read-aloud line on every student page. Move the side count into
  `check` whenever Chrome is present, and say plainly in the output when it was skipped.
- **Confidence.** Likely.

### 6. The template carries math-only assumptions; name them now

- **What is wrong.** Rule 1 ("every question... its key is computed"), rule 3 ("every number is new"), the
  display's "wrong answers to fix", the 60-minute day behind the 900-word cap, "Before class" at 80 words, and
  two sides of paper all assume grade 3 to 8 math. ELA's own approach page already decided different files
  (texts.csv, questions.csv, words.csv) and judged questions with look-fors and two samples. Science days need a
  safety note, materials per group, set-up that often starts the day before, clean-up minutes and a data sheet,
  and an investigation can span days.
- **Evidence.** APPROACH-ELA.md, "What ELA adds"; RUBRIC-ELA.md gateway 2 (texts at the right level with a
  reason, 80 percent of questions answerable only from the text, discussion routines, writing through the
  process); ADOPTION-BAR.md, science ("start from a real thing to explain").
- **Change.** Add a section "What changes by subject" now, so Cory's yes is a yes to the shared shape plus a
  list, not to the math details: (a) facts in data holds everywhere, but a judged item carries look-fors and two
  sample answers instead of a computed key; (b) the new-numbers rule is "nothing on a check is a taught item":
  for ELA a cold text, for science a new situation; (c) caps are per minute of the day (15 words a minute of
  teacher prose, so 900 at 60 minutes, 1,350 for a 90-minute literacy block) and "Before class" is set in each
  course's DEFAULTS.md; (d) science adds a required "Safety and set-up" heading; (e) ELA prints the text as its
  own piece, outside the two-side limit, with its rights line; a writing day prints a lined page outside it too;
  (f) a day may belong to a run of days (`continues: d091`) so investigations and the writing process are not
  forced into one sheet. Mark the template "proved on grade 4 math only" until the ELA and science pilots run.
- **Confidence.** Firm on the need (the project's own ELA decisions already differ); the numbers are a judgment
  call.

### 7. A printed page carries no version and no licence

- **What is wrong.** The header holds `version`, but the student page, exit slip, key and display print neither
  the version nor the Curio Class licence. A teacher with last year's photocopies cannot match them to today's
  key, and a reuser of a CC BY page cannot see whom to credit.
- **Evidence.** The built pages. Strategic review recommendation 12 (a versioning and errata rule).
- **Change.** Every built piece prints a foot line: "Curio Class, grade 4 math, day 90, version <v>, CC BY 4.0,
  curioclass.org". Template rule 8: "An item id is never reused for different numbers; a changed item gets a new
  id, and the version goes up."
- **Confidence.** Likely.

### 8. What the gates check, and what they miss

The gates do well what they claim: header fields, heading order, minutes against days.csv, caps, unknown or
unused ids, exit items kept off the student page, a key the script cannot reproduce. They miss:

- **A key that only restates its answer.** `s11-C90-1` computes `40/8 | 26/2-5`: it starts from the answer (8
  and 5), so it would pass with any stem. Change (plan.py): every number in a compute cell must appear in the
  stem, apart from 1 and 2; an item with several answers may check them instead (`5*8==40 and 2*(5+8)==26`,
  value `True`), which the compute rules already allow.
- **Reuse beyond a subset of stated numbers.** The gate compares exits with taught stems only. It misses the
  same fact turned round (a taught 6 × 8 = 48 and an exit "48, 8 wide"), the same answer, the readiness items
  (`s11-R1` is 6 × 7 = 42, and nothing stops an exit "42, 6 wide"), and the tool's own items (finding 2).
  Change: compare unordered fact triples (the two given numbers and the answer), include readiness rows, and
  report (not fail) an exit whose answer repeats a taught answer for the same part.
- **Side count** (finding 5) and **writing room**: a page can fit two sides by leaving no room to write (finding
  10).
- **Headings with nothing under them.** A one-word "Other rooms" passes. Change: each fixed heading has a
  minimum of one sentence, and "The day" blocks with sub-minutes (day 90's 6 + 6 + 3) must add to the block.
- **Prose that names things.** "Errors B and D", "error C" and the error signs in "Tomorrow" are not checked
  against errors.csv and wrongs.csv. Change: a letter named in teacher prose must exist in the stretch register,
  and each wrong answer quoted in "Tomorrow" must be a row for that day's exit.
- **The credit section against the header** (header "ours", section names sources): consistent today, unchecked.

What no gate can see, and the expert or a teacher must: whether the order teaches, whether the teacher's words
are right for nine-year-olds, whether the minutes are real, whether a context makes sense.

- **Confidence.** Firm (read in the code and run).

### 9. Teacher needs on the day that the pieces leave out (can wait for the taught run, cheap to add now)

- **Answers beside the questions.** The teacher page renders each `[[id]]` as its stem only; a teacher walking
  the room needs the answer on the same page. Change (lesson.py): render as stem plus the answer in brackets on
  the teacher page only. Add "the key, 1 for the teacher" to every `print` line.
- **Sample answers for open responses.** "What went wrong" on the fixes is written work; the key gives "Jo
  subtracted". Shared core C9 and C11 ask for a sample and a note telling a language gap from a content gap.
  Change: a judged part of an item carries one sample answer ("Jo took 5 away from 35, but area is rows times
  columns: 5 × 7 = 35, so 7 feet") and one language note ("a child who writes '5 × 7' with no words has it").
- **Grouping.** The template does not ask each part to say how students work (EdReports 3j to 3q; C6). Day 90
  says it in places. Change: each `####` part names alone, pairs, groups or whole class.
- **Confidence.** Likely.

### 10. Day 90's student page has no room to write

- **What is wrong.** On the rendered PDF, each fix has one line for "What went wrong" and a short blank for
  "Fix"; "On your own" gives about 1.2 inches for a four-term equation and no room to sketch; the table's
  equation column is about 1.3 inches for "5 + ? + 5 + ? = 30" in a nine-year-old's hand, and on the paper path
  the five notes have no working room at all. The lower third of side 1 is empty. "Check:" in Example 2 wraps
  onto its own line.
- **Change.** Give each fix a 1-inch "right working" box (using side 1's empty space); give each "On your own" a
  sketch box like the examples; widen the equation column to half the table by shortening the note column to
  the family name and the number given (the full stem stays on the display and in the key). Re-run the side
  count.
- **Confidence.** Firm (seen on the page).

### 11. Day 90's teacher wording: five small repairs

- **Readiness branch minutes.** "The warm-up and five more minutes go to the reteach" does not say which block
  gives up the five. Change: "five minutes from 'On your own' and the partner check; those two questions move to
  day 91's warm-up."
- **"Keep their 9 by 9 table out today."** Read straight after the facts check, it sounds like a support during
  the check. Change: "After the facts check, students under 32 of 36 on day 89 keep their 9 by 9 table out for
  the lesson."
- **Untimed in five minutes.** Say what happens at five minutes: "Collect at 5 minutes; an item not reached is
  left blank, not marked wrong."
- **The square foot.** Example 1 shades grid squares as square feet without saying so. Add: "Each square stands
  for one square foot."
- **The paper sign of "counted".** "Tomorrow" seats students whose tag says "counted", a tool sign. Add the paper
  sign: "or who shaded every square one by one".
- **Confidence.** Likely.

### 12. Day 90's minutes and talk (for the taught run)

- **What is at risk.** Six parts and two changes of medium (paper to devices and back) in 60 minutes, with no
  minutes for handing out or putting away devices. Students talk to each other only in the 3-minute partner
  check; IM lesson 17 (read today) puts its missing-side work in groups of 3 or 4. MP.3 has no moment.
- **Change, to try in the taught run.** Time the two changeovers. If the day runs long, take the minutes from
  the challenge, never from the fixes. Make the first fix a 1-minute turn-and-talk before the class discusses
  it.
- **Confidence.** A judgment call; the minutes are ours, untested.

### 13. The 900-word cap and the cost arithmetic (for the taught run)

- **Judgment.** 900 words of teacher prose for a 60-minute math day is lean beside the open courses I know
  (from memory, an Illustrative Mathematics lesson with its notes runs well past that), but it works here
  because the unit opener carries the background and the generated tables carry the facts. Day 90 fits in 880
  without losing a part. 80 words before class is right for math. Two sides is right for grades 3 to 8 math and
  keeps print volume down (recommendation 12). Keep all three for math; scale per minute for other subjects
  (finding 6).
- **What the cost line misses.** At 18 million words the cost is reading, not writing. The template should say
  how days are read: every day by the gates, a sample of days per unit by the expert, and the whole of the first
  unit in each course by a teacher. Put that sentence under "What the script checks".
- **Confidence.** A judgment call.

## Day 90: the six things asked

- **Mathematics and keys.** All fourteen keys reworked by hand and right: 63 ÷ 7 = 9; (38 − 24) ÷ 2 = 7; Lee 8
  long, fence 28; Nguyen 9, fence 26; Clark 12, fence 34; Ortiz 10, area 50; Abebe 4, area 32; Jo 7; Max 8; table
  9; dog run 8; challenge 5 by 8 (the only whole-number pair with area 40 and perimeter 26: 1 by 40, 2 by 20 and
  4 by 10 give 82, 44 and 28); exit 9 and 6. Lengths are always the longer side. The extension "every rectangle
  with area 36" has five answers (1 by 36, 2 by 18, 3 by 12, 4 by 9, 6 by 6; perimeters 74, 40, 30, 26, 24) and
  no row: add it as a row so the teacher does not work it out.
- **Worked examples.** Sound. Example 1 builds the missing factor from rows, which is the standard's own
  example and the Progressions' reading. Example 2 writes four sides first, then links to 2 × (l + w) as "half
  the fence". Keep both.
- **Order.** Model, practice with the tool or by hand, the register's two errors fixed, two alone, then the
  pull-together question and the exit. Right.
- **Minutes.** Add to 60 and agree with days.csv. Realism goes to the taught run (finding 12).
- **Numbers.** The gate passes, but the area answers are 9, 8, 9, 12, 7, 9 and the exit's is 9 again, with 9 the
  answer of the worked example. A child can score the exit by remembering "9". Changed under "Settled by the
  expert".
- **Reading load.** About 315 words; sentences of 14 to 18 words; plain words. "Pen" and "dog run" are the two
  words a new English learner may read wrongly (a pen to write with). Four fence stems say "has 30 feet of
  fence" without saying it all goes round the plot, the gap the earlier read found on end-check item 2.
- **Paper path.** Exists, but is thin (finding 3), and the page has no room for it (finding 10).
- **Wording to students.** "Copy each equation from Community Plot Planner" will copy 2 × (5 + ?) = 30 until tool
  ask 4 lands, while the key and teacher say 5 + ? + 5 + ? = 30. Until then, say on side 2: "Write the four
  sides."

## What is right and should not be touched

- One source file for teacher and student pages; questions named by id; keys only in data.
- Fixed headings in a fixed order; minutes headed on each part and tied to days.csv.
- "Ask." with the answers to expect and the order to show them. Spoken words written out only where they matter.
- A paper path every day, and "Shorter or longer" that never makes the work easier.
- No slides, as a rule, once finding 1 makes the display carry the pictures.
- No timer, score or rank; black and white; large print from the same file.
- The check-day variant, and the unit opener and family note per unit, not per day.
- Writing every minute down, which found 15 unplanned minutes in the plan's day 90.
- In day 90: "Write the four-side equation first, every time"; the partner check by putting the answer back in the
  equation; the pull-together question about why one problem never took anything away.

## What I could not judge

- Real minutes, and whether nine-year-olds finish five notes in 20 minutes on paper: the taught run.
- How the display looks on a classroom projector at the back of a room: needs finding 1 built, then a look.
- The tool's feel and timing: no build exists.
- IM's cool-downs and student responses (behind a sign-in), so how IM words its own missing-side exit.
- Whether ELA's and science's own pilots will need more than finding 6 lists.

## Sources

- Creative Commons, CC BY 4.0 legal code, sections 2 and 3: https://creativecommons.org/licenses/by/4.0/legalcode.en
  . Used for the attribution conditions, "any reasonable manner", no endorsement, trademarks (finding 4).
- Creative Commons wiki, Best practices for attribution: https://wiki.creativecommons.org/wiki/Best_practices_for_attribution
  . Used for title, author, source, licence, "adapted from", and ND not permitting adaptation (finding 4).
- Illustrative Mathematics K-5, grade 4, unit 5, lesson 17, "More Perimeter Problems":
  https://im.kendallhunt.com/k5/teachers/grade-4/unit-5/lesson-17/lesson.html . CC BY 4.0; read to learn, nothing
  copied. Used for: no slide deck but posted diagrams (finding 1), group work on missing sides (finding 12), the
  requested credit form and the excluded name and logo (finding 4).
- EdReports K-8 math criteria v2.0, as summarised in docs/RUBRIC-MATH-K8.md (gateway 3); not reopened.
- ADOPTION-BAR.md, ADOPTION-BAR-SUBJECTS.md shared core C6, C9, C10, C11, C14; RUBRIC-ELA.md; APPROACH-ELA.md.
- From memory, marked where used: the length of an IM lesson's teacher notes (finding 13).

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Exit `s11-X90a` becomes "A card covers 21 square inches. It is 3 inches wide. How long is it? Write the equation."; answer `3 × ? = 21; 7 inches`; compute `21/3`; value `7`. Wrong answers: `18 or 24` (`21-3 \| 21+3`, C) and `63` (`21*3`, C) replace 40 or 50 and 225 | The old exit's answer, 9, was the answer of the worked example and three practice items; 3 × 7 is used nowhere else in the stretch; a 5 by 9 inch "poster" was not real | items.csv, wrongs.csv; d090.md "Tomorrow" then reads "18 or 24, or 63, on the card" |
| Exit `s11-X90b` adds "Write the equation."; answer `17 + ? + 17 + ? = 46; 6 inches` | The day teaches writing the equation first; both exit items should ask it | items.csv |
| Fence stems say the fence goes all the way round: `s11-T90-4` "The Ortiz family puts 30 feet of fence all the way around their plot. The plot is 5 feet wide. How long is it?" (same pattern for `s11-T90-5`, 24 and 8); `s11-F90-2` "...a pen with 44 feet of fence all the way around..."; `s11-P90-2` "...42 feet of fence all the way around..." | Without it a careful child may answer "less than"; the same gap was fixed on end item 2. Keys unchanged | items.csv; the tool spec's Ortiz note to match |
| "A pen" becomes "a goat pen" in `s11-K90-2` and `s11-F90-2`; "a dog run" becomes "a dog yard" in `s11-P90-2` | A new English learner reads "pen" as a writing pen; numbers and keys unchanged | items.csv |
| Add a row for the extension, every whole-number rectangle with area 36 and its perimeter (five answers, compute as a check) | A teacher should not have to work out the extension's key | items.csv |
| Day 90's paper path, readiness branch and four wording repairs as written in findings 3 and 11 | Day-level wording inside the day's own minutes | d090.md |

## For the source list

- New: Creative Commons, Best practices for attribution, https://wiki.creativecommons.org/wiki/Best_practices_for_attribution
  (CC BY 4.0, HTML, WebFetch works). The CC BY 4.0 legal code, https://creativecommons.org/licenses/by/4.0/legalcode.en
  (WebFetch works). Both worth listing for every credit question.
- IM K-5 grade 4 unit 5 lesson 17 (already listed under the lesson pages): note that its page footer gives the
  requested credit form and the exclusion of the IM name and logo, and that the lesson lists no slide deck.

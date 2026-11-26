# Expert read: scope and sequence of Visual Arts, grades 9 to 12 (2026-11-26)

Course `visual-arts-grades-9-to-12`. Cold read by the curriculum expert (PRODUCTION-PATH step 3), per
docs/pipeline/briefs/sequence-read.md and build/scope-writes/ARTS-READ.md. I did not write the scope. This report is
the only file edited.

## What I read

- docs/agents/EXPERT.md; docs/agents/lenses/arts.md; docs/ADOPTION-BAR-SUBJECTS.md section "2. Arts" (items 1 to 9,
  "Fails if", "Scope and sequence states"); docs/courses/arts/STANDARD.md (3.2, 3.4 and the process lines);
  docs/courses/arts/APPROACH.md ("Practices", "Pacing", "High school levels and music").
- build/scope-writes/ARTS-BRIEF.md (how the writer applied sequence-write.md to band courses).
- docs/courses/visual-arts-grades-9-to-12/scope-and-sequence.md, in full.
- data/plans/visual-arts-grades-9-to-12/days.csv, all 640 rows (goal, codes, assess, retrieves, and the notes of
  every check, respond, baseline, fold-in and unit-opening day).
- docs/courses/visual-arts-grades-9-to-12/frame.md: brief, Seams, Models, the Units rows for units 1 to 3 in full
  and the rest for their evidence, short-path and Level 4 lines, Course-level checks, Cross-subject, For the lead.
- data/standards/ncas-performance-standards-words.txt for the ids the findings turn on.
- Earlier arts sequence reads of the same day (music 6 to 8, dance K to 2, media arts 6 to 8, theater K to 2), for
  the REPEAT tags.
- Gates run first: `scripts/sequence.py check visual-arts-grades-9-to-12` 0 failures (notes only: units 1, 6, 11
  and 16 to 19 own no id); `scripts/plan.py check` 0 failures for this course (algebra-ii fails, not this course);
  `scripts/frame.py calendar` 0 failures, 19 units, 640 days, 156 unit days a level; `scripts/stale.py check` 0
  failures. I scripted three checks the gates do not make: every owned id per level (15 in each of Levels 1 to 3,
  all on an `end` day, none in the wrong level; Level 4 carries the 15 `.IIIa` ids again); every short-path merge
  (counts match the frame, groups are consecutive, no Check or Respond day merged, no critique day merged); and
  every fold-in day (all 40 are Fluency, none assessed, none carries a baseline look).

No outside sources were opened on this run; the standards' meanings come from the repo's words file, and the
judgments on session load rest on the frame's own minute budget (set-up 3, clean-up 3 to 7) and from memory of
high school studio practice.

## Verdict

The scope is sound in its bones: four levels laid out cleanly with the right ids in each, every owned id taught
and assessed in its own level, technique before making in most units, one critique and a revision in every unit,
a wide range of works with their settings, and checks on the frame's weeks. The biggest risk is Level 4: the
self-directed series gets no class time after unit 16, yet both Level 4 course-level checks score it again, one
of them unchanged since its last scoring. The one change that matters most is to give the series class time and
replace the two Level 4 check items with fresh evidence (finding 1); close behind are the missing baseline looks
(finding 3) and the material trials held before their hazard card in unit 16 (finding 2).

13 findings: 3 serious, 6 moderate, 4 minor.

## Findings, most serious first

### 1. Level 4's series has no class time after unit 16, and two checks score it again (serious)

LAYER frame, sequence. REPEAT yes (the dance K to 2 read's finding 1: a check re-collecting what was just scored).

- **What is wrong.** Unit 16 ends on day 528 with "the series so far and the defended statement draft" scored. Day
  530's note says "The series continues in the studio sessions of units 18 and 19". It cannot: unit 17 is the
  essay, unit 18's 14 studio sessions (570 to 595) are the project's, and unit 19 has no making day at all. Then
  the Level 4 mid-year check (day 559) scores "the series to date reviewed against its proposal" on VA:Cr2.1.IIIa
  and VA:Cr3.1.IIIa: the same series, untouched since day 528, scored a second time against the frame's rule "no
  artifact is scored twice". The year-end check (day 639) scores "the series' final state against its proposal" on
  VA:Cr1.2.IIIa and VA:Cr3.1.IIIa, a final state no class day worked toward.
- **Why it matters.** A teacher following the days finds nothing new to score on day 559 and nothing finished to
  score on day 639; the "growing independence" Level 4 claims is never seen growing after day 530. Students who
  finish Level 4 most often are seniors, for whom this is the last arts evidence.
- **Fix.** (a) Day 530 note: "The series continues as homework sketchbook time; a student whose unit 18 project
  grows from the series works on it in the project's studio sessions (frame unit 16: the project may come from
  it)." Say the same in day 562's note. (b) Day 635 duplicates day 633 (both "a second talk to visitors"): make
  day 635 "Series studio: the next work of the series made toward its final state, the checkpoint calendar
  updated" (Application, VA:Cr2.1.IIIa), so the series has a class session before day 639. (c) The two Level 4 check
  items are the frame's (Course-level checks table), so the lead changes them there first, then the scope: day 559's
  creating part becomes a fresh timed study, in pencil or a dry medium, for the series' next work, with a written
  revision decision against one traditional and one contemporary criterion (VA:Cr2.1.IIIa, VA:Cr3.1.IIIa); day 639's
  creating part becomes a written plan for continuing the series (materials, the convention followed or broken)
  and a defended change on one exhibited piece (VA:Cr1.2.IIIa, VA:Cr3.1.IIIa). Both are new evidence, sat with no
  paint, ink or clay out.
- **Confidence.** Firm (the days and the frame's rule say it).

### 2. Unit 16 tries a student-chosen material before its hazard card is written (serious)

LAYER sequence. REPEAT new.

- **What is wrong.** Day 487 (Fluency): "Material trials in the proposed medium, repeated and logged". Day 488: "The
  hazard card for the chosen medium written and checked by the teacher". The frame's safety rules say a hazard card
  is read before each new material, and in Level 4 the material is the student's own pick, so it may be one the
  class has never handled.
- **Why it matters.** It is the one place in 640 days where the hazard routine runs after the hands-on use, on the
  least predictable material of the band.
- **Fix.** Swap the two days: day 487 the hazard card written and checked, day 488 the trials (the baseline look
  note moves with the trials to day 488). The short-path merges 6+7 and 8+9 still hold. Settled below.
- **Confidence.** Firm.

### 3. The baseline look is missing in eight units and sits on a first-teaching day in four (serious)

LAYER sequence. REPEAT yes (music 6 to 8 finding 6, dance K to 2 finding 8, theater K to 2 finding 4).

- **What is wrong.** The frame says every unit opens with a baseline look at its main look-for during the first
  practice days, so each student has two marks a unit and growth is the change; the logic model's outputs claim
  "two marks a unit per student". Notes name a baseline in units 2, 3, 7, 8, 12, 13, 14 and 16 only. Units 4, 5,
  9, 10, 15, 17, 18 and 19 have none. And in four units the baseline begins on the day the technique is first
  taught (day 15 unplanned ink, day 47 thumbnails, day 170 ink wash, day 331 the theme), against the frame's "No
  score comes from the day a technique or a work is first taught".
- **Why it matters.** Growth is the bar's assessment line (item 8) and the scope's only outcome measure; in eight
  units a teacher has nothing to compare the end mark to, and in four the baseline measures a skill not yet taught.
- **Fix.** Baseline notes (main look-for, two groups on two days), none on a fold-in day: unit 2 days 16 and 19;
  unit 3 days 48 and 49; unit 4 days 87 and 88; unit 5 days 125 and 126; unit 7 days 171 and 172; unit 9 days 248
  and 251; unit 10 days 289 and 291; unit 12 days 333 and 336; unit 15 days 443 and 444; unit 17 days 537 and 539;
  unit 18 days 570 and 572; unit 19 days 606 and 609. Units 8, 13, 14 and 16 keep theirs (unit 16's moves to day
  488 with finding 2). Settled below.
- **Confidence.** Firm.

### 4. VA:Cr2.2.IIIa's materials and tools part is on no Level 3 day (moderate)

LAYER sequence, frame. REPEAT yes (dance K to 2 finding 2, media arts 6 to 8 finding 3, music 6 to 8 finding 1:
a part of a code dropped).

- **What is wrong.** The id's words-file line is balancing liberty with duty "when using and sharing images,
  materials, and tools". Unit 12's days 339, 340 and 353 and its sitting (day 358) treat only the use of another
  maker's image (the Goldsmith and Warhol case). The frame's own unit 12 row names "images, materials and tools" in
  what students learn but only the image case in its end-of-unit evidence line, and the scope followed the evidence
  line. Level 4's unit 18 reaches materials (day 564), but Level 3 is where the id is claimed and met.
- **Why it matters.** A student can be marked met on VA:Cr2.2.IIIa with a third of the standard untaught.
- **Fix.** Day 340: "Write the weighing of freedom and responsibility in one use of another maker's image and one
  choice of a material or tool that affects others (a shared studio's ventilation, a found material's source, a
  borrowed tool's care)". Day 353's second case becomes a materials or tools case. Day 358's sitting adds a short
  second prompt on a materials or tools choice. The lead adds "and one materials or tools choice weighed" to the
  frame's unit 12 evidence line. Settled below (the scope days); the frame line is the lead's.
- **Confidence.** Firm.

### 5. Unit 12 makes a three-work series with no technique taught first (moderate)

LAYER sequence. REPEAT new.

- **What is wrong.** Unit 12 (VA:Cr2.1.IIIa, a themed series) opens its making on day 336 ("Work 1 begins", ink and
  paint per the note) after only a theme day (331), a thumbnail drill (332) and the theme plan (333). No day shows a
  technique in named steps with a step card; day 348 then "repeats the chosen medium's techniques" that were never
  taught. The frame's ladder says Level 3 drawing is "a planned series" and wet media "a series in one chosen
  medium", one step past Level 2's sustained studies.
- **Why it matters.** It is the lens's first unit-level error ("a making task with no technique taught first") and
  leaves Level 3's technique ladder flat at its first making unit (bar item 2).
- **Fix.** Day 332 becomes Understanding: "The series medium at Level 3 in named steps, by medium group (layered
  glazing in ink wash or watercolor, a two-color foam-plate print with registration, or a sustained charcoal drawing
  worked with an eraser), with the step card and the medium's hazard card"; the six-thumbnail drill moves to day
  333's opener. Day 332 is not a fold-in or check day. Settled below.
- **Confidence.** Likely.

### 6. Three course-level checks sample the unit just scored, and the .md says none does (moderate)

LAYER sequence, frame. REPEAT yes (dance K to 2 finding 1).

- **What is wrong.** The .md says "Every check sits right after a unit's end-of-unit assessment, so it draws its
  items from earlier units". Three do not: the Level 2 mid-year check (day 237) samples VA:Cr1.1.IIa from unit 8,
  scored on days 233 and 234; the Level 3 mid-year check (day 397) samples VA:Cr1.2.IIIa, "a series plan for a new
  theme", right after unit 13 scored the series plan; the Level 4 mid-year check (day 559) samples VA:Re8.1.IIIa and
  VA:Re9.1.IIIa right after unit 17's essay. The rule (sequence-read "Checks that do not repeat") lets a check sample
  the just-assessed unit's skills only from earlier units' content, said in the scope. The frame sets these samples
  and the days' notes half say it, but none names earlier-unit content. The Level 2 item also drops a part: the id
  is a problem posed "from your own earlier artwork", and the item uses "a given earlier work".
- **Why it matters.** The students repeat the task they just did; for VA:Cr1.1.IIa the check also stops measuring
  the "own work" part of the id.
- **Fix.** Day 237 note: the Cr1.1 item poses a new problem from a different piece of the student's own Level 1
  portfolio than the one used in unit 8 (earlier content, and the student's own work). Day 397 note: the Cr1.2
  item's theme is drawn from unit 12 (the pattern-study era or the student's unit 12 theme). Day 559 note: the
  reading item is on a unit 16 work (Monet's Stacks of Wheat or Ojih Odutola's series) with two given readings.
  Replace the .md's blanket sentence with one line per check saying where its items come from. Settled below.
- **Confidence.** Firm.

### 7. The 80-day path packs two or three first teachings into one 45-minute day (moderate)

LAYER sequence (and frame for units 6 and 11). REPEAT yes (theater K to 2 finding 1, dance K to 2 finding 3, media
arts 6 to 8 finding 5).

- **What is wrong.** Every merge count matches the frame and no check, respond or critique day is merged. But the
  merges join first-teaching days, not making days, in several places: unit 1 3+4+5+6 (the charcoal hazard routine,
  contour and gesture) and 7+8+9 (one-point perspective, mixing a color wheel with wet clean-up, the looking routine
  and credit); unit 2 3+4+5+6 (the unplanned ink technique, Frankenthaler, the clay hazard card and clay technique)
  and 18+19+20+21 (a making session, the everyday-image analysis taught and drafted, a drill); unit 7 1+2+3 (the
  hook, retrieval, the medium choice and foam-plate printing with brayer and ink); unit 13 1+2+3+4; unit 17 3+4+5
  (the claim-counterclaim bridge, reactions over time and shared features). Units 6 and 11 merge 1+2+3+4 (the hook,
  two review-station days and the placement checklist, which needs "a short making, handling or showing task for
  each process"). Every 1+2 merge also puts the retrieval on the hook day, which the .md says stays clean.
- **Why it matters.** A wet set-up and clean-up take 10 of 45 minutes; two techniques plus a hazard card do not fit,
  so a teacher on a semester schedule will drop a demonstration, which is the bar's first "Fails if" (making with no
  technique taught). The .md's sketchbook rule covers making sessions only.
- **Fix.** Re-pick the merges by one rule, written in the .md: a merged day holds at most one first teaching of a
  technique or hazard card; join making sessions (the rest as sketchbook time), fluency days and revision days
  instead; on a 1+2 merge the retrieval moves to the next day's opener. Units 6 and 11 cannot hold three short days
  under that rule: the lead picks between 4 short days for each review unit (unit 7 and unit 12 give one back, 16
  to 15) or the checklist filled from work brought before the level opens. The merge re-pick is settled below; the
  review-unit count is the lead's (frame).
- **Confidence.** Likely (session-load judgment from the frame's own minute budget).

### 8. Five units have no creating, against the lead's "all four processes in every unit" (moderate)

LAYER frame. REPEAT yes (media arts 6 to 8 finding 1, connecting missing from units).

- **What is wrong.** Units 5, 10, 15, 17 and 19 tag no creating day. The bar asks all four processes "in each
  course" (item 1; STANDARD.md, APPROACH "Practices": over a year), and every level here meets that. The frame says
  each unit touches at least two. ARTS-BRIEF and ARTS-READ ask all four in every unit. The writer flagged it (For
  the lead 2).
- **Why it matters.** An adoption reviewer would pass the course on the bar. It matters most where the year's
  making stops: Level 4's last two units have none, which is finding 1's gap again.
- **Fix.** Units 17 and 19 cheaply: day 537 adds two-minute compositional thumbnails of the two works as evidence
  (drawing as a way of looking); unit 19 gets creating through finding 1's day 635. Units 5, 10 and 15, the
  curating units: the lead picks between amending ARTS-BRIEF's line to "all four in every level, at least two in
  every unit" (the bar's and frame's rule; my recommendation) or adding a piece made for each show inside existing
  making days.
- **Confidence.** Firm on the facts; the rule to apply is a judgment call.

### 9. The senior calendar covers Level 4 only (moderate)

LAYER sequence. REPEAT new.

- **What is wrong.** The frame says any level may be taken in grade 12 (Levels 3 and 4 most often) and "the scope
  numbers the senior calendar day by day": the curating unit's last fluency and making days merge, five for a
  finish by day 155 and ten for day 150. The scope gives only Level 4's version. A Level 3 senior's teacher has no
  numbered path. The .md also does not say where the checks land on the 150-day year (days 149 and 150).
- **Why it matters.** Level 3 is the honors level most often taken by seniors; without the path the show or the
  check is what gets cut.
- **Fix.** Add to "Senior calendar": finish by level day 155 by folding four fluency days and merging one making
  pair in the curating unit. Level 1: fold 125, 134, 137, 144, merge 147+148. Level 2: fold 286, 292, 295, 306,
  merge 302+303. Level 3: fold 443, 447, 455, 467, merge 462+463. The show then falls on level day 150, its sitting
  151, respond days 152 and 153, the check 154 and 155. A finish by day 150 adds the unit's remaining fluency days
  and further making merges by the same rule. Add one line: on the 10-days-short year the checks fall on level days
  149 and 150. Settled below.
- **Confidence.** Firm.

### 10. Level headings do not name their standards set (minor)

LAYER sequence. REPEAT new.

- The bar's "Scope and sequence states" line and ARTS-READ ask each year's part to name whose standards it carries.
  The top bullets do; the four Level headings do not, and a writer working from one level's part will not see it.
  Fix: under each Level heading, one line: "Carries the 15 `.Ia` ids (Proficient)", `.IIa` (Accomplished),
  `.IIIa` (Advanced), and for Level 4 "Carries the 15 `.IIIa` ids again on new work; claims no new id". Settled.

### 11. Unit 3's three start routes are labeled as two (minor)

LAYER sequence. REPEAT new.

- Day 49 "Start route one: a word web and a thumbnail page", day 50 "Start route two". VA:Cr1.1.Ia's look-for is three
  routes. Fix: day 49 "Start routes one and two: a word web, then a thumbnail page", day 50 "Start route three: a
  photo walk or viewfinder walk". Settled.

### 12. Day 156's Pr6.1 item drops "your" awareness (minor)

LAYER sequence. REPEAT yes (a part of a code dropped).

- VA:Pr6.1.Ia is how an exhibit shapes "your awareness". Day 156 asks how a room plan shapes "awareness of a social
  or political question". Fix: "how the room plan and labels would shape your own awareness of the social or
  political question it raises". Settled.

### 13. Small text points (minor)

LAYER sequence. REPEAT yes (stale or contradictory lines, as music 6 to 8 finding 11).

- The process lists tag respond days as the responding process (for example unit 2 day 32, unit 4 day 40, units 6
  and 11 day 6); a respond day acts on a check (lens). Tag a respond day by the process of the part it reteaches, or
  leave it off.
- The Level 4 fold-in row lists 523 (16.43) after 574; put it in day order, and keep the senior "first five" as
  496, 503, 516, 523, 542, or say the five are chosen, not first.
- Unit 1 day 12 (a respond day) carries a retrieval of va-g8-ideas; it belongs in day 10's or day 11's work, or the
  table should say why a respond day retrieves.
- Unit 16 readiness on day 2 (For the lead 1): keep it in day 2's note as the frame says; the returning student does
  the readiness check while the class does the retrieval opener. Settled.

## What is right and should not be touched

- The band layout: four levels, named by level and never by grade, 160 days each, course day equal to school day,
  `school_day` blank and the rule stated.
- Every owned id: 15 per level, the right suffix in the right level, each on an `end` day; Level 4 claims none and
  carries `.IIIa` again, as STANDARD.md 3.2 and the frame set.
- Retrieval: day 2 of each paired unit, row by row, with the same-year rows (va-g9-ideas, va-g9-judge, va-g11-craft)
  retrieved; the review units' placement sittings standing as readiness for a placed or returning student.
- One critique with a revision after it in every unit, before the end days; written feedback and revision on every
  statement, rationale and argument.
- Technique before the making that needs it in units 1 to 4, 7 to 9, 13 and 14; the ruler card carrying the grade 7
  scale lean; the ELA bridge on day 533 for the essay.
- Works: Africa, Asia, Europe, Oceania and the Americas, with Native makers in units 5, 9, 13, 18 and 19, from about
  420 BCE to now, living makers every level, each with its setting and its sensitivity note.
- The two end days (a sitting on unseen works with no wet media, then the showing scored from kept work), and the
  checks on weeks 16 and 32 of every level.
- The 10-days-short path: 40 fold-ins, all Fluency, none assessed, none carrying a baseline look, nothing owned cut.
- Safety in the notes: no blades, no solvents or heat, damp-wiped dust, an adult hanging above head height.

## Lens checklist (scope and sequence layer)

| Line | Result |
|---|---|
| A grade's ids in the wrong year, or a high school level tied to a grade | Met |
| A year with one artistic process missing | Met (each level has all four; units: finding 8) |
| Works all from one tradition or one century | Met (Level 4 leans on candidates for Asia) |
| Technique that does not get harder across units or years | Partly missed (finding 5) |
| A plan that needs a daily period in K to 8 | Not applicable (9 to 12; STANDARD.md 3.4 sets a daily period) |
| No showing in a unit | Met (every unit shows, talks or exhibits) |

## The checks the brief asks for, in one place

- Order inside each unit: met except findings 2 and 5; arcs reach each compelling question and showing.
- Assessments: each end covers its ids; parts dropped in findings 4 and 12; mid-unit checks on the frame's days in
  every unit over 25 days; response time counted once.
- Readiness and retrieval: met; Level 4's day 2 readiness kept (finding 13).
- Checks that do not repeat: finding 6.
- Standards in full: findings 4, 6 and 12.
- Days by load: met; unit 16's 25 studio sessions are heavy but fit a self-led year.
- Calendar: checks on weeks 16 and 32 as the frame and CALENDAR.md rule 4 set; the ELA lean carries its bridge.
- Candidate cells: all settled (unit 2 dropped with a reason; the rest kept with a day).
- Shorter path: counts hold (scripted); feasibility finding 7; senior path finding 9. This course has no
  once-a-week path: meeting daily, its 80-day path is the rotation path STANDARD.md 3.4 names.
- Source map: not applicable (no base text).
- Stale notes: stale.py passes; findings 1 (day 530) and 13.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Swap days 487 and 488 (hazard card first, then trials; baseline note to 488) | Hazard card before any new material | days.csv |
| Day 530 and day 562 notes: the series continues as sketchbook time, and in unit 18's sessions where the project grows from it | Day 530's claim is false as written | days.csv |
| Day 635 becomes a series studio day (Application, VA:Cr2.1.IIIa) | It duplicated day 633's second talk; gives the series class time and unit 19 a creating day | days.csv, .md unit 19 |
| Baseline looks on days 16/19, 48/49, 87/88, 125/126, 171/172, 248/251, 289/291, 333/336, 443/444, 537/539, 570/572, 606/609; removed from 15, 47, 170, 331 | Every unit gets two marks; none on a first-teaching or fold-in day | days.csv |
| Day 340, day 353 and day 358 add a materials or tools case for VA:Cr2.2.IIIa | The id's materials and tools part | days.csv |
| Day 332 becomes the Level 3 series technique in named steps with step and hazard cards; the thumbnail drill moves to day 333's opener | Technique before unit 12's making | days.csv, .md unit 12 |
| Day 237, 397 and 559 notes name earlier-unit content (own Level 1 piece; a unit 12 theme; a unit 16 work); the .md's blanket check sentence replaced per check | Checks that do not repeat; Cr1.1.IIa's "own work" | days.csv, .md |
| Short-path merges re-picked: at most one first teaching of a technique or hazard card per merged day; retrieval off the hook day | Fits a 45-minute session | .md Shorter path |
| Senior calendar for Levels 1 to 3 (five-day lists in finding 9) and the 150-day check days | Frame asks the scope to number it | .md |
| Level headings name their id set | Bar's "Scope and sequence states" | .md |
| Day 49 and 50 route labels | Three routes, as the look-for counts | days.csv |
| Day 156 asks about the student's own awareness | VA:Pr6.1.Ia's "your" | days.csv |
| Day 537 adds compositional thumbnails of the two works | Gives unit 17 a creating moment at no day cost | days.csv, .md unit 17 |
| Readiness for a returning Level 4 student stays in day 482's note | Frame's placement; parallel to the retrieval opener | none |
| Text points in finding 13 (respond-day process tags, fold-in order, day 12 retrieval) | Accuracy | .md, days.csv |

## For the lead

1. Frame Course-level checks table: replace the Level 4 mid-year and year-end creating items as in finding 1 (c);
   then the scope's days 559 and 639 follow.
2. Frame unit 12 evidence line: add the materials or tools choice for VA:Cr2.2.IIIa (finding 4).
3. Short path for units 6 and 11: 4 short days with unit 7 and unit 12 at 15, or the checklist from brought work
   (finding 7).
4. ARTS-BRIEF's "four processes in every unit": amend to every level, at least two per unit (recommended), or ask
   for creating in units 5, 10 and 15 (finding 8).

## For Cory

- Nothing new. The frame's open picks still stand: two levels in one room (frame For the lead 4) and the $150
  supplies ceiling (frame For the lead 7).

## What I could not judge

- Whether each chosen work's rights line holds; each unit plan checks it on the holding page.
- Session minutes for the self-led Level 4 media, which depend on the students' picks.
- The safety guides the frame names (the consumer product safety agency's guide and California's school guidance):
  not opened on this run.

## Defect log

The brief allows only this report to be edited, so the findings are not logged with `scripts/plan.py defect`; the
caller logs them, found_by `expert`.

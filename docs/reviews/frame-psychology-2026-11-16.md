# Frame read: psychology (Psychology, grades 11 to 12, rows at grade 12), 2026-11-16

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/social-studies.md, section 1 of docs/ADOPTION-BAR-SUBJECTS.md,
  docs/courses/social-studies/STANDARD.md, docs/PRODUCTION-PATH.md (After the core subjects), docs/sources/BASE-TEXTS.md,
  docs/agents/lenses/health.md (for the safe-messaging and body rules the frame calls on).
- The frame docs/courses/psychology/frame.md in full, its row in data/plans/frames.csv (16 units, 160 days, year), and
  the 34 psy-* rows of data/progressions/social-studies.csv with the three us1-* rows that hand on to them.
- data/standards/apa-hs-psych-2022.txt, line by line against the source PDF S:\CurioClass-sources\psychology-curricula.pdf
  (55 PDF pages, text extracted with pypdf): the pillar model (PDF page 20 (18)), every standard area's content
  standards and learning targets (PDF pages 22 to 44 (20 to 42)), and Appendix B's pacing paragraph (two weeks a
  standard area in a year-long course; the ten priority areas).
- The base text S:\CurioClass-sources\openstax-retired-ccby\Psychology-OP.pdf (754 PDF pages, text extracted with
  pypdf): the table of contents against the Source map, and searches inside sections for the dated content the frame
  names and for content it does not name.
- Frames beside and before: docs/courses/us-history-i/frame.md (grade 11), docs/courses/us-history-ii/frame.md (the
  grade 12 timetable), docs/courses/us-government-and-politics/frame.md and docs/courses/economics/frame.md (same
  grade); cross-subject: docs/courses/biology/frame.md, docs/courses/algebra-i/frame.md,
  docs/courses/algebra-ii/frame.md, docs/courses/physics/frame.md, and the s8-senses-brain and bio-* rows of
  data/progressions/science.csv.
- Tool concepts and coverage rows for psychology: data/tools-concepts.csv lines 754 to 760, data/coverage.csv lines
  2163 to 2168.
- Earlier reads of the same layer: frame-economics-2026-11-13.md, frame-us-government-and-politics-2026-11-13.md,
  frame-us-history-ii-2026-11-13.md, frame-biology-2026-11-14.md, frame-physics-2026-11-14.md (for REPEAT tags).
- Gates: `python -X utf8 scripts/plan.py check` exits 1, but only on five courses in COURSE_ROWS with no frame yet
  (calculus, earth-and-space-science, environmental-science, precalculus, statistics); frame psychology: 0
  failures, 16 units, 160 days (156 in units, 4 for checks and respond days). `python -X utf8 scripts/stale.py check`:
  57 files, 0 failures. The plan.py note "us-history-i: Seams does not name psy-data-analysis, psy-research-methods,
  psy-science-of-mind" bears on this course (finding 9).

## Verdict

The frame is sound in design and unusually careful: all 34 rows sit in one unit each, all 141 learning targets and the
seven themes are placed and taught in full, the standard file is faithful to the 2022 document, the unit order puts
methods first and help-seeking last with reasons that hold, and the mental health, research ethics and paper-path
rules are the right ones. The biggest risk is that the frame's safety and accuracy flags are pinned to the wrong
places in the base text: suicide content sits in sections mapped to units 12 and 13, which the safe-messaging list
leaves out, and several dated or failed-replication claims (universal facial expressions, the "chemical imbalance"
account, the marshmallow test, the prison study, the Genovese case) are either unflagged or flagged on the wrong
section or unit, so a writer adapting those sections would carry them over. The one change that matters most is to
re-pin those flags section by section (findings 1 to 3), which costs no days.

## Findings, most serious first

### 1. Suicide content sits in base-text sections mapped to units the safe-messaging list leaves out (serious; firm)

**What is wrong.** The frame names safe-messaging guidance for units 9, 14, 15 and 16, tells the counselor before units
14 to 16 only, and asks the health expert's read for units 4, 9, 10, 14, 15 and 16. The base text puts suicide in two
more places that the Source map sends elsewhere:
- 12.6 Aggression (mapped to unit 12; the frame wrongly pins the Genovese case on 12.7, see finding 3) teaches bullying
  and cyberbullying with suicide outcomes for victims and perpetrators (Psychology-OP.pdf, chapter 12, the bullying
  and cyberbullying passage, text lines near "committing suicide (APA, 2010)" and "more likely to attempt suicide").
- 10.3 Sexual Behavior (mapped to unit 10, with its gender identity part sent to unit 13) tells the David Reimer case,
  including a threatened suicide and his death by suicide in 2004, and mentions conversion therapy.
Unit 15's line also names only suicide guidance, while it teaches eating disorders (10.2's eating-disorder part moves
there) and personality disorders (15.10 names "suicidal gestures" and self-harm).
**Why it matters.** A writer adapting 12.6 or the Reimer case follows the unit's own sensitivity line, which says
nothing about suicide; the sensitivity agent studies safe-messaging guidance only for the listed units. Bullying and
suicide in a high school class is exactly where contagion guidance applies, and the Reimer case is often taught in a way
that frames a transgender-adjacent story around a death.
**Fix (frame: Sensitivity reads, Mental health rules, unit 12, 13 and 15 rows, Source map rows 10.3 and 12.6).**
- Sensitivity reads: "the national recommendations for safe messaging about suicide for units 9, 12, 13, 14, 15 and
  16"; health expert read adds units 12 and 13.
- Unit 12 sensitive line: add "Bullying and cyberbullying (base 12.6) taught without any account of a named young
  person's death; where research ties bullying to suicide risk, safe-messaging guidance applies and help is named on
  the same page."
- Unit 13 sensitive line: add "The 1960s infant sex-reassignment case (base 10.3) is taught, if at all, for what it
  showed about the ethics of the research and of consent, with his death not described; safe-messaging guidance
  applies."
- Unit 15 sensitive line: add "Eating disorders taught with no weights, body sizes, calorie figures or descriptions of
  behaviours, and no images of bodies; self-harm named only as a sign to get help, never described."
- Mental health rules: "The school counselor is told before units 9, 12, 13 and 14 to 16 open" (or before the course
  opens, with the unit list).
- Source map rows 10.3 and 12.6: add "suicide content: safe-messaging guidance".
LAYER frame. REPEAT new.

### 2. Dated or contested claims in the base text that the frame does not flag (moderate; likely)

**What is wrong.** The frame's list "Where the base text is dated" is good but misses four places where 1e states as
settled what the field no longer holds, or tells a case that needs care:
- **10.4 Emotion:** "substantial evidence for seven universal emotions" each tied to a facial expression (Ekman and
  Keltner 1997). The frame's unit 10 line repeats "basic emotions and faces across cultures" with no qualifier, while it
  qualifies facial feedback, growth mindset and the hierarchy of needs. Large reviews since (Barrett and colleagues,
  2019, in Psychological Science in the Public Interest; from memory) find that people do not reliably show or read
  emotions from fixed facial configurations across cultures.
- **3.2 Cells of the Nervous System:** disorders "associated with imbalances" in neurotransmitter systems and
  medications that "treat psychiatric symptoms by restoring neurotransmitter balance". The serotonin "chemical
  imbalance" account of depression is not supported (umbrella review, Moncrieff and colleagues, 2022, Molecular
  Psychiatry; from memory). Unit 2 adapts 3.2, and unit 16 teaches medications.
- **5.1 Sensation versus Perception:** the eye "can detect a candle flame 30 miles away", a figure later analyses put
  far lower (from memory). Small, but it is the kind of number students repeat.
- **7.2 Language:** the Genie case, a child kept in extreme abuse and isolation, told as a language story. Unit 7's
  sensitive line does not name it, and the research on her raised its own ethics questions.
**Why it matters.** Values rule (b): claims rest on the discipline's evidence. The frame promises "claims rest on
research with its sample and replication record", and these four would reach students as settled fact through
adapted days.
**Fix (frame: "Where the base text is dated" list, unit 2, 7 and 10 rows, Source map rows 3.2, 5.1, 7.2, 10.4).** Add
to the list:
- "Unit 10: basic emotions are taught with the cross-cultural recognition studies beside the later evidence that
  expressions vary by culture and context; the base text's 'seven universal emotions' is not kept as settled."
- "Unit 2 and unit 16: the base text's 'neurotransmitter imbalance' account is replaced; medications are described by
  what they act on and what trials show, and 'chemical imbalance' is named as a simplification the evidence does not
  support."
- "Unit 3: the base text's candle-flame distance is dropped (or given with the later, lower estimate and its source)."
Unit 7 sensitive line: "The Genie case, if used, is read for what a single case can and cannot show and for the
ethics of the research on her, from a scholarly account, with no images of her and no detail of the abuse." Carry each
into its Source map row note.
LAYER base text. REPEAT new.

### 3. Four dated-content flags point at the wrong unit or section (moderate; firm)

**What is wrong.** Checked against Psychology-OP.pdf section by section:
- The delay-of-gratification ("marshmallow") study is in **11.4 Learning Approaches** (Mischel and the person-situation
  debate), mapped to unit 11. The frame pins its replication note on "unit 5 and unit 9", whose sections (chapters 6
  and 9) do not contain it, and the 11.4 Source map row has no flag.
- The facial-feedback hypothesis appears only in **10.4 Emotion**. The list says "Unit 3 and unit 10"; unit 3
  (chapter 5) has none of it.
- The Stanford prison study is told in **12.2 Self-presentation**, not 12.1; the 12.1 row carries the flag and the 12.2
  row does not.
- The 1964 Genovese case is told in **12.6 Aggression** (after bullying), not 12.7; the 12.7 row carries the flag and
  the 12.6 row does not.
- The old term for intellectual disability is not only in a box: it is in 7.5's body text, in chapter 7's review
  question 20, and in 9.3 (fetal alcohol exposure as a cause).
**Why it matters.** The unit plan adapts "lesson by lesson" from the Source map. A writer on 11.4, 12.2 or 12.6 finds no
flag and adapts the 2014 telling; a writer on unit 5 or 9 looks for a study that is not there.
**Fix (frame list and Source map).**
- List: "Unit 11 (and unit 5's check-set add): the delay-of-gratification findings (base 11.4) are taught with the
  later, larger replication that tied the effect to family background." Change "Unit 3 and unit 10: the
  facial-feedback hypothesis" to "Unit 10". Change "Unit 5 and unit 9" accordingly; keep unit 5's check-set add as it
  is (it is our own content, not the base text's).
- Source map: 11.4 note "psy-personality-approaches (social-cognitive); the marshmallow study with its later
  replication"; 12.1 note "psy-social-cognition (attribution)"; 12.2 note "psy-social-cognition; the prison simulation
  with its published critiques"; 12.6 note "psy-social-influence; the 1964 bystander case with the corrected account;
  bullying under safe-messaging guidance (finding 1)"; 12.7 note "psy-social-influence; newer bystander research".
- Unit 8 item of the list: "the book uses an old term for intellectual disability (7.5 text and box, chapter 7 review
  question 20, and 9.3); our pages use current, people-first terms".
LAYER base text. REPEAT new.

### 4. Unit 8 meets a Supreme Court ruling that upheld forced sterilization, and the frame does not say how values rule (a) applies (moderate; judgment call)

**What is wrong.** Unit 8 teaches "forced sterilization under eugenics laws" from primary sources, under values rules
(b) and (c). The central primary source for that history is Buck v. Bell (1927), in which the Supreme Court upheld a
state sterilization law; it has never been formally overruled. Values rule (a) reads "where a court has ruled, side
with the higher court". A writer applying the rules in order meets a conflict the frame does not resolve.
**Why it matters.** Without a stated reading, a writer either softens the harm (to avoid "contradicting" the Court)
or the sensitivity read flags a rule breach; both cost a rewrite. The grade 12 ELA unit plan resolved the same shape
for Plessy by teaching the ruling as the law it was, beside its dissent and the later holding.
**Fix (frame, unit 8 sensitive line).** "Buck v. Bell (1927) is taught as the law it was, with the dissent of Justice
Butler, Skinner v. Oklahoma (1942), which struck down a sterilization law on equal protection grounds, and the later
state apologies and compensation; the science of the time is judged by values rule (b), and the harm is named plainly
under (c)." If the lead reads rule (a) differently, this is a values-rule question for Cory.
LAYER frame. REPEAT new.

### 5. Days do not follow the standard's priority marks, and unit 16 is under its share (moderate; likely)

**What is wrong.** Teaching days (unit days less the end-of-unit assessment and respond day):
| Unit | Days | Teaching days | Ids owned | Priority area in the standard |
|---|---|---|---|---|
| 3 Sensation and perception | 12 | 10 | 14 | no (both areas) |
| 4 Consciousness | 10 | 8 | 11 | no |
| 10 Motivation and emotion | 11 | 9 | 12 | no |
| 5 Learning | 8 | 6 | 6 | yes |
| 6 Memory | 8 | 6 | 7 | yes |
| 13 Culture, gender and identity | 8 | 6 | 8 | yes |
| 16 Treatment and getting help | 7 | 5 | 6 | no |
Unit 16 is the shortest unit in the course though the frame says "the methods-heavy and sensitive units get more" and
that "the two-row units with four to seven targets get 8". Its 5 teaching days must hold six psychological and two
biomedical treatment kinds with their evidence, cultural fit, the history of misuse and deinstitutionalization, 16.4
on substance treatment, provider types, legal duties and the local help list: the unit the course ends on. Unit 13 is a
priority area, almost wholly our own content (no base text), sensitive, with theme D taught explicitly and a family
note, at the floor of 8. The standard file says the priority marks are "noted in the frame"; the frame never states
them.
**Why it matters.** The standard's pacing appendix (PDF page 49 (47)) gives about two weeks a standard area in a year
course and names ten priority areas for when time is short; this year has about 8.7 days an area, so time is short
and the priority marks should show. A rushed unit 16 is a risk to the course's own stated purpose (ending on
help-seeking).
**Fix (frame: Days line, units 3, 9, 13 and 16).** Unit 16 to 8 days and unit 3 to 11 (its two areas are non-priority
and SEN owns six short targets); unit 13 to 9 and unit 9 to 10 (judgment call: unit 9's DEV.1 methods reuse unit 1's
design model). Add to the Days line: "The standard marks ten areas as priorities when time is short (Scientific
Inquiry, Biological Bases, Cognition, Memory, Life Span Development, Learning, Social, Multiculturalism and Gender,
Disorders, Health); no priority unit sits below a non-priority unit of like load." Total stays 156.
LAYER frame. REPEAT yes (unit days against load: economics 2, government 3, US History II 2, biology 1).

### 6. Counts and claims in the prose do not match the table (minor; firm)

**What is wrong.**
- Days line: unit 1 has "19 targets"; it owns 18 ids (15 targets and 3 themes).
- Days line: "the two-row units with four to seven targets get 8"; unit 11 has 8 targets at 8 days and unit 16 has 6
  targets at 7.
- Unit 15 "Why": "The longest of the health units for its load"; units 9 and 10 (health units in the frame's own list)
  have 11 days to its 10.
- Unit 8 "Why": "Ends the fall half before the mid-year check"; units 1 to 8 total 81 days, so unit 8 ends on day 81,
  and the timetable's fall half is days 1 to 80 (docs/courses/us-history-ii/frame.md). Unit 9 then "opens the spring
  half" on day 84.
**Why it matters.** Small, but the scope writer reads these lines as the rule for days.
**Fix (frame).** "unit 1 (three rows, 15 targets and 3 themes ...)"; replace the "get 8" clause with the counts after
finding 5; unit 15 "Why": "the disorders unit, given 10 days for the care it takes"; unit 8 "Why": "Ends the course's
first half (day 81) before the mid-year check". LAYER frame. REPEAT yes (miscounts: physics 3, biology 9).

### 7. The standard's own-words line for INT.1.1 changes its meaning (minor; firm)

**What is wrong.** data/standards/apa-hs-psych-2022.txt gives APA22.INT.1.1 as "Explain intelligence as a construct, an
idea defined by how it is measured", and the row psy-intelligence-theories repeats "(an idea defined by how it is
measured)". The document's target (PDF page 31 (29)) says only "explain intelligence as a construct". "Defined by how it
is measured" is one historical position (intelligence is what the tests test), which the unit itself is meant to
weigh.
**Why it matters.** The id line is what writers and checks cite; it would teach a contested position as the target.
**Fix (standard file line and row note).** "Explain intelligence as a construct: an idea inferred from behaviour and
measured only indirectly". The rest of the file checks out (see "Checked and found right").
LAYER standard. REPEAT new.

### 8. The integrative themes are not assessed in either course-level check (minor; likely)

**What is wrong.** The document asks teachers to make the seven themes explicit and to assess them in formative and
summative assessments (PDF page 21 (19), and on each pillar page). The frame teaches each explicitly and names them in
later units, but neither check names a theme item; the year-end check uses the research-design and biopsychosocial
models (theme C only).
**Fix (frame, course-level checks, year-end row).** Add: "one short item per theme A to G, each set in a finding from a
different unit (for example theme A on a study that failed to replicate, theme E on a perception or memory finding,
theme G on a historical study's ethics)". LAYER frame. REPEAT new.

### 9. The seams are not named from the other side (minor; firm)

**What is wrong.** plan.py notes that the US History I frame's Seams does not name psy-science-of-mind,
psy-research-methods or psy-data-analysis, though its rows us1-news-reading, us1-research-inquiry and
us1-argument-writing hand on to them. The US History II timetable table, which this frame cites for the grade 12
timetable, has no Psychology line.
**Fix (docs/courses/us-history-i/frame.md Seams; docs/courses/us-history-ii/frame.md timetable).** Add the three psy-*
rows to US History I's handed-on table with "Psychology (grade 12, or the same year for a grade 11 student), unit 1".
Under US History II's timetable table add: "Psychology, if taken, is its own period all year
(docs/courses/psychology/frame.md)." LAYER frame. REPEAT yes (a seam missing on the other frame: biology 3).

### 10. Two tool concepts and the coverage rows collide with this frame (minor; firm)

**What is wrong.** data/tools-concepts.csv line 760, case-conference ("roleplay": students sit on a clinic team and
classify fictional cases), breaks the frame's rule that no student diagnoses a fictional character and that no role
play puts a student in a clinical scene; line 758, go-along ("sit in a recreated line-judging study as classmates all
answer wrong"), is a deception simulation, which the research-ethics note keeps on paper. data/coverage.csv lines 2163
to 2168 map psychology tools to 2011 domain names (APA.Sociocultural, APA.Individual Variations) that the 2022 standard
no longer uses.
**Fix (frame, For the lead, a new item 5).** "The tool concepts case-conference and go-along conflict with the mental
health and research-ethics rules; at tool stage case-conference becomes a reading of published, de-identified case
vignettes for what a classification can and cannot say (no student assigns a diagnosis), and go-along shows the
conformity study's method and data rather than placing the student in it. data/coverage.csv's psychology rows move to
APA22 ids." Add a row to data/plans/later.csv when the lead files it. LAYER process. REPEAT new.

### 11. Stale notes still say psychology waits and its standard is not loaded (minor; firm)

**What is wrong.**
- docs/courses/social-studies/STANDARD.md section 4: "It waits for the after-the-core stage ... the file is loaded by
  hand when psychology's turn comes"; and its course table row: "APA, after the core (section 4) | no | None".
- docs/ADOPTION-BAR-SUBJECTS.md section 1: "Psychology is not core and waits for the after-the-core stage" and, under
  Unsupported, "loaded by hand when psychology's turn comes".
- docs/agents/lenses/social-studies.md, "What this lens does not cover: ... Psychology (after the core)", while this
  read is made with that lens; its course-frame checklist has no line for a course without a Massachusetts anchor.
**Fix.** STANDARD.md section 4: "Its standard is loaded as data/standards/apa-hs-psych-2022.txt (2026-11-16); the
frame is docs/courses/psychology/frame.md." Table row: "APA 2022 (data/standards/apa-hs-psych-2022.txt)". Bar section
1: "Psychology is not core; it is framed in the after-the-core stage" and "loaded as data/standards/apa-hs-psych-2022.txt".
Lens: replace the "Psychology (after the core)" clause with a course-frame line "Psychology: every APA22 target and
theme placed, the priority areas weighted, and each study taught with its sample and replication record". LAYER
process. REPEAT yes (stale notes: economics 6, government 7, US History II 8).

### 12. The informed action has no classroom-only version (minor; firm)

**What is wrong.** Bar item 8: every action keeps a classroom-only version that needs no money, travel or public
identity. Unit 14's piece is "shared through the school" with no stated alternative.
**Fix (frame, Inquiry arc paragraph and unit 14).** Add: "Classroom-only version: the piece is shared with the class and
filed, unsigned, where the school permits no posting." LAYER frame. REPEAT new.

## Checked and found right (do not undo)

- **Owned skills.** All 34 psy-* rows in exactly one unit; no row from another grade taught here except named
  retrieval. Assumes only from grade 11 (three us1-* rows), each with an "if later" line for a grade 11 student.
- **Standards in full.** All 141 targets and 7 themes, each in one unit, every content standard whole inside one unit;
  no target split.
- **The standard file.** Every content standard (44) and learning target (141) of the 2022 document is present, with
  the document's own numbers; area codes are ours and declared; the ten priority areas match the pillar model; lines
  are our own words (a few are two or three words long and close to the source, such as "Define self-concept", where no
  other wording exists; the document permits educational reproduction with credit, and the header credits it).
- **Unit order.** Methods, then brain and genes, then senses, consciousness, learning, memory, thinking, intelligence,
  development, motivation, personality, social, culture, stress, disorders, treatment: each "Needs" line is met by an
  earlier unit; no model is used before it is introduced (research-design in unit 1, biopsychosocial in unit 2).
- **Source map.** Every one of the 82 sections in the table of contents is placed or left out with a reason; the three
  left out (13.2 to 13.4) have no standard area; no NC or reference source is mapped; the departures from the book's
  order are reasoned. The 1e publication year (2014), DSM-5 in the book, the date of the 988 line (2022) and the old
  term's box in 7.5 are as the frame says.
- **Cross-subject.** The Biology, Physics, Algebra I and Algebra II units and weeks cited match those frames; the claim
  that no Biology row teaches the neuron or synapse holds; every same-year lean has a bridge.
- **Same-grade seams** with Government and Economics are in prose by course order, as the gate requires.
- **Mental health and research-ethics rules**, the paper path, the informed-action topic limits, help named on every
  page in units 14 to 16, and the "no disclosure, no self-diagnosis" rules are right and should stay.
- **Replication handled as content.** The replication crisis in unit 1 (theme A), stereotype threat, growth mindset,
  implicit bias, priming, the obedience reanalyses and positive-psychology effect sizes are each given with their
  record.

## Seams

From grade 11 US History I: news reading, research inquiry and argument writing, picked up as retrieval in unit 1 with
a brief reteach for a grade 11 student. Same grade: Government (fall) and Economics (spring) by course order. Handed
on: none (the last psychology course); the threads table is right. The missing names are on the other frames
(finding 9).

## Cross-subject

Biology grade 9 (body systems, homeostasis, genetics, variation, natural selection) with a readiness check before
unit 2; grade 8 senses with a readiness check before unit 3; Physics wave math, Algebra I statistics and Algebra II
study design, significance and the normal curve as retrieval, each with an "if later" bridge. All check out. No
finding.

## The lens checklist (course frame layer)

| Line | Result |
|---|---|
| An anchor standard in the course's Massachusetts topic range has no unit | Not applicable (no Massachusetts anchor); its equivalent, every APA22 target and theme placed: met |
| The replaced grade 3 year, or "your state" in grade 8, keeps Massachusetts-only content | Not applicable |
| No unit lists what the check set adds, or an addition has no recorded source | Met: each unit names one candidate inside a named target, sourced to Tennessee's psychology course or the first-year college level framework |

## What I could not judge

- Tennessee's psychology standards and the college-level framework were not opened; the "Check set adds" are judged
  as plausible from memory and are checked at the unit plan.
- The evidence claims in finding 2 rest on memory of the named reviews (not opened in this read).
- Whether the day changes in finding 5 hold day by day; the scope and sequence tests them.

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Unit 10's basic-emotion lesson pairs one cross-cultural recognition study with one later study that found recognition varies by culture and context | Two lines of evidence, the student judges, as the values rule asks; keeps the lesson to one period | docs/courses/psychology/frame.md (unit 10) |
| Unit 8's eugenics sources: Buck v. Bell with Butler's dissent, Skinner v. Oklahoma (1942), Virginia's 2002 apology and North Carolina's 2013 compensation programme | Public-domain court records and state records; shows the ruling, its limit and the later reckoning | docs/courses/psychology/frame.md (unit 8) |
| Medications in unit 16 are named by class with what they act on and the trial evidence; no single-chemical cause is stated for any disorder | Accurate and avoids the dated "imbalance" account | docs/courses/psychology/frame.md (units 2 and 16) |
| The Genie case is optional in unit 7; if used, one scholarly account, no images | The language point is made as well by the deprivation follow-up studies unit 9 already reads | docs/courses/psychology/frame.md (unit 7) |

## For Cory

None. The day moves (finding 5) stay inside the course's 160 days and move no standard; the values-rule reading in
finding 4 goes to Cory only if the lead reads rule (a) differently from the frame fix.

Not logged in the defect ledger: the brief allows edits to this report only. The caller may log findings 1 to 12 with
found_by `expert`.

## Sources

- S:\CurioClass-sources\psychology-curricula.pdf (APA, National Standards for High School Psychology Curricula, 2022),
  read with pypdf: targets, pillar model, priority areas, pacing appendix, the themes' assessment request.
- S:\CurioClass-sources\openstax-retired-ccby\Psychology-OP.pdf (OpenStax Psychology 1e, 2014, CC BY 4.0), read with
  pypdf: table of contents and the sections named in findings 1 to 3.
- From memory, not opened: Barrett and colleagues, "Emotional expressions reconsidered" (Psychological Science in the
  Public Interest, 2019); Moncrieff and colleagues, umbrella review of the serotonin theory of depression (Molecular
  Psychiatry, 2022); Buck v. Bell, 274 U.S. 200 (1927) and Skinner v. Oklahoma, 316 U.S. 535 (1942); the national
  safe-messaging recommendations on suicide.

## For the source list

- Barrett et al. 2019 (PSPI) and Moncrieff et al. 2022 (Molecular Psychiatry; open access), for the unit 10 and unit
  2/16 accuracy notes. Not opened in this read.
- The US Reports pages for Buck v. Bell and Skinner v. Oklahoma (govinfo.gov), public domain, for unit 8's sources.

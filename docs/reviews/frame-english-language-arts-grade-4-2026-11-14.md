# Frame read: english-language-arts-grade-4 (ELA, grade 4), 2026-11-14

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/ela.md, docs/RUBRIC-ELA.md (Gateway 1 and the grades 3 to 5 shares).
- The frame docs/courses/english-language-arts-grade-4/frame.md and its row in data/plans/frames.csv (4 units, 160
  days). No data/plans/english-language-arts-grade-4/source-map.csv exists yet; the frame's "## Source map" section is
  the map read here.
- The 30 grade 4 rows of data/progressions/ela.csv, and the grade 3 and grade 5 rows at the seams.
- The frames before and after: docs/courses/english-language-arts-grade-3/frame.md and
  docs/courses/english-language-arts-grade-5/frame.md.
- Same-year frames: docs/courses/social-studies-grade-4/frame.md (unit 5) and docs/courses/science-grade-4/frame.md.
- docs/sources/BASE-TEXTS.md and the base text, S:\CurioClass-sources\el-education-k5-2017, grade 4: module and unit
  overviews, lesson file lists, and the M3 lessons on the Declaration of Independence, counted lesson by lesson.
- docs/pipeline/briefs/frame-write.md, "Lessons from the social studies frames".
- docs/agents/decisions/DESK-ANSWERS.md (2026-11-12 and 2026-11-13 ELA cards).
- Gates: `frame.py check english-language-arts-grade-4` 0 failures; `plan.py check` passes for this frame;
  `stale.py check` 0 failures.
- Standards are judged from my knowledge of the Common Core ELA standards (2010), not re-fetched.

## Verdict

The frame keeps EL grade 4's four modules in order and its day counts are right (37 + 39 + 39 + 38 = 153 base
lessons, 153 unit days), and the Erie Canal replacement for the Revolution module is a sound, local-history choice.
The biggest fault is in that replacement: the source map cuts M3U1 lessons 1 to 3 as "the Declaration of
Independence", but those lessons are the topic launch and a read of a Revolution overview; the Declaration close reads
sit elsewhere and stay mapped. Next, the base's unit 1 informative essay is kept but its rows (informative writing,
the writing process, grammar) are placed in units 2 and 4. Both are fixable without changing a day count.

## Findings, most serious first

### 1. The Revolution cut names the wrong lessons (major; firm)

**What is wrong.** The source map says M3U1 lessons 1 to 3 are "on the Declaration of Independence" and replaces them
with three myth days. In the base those lessons are the topic launch, a gist read of "Revolutionary War, Part I" and
a close read of it. The Declaration close reads are M3U2 lessons 5 and 13, with Part II inside lesson 8, and the map
keeps them as canal days without saying what replaces the Declaration text. The M3U2 label also leaves out its
first-person narrative.

**Why it matters.** A writer following the map cuts the launch the canal unit needs and keeps two close-read days
with no text.

**Fix (settled, a day swap inside unit 3).** Keep M3U1 lessons 1 to 3 as the canal launch (a gist read and a close
read of the canal overview). Make M3U2 lessons 5 and 13 close reads of the 1816 canal memorial. Take the three myth
days from M3U2 lessons 11 and 12 (peer critique and assessment of the first-person narrative; W.4.3 is already taught
in unit 2) and one of M3U1 lessons 4 and 5 (the Loyalists and Patriots research becomes one day on the canal's
supporters and opponents). Relabel M3U2 to name its narrative. Unit 3 stays 39 days. LAYER base text. REPEAT new.

### 2. Unit 1's essay rows are placed later (major; firm)

**What is wrong.** Base M1U2 assesses W.4.2, W.4.5, L.4.1f and L.4.2b; its four-paragraph essay is informative. The
frame keeps it but places e4-informative and e4-writing-process in unit 2 and e4-grammar in unit 4. The
essay-structure model is "introduced unit 2", yet unit 1's essay already uses it: a model used before it is taught.

**Why it matters.** Order of first teaching is what the gate cannot see and what the rubric's progression items read.

**Fix.** Move e4-informative and e4-writing-process to unit 1, and the essay-structure model with them. Place e4-grammar
where its parts are taught in the base, named by part: L.4.1f in unit 1; 1b, 1e and 1g in unit 3; 1a, 1c and 1d in
unit 4. Unit 4 is lighter still; that is acceptable for a year-end synthesis unit (finding 6). Row moves go to Cory
through the lead. LAYER frame and progression. REPEAT new (base-order placement).

### 3. RL.4.7 is first taught on a poem (moderate; firm)

**What is wrong.** RL.4.7 asks for connections between the text of a story or drama and a visual or oral presentation
of it. The frame first teaches it on a poem against its recording.

**Fix.** Teach it on the unit 2 drama scene against a staged or recorded reading, or on the prose story against a
recording; the poem can stay as practice. The row text on e4-poetry-drama changes to match: add it to the lead's item
3. LAYER standard. REPEAT yes (standards in full).

### 4. The Erie Canal overlaps social studies grade 4 unit 5 (moderate; settled pick)

**What is wrong.** Social studies grade 4 unit 5 (about school days 77 to 100) lists "the Erie Canal as the case of a
canal" as a candidate. ELA unit 3 runs about days 78 to 116, on the same canal, at the same time. The frame does not
say how the two meet.

**Fix (settled).** Social studies unit 5 uses the ELA canal set as its case, with no second canal text; ELA unit 3
names social studies unit 5 as the lean. Record both ends. Also: the history text's "taken by treaty and sale"
understates the record. New York's purchases of Oneida and other Haudenosaunee land in the 1780s and 1790s were later
found to break the federal Nonintercourse Act (the Oneida land claim cases, 1985; from memory). The history set should
say so plainly. The Haudenosaunee community reader the frame names is right. LAYER frame. REPEAT yes (both ends of a
handoff).

### 5. Life Science alternative module not named (moderate; firm)

EL 2017 grade 4 ships an alternative module 2 (module-2-life-science). **Fix.** One source-map line: left out, with
the reason the animal-defenses module is kept. LAYER base text. REPEAT new.

### 6. Unit 4 owns 3 rows; the skills block (minor; judgment call)

Unit 4 owns 3 rows against 37 days, lighter after finding 2. The days follow EL module 4 and carry the year-end
product; the unit's reason should say so. The 90-minute day (60 plus 30) is workable for grade 4, but the frame should
state a floor for independent reading in the 30 (at least 20 minutes on three days a week) and where grammar practice
sits, since the ALL Block's grammar part is otherwise dropped unnamed. LAYER frame. REPEAT yes (days by load).

### 7. Science calendar line (minor; firm)

The frame says science grade 4 teaches 4-LS1-1 "before or during" ELA unit 2. Science grade 4 teaches it in its unit
6, about school days 129 to 156. **Fix.** "ELA unit 2 reads about animal defenses first; science unit 6 builds the
structure-function model later in the year." LAYER frame. REPEAT yes ("first" claims).

### 8. W.4.9b has no named home (minor; firm)

e4-evidence-inference carries W.4.9 but the frame names only the literary part. **Fix.** Name 9b on the unit 3
informative writing from the canal texts. LAYER standard. REPEAT yes.

### 9. Myths in a canal unit (minor; judgment call, not required)

Three myth days inside a canal unit fit the topic thinly. An option: teach RL.4.9 on trickster and animal tales in
unit 2 (animal defenses), freeing unit 3 for the canal. The frame may keep its choice. LAYER frame. REPEAT new.

## Checked and found right (do not undo)

- Base counts 37, 39, 39 and 38 match the frame's units; unit days 38, 39, 39, 37 with the screens and audio swap named.
- Every row placed once; every lettered part named.
- Band 740 to 1010; picks named; paper path; respond days and "Candidate:" cells; sensitivity reads with qualified
  readers; no percents ahead of math.

## Seams

- Grade 3 to 4: grade 3's handoffs are picked up. Grade 4 to 5: grade 5's assumes match what grade 4 hands on.

## Cross-subject

Social studies grade 4 unit 5 (finding 4); science grade 4 (finding 7).

## Lessons from the social studies frames

1 met. 2 met. 3 met (split of the 30 not stated, finding 6). 4 partly (findings 3, 8). 5 missed (finding 2). 6 missed
(finding 7). 7 missed for the canal lean (finding 4). 8 met. 9 partly (finding 6). 10 met. 11 met. 12 met. 13 met. 14
met. 15 met.

## The lens checklist (course frame layer)

Met: rows once; band; picks; sensitivity; paper path. Missed: base-order placement (finding 2); the replacement map
(finding 1). Not applicable: none.

## What I could not judge

- Whether the 1816 memorial and the canal texts reach the band's top end: texts not chosen.
- The Oneida case details are from memory; the history set's writer should check them at source.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Unit 3 day swap: M3U1 1 to 3 as canal launch; M3U2 5 and 13 on the 1816 memorial; myth days from M3U2 11, 12 and one of M3U1 4, 5 | The cut named the wrong lessons; day count unchanged | frame Source map, unit 3 |
| Social studies grade 4 unit 5 uses the ELA canal set as its case | One canal text set, both ends recorded | frame unit 3; social studies grade 4 unit 5 (through its lead) |
| RL.4.7 first taught on the drama scene | The standard names story or drama | frame unit 2 |
| Science calendar line rewritten | Science teaches 4-LS1-1 late in the year | frame cross-subject |
| W.4.9b named on unit 3 | Standard in full | frame unit 3 |

## For the lead (row moves, through Cory)

- e4-informative and e4-writing-process to unit 1; e4-grammar spread by part (finding 2).
- e4-poetry-drama text adjusted for RL.4.7 (finding 3; adds to the lead's item 3).

## For Cory

- A Haudenosaunee community reader for the canal unit (already named in the frame): people.

## Sources

From memory, not re-fetched: Common Core ELA (2010) grade 4; the Oneida land claim history (County of Oneida v.
Oneida Indian Nation, 1985). EL Education K-5 2017 grade 4 from the repository copy. The rest from the repository.

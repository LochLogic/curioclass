# Frame read: english-language-arts-grade-3 (ELA, grade 3), 2026-11-14

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/ela.md, docs/RUBRIC-ELA.md (Gateway 1 and the grades 3 to 5 shares).
- The frame docs/courses/english-language-arts-grade-3/frame.md and its row in data/plans/frames.csv (4 units, 160
  days). No data/plans/english-language-arts-grade-3/source-map.csv exists yet; the frame's "## Source map" section is
  the map read here.
- The 28 grade 3 rows of data/progressions/ela.csv, and the grade 2 and grade 4 rows at the seams.
- The frame before, docs/courses/english-language-arts-grade-2/frame.md, and the frame after,
  docs/courses/english-language-arts-grade-4/frame.md.
- Same-year frames: docs/courses/social-studies-grade-3/frame.md and docs/courses/science-grade-3/frame.md.
- docs/sources/BASE-TEXTS.md and the base text itself, S:\CurioClass-sources\el-education-k5-2017, grade 3: the
  module, unit and ALL Block overviews and the lesson file lists, counted lesson by lesson.
- docs/pipeline/briefs/frame-write.md, "Lessons from the social studies frames" (all 15 checked below).
- docs/agents/decisions/DESK-ANSWERS.md (2026-11-12 and 2026-11-13 ELA cards).
- Gates: `frame.py check english-language-arts-grade-3` 0 failures; `plan.py check` passes for this frame;
  `stale.py check` 0 failures.
- Standards are judged from my knowledge of the Common Core ELA standards (2010), not re-fetched.

## Verdict

The frame is sound in its bones: the four EL grade 3 modules are kept in order, 37 + 38 + 39 + 39 = 153 base lessons
match the 153 unit days, all 28 rows sit once, every lettered part is named, and the 420 to 820 band, paper path,
picks and sensitivity notes are right. The biggest fault is that several rows sit in a later unit than the kept base
lessons that teach and assess them (fluency, the writing process, word strategies, speaking), so unit 1 uses tools the
frame says arrive in unit 2. The one change that matters most is to place those rows where the base assesses them;
next, the 30-minute skills block is too small for what grade 3 asks of it.

## Findings, most serious first

### 1. Rows sit later than the kept base lessons that assess them (major; firm)

**What is wrong.** The frame keeps EL module 1 whole as unit 1, but that module teaches and assesses more than the
frame places there. From the unit overviews: M1U3's end-of-unit assessment is the recorded reading (RF.3.4, SL.3.5)
and the revised reading contract (W.3.2, W.3.5); the performance task is assessed on W.3.4 and W.3.5. M1U1's
end-of-unit assessment covers RL.3.4 and L.3.4; M1's first mid-unit covers SL.3.6. The frame puts e3-fluency and
e3-writing-process in unit 2, e3-literal-nonliteral and e3-word-strategies in unit 2, and e3-speaking-reports in unit
4. Smaller cases of the same kind: M2 assesses L.3.1d, e, g, h and i, but e3-word-forms sits in unit 4 and
e3-sentences in unit 3; M3's performance task assesses SL.3.4 and SL.3.6.

**Why it matters.** A writer following the frame either drops the base's unit 1 assessment or teaches a row before
its placed unit, which the gate cannot see. The rubric's growth-across-the-year items read the order of first teaching.

**Fix.** Move e3-fluency and e3-writing-process to unit 1 (the recorded reading, the reading contract and the
bookmark); unit 2's poems then count as the fluency extension. Move e3-word-strategies and e3-literal-nonliteral to
unit 1 where the base assesses them (RL.3.4 on the unit 1 stories, L.3.4 on its words), leaving unit 2 the poems as
practice. Put e3-speaking-reports in unit 3 (the M3 performance task) and e3-word-forms in unit 2 (the M2 grammar
lessons), naming any part that waits. Add the recorded reading and the reading contract to the unit 1 description.
These are standard moves between units, so they go to Cory through the lead (For the lead). LAYER frame and
progression. REPEAT new (base-order placement).

### 2. The 30-minute skills block cannot hold its list (major; likely)

**What is wrong.** The second block is 30 minutes for daily long-word work and spelling, then fluency partner reading
or independent reading conferences on alternate days, plus small-group help. Independent reading falls to about 15
minutes every other day, roughly 37 minutes a week. The EL ALL Block's grammar, usage and mechanics practice is
dropped without saying so, and the grammar openers are added to a base lesson the frame says is "kept whole", so the
unit lesson runs over 60 minutes.

**Why it matters.** Rubric item 2a wants an independent reading system a teacher can track, and grade 3 is the year
word reading and fluency must close (22 of 24 and 6 of 8 on the word-reading and fluency items).

**Fix.** State the minute split of the 30, set a floor for independent reading (at least 20 minutes on three days a
week), say where grammar practice sits (the openers inside the 30, not on top of the 60), and name what of the ALL
Block is cut. Whether grade 3 needs more than 90 minutes is already the lead's item 1; it stays with Cory. LAYER
frame. REPEAT yes (days by load).

### 3. The Life Science alternative module is not named (moderate; firm)

**What is wrong.** EL 2017 grade 3 ships an alternative module 2 (folder module-2-life-science). The source map
neither places it nor lists it as left out.

**Why it matters.** The brief asks every base unit to be placed or cut with a reason.

**Fix.** Add one line to the source map: "Left out: the Life Science alternative module 2; the frog module is kept
because [reason]." LAYER base text. REPEAT new.

### 4. Row text that contradicts the frame (moderate; firm)

**What is wrong.** e3-character-actions' note says children are "kept from school by war or poverty", but the frame
replaced the war text and keeps no war. e3-compare-two-texts says it is practised "in unit 2 on two frog texts"
before its unit 4 placement. Neither is in For the lead.

**Fix.** Add both to For the lead with replacement text: "kept from school by poverty, distance or work" and "first
practised in unit 4 on the two water texts; unit 2 reads two frog texts side by side without the comparison task".
LAYER progression. REPEAT yes.

### 5. Slavery is named in ELA before social studies teaches it (minor; likely)

**What is wrong.** Unit 1's short excerpt from Booker T. Washington's own account names slavery; social studies
grade 3 teaches it in unit 5.

**Fix.** Add an "if later" line: unit 1 gives one sentence of context in plain words and social studies unit 5 builds
it; the sensitivity read already covers the excerpt. LAYER frame. REPEAT yes (if-later line).

### 6. Unit 4 owns only 3 rows (minor; judgment call)

**What is wrong.** Unit 4 owns 3 rows against 37 days.

**Why it is not worse.** The days follow EL module 4 lesson for lesson and carry the year-end opinion essay and the
water product. The "why" line should say so plainly.

**Fix.** Add to unit 4's reason: "owns few new rows; its 37 days are the base module's practice and the year-end
product." LAYER frame. REPEAT yes (days by load).

### 7. Typo in the models table (minor; firm)

"units 1 uses it" in the context-clues row. **Fix.** "unit 1 uses it". LAYER frame. REPEAT new.

## Checked and found right (do not undo)

- Source map against the base: modules 1 to 4 have 37, 38, 39 and 39 lessons, 153 in all, matching the frame. The
  unit 1 screens (+2) and unit 4 audio announcement (-2) are named.
- Every row placed once; every lettered part of L.3.1, L.3.2, L.3.3 and the rest named.
- Text band 420 to 820; one chapter book read whole.
- Two checks, each with a respond day after; check-set cells start "Candidate:".
- Picks named; readiness checks on unit 1; paper path; no student account; qualified readers named for the
  sensitivity reads.
- Water in grade 3 kept different on purpose from grade 5.

## Seams

- Grade 2 to grade 3: every grade 2 handoff in the frame's table is picked up, and grade 2's frame names the same
  rows. Matches.
- Grade 3 to grade 4: grade 4's frame assumes what grade 3 hands on; finding 1 moves rows earlier inside grade 3 and
  does not change what reaches grade 4.

## Cross-subject

- Social studies grade 3: map skills and claim-evidence leans line up in time.
- Science grade 3: life cycles (school days about 49 to 77) run during ELA unit 2 (frogs). Habitats (3-LS4-3, about
  days 79 to 104) come after; the frame's "if later" line covers it.
- Slavery: finding 5.

## Lessons from the social studies frames

1 respond day after each check: met. 2 "Candidate:" cells: met. 3 time a day stated: met, but the split inside the 30
is not (finding 2). 4 standards in full: met. 5 each thread starts where first used: missed (finding 1). 6 "first"
claims checked: missed in two rows (findings 1, 4). 7 both ends of every handoff: met. 8 "if later" lines: met except
finding 5. 9 days by load: partly (findings 2, 6). 10 questions answerable from the unit: met. 11 picks named: met.
12 sensitivity reads: met. 13 no math ahead of math: met (no fractions or percents). 14 paper path: met. 15 no status
lines about other files: met.

## The lens checklist (course frame layer)

Met: every row once; base text followed in order; band and volume; picks; sensitivity; paper path. Missed: order of
first teaching against the base (finding 1); independent reading time (finding 2). Not applicable: none.

## What I could not judge

- The real minute load of the EL lessons once the openers are added: needs one lesson timed by a teacher.
- Whether the replacement water texts reach the band's top end: the texts are not chosen yet.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Recorded reading and reading contract named in unit 1's description | They are the base's unit 1 assessment | frame unit 1 |
| Grammar openers sit inside the 30-minute block | The base lesson is kept whole at 60 | frame Days |
| Life Science module listed as left out | Every base unit placed or cut | frame Source map |
| Typo fixed | | frame models table |

## For the lead (row moves, through Cory)

- Move e3-fluency, e3-writing-process, e3-word-strategies and e3-literal-nonliteral to unit 1; e3-speaking-reports to
  unit 3; e3-word-forms to unit 2 (finding 1).
- Replacement text for e3-character-actions and e3-compare-two-texts (finding 4).

## For Cory

- Grade 3 day length: 90 minutes or longer (the frame's own lead item 1; finding 2): scope.

## Sources

From memory, not re-fetched: Common Core ELA (2010) grade 3 standards. EL Education K-5 2017 grade 3 from the
repository copy (module and unit overviews, lesson lists). The rest from the repository files above.

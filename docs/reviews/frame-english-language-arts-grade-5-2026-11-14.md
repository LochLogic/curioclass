# Frame read: english-language-arts-grade-5 (ELA, grade 5), 2026-11-14

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/ela.md, docs/RUBRIC-ELA.md (Gateway 1 and the grades 3 to 5 shares).
- The frame docs/courses/english-language-arts-grade-5/frame.md and its row in data/plans/frames.csv (4 units, 160
  days). No data/plans/english-language-arts-grade-5/source-map.csv exists yet; the frame's "## Source map" section is
  the map read here.
- The 30 grade 5 rows of data/progressions/ela.csv, and the grade 4 and grade 6 rows at the seams.
- The frames before and after: docs/courses/english-language-arts-grade-4/frame.md and
  docs/courses/english-language-arts-grade-6/frame.md.
- Same-year frames: docs/courses/social-studies-grade-5/frame.md and docs/courses/science-grade-5/frame.md.
- docs/sources/BASE-TEXTS.md and the base text, S:\CurioClass-sources\el-education-k5-2017, grade 5: module and unit
  overviews, assessment overviews and lesson file lists, counted lesson by lesson.
- docs/pipeline/briefs/frame-write.md, "Lessons from the social studies frames".
- docs/agents/decisions/DESK-ANSWERS.md, 2026-11-13, card q-cross-progression-1 (the water replacement).
- Gates: `frame.py check english-language-arts-grade-5` 0 failures; `plan.py check` passes for this frame;
  `stale.py check` 0 failures.
- Standards are judged from my knowledge of the Common Core ELA standards (2010), not re-fetched.

## Verdict

The frame's topics are good (the start-over unit, El Yunque, Jackie Robinson, water and the Colorado River) and its
form follows the brief: rows once, standards by part, picks, paper path, respond days, hundredths not percents. But
its source map does not match the base text: it counts 151 base lessons where there are 154, so "no base lesson is
left out" is false, and it mislabels three base units, which moves the literary anchor out of unit 2 and hides the unit
1 monologue. The one change that matters most is to correct the map and put the rows back where the base teaches
them; next, the grade 6 seam repeats the flood and start-over question.

## Findings, most serious first

### 1. Base lesson counts are wrong (major; firm)

**What is wrong.** Counted from the lesson files: M1 = 12 + 16 + 13 = 41; M2 = 13 + 13 + 13 = 39; M3 = 12 + 15 + 13
= 40; M4 = 13 + 9 + 12 = 34; 154 in all. The frame says 151 and maps M2U2, M3U3 and M4U1 as lessons 1 to 12. Each of
those units runs to lesson 13; lessons 12 and 13 come in one download, which is likely why they were missed.

**Fix (settled).** Unit 1 41 days, unit 2 39, unit 3 40, unit 4 33. Merge M4U1 lessons 12 and 13 (recording the
announcement) into one audio day, as grades 3 and 4 already do. The community water research takes M4U3's research
week (the base's kit-supply research); no days added. Total 153 in units plus 7 at course level = 160, unchanged in
frames.csv. LAYER base text. REPEAT new.

### 2. Base units mislabelled; unit 2 loses its literary anchor (major; firm)

**What is wrong.** Base M2U2 is literary: it teaches and assesses RL.5.6 and RL.5.9 (mid-unit), RL.5.4, and a literary
analysis essay (W.5.2, W.5.9). The frame labels it "comparing structures; research", which is M2U1. Base M4U1 week 2 is
planning and recording the announcement (SL.5.4, SL.5.6, L.5.2a, L.5.2c); base M4U3 is kit research, the opinion
essay, the leaflet and a live presentation (performance task SL.5.4 to 5.6). With M2U2 misread, the frame's unit 2 has
no literary anchor, and RL.5.6 and RL.5.9 move to unit 4 with no reason given.

**Fix.** Relabel the three units in the source map. Restore a literary pair in unit 2 (two stories set in the
rainforest, or a story and a poem) and place e5-genre-compare there; the row already names unit 2 as an option. Keep
e5-narrator-influence in unit 4, or say plainly that unit 2 previews it. LAYER base text and frame. REPEAT new.

### 3. The unit 1 monologue is missing and its rows sit in unit 2 (major; firm)

**What is wrong.** Base M1U3 is the monologue: W.5.3 is taught and assessed there (mid-unit), and the performance task
is assessed on RF.5.4, W.5.4, W.5.5 and W.5.8. The frame's unit 1 never mentions the monologue, places e5-narrative,
e5-writing-process and e5-research in unit 2, yet the e5-narrative and e5-fluency rows themselves name the unit 1
monologue.

**Fix.** Name the monologue and its recorded performance in unit 1. Move e5-narrative and e5-writing-process to unit 1;
e5-research to unit 1 if the base's W.5.8 sources are kept, else say unit 1 previews it. Row moves go to Cory through
the lead. LAYER frame and progression. REPEAT new (base-order placement).

### 4. Rows still worded for the replaced module (moderate; firm)

**What is wrong.** Eight rows still carry the replaced disaster module's wording. The lead's item 2 gives replacement
text for all eight, which is good. Not covered: e5-informative ("unit 2 essay on sensory language", "unit 3 essay
comparing athletes"), e5-integrate-several ("compare and contrast essay"), e5-opinion (unit 3 "factors" against the
frame's "qualities"). Also, DESK-ANSWERS 2026-11-13 (q-cross-progression-1) says "Nine grade 5 rows ... updated", but
eight still carry the old wording.

**Fix.** Add the three rows to the lead's item 2 with text that matches the frame (unit 2 literary analysis essay;
unit 3 essay on a quality shown across accounts; "qualities" throughout). Rewrite the DESK-ANSWERS note: "Nine grade 5
rows named for update; replacement text sits in the grade 5 frame's For the lead item 2; rows not yet edited." LAYER
progression and process. REPEAT yes (stale notes).

### 5. Seam with grade 6 repeats flood and start-over (moderate; likely)

**What is wrong.** Grade 6 unit 1 asks what a family and a town need to start again after a flood. That nearly repeats
grade 5 unit 1's start-over question and grade 5 unit 4's flood survival story. Water now runs through grades 3, 5 and
6.

**Fix.** Make both grade 5 unit 4 stories about drought and scarcity, not flood, and record the grade 6 seam in both
frames' seam tables. LAYER frame. REPEAT yes (seams).

### 6. Rights routes for two text kinds (moderate; likely)

**What is wrong.** Unit 3's 1947 newspaper reports and "a teammate's later memory" have no stated rights route;
whether a 1947 copyright was renewed is case by case. The UDHR "plain-language form" has unclear authorship (from
memory).

**Fix.** For 1947 reports, name the check (renewal search) and a fallback (Curio Class's own account built from the
facts). For the UDHR, use the official text or Curio Class's own plain explainer. LAYER frame. REPEAT new.

### 7. Life Science alternative module not named (moderate; firm)

EL 2017 grade 5 ships an alternative module 2 (module-2-life-science). **Fix.** One source-map line: left out, with
the reason. LAYER base text. REPEAT new.

### 8. Unit 4's load reason (minor; judgment call)

Unit 4 owns 3 rows but carries the year-end opinion essay, leaflet and presentation. Its days are fine at 33; its
reason should say the load is the product, not new rows. The 90-minute day is workable for grade 5; state a floor for
independent reading inside the 30 and where grammar practice sits. LAYER frame. REPEAT yes (days by load).

## Checked and found right (do not undo)

- Topics and replacements: El Yunque, Jackie Robinson, water and the Colorado River.
- Rows once; standards by part; band 740 to 1010; picks; paper path; respond days and "Candidate:" cells; sensitivity
  reads with qualified readers.
- Hundredths, not percents, in the water unit (no math ahead of math).
- Science grade 5 units 5 and 6 (water) line up in time with ELA unit 4.
- Water in grade 5 kept different from grade 3.

## Seams

- Grade 4 to 5: grade 4's handoffs are picked up.
- Grade 5 to 6: finding 5.

## Cross-subject

Science grade 5 units 5 and 6 (water) line up in time with ELA unit 4. I found no lean on social studies grade 5 that its frame teaches later.

## Lessons from the social studies frames

1 met. 2 met. 3 met (split of the 30 not stated, finding 8). 4 met. 5 missed (finding 3). 6 missed ("no base lesson
is left out", finding 1). 7 partly (finding 5). 8 met. 9 partly (finding 8). 10 met. 11 met. 12 met. 13 met. 14 met.
15 met.

## The lens checklist (course frame layer)

Met: rows once; band; picks; sensitivity; paper path. Missed: source map (findings 1, 2); base-order placement
(finding 3). Not applicable: none.

## What I could not judge

- Renewal status of any particular 1947 report: needs the texts chosen.
- Whether a literary pair for unit 2 can be found at band: texts not chosen.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Unit days 41, 39, 40, 33; M4U1 12 and 13 merged into one audio day; water research takes M4U3's research week | Base counts are 154; total stays 160 | frame Days, Source map |
| Source map relabels M2U2, M4U1, M4U3 | Match the base | frame Source map |
| Unit 4 stories both about drought | Keeps grade 6's flood question fresh | frame unit 4 |
| UDHR official text or Curio Class's own explainer | Clear authorship | frame unit 4 |
| Monologue named in unit 1 | Base M1U3 | frame unit 1 |

## For the lead (row moves, through Cory)

- e5-genre-compare to unit 2 (finding 2); e5-narrative and e5-writing-process (and possibly e5-research) to unit 1
  (finding 3).
- Replacement text for e5-informative, e5-integrate-several and e5-opinion (finding 4).

## For Cory

- None beyond the row moves above.

## Sources

From memory, not re-fetched: Common Core ELA (2010) grade 5; the UDHR plain-language version's authorship; US
copyright renewal rules for 1947 works. EL Education K-5 2017 grade 5 from the repository copy. The rest from the
repository.

# Health progression: expert cold read, 2026-11-19

Reader: the curriculum expert (docs/agents/EXPERT.md), run cold on a draft that is not yet in data/progressions/.
Nothing was edited except this report.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/health.md, the health part of docs/ADOPTION-BAR-SUBJECTS.md (items 1 to 10, "Fails if"),
  docs/courses/health/STANDARD.md and APPROACH.md (the layer above; not earlier versions of the progression).
- The draft: data/progressions/parts/health.csv (206 rows, K to 9) and parts/health-edges.md (51 band-crossing edges).
  Rows by grade: K 19, 1 20, 2 17, 3 21, 4 19, 5 20, 6 21, 7 20, 8 21, 9 28. Sensitive rows: 22 (K 1; grades 1 to 6 two each; grades 7 to 9 three each).
- data/standards/nhes-2024.txt (172 indicators, our words) and data/standards/hecat-topics.txt (81 outcomes, our words).
- For cross_subject only: data/progressions/science.csv, math.csv and ela.csv (ids and standard codes, to see what those subjects own).
- Gate: `gate_part.py health` reports 206 rows, 0 failures. `stale.py check`: 62 files, 0 failures. plan.py not run, as told.
- I did not open earlier health course pages, reconcile reports or the earlier prework read. For REPEAT I compared finding types with the
  headings of the science, social studies and ELA progression reads of 2026-11-13.
- Checks run by script over the csv (my own, in the scratchpad): ownership by span, every indicator owned once, owner grade inside span,
  assumes/hands_on reciprocity and grade gaps, model_in against assumed rows' model_out, sensitive rules 2 and 4, HECAT tag validity and a
  comparison of the tags with the band coverage map in STANDARD.md section 4, edges file against the csv.

## Verdict

The frame is sound: all 172 indicators have exactly one owner inside its span, every owner grade is defensible, no row owns an indicator
from the wrong span, every sensitive row owns nothing and nothing non-sensitive assumes one, and assumes/hands_on agree both ways with the
edges file. The biggest risks are three. Grade 9 carries 54 owned indicators in 80 days, about twice the density of any earlier grade.
The HECAT "Serves" tags leave 32 cells of the coverage map unmatched and are checked by nothing. And the notes lean on science
for germs, body facts and puberty, none of which the science progression owns (cross_subject is empty on all of them). If one change is
made first: add a machine check of the "Serves HECAT" tags against the band map, because it will show every other coverage gap at once.
Twelve findings; none blocks moving the draft into data/progressions/ once findings 1 to 4 are decided.

## Findings, most serious first

### 1. Grade 9 fits 80 days only by thin coverage (serious; judgment call on the fix)

Counts (owned indicators per grade, from the standard column): K 10, 1 14, 2 9, 3 11, 4 14, 5 14, 6 13, 7 17, 8 16, **9 54**.
Per teaching day (K to 5: 30 sessions of 30 minutes, 6 to 8: 45 sessions of 45 minutes, grade 9: 80 days of 45 minutes, per APPROACH.md Pacing):
K to 2 about 0.37 indicators a day, 3 to 5 about 0.43, 6 to 8 about 0.34, **grade 9 about 0.68**. Rows per day look the opposite
(0.35 at grade 9, 0.44 in 6 to 8, 0.67 below), which is why 28 rows seems to fit: the rows at grade 9 are not smaller, they own 2 or 3
indicators each (25 non-sensitive rows own all 54), and span-12 verbs are the hardest (evaluate, appraise, design, measure).
APPROACH.md says a full skill unit is understanding, two fluency days, application, check and respond: six days. At two to three rows per
unit, 28 rows make about 11 units, about 66 days, plus the goal thread, plus cumulative checks: it just fits, but each unit then covers
five to eight span-12 indicators in six days, with one check each. The three sensitive units are inside the 80 days (rule 6), so a school
that leaves them out gains days but a school that keeps them has about 2.6 days per non-sensitive row.
Fix (no row deleted): (a) mark `g9-phw-goal-assess-write` and `g9-phw-goal-carry-revise` (6 indicators, S6.12.1 to 6) as one running thread
of short weekly slots across the semester, not two units, in the frame; (b) the frame names the seven rows with three indicators
(`g9-phw-factors-and-behaviour`, `g9-phw-access-to-care`, `g9-fn-information-skill`, `g9-meh-influences-judge-plan`,
`g9-meh-teams-negotiate-views`, `g9-t-decision-views-process`, `g9-s-advocacy-issue`) as four-day units and the one-indicator rows
(`g9-meh-counter-disinformation`, `g9-meh-boundaries-consent`, `g9-aod-say-no-across`, `g9-v-conflict-manage`, `g9-pa-measure-decisions`)
as two-day revisits. Whether that depth is enough is Cory's (see For Cory).
LAYER progression. REPEAT no (new for a one-semester course).

### 2. HECAT coverage: the tags are the only carrier, they are unchecked, and the map is not met (serious)

Every row carries exactly one "Serves HECAT.X.HBOn" sentence and every code exists (topic and 1..n all valid), so the format is
machine-readable. As a carrier of coverage it is good enough for the outcome list (bar item 10 asks for a coverage map, not scoring), with
three conditions the draft does not meet:

a. **Nothing checks it.** The gate does not read notes. I compared the tags with STANDARD.md section 4. Cells in the map that no row serves:
   PHW 3, 4 (6 to 8); PHW 3, 4, 8, 12 (9); FN 6 (3 to 5); FN 2 to 7, 9 (9); MEH 2, 3 (K to 2); MEH 3 (3 to 5); MEH 3, 5 (9);
   PA 3, 4, 6 (6 to 8); PA 3, 4 (9); S 1, 3, 6 (6 to 8); S 2, 7 (9); V 6 (6 to 8); T 2 (9); AOD 8 (6 to 8). 32 cells. Tags in cells the map
   does not list (harmless, update the map): S 8 (K to 2), FN 10 (3 to 5), FN 11 (6 to 8), SH 10 (6 to 8).
b. **Tags over-claim depth.** `g9-sh-health-and-consent` serves 10 outcomes and `g6-fn-eating-patterns` 9. A tag says "touches", not
   "knowledge expectation met and skill practised", which is what HECAT scores. Fine for a map; the unit plans must state which of a row's
   outcomes the days actually teach.
c. **Mis-tagged food rows.** `g4-fn-food-claims-source-check`, `g5-fn-claims-that-hurt` and `g9-fn-information-skill` carry FN12 (help others
   eat well) for source-checking food claims. The matching outcome is PHW12 (avoid harm from fads and trends), which no row serves in any band,
   although `g7-fn-judge-claims` ("a wellness fad") and `g8-phw-handle-false-messages` teach exactly that.
Fix, row edits (item-level, I settle these): in notes, `g4-fn-food-claims-source-check` change "HECAT.FN.HBO8, HECAT.FN.HBO12" to
"HECAT.FN.HBO8"; `g5-fn-claims-that-hurt` change to "HECAT.FN.HBO8, HECAT.PHW.HBO12"; `g7-fn-judge-claims` add HECAT.PHW.HBO12;
`g9-fn-information-skill` replace FN12 with PHW12; `g3-fn-added-sugar-drinks` add FN6 (it already says water and milk are the everyday
drinks); `k-meh-calm-body` add MEH2; `g2-v-settle-it-with-words` add MEH3; `g5-v-conflict-steps` add MEH3 only if the map is widened;
`g7-v-conflict-prevent-end` add V6 ("when a person is not safe, walk away"); `g6-phw-prevent-illness-injury` add PHW3, PHW4 (sun and
hearing protection join helmets and handwashing in the comparison); `g8-aod-refusal-and-driving` add AOD8 (a plan that helps a friend
avoid the ride); `g9-aod-say-no-across` add S2; `g9-v-conflict-manage` add MEH3; `g9-aod-weigh-options-plan` add MEH5.
Process fix: a check in scripts/progression.py (separate job, not mine) that parses "Serves HECAT" from notes, checks the codes against
hecat-topics.txt, and lists each map cell no row serves, so STANDARD.md section 4 stops being unchecked.
The remaining cells are decisions for Cory (findings 1 and 4, For Cory).
LAYER progression and process. REPEAT no.

### 3. The non-sensitive place for correct private body part names is not in the row (serious)

STANDARD.md section 5 rests removability of every sexual health unit on one claim: correct body part names are first taught in
non-sensitive terms in PHW K to 2. `k-phw-body-names` words are head, arm, leg, heart, lungs, stomach, skin and the note says "outside body
parts and the main inside ones (heart, lungs, stomach, brain)". It names no private body parts. Yet `k-v-body-safety`, `g1-sh-families-and-respect`
and `g2-sh-bodies-grow-respect` each say "correct names are already taught". As written they are not, so leaving out the sensitive units
leaves K to 2 children without the names body safety needs. A K teacher reading this row would stop at the stomach.
Fix: in `k-phw-body-names` notes add "and the correct names for private body parts (penis, vulva, breasts, buttocks), taught in the same
plain voice with the idea of private, which is also the first word body safety uses"; add "private" to words; keep "Serves HECAT.PHW.HBO1".
This follows the rule already decided, so it is not new scope, but it changes what K teaches in plain terms, so it is on the For Cory list.
LAYER progression. REPEAT no.

### 4. Science leans are in notes only, and the science progression owns none of them (moderate; firm)

cross_subject is empty on rows whose notes say they use science: `k-phw-body-names` ("science course's body facts"), `g1-phw-stop-germs`
("science course's idea of tiny living things"), `g4-phw-prevent-illness-injury` ("science course's germs fact"), `g6-phw-prevent-illness-injury`
("science course's germ model"), plus the puberty rows (`g4-sh-body-changes`, `g5-sh-consent-and-health`, `g6-sh-puberty-and-health`) and
`g8-sh-prevention-and-health` (how infections spread, how pregnancy happens). I searched data/progressions/science.csv: it owns no germ,
microbe, infection, immune or puberty skill in K to 8. Body structures arrive at `s4-structures-function` (grade 4, 4-LS1-1, organs including
heart, lung, stomach, brain, skin) and `s6-cells-body-systems` (6) and `s7-body-systems-food` (7); human reproduction and puberty appear
nowhere (`s8-reproduction-behaviors` is animal behaviour). So STANDARD.md section 8 ("health uses the science model, does not reteach it")
cannot hold for germs, and at K the lean points forward four grades.
Fix: (a) `k-phw-body-names` and `g1-phw-stop-germs` drop the claim of a science lean: health teaches the plain facts (names; germs are tiny
living things that spread) itself in one or two sentences; (b) `g4-phw-prevent-illness-injury` and `g6-phw-prevent-illness-injury` rewrite
"uses the science course's germs fact" as "states the one fact needed (germs spread by touch, air, food and water; vaccines teach the body
to defend itself) and sources it"; (c) `g6-phw-habits-for-each-part` may lean on `s6-cells-body-systems`, and `g7-phw-living-with-conditions`
on `s7-body-systems-food`, written in cross_subject as `science:MS-LS1-1 (body systems work together)` and `science:MS-LS1-3 (body
systems, food)`. Whether science should add a germs and disease row is Cory's (cross-subject scope).
LAYER progression. REPEAT yes (a lean on nothing, as in the math and social studies reads).

### 5. Three real cross_subject leans are too early or wrong (moderate; firm)

- `g9-fn-information-skill` leans on `ela:RI.9-10.8`, and `g9-s-advocacy-issue` on `ela:W.9-10.1`. ELA owns both at grade 10
  (`e10-ri-argument-evaluate`, `e10-w-argument`); grade 9 only carries them (`~`). Health at grade 9 leans on a skill ELA has not yet
  owned. Fix: lean on the grade 8 owners instead: `ela:RI.8.8 (evaluate an argument and its evidence)` and `ela:W.8.1 (write an argument
  for an audience)`, or on the grade 9 carry rows `e9-ri-argument-evaluate` and `e9-w-argument` by id.
- `g7-pa-influence-differs-by-group` leans on `math:7.SP.A.1` (random samples). What the row does, compare two community profiles, is
  `math:7.SP.B.3` (`m7-compare-populations`). Settled below.
- `g6-fn-eating-patterns` leans on `math:6.RP.A.3` and `g6-pa-habits-supports-barriers` on `math:6.SP.B.5`: both math skills are owned at grade 6,
  the same grade. This is legal but the frame must place those health units after the math units; say so in the cross_subject text
  ("after the grade 6 ratio unit"). Other leans checked and correct: `ela:RI.4.8`, `W.4.1`, `RI.7.8`, `W.7.1`, `W.8.1`, `RI.8.8`, `SL.8.4`.
- Missing: PE shares nine PA rows ("Shared with PE") with no PE skill named in cross_subject. Name the PE skill by id when the PE progression
  is stitched; I did not read it.
LAYER progression. REPEAT yes (cross_subject; ELA read finding 4 is the same kind).

### 6. The weak assumes chains the writer named, and four more (moderate; firm)

The writer's three flags are right, and the strengths thread (S1.2.1, 1.5.1, 1.8.1, 1.12.1) is the broken one:

- `g3-phw-grow-strengths` hands on to `g5-meh-mind-habits`, two grades; grade 4 has no strengths row. `g5-meh-mind-habits` is about coping habits
  with strengths as a side clause, and `g6-phw-strengths-and-wellness` (S1.8.1) assumes it. Then `g6-phw-strengths-and-wellness` hands on to
  nothing, and `g9-phw-strengths-wellness-links` assumes `g8-phw-factors-shape-health`, a row about factors, not strengths: grade 6 to
  grade 9 is a three-grade jump with no strengths in grades 7 or 8. The thread is: g1, g2, g3, then a gap at 4, a partial at 5, g6, a gap
  at 7 and 8, g9.
  Fix (row edits): `g3-phw-grow-strengths` hands_on `g4-phw-goal-plan` (not g5); `g4-phw-goal-plan` add to assumes `g3-phw-grow-strengths`,
  add `~NHES.S1.5.1` to standard, add to notes "the first plan can build a strength"; `g4-phw-goal-plan` hands_on add `g5-meh-mind-habits`;
  `g5-meh-mind-habits` assumes `g4-phw-goal-plan; g4-meh-calm-stress` (replacing g3-phw-grow-strengths); `g4-meh-calm-stress` hands_on add
  `g5-meh-mind-habits`. For 7 and 8: `g6-phw-strengths-and-wellness` hands_on `g7-phw-living-with-conditions` (strengths and supports of
  characters; add `~NHES.S1.8.1`); `g8-phw-factors-shape-health` assumes add `g7-phw-living-with-conditions` (its own case is asthma) and
  add `~NHES.S1.8.1` (personal factors include strengths); `g9-phw-strengths-wellness-links` keeps `g8-phw-factors-shape-health` and adds
  note "revisits g6 strengths".
- `g6-meh-stress-coping` assumes `g5-meh-mind-habits` but its real prerequisite is `g4-meh-calm-stress` (the stress tools). Add
  `g4-meh-calm-stress` to its assumes (and hands_on there).
- `g6-phw-prevent-illness-injury` assumes `g5-s-choose-safe-option` (a decision row); its real prerequisite is `g4-phw-prevent-illness-injury`
  (two grades earlier, no grade 5 carrier). `g5-s-choose-safe-option` notes say "injury-prevention link back to ~S1.5.3" but the standard
  column does not carry `~NHES.S1.5.3`. Fix: add `~NHES.S1.5.3` to its standard, `g4-phw-prevent-illness-injury` hands_on
  `g5-s-choose-safe-option`, and `g5-s-choose-safe-option` assumes `g4-phw-prevent-illness-injury`.
- `g9-fn-habits-groups` says "revisits grade 6 patterns" but assumes only `g8-phw-habits-personal-community`; add `g6-fn-eating-patterns`
  (accept the three-grade jump, mark it a deliberate revisit) or carry `~NHES.S7.8.2` on `g7-fn-influences-on-eating`.
- `g9-phw-evaluate-habits` (S1.12.4, care of ongoing conditions) assumes `g8-phw-habits-personal-community`; add `g7-phw-living-with-conditions`
  (S1.8.4, owns the same idea, and is a dead end today).
- `g8-phw-factors-shape-health` (S1.8.6) assumes `g7-pa-influence-differs-by-group` but not `g5-phw-surroundings-community` (S1.5.6, dead end
  today). Add it as an assume with note.
LAYER progression. REPEAT yes (assumes that point at a topic or a neighbour, not the prerequisite; same as the science and social studies reads).

### 7. Care-seeking indicators: under PHW, but under the wrong outcomes and a late map (moderate; likely)

NHES care-seeking indicators: S1.2.7 (`g2-phw-doctor-nurse-visit`), S1.5.7 (`g5-phw-when-to-get-care`), S3.8.1 (`g6-phw-adult-or-professional`),
S1.8.7 (`g8-phw-health-care-services`), S1.12.9 and S3.12.1 and S3.12.2 (`g9-phw-access-to-care`). Placing them in PHW strand rows is right. The
outcome tags are not: PHW10 (use health care for illness and conditions) and PHW11 (checkups and screenings) first appear at grade 6,
while the standard requires care-seeking from K to 2. The writer worked around the map (g2 tagged PHW5, germs; g5 tagged PHW9, managing
conditions). PHW5 is not "when to see a doctor", and PHW9 is not "checkups, vaccines, screening" (`g5-phw-when-to-get-care` is exactly that,
plus "a long-lasting cough, an injury").
Fix (settled below): `g2-phw-doctor-nurse-visit` tag PHW11; `g5-phw-when-to-get-care` tag PHW10 and PHW11 (drop PHW9, which
`g4-phw-routines-and-conditions` already serves); amend the STANDARD.md map cells K to 2 (add 11) and 3 to 5 (add 10, 11) and replace the
note in `g2-phw-doctor-nurse-visit` that "the care-seeking outcomes are not in this band map". Also the handoff: `g2-phw-doctor-nurse-visit`
hands on to nothing and the S1.2.7 to S1.5.7 line has no carrier in grades 3 and 4: `g2-phw-doctor-nurse-visit` hands_on
`g3-phw-find-resources` (and that row assumes it), and `g3-phw-find-resources` hands_on `g4-phw-routines-and-conditions` (a clinic for a
long-term condition), which already hands on to `g5-phw-when-to-get-care`.
LAYER progression and standard. REPEAT no.

### 8. Handoffs that skip a grade, and dead ends where a strand stops and restarts (moderate; firm)

Gaps of two grades in assumes/hands_on (the notes say "skips" on purpose; STANDARD.md section 4 allows alternate years, but the row graph
should still carry the idea through the skipped year):
`k-s-safety-gear-and-cars` to `g2-s-outdoor-and-home-safety`, `k-t-smoke-and-vapor` to `g2-t-no-thanks-smoke`, `g1-aod-medicine-helpers` to
`g3-aod-medicine-rules`, `g3-phw-grow-strengths` to `g5-meh-mind-habits` (finding 6).
Fix with a carry row in the skipped grade: `g1-pa-play-safe` assumes `k-s-safety-gear-and-cars` (helmets in safe play) and hands_on
`g2-s-outdoor-and-home-safety`; `g1-s-unsafe-feels-wrong` assumes `k-t-smoke-and-vapor` (a found vape or pills: leave it, tell) and hands_on
`g2-t-no-thanks-smoke`, then drop the direct K to g2 edge; `g2-s-outdoor-and-home-safety` carries `~NHES.S1.2.3` medicine and cleaners stay
with adults, assumes `g1-aod-medicine-helpers`, and hands_on `g3-aod-medicine-rules`, then drop the g1 to g3 edge. These are the first three
rows' `assumes`, `hands_on` and notes only; no new rows. Edit `parts/health-edges.md` to match (three K-2 to 3-5 lines change).
Dead ends (no hands_on, K to 8): 30 rows. Most are fine leaves (the last use of a skill). The ones that break a strand: `g6-phw-adult-or-professional`
(care thread stops at 6; `g8-phw-health-care-services` assumes g7 literacy, not it: add it), `g6-phw-prevent-illness-injury` (g9 `evaluate-habits`
needs it: add `g7-phw-sleep-habits-community` as carrier or accept a three-grade jump and say so), `g5-s-online-safety` and `g7-s-online-boundaries` (the
online thread has no g8 or g9 row; `g9-meh-boundaries-consent` should assume `g7-s-online-boundaries`), `g4-s-decide-with-help`
(`g5-s-choose-safe-option` should assume it: S5.5.2 then S5.5.4), `g8-t-tobacco-influences` (the g9 tobacco rows assume an AOD row; add it to
`g9-t-decision-views-process` assumes), `g1-phw-surroundings` and `g1-phw-how-things-touch-me` (influence-check enters through g2 and g3 rows
that skip them; acceptable).
LAYER progression. REPEAT yes (dead ends and skipped grades are the science and social studies read findings).

### 9. Models: no row uses a model before it is introduced, but 52 rows do not receive it from what they assume (minor; firm)

All 11 models (influence-check, help-steps, i-statement, listening-steps, decision-steps, goal-plan, boundary-steps, conflict-steps,
source-check, refusal-steps, speak-up-plan) are introduced in or before the grade that first uses them; none is used early. But 52 rows list
a model_in that no assumed row carries out (help-steps 15 rows, influence-check 9, goal-plan 7, listening-steps 4, boundary-steps 4,
refusal-steps 4, others). The step cards return across topics by design (APPROACH.md "Practice that returns"), so this is a recording
gap, not a teaching gap. Cheap fix at stitch time: state in the frame that model_in is satisfied by the step card's first-introduction
row, or let the gate accept a model whose introducing row is anywhere earlier. Do not hand-edit 52 rows. The ones worth editing, because
the card first returns after a gap, are `g3-phw-grow-strengths` (goal-plan; its assumed row has no model) and
`g4-v-limits-and-respect` (conflict-steps, first introduced at g2 in a different strand than anything it assumes).
LAYER process. REPEAT yes (model recording).

### 10. Sensitive rule 4 broken once across topics, and one near-leak (minor; firm)

Checked by script: no non-sensitive row assumes a sensitive row; no sensitive row owns an indicator; every indicator a sensitive row carries
is owned by a non-sensitive row in the same band (rule 2); non-sensitive help routes exist in every band (rule 3).
Exceptions: `g1-sh-families-and-respect` assumes `k-v-body-safety`, a different sensitive topic. A school that leaves out body safety but keeps
sexual health has a unit that assumes it. Fix: `g1-sh-families-and-respect` assumes `k-v-kind-words-and-hands` (it already carries
`~NHES.S4.2.5`, owned there) and drop it from `k-v-body-safety` hands_on. Near-leak: `g7-meh-seek-and-give-support` (non-sensitive) includes "a friend
who seems very down: stay, listen, tell an adult at once". That is help-seeking, not method content, and fine, but the lens "No sensitive
content inside a non-sensitive unit" means the row's note must say it stops at telling an adult and never names self-harm; add "Stops at 'tell an
adult'; self-harm is `g7-meh-self-harm-help`." Likewise `g9-aod-say-no-across` lists "a partner" among circumstances: say "a partner or friend
asks you to ride or use" so dating content stays in `g9-v-abuse-and-dating-violence`.
LAYER progression. REPEAT no.

### 11. Notes that disagree with the standard column (minor; firm)

`g2-phw-why-health-matters` notes "reuses strengths from grade 1 (~S1.2.1)" but the standard column has only `NHES.S1.2.5`.
`g5-s-choose-safe-option` notes "link back to ~S1.5.3" but the column has only `NHES.S5.5.4` (see finding 6). Add the carries to the column
or drop the claim. Also stale for the move: `g2-phw-doctor-nurse-visit` note about the map (finding 7), and STANDARD.md section 4 "In the
progression (data/progressions/health.csv)" until the draft is placed. `stale.py` reports none.
LAYER process. REPEAT yes (stale notes).

### 12. Pace and words (minor; judgment call)

Row counts K 19, 1 20, 2 17, 3 21, 4 19, 5 20, 6 21, 7 20, 8 21, 9 28. Grades K to 8 are even (17 to 21). Grade 9 is 33 to 47 percent
above its neighbours (finding 1). Strand gaps: AOD has no row in grades 2 and 4; T none in grade 1 (both allowed as alternate years once the
carry rows of finding 8 are in); sexual health has no K row by design; PA has one row a year K to 7 (PE carries the moving). Safety in grade 8 has one
row (`g8-s-advocacy-results`), and safety 6 to 8 has no content row at all: S1, S3, S6 (vehicles, gear, dangerous places) are unserved there
(finding 2); that is a content gap, not only a tag gap, and is a For Cory item. Words: taught before used, at a fitting level, with
one watch: "advocacy" is the standard's word from grade 5 (S8.5.3) but the first word list that carries it is grade 7; the grade 4 and 5
rows use "speak up", which is right for children, so the unit plans should name it. "hotline" (g3) and "988" (g7) are used before the list at the
parent-facing notes only; fine.
LAYER progression. REPEAT yes (pace counts).

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Tag PHW12 on `g7-fn-judge-claims` and `g9-fn-information-skill`; drop FN12 from the g4, g5 (replace with PHW12) and g9 source-check rows | PHW12 is fads and trends; FN12 is helping others eat well | parts/health.csv notes |
| Map: PHW12 belongs in 6 to 8 (adds to the "All but 12" cell) | fads and supplements are judged at g7 under S3.8.4 | docs/courses/health/STANDARD.md section 4 |
| Care outcomes: PHW11 on `g2-phw-doctor-nurse-visit`; PHW10 and PHW11 on `g5-phw-when-to-get-care`; map K to 2 gains PHW11, 3 to 5 gains PHW10, 11 | S1.2.7 and S1.5.7 require care-seeking before grade 6; HBO5 and HBO9 do not fit | parts/health.csv, STANDARD.md map |
| Lean `g7-pa-influence-differs-by-group` on `math:7.SP.B.3` | comparing two community profiles is B.3, not random sampling | parts/health.csv cross_subject |
| Lean grade 9 rows on the grade 8 ELA owners `RI.8.8` and `W.8.1` | ELA owns the 9 to 10 versions at grade 10 | parts/health.csv cross_subject |
| Tag adds: FN6 g3-fn-added-sugar-drinks; MEH2 k-meh-calm-body; MEH3 g2-v-settle-it-with-words and g9-v-conflict-manage; V6 g7-v-conflict-prevent-end; PHW3, PHW4 g6-phw-prevent-illness-injury; AOD8 g8-aod-refusal-and-driving; S2 g9-aod-say-no-across; MEH5 g9-aod-weigh-options-plan | each row already teaches the behaviour | parts/health.csv notes |
| Strengths thread through g4-phw-goal-plan, g7-phw-living-with-conditions and g8-phw-factors-shape-health (finding 6) | a thread with a row in every grade is checkable | parts/health.csv, parts/health-edges.md |
| Carry rows for the three K to 2 and g1 to g3 skips (finding 8) | alternate-year topics still need a graph edge each year | parts/health.csv, parts/health-edges.md |
| `g1-sh-families-and-respect` assumes `k-v-kind-words-and-hands` | rule 4 | parts/health.csv |

## For Cory

1. **Grade 9 depth (changes what a semester teaches).** 54 span-12 indicators in about 80 days is twice the load of any earlier grade.
   Options: accept it as written (units of 2 to 4 days, goals as a running thread); or add a half-year course at grade 10 and move some
   owner rows there (the gate allows any grade in the span); or keep the semester and let the standard's last owners be graded 9 only for
   the 25 non-sensitive rows' cores. My lean: the first, with the frame naming the days, unless you want a second semester.
2. **Grade 9 map cells nothing serves (scope; STANDARD.md section 4 says bring these to you rather than drop them).** PHW 3, 4, 8; FN 2 to 7, 9;
   PA 3, 4; S 7; T 2 (and the cheap ones I settled). Is the 9 to 12 cell "all, as revisits", or "all not met by grade 8, and only these
   revisits"? I recommend rewriting the cell as the revisit list the 28 rows actually carry.
3. **Safety content in grades 6 to 8 (what a grade teaches).** No row teaches motor vehicle rules, gear or noticing dangerous places after
   grade 5 (S1, S3, S6 in the map). Add one row at grade 6 or 7, or let the map say these end at grade 5?
4. **Private body part names in kindergarten (what K teaches, audience).** The rule already says non-sensitive; the row does not do it yet.
   Confirm the plain wording in finding 3.
5. **Germs and disease in science.** Health cannot "use the science model" because the science progression owns none before the
   middle grades. Teach one plain fact in health (my fix), or add a short row to science?
6. **PE.** Nine PA rows say "Shared with PE" but name no PE skill. Do you want the PA 3, 4, 6 outcomes in 6 to 8 assigned to PE and
   marked so in the map?

## Lens checklist, progression layer

| Line | Result |
|---|---|
| Every band reaches all eight standards | met (every grade 1 to 9 touches S1 to S8; K has no S8 indicator in its span range) |
| Every skill standard practised in two or more topics in a band | met (checked from the strand spread; S4 in nine topics, S6 in PHW and PA only in K to 2: PHW and S; acceptable) |
| A coverage map whose cells name units | missed in part: the map is not machine-checked and 32 cells are unmatched (finding 2) |
| A topic taught once in a band with nothing after | met for all topics after carry rows (finding 8); AOD K to 2 is one row |
| A sensitive unit is removable | met with two flaws: body names (finding 3) and the g1 cross-topic assume (finding 10) |
| Getting help not only in a sensitive unit | met in every band |
| Indicators claimed in the wrong span | met: none outside its span, one owner each, no ~ before the owner except as preparation |
| Health reteaching a science model | missed in intent: leans on a science model that does not exist (finding 4) |
| Health and PE both planning the same lesson | not applicable at this layer; flagged (finding 5) |
| Behaviour named per unit, skills with steps, no scare content | met in notes: every row ends with a behaviour tag; teacher notes carry no-blame and no-weight lines |
| Figures dated | met: figure-bearing rows say "source and year" (tobacco, AOD) |

## What is right and should not be touched

- One owner each, inside its span, no gaps: 172 of 172, and the choice of "first fully met" is right throughout, including the grade 9
  rows (span 12 indicators cannot be met earlier).
- The sensitive-unit design: sensitive rows own nothing and carry `~`, non-sensitive units teach help twice, the notes name the leave-out and
  disclosure handling. It nearly works; fix the two items and leave the pattern.
- The shared step cards (help-steps, goal-plan, influence-check and the rest) and the safe-list goal rule.
- The edges file matches the csv exactly (51 band-crossing edges each way).
- No weight, calorie or good-and-bad-food language anywhere; no row asks a student for their own history.

## What I could not judge

- Medical and scientific accuracy of any fact (a separate pass, lens "expert read").
- The other eight HECAT modules' span tables (unread, per STANDARD.md); the map cells I compared against are the writer's.
- Whether the day counts are enough: that is for the frames.
- PE's progression for the PE leans.

## Sources

Files only, all in this repository (named under "What I read"). No outside source was opened; outside knowledge was not used for any finding.

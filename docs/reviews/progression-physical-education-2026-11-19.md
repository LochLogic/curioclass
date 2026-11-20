# Expert read: the physical education progression draft, K to 12 (2026-11-19)

A blind read. The draft is not yet in data/progressions/, so it was read from its parts file. Nothing but this report was edited.

## What I read

- data/progressions/parts/physical-education.csv: 203 rows (K 17, grade 1 16, 2 15, 3 18, 4 17, 5 14, 6 18, 7 20, 8 20, 9 14, 10 14, 11 10, 12 10), every column of every row.
- data/progressions/parts/physical-education-edges.md: the cross-band handoff list (agrees with the CSV).
- data/standards/shape-pe-2024.txt: all 210 indicators and our one-line words.
- The bar: the PE part of docs/ADOPTION-BAR-SUBJECTS.md; docs/courses/physical-education/STANDARD.md (band rule, rules 1 to 5, the PECAT placement paragraph); the head of docs/courses/physical-education/APPROACH.md; docs/standards-notes/pe-2014-to-2024.md (the five-to-four map, for the "older S2/S3/S5" wording).
- docs/agents/EXPERT.md, docs/agents/lenses/physical-education.md, docs/pipeline/briefs/progression-read.md.
- Lean targets only: data/progressions/math.csv and science.csv, social-studies.csv (to check each named skill exists and its grade). The headings of the four 2026-11-13 progression reads, only to tag REPEAT.
- Not opened: any reconcile report, any earlier PE review, STANDARD-adjacent course pages beyond the two allowed, anything under the forbidden paths.
- Gate: `gate_part.py` gave 203 rows, 0 failures. `scripts/stale.py check` gave 62 files, 0 failures; run on the parts file alone, 0 failures. plan.py was not run, as told.
- My own checks by script on the parts file: all 210 indicators owned exactly once; none owned outside its span; no unknown ids; assumes and hands_on are symmetric in every row; no em dashes; no company or product names.

## Verdict

Sound, with fixes to make before it moves into data/progressions/. Ownership, coverage and the band rule hold: every indicator has one owner in its own span, and every grade states an outcome for all four standards. The most serious faults are about the kindergarten and grade 1 placements against the review tool (three items the tool expects in kindergarten are carried as "tries, never graded", which leaves kindergarten with no assessment of them), the water rows (a skill indicator assessed by knowledge alone in schools with no pool, plus a contradictory safety line), and a short list of handoffs that point at a topic neighbour instead of the real prerequisite. Fitness data is private everywhere it appears; the gaps there are small. **12 findings** (3 moderate, 9 minor). Nothing moves a standard between grades by force; two choices go to Cory.

## Findings, most serious first

### 1. Review-tool placement in K to 2: three kindergarten items have no assessment, and placements are unmarked (moderate; likely; LAYER progression; REPEAT new)

What I checked against STANDARD.md section 3 (the placement paragraph, read 2026-11-16 and 2026-11-19):

- S2.2.2 chase and flee (g2-chase-flee) and S2.2.7 why stretch (g2-stretch-why): **right.** The tool first expects tactics and warm-up/cool-down in grade 3. Grade 2 is the last grade of the span, so a row must own them there, and both rows hold to naming ("names one move", "says one reason"), no scoring, no elimination. Keep.
- S1.2.9 overhand throw (g2-overhand-throw): **right** as rule 3 writes it (overhand first expected in grade 2). Cues are three; fine.
- S1.2.16 rope (g2-rope-fixed): **a judgment call, keep at grade 2.** Rule 3's general sentence says a skill the tool first expects in a grade is owned there, and the same paragraph says rope starts in kindergarten, then says rope is only attempted in K. The indicator itself (self-turned rope in a fixed spot) is a hard first-grade-or-later pattern, and the K row does cover hopping over a still and a slowly swung rope. Keep grade 2, but say so.
- S1.2.6 bounce (g1-bounce): same pattern; the tool expects hand dribbling in K, the row owns it in grade 1.

The faults:

a. **k-bounce-throw-tries** carries three tool-expected K items (bounce, underhand toss, rope) as "marked as seen, never graded". PECAT's three marks (stated, taught, assessed) then fail at K for these. Every other K row has the met, partly or not yet check. Fix: in k-bounce-throw-tries notes, replace "Assessed by a skill task: one try of each, marked as seen, never graded." with "Assessed by a skill task: one try of each, marked met, partly or not yet on one cue each (look, swing low, toss), as growth from the first try."
b. **No row carries the "from the tool / from memory / ours, untested" mark** that rule 3 requires, on g1-bounce, g2-overhand-throw, g2-rope-fixed, k-bounce-throw-tries. Fix: add to g1-bounce "Hand dribbling is first expected in kindergarten in the tool; owned here (ours, untested)."; to g2-rope-fixed "Rope is first expected in kindergarten in the tool; owned here because a self-turned rope is the indicator (ours, untested)."; to g2-overhand-throw "Overhand is first expected in grade 2 (from the tool)."
c. **Jog in grade 1.** The tool first expects jogging in grade 2 (rule 3), but g1-travel-ways lists jog in notes and words. Fix: in g1-travel-ways replace "jog" with "run" in the notes and in `words` (`skip; run; gallop; ...`); add "jog (a slow steady run)" to the g2-travel-jump-balance notes.
d. **S4.2.2** (activities that let you be with others; the older "social interaction", not expected before grade 3 per the paragraph) is owned in grade 1 (g1-together-favorites), while the paragraph says K to 2 rows carry these as `~CODE` at most. It must still be owned somewhere in the span, so the right treatment is the same as S2.2.2: keep it, and mark it naming-level. Fix: append to g1-together-favorites "Social interaction is first expected in grade 3 in the tool, so this stays at naming a favorite and whether it is alone or with others."

Why it matters: a writer building kindergarten days from k-bounce-throw-tries has been told not to check it, and a reviewer using the tool will find a K outcome with no assessment.

### 2. Water rows: the skill indicator is assessed only by knowledge where there is no pool, one safety line contradicts the skill task, and gaps are long (moderate; likely; LAYER progression; REPEAT new)

Checked: owned in grades 2, 5, 8 and 10 (S1.2.17 and S2.2.12; S1.5.22 and S2.5.18; S1.8.20 and S2.8.22; S1.12.9 and S2.12.17), one per span, which is the minimum the band rule needs. The skip notes name the gaps honestly.

- **Dry-land skill is missing.** S1 water indicators are skill indicators ("show ... skills, and simple swimming where a pool is available"). g2-water-skills does say a floor version; g5-water-skills says "a floor-based version"; g8-water and g10-water say nothing for a school with no pool and assess by knowledge task alone. Water-safety skills can be shown on dry land (reach rescue with a pole, throw a rope bag to a target, fasten a life jacket, a mat float posture). Fix: in g5, g8 and g10 water rows, end the assessment line with "and a dry-land skill task for every school: a reach rescue, a throw rescue to a target and fastening a life jacket; in-water tasks only where a pool exists."
- **Contradiction.** g2-water-skills and g8-water say "nobody is put in water" while assessing "float and kick" and "float, tread, a stroke" where a pool exists. Read by a busy writer this either bans the skill task or means no child is forced in. Fix, all four rows: "No child is made to enter water. Any in-water task belongs to the school's own aquatics program, with a qualified lifeguard on site and the school's swim policy."
- **Long gaps (judgment call).** Nothing touches water safety in grades 3, 4, 6, 7, 9 and 11 to 12, and kindergarten and grade 1 have no water row at all. Ownership cannot be repeated (an indicator has one owner and a `~` must sit inside the span), so I would not add rows. Fix: add "near water, stay with a grown-up and wear a life jacket on a boat" to the g3-stay-safe-own teacher note and "the buddy rule and what to do near water" to the g6-rules-safe note, so the idea comes back in the rows already named for stay-safe.

### 3. A gendered term in a student word list (minor; firm; LAYER progression; REPEAT new)

g7-invasion-defend lists "man-to-man" in `words` and in the notes. The lens and the practice points require gender-neutral language. Fix: in `words`, "man-to-man" to "person-to-person"; in the notes "man-to-man and zone" to "person-to-person and zone".

### 4. Cultural claims: four rows are flagged for a source, seven that make cultural claims are not (minor; firm; LAYER progression; REPEAT new)

Flagged correctly: g1-world-games, g4-world-activities, g8-culture-matters, g10-games-culture.
Unflagged though they name a culture or a custom: g1-dance-moves ("dance styles come from many cultures"), g3-dance-steps (folk dance), g4-dance-sequence (folk dance), g5-fair-decisions (a bow in a martial form, a handshake), g6-dance-sequences ("a cultural dance"), g9-dance-forms (a social dance, a canon), g12-community (how an activity is valued in other cultures).

Why it matters: the claim is what a unit page will repeat to a child. Fix: append to each of those seven rows "Each cultural claim is checked against a source before a unit names it." and add once, to g1-world-games and g6-dance-sequences: "A sacred or ceremonial dance is never used as a game or a warm-up; a unit uses an activity only when its source says it is open to be taught." (The second sentence is a Cory item, see For Cory.)

### 5. Fitness data and privacy: met everywhere it shows, with five small gaps (minor; likely; LAYER progression; REPEAT new)

Met: no weighing, no body measures, no scores for grades, no ranking, no public posting. Explicit in g1-heart-muscle, g3-health-fitness, g3-stay-safe-own (reminder count private), g4-skill-fitness, g4-pulse-body, g5-goal, g5-tech, g6-heart-rate, g7-effort-aerobic, g7-fitt-principles, g8-fitness-test-track, g8-tech-judge, g9-effort-heart-rate, g10-mixed-plan, g10-tech, g12-own-program, g12-active-adult. Equipment-free alternatives and "a child may choose a different test" are present. No row assesses a result; they assess a plan or a record. Good.

Gaps:
- g3-health-fitness lists "body composition" in the student `words` while the note says it is not taught as a body measure; nothing later teaches it. A word list is what children see. Fix: drop "body composition" from `words` and keep the note.
- g11-plan-for-self and g11-train-by-effort assess a "log summary" and "effort ratings" with no private line. Fix: append "Logs and ratings are the student's own and private; they are never graded on results."
- g5-fitt says "no fitness scores are used for grades" but not private; fix: "Fitness records are kept privately by the student."
- g8-fitness-test-track assesses "a baseline, a goal and a retest". Fine, but a writer could read it as handing the numbers in. Fix: "The student shows the teacher the plan change and the reason, not the numbers."
- g8-fitness-test-track names "a mile walk or run" first in a list; a timed mile is the test most often posted. Fix: "a mile walk or run at a self-set pace" and leave the time out of the record.

### 6. Handoffs that point at a topic neighbour, not the real prerequisite, and one gap with no reason (moderate; firm; LAYER progression; REPEAT yes, same kind as the social studies read finding 2 and the science read finding 6)

- **Solving conflicts.** g7-settle-disagreements (S3.8.8) assumes g6-rules-safe (rules). The real prerequisite is g5-conflict-solve (S3.5.5, "work through problems"), which today hands on to g6-welcome-differences (differences). Fix: g5-conflict-solve hands_on `g6-welcome-differences; g7-settle-disagreements`; g7-settle-disagreements assumes `g6-rules-safe; g5-conflict-solve`; add "The grade 5 conflict handoff skips grade 6 because conflict work returns in a game setting here." to g7-settle-disagreements.
- **Calm steps.** g7-manage-feelings (S4.8.8) assumes g6-express-variety (self-expression), not the calm-steps rows. g3-calm and g5-review-experiences carry calm-steps and hand on to nothing relevant. g12-manage-emotions assumes g11-fitting-challenge (challenge level), but the row that carries `~S4.12.8` is g10-choose-active-apply. Fix: g7-manage-feelings assumes `g6-express-variety; g5-review-experiences` (g5-review-experiences hands_on adds g7-manage-feelings, with a skip note); g12-manage-emotions assumes `g10-choose-active-apply; g11-fitting-challenge` (g10-choose-active-apply hands_on adds g12-manage-emotions, with a skip note: "The grade 10 handoff skips grade 11 because the strategies are practiced inside the chosen-activity rows").
- **Skill-related fitness.** g10-skill-fitness-training (S1.12.8) assumes g9-strength-form (strength, not skill-related fitness). Fix: assumes `g9-lifetime-sport-skills; g8-fitness-dance-apply` (g8-fitness-dance-apply carries `~S1.8.4`), with hands_on added on that g8 row and a skip note "the grade 8 handoff skips grade 9 because the sport rows use these drills".
- **Rest.** g10-rest (S2.12.12) assumes g9-exercise-principles; g7-rest, the row that teaches rest, hands on to nothing. Fix: g10-rest assumes `g9-exercise-principles; g7-rest`, with a skip note.
- **Ways to stay active.** g6-ways-active assumes g5-tech (technology) beside g5-goal. Technology is not what the row builds on; g4-reasons-strengths is. Fix: assumes `g5-goal; g4-reasons-strengths` with a skip note, drop g5-tech from that row's assumes and from g5-tech's hands_on.
- **Outdoor safety with no reason.** g8-outdoor-safety assumes g6-rules-safe (a two-grade gap) and carries no skip note, while the grade 7 outdoor row it practices beside, g7-fitness-dance-outdoor-use, is not named. Fix: assumes `g7-fitness-dance-outdoor-use; g6-rules-safe`; g7-fitness-dance-outdoor-use hands_on adds g8-outdoor-safety; note "The grade 6 safety handoff skips grade 7 because the first outdoor day is in grade 7."
- **Dead ends.** g6-catch-form hands on to nothing though g8-striking-fielding-play uses catching. Fix: g6-catch-form hands_on `g8-striking-fielding-play`; that row assumes it too, with a skip note. g7-skill-fitness-use also hands on to nothing; fix covered by the skill-related fitness item above (hands_on `g10-skill-fitness-training`).

The gate cannot see these because it checks that the named rows exist and are adjacent or noted, not that they are the right ones.

### 7. cross_subject: one thin lean, several missing, one imprecise (minor; firm; LAYER progression; REPEAT yes, same kind as the three 2026-11-13 reads)

Checked every cell against the other progressions. All named skills exist and sit at or before the PE grade: 5.G.A.2 (m5-graph-points, grade 5), 6.RP.A.3 (m6-equivalent-ratios), 6.SP.B.4 (m6-data-displays, grade 6), MS-PS2-2 (s8-forces-motion-mass, grade 8).

- **g1-heart-muscle leans on science 1-LS1-1** (s1-parts-mimic, about external parts that help animals live). It does not own "the heart is a muscle". The lean names nothing the row builds on. Fix: clear the cell, or write `science:1-LS1-1 (animals have body parts that do jobs; the heart is one)` only if the science grade 1 unit plan will say so.
- **g6-heart-rate leans on 6.RP.A.2**, but the step the row uses (a ten-second count times six) is an equivalent ratio, 6.RP.A.3 (m6-equivalent-ratios). Same grade: the row should say it can use "times six" before grade 6 ratios. Fix: `math:6.RP.A.3 (a ten-second count scaled to a minute; times six is multiplication from earlier grades)`.
- **g9-effort-heart-rate** uses the same 6.RP.A.2 wording; change to the same text.
- **Missing, where the body science is plainly used:** g4-pulse-body (science:4-LS1-1, s4-structures-function), g6-heart-rate (science:MS-LS1-1, s6-cells-body-systems), g7-eat-move-well and g7-rest (science:MS-LS1-3, s7-body-systems-food, and MS-LS1-7, s7-cell-respiration-growth). The standard's section 6 already says PE leans on the life science body-systems grades. Fix: add those cells.
- **g8-culture-matters** and **g10-games-culture** say social studies units name the row but the cell is empty. Fix: `social-studies:MA.4.T4 (ss4-regional-cultures)` and, for g10, `social-studies:MA.6.T2 (ss6-complex-societies)`.

### 8. Forward claims written as present facts, and one "not yet" to reword (minor; firm; LAYER process; REPEAT yes, same kind as the stale-note findings in the social studies and science reads)

Sixteen notes say another course "names this row": 7 dance rows (g1-dance-moves, g2-dance-sequence, g4-dance-sequence, g6-dance-sequences, g7-dance-ideas, g9-dance-design, g9-dance-forms), 7 health rows (g2-foods-energy, g3-active-outside, g5-food-drink, g7-eat-move-well, g10-fitness-life, g10-food, g12-active-adult), and g8-culture-matters and g10-games-culture for social studies. Today the dance and health courses have no unit plans or progression rows (data/plans/ has neither), so the sentence is a promise, not the repository's state. stale.py does not flag it because it has no work-status phrase. When the courses are written the sentence will either come true or go stale without a marker. Fix: reword every one to "The <dance|health|social studies> course units must name this row when they are written." followed by a `Pending(<node>)` marker with the plan-flow node of that course's units, so stale.py resolves it when the units exist.

**The six "not yet" notes** (k-locomotor-basics, k-balance, k-catch, k-foot-tap, g1-travel-ways, k-bounce-throw-tries). Judged: a stale-note scan would not misread them. Five are the teacher's three-way mark "met, partly or not yet", each followed by a period, and the APPROACH page uses the same mark ("the cue marked not yet"). The sixth is "not yet an owned pattern". stale.py's work-status pattern matches only "not yet" followed by in the, placed, written, built, added, loaded, in a Curio Class, named by, decided or chosen; none of the six does, and the run gave 0 failures. The risk is only a future widened scan. Item-level fix: in k-bounce-throw-tries reword "Early tries, not yet an owned pattern:" to "Early tries only, not an owned pattern:". Keep the mark in the other five.

### 9. Grades 11 and 12 at ten rows each: acceptable, with four conditions (moderate; judgment call; LAYER progression; REPEAT new)

Checked against rule 5 and the tool's two-level high school table: grade 11 has 5 owned indicators and 22 `~`; grade 12 has 4 owned and 24 `~`; all four standards have a stated outcome in both grades; every row has an assessment. That meets the bar (stated outcome, content, assessment) and the tool's level-two expectation. Nine of ten rows in each grade are mostly or wholly `~`; the S4 choice and plan rows are the owned ones (S4.12.1 to 5 in grade 11, S4.12.6 to 9 in grade 12). Four conditions:

- **Near-duplicate pairs.** g11-chosen-activity-skills and g12-lifelong-skills carry the same four codes; so do g11-training-form and g12-fitness-technique (S1.12.5 to 8), and g11-lead-feedback and g12-lead. The notes differ only slightly. Fix: state the new setting in each grade-12 row's notes in a way a unit can build from: g12-lifelong-skills "the student writes the cue sheet and coaches a partner"; g12-fitness-technique "a session the student designs and a partner coaches"; g12-lead "the student organizes an event, not a single session".
- **Indicators with no `~` in 11 or 12:** S1.12.9 and S2.12.17 (water, only 10), S2.12.4 dance forms, S2.12.13 force and motion, S2.12.14 games and culture. The tool expects every outcome at both levels. Fix: add `~SHAPE.S2.12.4` to g11-chosen-activity-skills (a chosen dance), `~SHAPE.S2.12.13` to g11-training-form (checking form with force and rotation), and `~SHAPE.S2.12.14` to g12-community. Leave water at grade 10 (see finding 2).
- **S3.12.1 and S3.12.7** appear as `~` only in grade 12 and S3.12.6 only in 11; fine, leave.
- **Who meets the owned rows.** Grades 9 and 10 own 34 indicators; S4.12.1 to 9 is first owned in 11 and 12. A student whose school requires PE only for grades 9 and 10 meets S4 only as `~` toward. That is a choice about the course shape, see For Cory.

### 10. Words: four to fix (minor; firm; LAYER progression; REPEAT yes, same kind as the science and ELA reads)

- g4-feet-hands-weight words: "handstand lean" contradicts its own teacher note ("no inverted balances"). Drop it; keep "bridge".
- g10-stretch-technique words: "PNF" is a partner stretch method with injury risk, and the row teaches static and dynamic only. Drop it.
- g3-health-fitness words: "body composition" (finding 5).
- g6-skill-fitness-technique notes: "a medicine-ball-free power jump" is clumsy and reads as a gear list. Reword: "a power jump with no equipment".

### 11. Pace through the grades (minor; judgment call; LAYER progression; REPEAT yes)

Rows: K 17, 16, 15, 18, 17, 14, 18, 20, 20, 14, 14, 10, 10. Indicators owned (not `~`): K 17, 1 17, 2 15, 3 23, 4 22, 5 12, 6 20, 7 22, 8 19, 9 17, 10 17, 11 5, 12 4. Grades 3 and 4 own nearly twice what grade 5 does (grade 5 is the application grade, 17 `~`). That is defensible, because grade 5 holds the games, but grade 3 carries 23 indicators in 18 rows, the heaviest owned load in K to 8. Not strand-stopping: dance runs K to 9, water 2, 5, 8, 10, outdoor 7, 8, 10, 11, rope K to 3 and 5. Gymnastics stops after grade 5 because the span 6 to 8 has no gymnastics indicator, which is correct. Fix (optional): move nothing now. When the grade 3 unit plans are cut, check the load; if grade 3 runs long, S1.5.8 (balance, in g3-jump-land-balance) can move to g4-in-place-sequence with grade 3 carrying it as `~`.

### 12. Models: tokens on rows that do not use them, and order inside a grade (minor; judgment call; LAYER progression; REPEAT yes, same as the science read finding 9)

The model chains run without a gap (cue-words, safe-space, effort-scale, goal-cycle from K; pulse-check and calm-steps from 1; tactics-question and team-talk from 2; fitness-parts 3; fitt-plan 5; skill-analysis 6) and no row uses a model before its introducer's grade. But some `model_in` and `model_out` entries are on rows whose notes never use them: g1-together-favorites and g1-do-well (calm-steps), g2-goals (calm-steps), g4-with-others (team-talk). And in grade 6 the motor rows carry `skill-analysis` while the row that introduces it, g6-analyze-skill, is a concepts row with no order given. Fix: remove the calm-steps token from g1-together-favorites, g1-do-well and g2-goals; add to the g6-analyze-skill notes "Taught in the first section of the grade; the motor rows then use the analysis words."

## Lens checklist, progression layer (docs/agents/lenses/physical-education.md)

| Line | Mark |
|---|---|
| Outcomes, not a year of games | Met: every row has a skill, a setting and an assessment. |
| A grade with no outcome for one of the four standards | Met in all 13 grades. |
| A span indicator placed in no year | Met: 210 of 210 owned once. |
| Skills in developmental order | Met, with the marked exceptions in finding 1 (three K items). |
| Dance or fitness taught once and never again | Met: dance K to 9 and `~` in 11 and 12; fitness every grade from 3. |
| Fitness is learned, not judged | Met; gaps in finding 5. |
| Safe place: no elimination, no human targets, no public picking, no exercise as punishment | Met in the rows that name them (g2-chase-flee, g4-attack-ideas, g5-invasion-skills, g6-health-fitness-technique, g7-rest). |
| Every body included (language, cultures) | One missed line: finding 3 (gender), and finding 4 (cultural sourcing). |
| Assessment shows growth, not rank | Met at this layer; growth from a baseline is named in g3-rope, g4-in-place-sequence, k-jump-land, g5-goal. The unit layer must carry it for the rest (APPROACH already says so). |
| No more than two or three cues | Met: every row lists three or fewer. |
| Indicator wording not copied | Met: our words only. |
| PE and health both teaching, or neither, the physical activity outcomes | Not applicable here; health has no progression yet (finding 8). |
| PE dance and the dance course teaching the same thing in the same year | Not applicable; no dance progression yet (finding 8). |

## What is right and should not be touched

- The ownership rule and its use. Every indicator is owned once inside its span, `~` before and after, and the owner column is easy to audit.
- S2.2.2, S2.2.7 at grade 2 as naming-level only, with the "no scoring, no elimination" lines.
- The band structure: S4 owned late in high school, S1 to S3 owned in grades 9 and 10.
- The water gaps are honest and the skip notes say why. The decision to keep a floor-based version is right.
- The privacy lines on fitness data are in nearly every place that needs them, including the technology rows ("no data leaves the student").
- "Met, partly or not yet" as the teacher mark.
- The balanced social strand: two rows in every grade, so S3 is never absent.

## What I could not judge

- Whether the PECAT K to 5 expectations I used (from STANDARD.md, read 2026-11-16 and 2026-11-19) match the tables' per-outcome detail; I took the paragraph as given and did not re-read the tool. Findings 1 and 9 rest on it.
- Whether health, arts and social studies units will name these rows; none exist yet.
- Whether a student's school will have a pool, and what the school's swim policy is.

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| S2.2.2 and S2.2.7 stay in grade 2 as naming-level only | Last grade of the span; the tool expects them in grade 3 | no change |
| S1.2.9 stays in grade 2, S1.2.16 in grade 2, S1.2.6 in grade 1, each marked "ours, untested" | The indicator is the pattern; K content already tries each | g1-bounce, g2-overhand-throw, g2-rope-fixed notes |
| S4.2.2 stays in grade 1, marked naming-level | Needs an owner in the span; adding it to grade 2 makes grade 2 heavier | g1-together-favorites notes |
| "Not yet" stays as the mark; one note is reworded | Matches APPROACH; stale.py does not match the phrase | k-bounce-throw-tries notes |
| "man-to-man" to "person-to-person" | Gender-neutral language | g7-invasion-defend |
| Jog out of grade 1 to run; jog belongs to grade 2 | Tool expects jogging in grade 2 | g1-travel-ways, g2-travel-jump-balance |
| Handoff repairs in finding 6 (assumes and hands_on edits, skip notes) | Real prerequisites, same grades | the rows named there |
| Words dropped: body composition, handstand lean, PNF | Contradict the row's own note or the privacy rule | g3-health-fitness, g4-feet-hands-weight, g10-stretch-technique |
| 6.RP.A.2 changed to 6.RP.A.3 for the ten-second-count conversion | That is the ratio the row uses | g6-heart-rate, g9-effort-heart-rate |
| Dry-land water skill added to g5, g8, g10 | Needed so the skill indicator can be assessed with no pool | g5-water-skills, g8-water, g10-water |
| Private line added to g11-plan-for-self, g11-train-by-effort, g5-fitt | Rule: records private everywhere | the rows named |
| Cultural-claim line added to the seven rows in finding 4 | Same rule the four flagged rows already follow | the rows named |

## For Cory

1. **Is the high school band a four-year sequence, or one or two required courses?** Rule 5 owns S1 to S3 in grades 9 and 10 and S4 in 11 and 12, which only works if a student takes the whole run. If one or two courses are required, S4 (choice, goals, after-school life) must move into grade 10 or be duplicated. This changes what a grade teaches.
2. **Water safety scope.** Curio Class gives the dry-land safety and skill tasks (reach, throw, life jacket); in-water tasks belong to a school's own aquatics program and lifeguard. Say it as a course-page line, or leave water as a knowledge unit only. This is a scope and a people question.
3. **Sacred and ceremonial activities.** The new line in finding 4 says a unit does not use one as a game unless its source says it is open to teach. If that is too strict, or not strict enough, it is your call (audience and outside people).
4. **Kindergarten rope and hand dribbling.** The tool expects both in kindergarten; this draft owns them in grades 2 and 1. I would keep it (marked "ours, untested"); if you want a kindergarten that matches the tool outright, K gains two owned rows and grades 1 and 2 shrink.

## Sources

- data/standards/shape-pe-2024.txt, docs/courses/physical-education/STANDARD.md (the tool's placement as read there), docs/ADOPTION-BAR-SUBJECTS.md (PE part), the PE lens and approach head: the bar and the placement facts.
- data/progressions/math.csv, science.csv and social-studies.csv: to confirm each lean's target skill and grade.
- scripts/stale.py: the exact pattern the stale scan uses.
- The review tool's grade tables (CDC, 2019) were not re-read. My belief that the tool's kindergarten rope outcome is about a still or swung rope rather than a self-turned one is from memory, unchecked.

## For the source list

Nothing new found.

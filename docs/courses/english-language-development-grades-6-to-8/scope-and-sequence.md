# Scope and sequence: English Language Development, grades 6 to 8

> **Held on C11 (Cory 2026-11-26, Desk q-eld-scope-1).** A draft, written before the ELD C11 gate passed (docs/courses/eld/STANDARD.md section 6). It has had no expert read or fix pass; the read, fix, unit plans and days wait until C11 passes, and the read then runs on this draft.

Draft, written 2026-11-26 from the frame (docs/courses/english-language-development-grades-6-to-8/frame.md), its two
reads and their fixes, and the after-core Desk calls. The day-by-day plan is
data/plans/english-language-development-grades-6-to-8/days.csv (480 rows). Curio Class plans this course in its own
words; the framework's ids are named, its wording is not used, and no alignment is claimed.

## The band

- **Three years, one file.** Grade 6 is band days 1 to 160, grade 7 days 161 to 320, grade 8 days 321 to 480. Each
  year is 154 unit days and 6 check days (two course-level checks of 2 days, each with a respond day), one 45-minute
  period a day, five a week, 32 weeks (120 hours a year, STANDARD section 2).
- **Whose standards fall in which year.** Grade 8 owns the 18 content ids, written plain in `codes` (units 18 to 26).
  Grades 6 and 7 carry the same ids (written with `~`): they teach them at grade 6 and 7 language demands, and the
  owning year is grade 8. The social and instructional ids (SI, `~WIDA.ELD-SI.4-12.<use>`) are owned in grade 4 and
  carried in every year here. On each day the Interpretive id is listed when students read or listen, the Expressive
  id when they speak or write.
- **school_day.** school_day is the band day (as the other band scopes count it). The week within its year is
  ((school_day - 1) mod 160) // 5 + 1. Every unit and course-level check falls in the weeks the frame gives (table
  below).
- **The core days this course supports are named, not taught again.** Each unit's first-day note names the host unit
  and its days; ELD takes the host's text, model or data apart for language, and the host teaches the content.
- **Entry points.** Every day runs at levels 1 and 2, 3 and 4, and 5 and 6 on the same task and the same thinking.
  Help comes off on set days, named in the notes: 5 and 6 drop the frame the day after the unit's first application
  day; 3 and 4 work without the frame on the last teaching day, as they will on the end-of-unit tasks; 1 and 2 keep
  the word bank, and the cloze comes off on that same day.
- **Talk routines.** Grade 6 learns the role circle (days 1 to 4), grade 7 build or question (unit 9, days 161 to
  163), grade 8 the student-led round (unit 18, days 321 to 323). Each is kept all year; a class new to the band
  learns the earlier routine in the same week.
- **Language Dive.** Each unit takes one host sentence or paragraph apart in a Language Dive; the note on that day
  credits it: Language Dive routine adapted from EL Education K-5 Language Arts (2017 edition, CC BY 4.0).
- **New texts on checks.** Every end-of-unit and course-level check uses a new Curio Class text, invented for
  practice and checked unused in docs/ and data/ (section plans and items.csv too) before it is written in.
- **Paper path.** Every day runs on paper: the model page, the card set, the self-check page and the look-for sheet.
  No device is needed.
- **No base text.** ELD has no base text of its own; the host's texts are the reading.

## Readiness and retrieval

No readiness check is placed: every row a unit assumes was used the year before or earlier in the same year, so each
unit opens with a retrieval task in the first ten minutes of its day 2 (listed in `retrieves`), and day 1 stays clean
for the hook. A student who joins without the earlier year meets the retrieval at entry points 1 and 2 with the
earlier year's model on the card; a newcomer takes the newcomer strand beside it. SI review rows come back on a named
day in a later unit (in `skills` that day and in `retrieves` on the first day each returns).

| Unit | Day 2 retrieves | Later in the unit |
|---|---|---|
| 1 | g5-la-narrate; g5-si-narrate; g5-si-inform | |
| 2 | g5-la-argue; g5-si-argue; e6-collab-discussion | |
| 3 | g5-ss-explain; g5-si-explain | |
| 4 | g5-sc-explain; g6-ss-explain | g6-si-narrate (day 69) |
| 5 | g5-la-inform; g6-si-inform; e6-pronouns | g6-si-inform review (day 86) |
| 6 | g5-ss-argue; g6-la-argue; ss6-changing-interpretations | g6-si-argue (day 108) |
| 7 | g5-sc-argue; g6-la-argue | g6-si-inform (day 121), s6-particle-temperature (day 124) |
| 8 | g5-ma-explain; g5-ma-argue; m6-ratio-parts-problems | g6-si-explain (day 145) |
| 9 | g6-la-narrate; g6-si-narrate | |
| 10 | g6-la-inform; g6-si-inform | |
| 11 | g6-ma-explain; m7-proportional-equations | g7-si-narrate (day 216) |
| 12 | g6-sc-explain; g6-si-explain; s7-cell-respiration-growth | |
| 13 | g6-la-argue; g6-si-argue | |
| 14 | g6-ss-argue; ss7-comparing-societies | g7-si-argue (day 269) |
| 15 | g6-sc-argue | g7-si-inform (day 283), s7-body-systems-food (day 285) |
| 16 | g6-ma-argue | g7-si-explain, g7-ma-explain, m7-two-step-equations (day 294) |
| 17 | g6-ss-explain; ss7-silk-road-trade | g7-si-narrate (day 311) |
| 18 | g7-la-inform; g7-si-inform | |
| 19 | g7-ma-argue; m8-congruence | m8-angle-facts (day 344), g8-si-inform (day 346) |
| 20 | g7-la-argue; g7-si-argue | |
| 21 | g7-sc-argue; g7-si-explain | |
| 22 | g7-ma-explain | g8-si-argue (day 409) |
| 23 | g7-la-narrate; g7-si-narrate; e8-dialogue-incidents | |
| 24 | g7-ss-explain; ss8-three-branches | g8-si-explain (day 442) |
| 25 | g7-ss-argue; g8-la-argue; ss8-ratification-debate | g8-si-narrate (day 458) |
| 26 | g7-sc-explain; s8-forces-motion-mass | g8-si-inform (day 471) |

## How every unit runs

Hook (Understanding), the day-2 retrieval and the unit's first form, a Language Dive on the host, word work
(Fluency), the form built with the teacher (Application), an own piece, a change of audience (the same content for a
second reader, saying what changed), the self-check page, pairs work on new text, then the end-of-unit assessment
over two Check days and one Respond day inside the unit. End day 1: the interpretive part on a new text for the whole
class, and the talk task for half the class (about two minutes a student, 15 a day, about 30 minutes for a class of
30). End day 2: the writing task and the talk task for the other half. The respond day reteaches in up to four groups
by form and entry point. Fluency is about a fifth of teaching days; no Fluency day drafts, edits or introduces.
Candidate cells (bar items, California 1.26, PRIME as a planning reference only) are all kept inside existing days at
no day cost; each unit names its day.

## Grade 6 (band days 1 to 160)

### Unit 1. A new school and a flood year
Days 1 to 30, weeks 1 to 6. Host: ELA grade 6 unit 1 (days 1 to 32). Skills: g6-la-narrate, g6-si-narrate,
g6-si-inform. The role circle (days 1 to 4), point of view and the past perfect in the novella (days 5 to 8), a
first-week recount by class period (day 9), a scene with steady point of view (days 10 to 13); mid-unit assessment
day 15 (a spoken recount, about a minute each); change of audience to next year's new students (days 16 to 17);
revision and self-check (days 18 to 27). End-of-unit days 28 and 29, respond 30. Bridge: e6-present-claims comes
later, so the unit teaches its own order-and-audience moves (day 2). Sensitivity: flood and moving; the family note
goes home day 1 with the other text named. Candidate: the self-check page's first use, day 21.

### Unit 2. The first written laws
Days 31 to 47, weeks 7 to 10. Host: ELA grade 6 unit 2 (days 33 to 58); days 31 and 32 retrieve e6-collab-discussion
on the ELA novella, and the law-code texts are taken apart from day 33. Skills: g6-la-argue, g6-si-argue. Claim,
evidence and "according to"; the claim chart's counterclaim stage; a role-circle decision on a class matter. End
days 45 and 46, respond 47. Sensitivity: punishments and slavery are not ranked; enslaved people are framed as
people. Candidate: self-check page, day 42 (bar item 12).

### Unit 3. Why the first cities grew
Days 48 to 63, weeks 10 to 13. Host: social studies grade 6 unit 4 (to day 54), then unit 5, Egypt and Kush, from day
56. Skills: g6-ss-explain, g6-si-explain. The cause chain with one unseen step, surplus and the Nile flood, a
deadline plan explained to a partner and to a family. End days 61 and 62, respond 63. Bridge: if the Egypt unit
starts later, the Nile chain moves to the respond day (day 56 note). Candidate: the change of audience to a family,
day 54 (bar item 10).

### Unit 4. Water, weather and the unseen step
Days 64 to 80, weeks 13 to 16. Host: science grade 6 unit 3 (days 52 to 89). Skills: g6-sc-explain (with the SI
narrate review, day 69). The water cycle's mechanism with its unseen step, air masses, the week's weather recounted.
End days 78 and 79, respond 80; the record goes to the mid-year check unscored. Candidate: PRIME Depth.LE, the unseen
step named, day 70.

### Grade 6 mid-year check
Days 81 and 82, respond 83, week 17. Samples units 1 to 3 on new content: LA Narrate, LA Argue and SS Explain
(interpretive), a talk task (SI Narrate or SI Argue) and a written argument paragraph (LA Argue expressive). Unit 4's
record is carried unscored; the talk and writing avoid unit 4's explanation so no task form repeats within two
weeks.

### Unit 5. How a text is built
Days 84 to 100, weeks 17 to 20. Host: ELA grade 6 unit 3 to day 86 (the forecasters text), then ELA grade 6 unit 4
(the scripts text) from day 87. Skills: g6-la-inform, g6-si-inform. Sections and a central idea, the classifying
sentence, clear pronouns, an informative section for a class display. End days 98 and 99, respond 100. Candidate:
PRIME Match.LE, the classifying sentence on new text, day 97.

### Unit 6. Why historians disagree
Days 101 to 115, weeks 21 to 23. Host: social studies grade 6 unit 8 (days 100 to 113). Skills: g6-ss-argue (SI
argue review, day 108). Two interpretations weighed, a research claim citing two sources. End days 113 and 114,
respond 115.

### Unit 7. Moving plates and hazards
Days 116 to 131, weeks 24 to 27. Host: science grade 6 unit 4 (just before) and unit 5 (alongside as context); unit 2
retrieved for the shorter claim (day 124). Skills: g6-sc-argue (SI inform review, day 121). A counterclaim answered
from fossil and rock data. End days 129 and 130, respond 131. Sensitivity: hazards from the host's data only; the age
of Earth as the evidence shows, beliefs respected. Candidate: PRIME Match.LE, day 128.

### Unit 8. Ratios, equations and claims
Days 132 to 157, weeks 27 to 32. Host: math grade 6 unit 6 (just before), unit 7 to day 141, unit 8 from day 142.
Days 132 to 141 work the explain row and equivalence claims; statistical questions from day 142. Skills:
g6-ma-explain, g6-ma-argue (SI explain review, day 145). Mid-unit assessment day 146 (a ratio method explained, a
minute each). Critique of a worked solution. End days 155 and 156, respond 157; the record goes on unscored.
Candidate: one worked page at all three entry points, day 149 (bar item 3).

### Grade 6 year-end check
Days 158 and 159, respond 160, week 32 (finals week). Samples units 4 to 7: SC Explain, LA Inform, SS Argue and SC
Argue (interpretive), an informative summary as the talk task (SI Inform, LA Inform expressive) and a written
weather mechanism explanation (SC Explain expressive). Unit 8's record is carried unscored.

## Grade 7 (band days 161 to 320)

### Unit 9. The salmon year
Days 161 to 185, weeks 1 to 5. Host: ELA grade 7 unit 1 (days 1 to 30); science grade 7's first labs for the
recount. Skills: g7-la-narrate, g7-si-narrate. Build or question (days 161 to 163), setting that changes a character,
speech verbs, a lab recount with each member's part kept straight. End days 183 and 184, respond 185. Bridge:
e7-present-salient comes later; the unit teaches its own order-and-audience moves (day 168). Sensitivity: Karuk and
Yurok families in their own names, the river's place as present. Candidate: California 1.26, all four domains, day
182.

### Unit 10. Alike and different
Days 186 to 208, weeks 6 to 10. Host: science labs for days 186 to 190 (the SI plan report), then the Dust Bowl text
(ELA grade 7 unit 2) from day 191. Skills: g7-la-inform, g7-si-inform. Comparing and classifying paragraphs, "unlike"
and "which means". End days 206 and 207, respond 208. Unused lean: e7-text-organization comes later (day 194).
Sensitivity: families forced to move for work stay in the text. Candidate: PRIME Depth.KLU, day 195.

### Unit 11. What each part means
Days 209 to 226, weeks 10 to 14. Host: math grade 7 unit 4 (days 47 to 68), unit 2 retrieved. Skills: g7-ma-explain
(SI narrate review, day 216). "Represents" for each part of a proportional or percent equation, if-then steps. End
days 224 and 225, respond 226. Bridge: two-step equations come later and return in unit 16. Candidate: one worked
page at three entry points, day 213 (bar item 3).

### Unit 12. Where food comes from
Days 227 to 244, weeks 14 to 17. Host: days 227 and 228 work from science grade 7 unit 3's respiration model; the
photosynthesis unit (science grade 7 unit 4) alongside from day 229. Skills: g7-sc-explain, g7-si-explain. A process
with its unseen step, a lab procedure with a reason for each step. End days 242 and 243, respond 244; the record goes
to the mid-year check unscored. Candidate: PRIME Depth.LE, day 233.

### Grade 7 mid-year check
Days 245 and 246, respond 247, weeks 17 and 18. Samples units 9 to 11: LA Narrate, LA Inform and MA Explain
(interpretive), a recount as the talk task (SI Narrate) and a written comparing paragraph (LA Inform expressive).
Unit 12's record is carried unscored.

### Unit 13. Athens: who could speak?
Days 248 to 263, weeks 18 to 21. Host: ELA grade 7 unit 4 (days 87 to 108). Skills: g7-la-argue, g7-si-argue. Is the
evidence enough, a counterclaim answered, a structured debate on a class issue. End days 261 and 262, respond 263.
Unused lean: e7-evaluate-argument comes later (day 251). Candidate: PRIME Match.LE, day 260.

### Unit 14. Greek claims
Days 264 to 278, weeks 21 to 24. Host: social studies grade 7 unit 9 (days 101 to 115). Skills: g7-ss-argue (SI argue
review, day 269). Comparison claims with "whereas", a research claim answering another reading. End days 276 and
277, respond 278.

### Unit 15. When an ecosystem changes
Days 279 to 291, weeks 24 to 27. Host: science grade 7 unit 5 (to day 128), unit 3 retrieved for the shorter claim
(day 285). Skills: g7-sc-argue (SI inform review, day 283). Evidence linked to a claim with reasoning. End days 289
and 290, respond 291. Tight unit: review forms go to the respond day.

### Unit 16. Is it always true?
Days 292 to 304, weeks 27 to 29. Host: math grade 7 unit 7, triangles, to day 138 (band 298); chance experiments
from day 139 (band 299). Skills: g7-ma-argue, g7-si-explain. Triangle conditions, the required two-step-equation
return with an exit ticket (day 294), chance claims with an exit ticket (day 300). End days 302 and 303, respond 304.
Unused lean: m7-compare-populations (sampling) comes after the unit. Candidate: the condition at three entry points,
day 296 (bar item 3).

### Unit 17. Why Rome fell
Days 305 to 317, weeks 29 to 32. Host: social studies grade 7 unit 12 (days 145 to 156), Silk Roads retrieved.
Skills: g7-ss-explain (SI narrate review, day 311). Two causes weighed with "not only ... but also". End days 315 and
316, respond 317; the record goes on unscored. Sensitivity: invasion and the end of a state; family note, and the Silk
Road host may carry the unit.

### Grade 7 year-end check
Days 318 and 319, respond 320, week 32 (finals week). Samples units 12 to 16: SC Explain (label the unseen step),
LA and SS Argue (is the evidence enough), SC and MA Argue (which claim the data supports), a build-or-question turn
as the talk task (SI Argue, LA Argue expressive) and a written argument from data (SC Argue expressive). Unit 17's
record is carried unscored.

## Grade 8 (band days 321 to 480)

### Unit 18. The missing letter
Days 321 to 340, weeks 1 to 4. Host: ELA grade 8 unit 1 (days 1 to 30). Skills: g8-la-inform, g8-si-inform. Owns LA
Inform. The student-led round (days 321 to 323), transitions, formal style and verbals, a briefing on a task, a formal
informative section. End days 338 and 339, respond 340. Unused lean: e8-paragraph-structure (day 328). Sensitivity:
wartime loss and a parent living apart, with the family note and the other text. Candidate: PRIME Match.LE and
California 1.26, day 337.

### Unit 19. Prove it
Days 341 to 356, weeks 5 to 8. Host: math grade 8 unit 1 (just before) and unit 2 (alongside). Skills: g8-ma-argue
(SI inform review, day 346). Owns MA Argue. A congruence argument from definitions, the triangle angle sum, a critique
naming a gap. End days 354 and 355, respond 356. Candidate: judging another's and one's own argument, day 352 (bar
item 12).

### Unit 20. Founding words, answered
Days 357 to 378, weeks 8 to 12. Host: ELA grade 8 unit 2 (days 31 to 62). Skills: g8-la-argue, g8-si-argue. Owns LA
Argue. Counterclaims from credible sources, reporting verbs, leading a group decision. End days 376 and 377, respond
378. Sensitivity: slavery, Banneker, yellow fever. Candidate: PRIME Match.LE, day 375.

### Unit 21. What the data shows
Days 379 to 401, weeks 12 to 17. Host: science grade 8 unit 3 to day 74 (band 394); from day 395 the unit works from
its completed records. Skills: g8-sc-argue, g8-si-explain. Owns SC Argue. Arguments from energy and collision data,
explaining how a group disagreement was solved. End days 399 and 400, respond 401. Unused lean: s8-gravity-mass comes
after the unit. Candidate: bar item 12 and PRIME Depth.LE, day 393.

### Unit 22. What the graph shows
Days 402 to 417, weeks 17 to 20. Host: math grade 8 unit 5 to day 92 (band 412), function table and graph days 93 and
94 (band 413 to 414). Skills: g8-ma-explain (SI argue review, day 409). Owns MA Explain. Each step with its reason,
what the slope represents. End days 415 and 416, respond 417; the record goes to the mid-year check unscored. Unused
lean: m8-function-model. Candidate: one worked page at three entry points, day 406 (bar item 3).

### Grade 8 mid-year check
Days 418 and 419, respond 420, week 20. Samples units 18 to 21: LA Inform (both modes, the spoken briefing standing
for the expressive part), MA Argue and LA Argue (interpretive), and SC Argue in both modes (a new cart-and-spring
table and a written argument from it). Unit 22's record is carried unscored.

### Unit 23. Myths made new
Days 421 to 437, weeks 21 to 24. Host: ELA grade 8 unit 4 (days 93 to 124). Skills: g8-la-narrate, g8-si-narrate.
Owns LA Narrate. Dialogue and incidents that reveal a character, flashback and tension, a newsletter recount. End
days 435 and 436, respond 437. Sensitivity: Persephone and a shared child. Candidate: PRIME Match.LE, day 434.

### Unit 24. Who decides?
Days 438 to 451, weeks 24 to 27. Host: social studies grade 8 unit 7 to day 119 (band 439), unit 8 from day 120 (band
440). Skills: g8-ss-explain (SI explain review, day 442). Owns SS Explain. How power divides and why a check works.
End days 449 and 450, respond 451. Sensitivity: civics, never status.

### Unit 25. The press and the other side
Days 452 to 464, weeks 27 to 29. Host: social studies grade 8 unit 9 (days 131 to 144). Skills: g8-ss-argue (SI
narrate review, day 458). Owns SS Argue. The ratification debate in two parts (days 453 and 454), editorials and
their other side. End days 462 and 463, respond 464. Sensitivity: local matters only, never status.

### Unit 26. How it works: natural selection
Days 465 to 477, weeks 29 to 32. Host: science grade 8 unit 6 (days 132 to 158). Skills: g8-sc-explain (SI inform
review, day 471). Owns SC Explain. A mechanism tied to evidence. End days 475 and 476, respond 477; the record goes
on unscored to grade 9. Sensitivity: beliefs respected; no student states a belief.

### Grade 8 year-end check
Days 478 and 479, respond 480, week 32 (finals week). Samples units 22 to 25: MA Explain (both modes), LA Narrate, SS
Explain (name the unseen step) and SS Argue (both modes, the talk task arguing the editorial's other side, SI Argue).
Unit 26's record is carried unscored.

## Course-level checks and what they sample

| Check | Band days | Week | Sampled | Not re-collected |
|---|---|---|---|---|
| Grade 6 mid-year | 81, 82; respond 83 | 17 | LA Narrate I, LA Argue I and E, SS Explain I; SI Narrate, SI Argue | Unit 4 |
| Grade 6 year-end | 158, 159; respond 160 | 32 | SC Explain I and E, LA Inform I and E, SS Argue I, SC Argue I; SI Inform | Unit 8 |
| Grade 7 mid-year | 245, 246; respond 247 | 17, 18 | LA Narrate I, LA Inform I and E, MA Explain I; SI Narrate | Unit 12 |
| Grade 7 year-end | 318, 319; respond 320 | 32 | SC Explain I, LA Argue I and E, SS Argue I, SC Argue I and E, MA Argue I; SI Argue | Unit 17 |
| Grade 8 mid-year | 418, 419; respond 420 | 20 | LA Inform I and E, MA Argue I, LA Argue I, SC Argue I and E; SI Inform | Unit 22 |
| Grade 8 year-end | 478, 479; respond 480 | 32 | MA Explain I and E, LA Narrate I, SS Explain I, SS Argue I and E; SI Argue | Unit 26 |

Rules each check keeps: a check right after a unit's end carries that unit's record unscored and samples earlier
units (collect once); no task form repeats within two weeks of the unit before it; the talk task is about two minutes
a student, 15 a day over the two days for a class of 30. **Owned ids no grade 8 check samples:** SC Explain (unit 26
sits right before the year-end check, so its record is carried, not re-collected), and the expressive modes of MA
Argue, LA Argue and LA Narrate, and SS Explain expressive. Each is assessed in both modes in its own unit's
end-of-unit assessment (units 19, 20, 23, 24 and 26), and the record goes on to grade 9's teacher.

## Newcomer strand

An added period with the ELD teacher (Cory, 2026-11-26), 20 days beside each year, outside the 160 days: survival
and school language (names, routines, asking for help), the current host unit's pictures and labeled models, and a
short catch-up card set for the unit language missed. A newcomer who needs early reading in English works the ELA K
to 2 foundational rows beside it, with age-fit texts. The strand and every family note get the sensitivity read
before use. Its days are planned with the unit plans, not in this file.

## Shorter path

- **A year about 10 days short.** Fold ten Fluency days a year into the next day's first five minutes (45 minutes
  saved each, 450 minutes a year; 150 days a year, 450 against 480). Nothing assessed and no owned part is cut: each
  is practice of a form already taught.
  - Grade 6: days 12, 19, 23, 26, 39, 71, 92, 139, 144, 153.
  - Grade 7: days 166, 175, 180, 193, 201, 204, 214, 235, 256, 271.
  - Grade 8: days 332, 335, 347, 367, 372, 386, 396, 407, 429, 446.
- **A shorter period.** Where the ELD period is under 45 minutes, the end-of-unit talk task runs over three days (10
  students a day) and the respond day's groups drop to three; no unit day is cut.
- **A leave-out unit.** The frame names none: every grade 8 unit owns an id and every grade 6 and 7 unit carries an
  assessed row. If a school must leave one out, the leave-out bridge rule applies: the next unit that uses the left
  out unit's card (the cause chain from unit 3, the claim chart from unit 2, the story map from unit 1) teaches its
  one-step form in its first ten minutes, and the left-out unit's row is assessed on that unit's end-of-unit task.
- **Mixed-grade groups.** A school with one ELD group across 6 to 8 runs the year matching the most students' grade;
  the other grades' units are met through the retrieval tasks the following year.

## Sources not loaded

The framework's printed grades 6 to 8 expectation lists are not stored locally and were not opened (frame For the
lead item 2). Every unit's parts are drawn from the stored id words (data/standards/wida-2020-words.txt) and the
frame. Host texts and models are named by host unit; their section plans are read at the unit-plan stage.

## For the lead

1. **C11 gate.** This scope is written under the after-core call; STANDARD section 6 holds the unit plans and days
   until C11 passes in two core subjects' probe and guard units, one of them ELA. The scope does not change that.
2. **Codex finding 1 (owned-id coverage), not applied.** Until the printed lists are checked, these are the target
   days where each addition fits without a new day: unit 18, impartial stance and defining the topic, days 331 and
   333; unit 19, compare strategies and generalize, days 349 and 351; unit 20, summary separated from opinion and a
   conclusion, days 369 and 374; unit 21, two same-topic arguments compared, day 397; unit 22, compare
   representations, days 405 and 413; unit 23, theme and word choice, days 425 and 432; unit 24, experts compared and
   interacting causes, days 443 and 446; unit 25, source purpose and credibility, days 456 and 459; unit 26, an
   investigable question and variable relationships from supplied records, days 467 and 470.
3. **Two check items differ from the frame's table.** The grade 7 year-end process item labels the unseen step
   instead of ordering the chain, and the grade 8 year-end council item names the unseen step instead of ordering the
   check, because units 17 and 26 used ordering on their end-of-unit tasks within the last two weeks. The frame's
   table could be updated to match.
4. **After-core calendar pass.** The check days are as the frame gives them (For the lead item 4); the grade 6 PE
   overlap the second read found (day 82) no longer shows in calendar.csv. See the calendar result in the report.
5. **Frame note.** The frame's Units table writes "None" in the owned-standards column for units 1 to 17, which
   sequence.py reads as a standard named None (17 notes). A blank or a dash would read cleanly.

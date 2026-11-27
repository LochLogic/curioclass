# Scope and sequence: English Language Development, grades 3 to 5

> **Held on C11 (Cory 2026-11-26, Desk q-eld-scope-1).** A draft, written before the ELD C11 gate passed (docs/courses/eld/STANDARD.md section 6). It has had no expert read or fix pass; the read, fix, unit plans and days wait until C11 passes, and the read then runs on this draft.

Course `english-language-development-grades-3-to-5` (catalog id `eld-3-5`), grades 3 to 5, a band course of three grade years; draft, written 2026-11-26 from the frame (docs/courses/english-language-development-grades-3-to-5/frame.md). The days live in data/plans/english-language-development-grades-3-to-5/days.csv; this page holds the judgment.

## The band on one page

- **Which grade's standards fall in which year.** Year 3 (band days 1 to 160, units 1 to 8) is the owner year for 20 ids: the four SI K-3 ids and the 16 cluster 2-3 content ids (LA Narrate and Inform; MA, SC and SS Explain and Argue; each in both modes). Year 4 (band days 161 to 320, units 9 to 17) owns the four SI 4-12 ids and carries the cluster 4-5 content ids, which grade 5 owns: a grade 4 day lists the carried id it works on, as practice toward grade 5, never as the owner's claim. Year 5 (band days 321 to 480, units 18 to 25) owns the 18 cluster 4-5 ids (LA Narrate, Inform and Argue; MA, SC and SS Explain and Argue) and carries the SI 4-12 ids owned in grade 4. That is the frame's 42 owned ids, each on at least one teaching day and one end-of-unit assessment in its owner year. Public pages say "English language development standards" with the id; no framework wording appears in any goal or note.
- **Meetings and school days.** One 30-minute lesson every school day, five a week, 32 weeks, 160 days a year: the protected daily ELD period, not ELA time. `school_day` counts school days through the whole band, 1 to 480, and equals the course day: year 4's own school day is `school_day` minus 160 and year 5's is `school_day` minus 320. The week within a year is (year school day - 1) // 5 + 1. Every unit and every course-level check was checked to fall in the frame's weeks and CALENDAR.md's: grade 3 checks in weeks 19 and 27, grade 4 in weeks 15 and 29, grade 5 in weeks 18 and 28. ELD is a special in K to 5 and does not count in the stagger (CALENDAR.md rule 1); `frame.py calendar` reports no stagger break.
- **Every day's 30 minutes.** Set-up and cards out (about 2 minutes), the day's talk in the year's routine before any writing, the form taught or used on the host content, and a one- or two-sentence exit ticket of the day's form on the day's content, seen against two or three look-fors on the teacher's paper sheet ("seen" or "not yet"). A retrieval task takes 10 minutes after the opener. No lab or field clean-up: ELD runs no investigation.
- **The routine.** Grade 3 "tell, ask, retell" (taught days 1 to 3), grade 4 "plan, check, report" (band days 161 to 163, groups of four with named roles), grade 5 "report, sum up, answer" (band days 321 to 323). The same routine runs every week of its year.
- **Entry and exit points.** Three entry points by proficiency: levels 1 and 2, 3 and 4, 5 and 6. Every entry point does the same task on the same content at the same thinking demand; the help changes, never the task. Help comes off on named days in every unit: for 5 and 6 the frame comes off after the first alone application day (the "Make it alone" day); for 3 and 4 on the self-check day, before the end-of-unit telling and writing tasks; 1 and 2 keep the word bank and lose the cloze before the end-of-unit assessment. Each year's first day also removes the earlier band's or year's cards or clozes for 3 and 4. A student moves to the next entry point when the sheet shows the unit's look-fors "seen" in the end-of-unit assessment and in one course-level check, or on the school's own progress check. Placement and exit from the program use the school's proficiency score; Curio Class gives no placement test and keeps no scores.
- **Mixed-grade groups.** A mixed-grade group uses the year of its youngest grade, and the teacher page says so.
- **No readiness checks.** Every grade 3 row assumes its grade 2 row (ELD K to 2), and every grade 4 and 5 row the row of the year before; each was last used one grade back, so each opens as a retrieval task inside the unit's day 2 (after day 1's hook), counted by grade number as sequence-write rule 2 says. SI rows met again as review use retrieval through use on the unit's talk-move day. The table under each year lists every earlier-grade row with its last-use grade and its day.

## Grade 3 (band days 1 to 160, units 1 to 8)

#### Year map, grade 3

| Unit | Days (band) | Weeks | Key language use | Ids (owned or carried) | Sentence forms | Grows from |
|---|---|---|---|---|---|---|
| 1 Getting to books | 1 to 21 | 1 to 5 | inform | LA.2-3.Inform.Interpretive (owned), LA.2-3.Inform.Expressive (owned), SI.K-3.Inform (owned) | a topic sentence and a detail joined with "for example" and "also" | grade 2's paragraph with a topic sentence (ELD K to 2 unit 14) |
| 2 Who decides in our town | 22 to 38 | 5 to 8 | explain | SS.2-3.Explain.Interpretive (owned), SS.2-3.Explain.Expressive (owned), SI.K-3.Narrate (owned) | "The town council decides ___, so ___", cause with "so" and "because", and the present tense for what a level does | grade 2's resource-to-use chain (ELD K to 2 unit 16) and the unit 1 land-change record |
| 3 The class deliberation | 39 to 57 | 8 to 12 | argue | SS.2-3.Argue.Interpretive (owned), SS.2-3.Argue.Expressive (owned), SI.K-3.Argue (owned) | "I think ___ because ___" with "the source says ___" | grade 2's claim from sources (ELD K to 2 unit 19) and social studies unit 1's claim with evidence |
| 4 Life cycles and forces | 58 to 76 | 12 to 16 | explain | SC.2-3.Explain.Interpretive (owned), SC.2-3.Explain.Expressive (owned), SI.K-3.Explain (owned) | sequence words with "so" ("First it is a ___. Next it ___, so ___") | grade 2's material-and-use explanation (ELD K to 2 unit 17) and science unit 1's force test |
| 5 Arrays and equal groups | 77 to 92 | 16 to 19 | explain | MA.2-3.Explain.Interpretive (owned), MA.2-3.Explain.Expressive (owned), SI.K-3.Inform (owned) | "There are ___ rows of ___, so ___" and "This works because ___" | grade 2's explanation of a sum (ELD K to 2 unit 15) and math unit 4's area model |
| 6 Surviving where you live | 96 to 113 | 20 to 23 | argue | SC.2-3.Argue.Interpretive (owned), SC.2-3.Argue.Expressive (owned), SI.K-3.Explain (owned) | "Our claim is ___. The data shows ___. Another clue is ___." | grade 2's claim from a material test (ELD K to 2 unit 17) and unit 4's life cycles |
| 7 Fractions on the line | 114 to 132 | 23 to 27 | argue | MA.2-3.Argue.Interpretive (owned), MA.2-3.Argue.Expressive (owned), SI.K-3.Argue (owned) | comparatives with "than" and "I claim ___ because the model shows ___" | grade 2's number claims with a drawing (ELD K to 2 unit 18) and math unit 6's number line |
| 8 A story with a voice | 136 to 160 | 28 to 32 | narrate | LA.2-3.Narrate.Interpretive (owned), LA.2-3.Narrate.Expressive (owned), SI.K-3.Narrate (owned) | quoted speech with "said" and "asked", in the past tense | grade 2's fable map (ELD K to 2 unit 20) and the chapter book's story parts (ELA unit 3) |

Earlier-grade rows each unit assumes, last use and treatment:

| Unit | Row | Last used | Treatment |
|---|---|---|---|
| 1 | g2-la-inform | grade 2 (ELD K to 2) | retrieval, day 2 |
| 1 | g2-si-inform | grade 2 (ELD K to 2) | retrieval, day 2 |
| 2 | g2-ss-explain | grade 2 (ELD K to 2) | retrieval, day 23 |
| 2 | g2-si-narrate | grade 2 (ELD K to 2) | retrieval through use, day 24 |
| 3 | g2-ss-argue | grade 2 (ELD K to 2) | retrieval, day 40 |
| 3 | g2-si-argue | grade 2 (ELD K to 2) | retrieval, day 40 |
| 4 | g2-sc-explain | grade 2 (ELD K to 2) | retrieval, day 59 |
| 4 | g2-si-explain | grade 2 (ELD K to 2) | retrieval, day 59 |
| 5 | g2-ma-explain | grade 2 (ELD K to 2) | retrieval, day 78 |
| 5 | g3-si-inform | earlier this year | retrieval through use, day 81 |
| 6 | g2-sc-argue | grade 2 (ELD K to 2) | retrieval, day 97 |
| 6 | g3-sc-explain | earlier this year | retrieval, day 97 |
| 6 | g3-si-explain | earlier this year | retrieval through use, day 100 |
| 7 | g2-ma-argue | grade 2 (ELD K to 2) | retrieval, day 115 |
| 7 | g3-si-argue | earlier this year | retrieval through use, day 118 |
| 8 | g2-la-narrate | grade 2 (ELD K to 2) | retrieval, day 137 |
| 8 | g2-si-narrate | grade 2 (ELD K to 2) | retrieval, day 137 |
| 8 | g3-si-narrate | earlier this year | retrieval through use, day 140 |

### Unit 1. Getting to books

*What is the main idea, and how do the parts hold it up?* band days 1 to 21 (grade 3 days 1 to 21, weeks 1 to 5); 21 days: 6 Understanding, 4 Fluency, 8 Application, 2 end-of-unit assessment days and 1 respond day. Key language use: inform. Rows: g3-la-inform, g3-si-inform.

- **Host.** E.LA grade 3 unit 1 (days 1 to 39), its paired articles on book carriers today and the 1930s packhorse librarians
- **Arc.** Day 1 opens on the question and names the key language use. Day 2 retrieves the year before's row, then takes one section of the packhorse librarian article apart (how the heading groups facts under one main idea) on the text map (2 to 3 stage, grouped boxes with headings). Day 3 is the Language Dive on the sentence form (a topic sentence and a detail joined with "for example" and "also"). Day 5 gives the talk move for SI Inform. Day 9 meets the second part, the paired article on book carriers today. The class builds a grouped piece with a heading on the packhorse librarians with the teacher on day 6, students make a grouped piece about one way books reach children, with a heading, linking words and a conclusion alone on day 12, the change of audience comes on day 13 (the sharing time told to a classmate, then written as a page for a grade 2 reader), and the self-check page on day 15 asks what a heading does for a reader.
- **Why this order.** the model is taken apart before it is built with the teacher, and built with the teacher before anyone makes it alone; talk comes before writing on every day; a form is taught on an Understanding day before a Fluency day practices it. 
- **Assessments.** No readiness check: day 2 retrieves g2-la-inform, g2-si-inform (last used the year before, so retrieval). End-of-unit assessment days 19 and 20: read a new short informational page and name its main idea and two details; share it with the teacher and answer one clarifying question; then write a grouped piece with a heading on the new page, on a short page on how a mobile library reaches a town, Curio Class's own and unseen. A prompt per part of each id; look-fors at each entry point. Response time: respond day 21, counted once. No mid-unit assessment (21 days, not over 25).
- **Help withdrawn.** Entry points 5 and 6 after day 12; 3 and 4 from day 15; 1 and 2 lose the cloze before day 19.
- **Candidate: California 1.26, all four domains in the unit.** Kept, no day cost: listening and reading on days 2 and 9, speaking in the sharing time on day 5, writing on day 12; the unit plan marks the four domains on its day list.
- **Candidate: PRIME Match.LE, one interpretive item on the new page.** Kept inside the end-of-unit assessment (day 19), no day cost.
- **Candidate: Bar item 12, the self-check page's first use.** Kept on day 15, no day cost; the page is kept all year.
- **Sensitive ground.** children kept from books by distance or poverty are the host's theme; no student is asked how many books they own or whether there is a library near home. Agent reads with the unit plan: sensitivity; spanish.
- **Host-teacher note.** Content used: ELA unit 1's packhorse librarian and book carrier articles. Language taught: main idea and grouped details, topic sentences with "for example" and "also", the clarifying question.

### Unit 2. Who decides in our town

*What does each level of government do, and why?* band days 22 to 38 (grade 3 days 22 to 38, weeks 5 to 8); 17 days: 5 Understanding, 3 Fluency, 6 Application, 2 end-of-unit assessment days and 1 respond day. Key language use: explain. Rows: g3-ss-explain, g3-si-narrate.

- **Host.** S.ocial studies grade 3 unit 2 (days 25 to 48), levels of government; social studies grade 3 unit 1 (days 1 to 24), how the land changed, just studied
- **Arc.** Day 22 opens on the question and names the key language use. Day 23 retrieves the year before's row, then takes the social studies page on who makes which rules (town, state, nation) apart (a decision and its effect, box by box) on the cause chain (2 to 3 stage, linked boxes with "so"). Day 25 is the Language Dive on the sentence form ("The town council decides ___, so ___", cause with "so" and "because", and the present tense for what a level does). Day 24 gives the talk move for SI Narrate (review; owned in unit 8). The class builds an explanation of what the town council decides and why with the teacher on day 27, students make a short paragraph on what one level of government does and why, and one change in the land and its effect alone on day 31, the change of purpose comes on day 32 (the explanation given to a partner, then written as a caption for the class's town map), and the self-check page on day 33 asks what "so" does that "and" does not.
- **Why this order.** the model is taken apart before it is built with the teacher, and built with the teacher before anyone makes it alone; talk comes before writing on every day; a form is taught on an Understanding day before a Fluency day practices it. Days 22 to 24 come before the host's government pages (host day 25), so they work the land change from unit 1, already studied (the frame's "If later" line).
- **Assessments.** No readiness check: day 23 retrieves g2-ss-explain (last used the year before, so retrieval); day 24 retrieves g2-si-narrate through use. End-of-unit assessment days 36 and 37: hear a new short page and order its cause chain; explain it to the teacher; then write a short explanation of the new page, on a short page on who fixes a town's park, Curio Class's own and unseen. A prompt per part of each id; look-fors at each entry point. Response time: respond day 38, counted once. No mid-unit assessment (17 days, not over 25).
- **Help withdrawn.** Entry points 5 and 6 after day 31; 3 and 4 from day 33; 1 and 2 lose the cloze before day 36.
- **Candidate: PRIME Depth.KLU, the cause chain's links named openly.** Kept, no day cost: day 23 names each link, and the end-of-unit look-for asks for "so" or "because" between boxes.
- **Candidate: California 1.23, a long-term English learner note on "so" and "because" in writing.** Kept, no day cost: the note sits on day 31, where the written explanation first goes alone.
- **Sensitive ground.** No student is asked how government works in another country or whether a family votes or is a citizen. Agent reads with the unit plan: sensitivity.
- **Host-teacher note.** Content used: social studies unit 2's levels of government and unit 1's land change. Language taught: a decision and its effect with "so" and "because", the present tense for what a level does, a recount in three parts.

### Unit 3. The class deliberation

*What is our claim, and what does the source say?* band days 39 to 57 (grade 3 days 39 to 57, weeks 8 to 12); 19 days: 6 Understanding, 3 Fluency, 7 Application, 2 end-of-unit assessment days and 1 respond day. Key language use: argue. Rows: g3-ss-argue, g3-si-argue.

- **Host.** S.ocial studies grade 3 unit 2 (days 25 to 48), its class deliberation on a local question and its vote; a claim with evidence from social studies unit 1 retrieved
- **Arc.** Day 39 opens on the question and names the key language use. Day 40 retrieves the year before's row, then takes the first of two short sources on the host's local question apart (which sentence gives the claim and which gives its evidence) on the claim chart (2 to 3 stage, a claim and two reasons with their sources). Day 41 is the Language Dive on the sentence form ("I think ___ because ___" with "the source says ___"). Day 43 gives the talk move for SI Argue. Day 46 meets the second part, the second source on the same question. The class builds a claim with two reasons and their source with the teacher on day 44, students make a claim with evidence on the local question alone on day 50, the change of audience comes on day 51 (the claim said to a group, then written as a note to the town council), and the self-check page on day 52 asks how "the source says" changes a claim.
- **Why this order.** the model is taken apart before it is built with the teacher, and built with the teacher before anyone makes it alone; talk comes before writing on every day; a form is taught on an Understanding day before a Fluency day practices it. From day 49 the unit runs just after the host's vote (host day 48), from the class's own record of it.
- **Assessments.** No readiness check: day 40 retrieves g2-ss-argue, g2-si-argue (last used the year before, so retrieval). End-of-unit assessment days 55 and 56: read two new short sources and say which claim each supports; reach a decision with a group while the teacher listens; then write a claim with evidence, on two short sources on a made-up town question (where a crosswalk goes), Curio Class's own and unseen. A prompt per part of each id; look-fors at each entry point. Response time: respond day 57, counted once. No mid-unit assessment (19 days, not over 25).
- **Help withdrawn.** Entry points 5 and 6 after day 50; 3 and 4 from day 52; 1 and 2 lose the cloze before day 55.
- **Candidate: PRIME Breadth.LE, two argue ids met on one host.** Kept, no day cost: SS Argue on days 40 to 50, SI Argue on days 43 and 49, both in the end-of-unit assessment.
- **Candidate: Bar item 4, the deliberation's talk frames.** Kept, no day cost: the frames are taught on day 43 and used in the group decision on day 49.
- **Sensitive ground.** The local question is the host's (a park rule, a crosswalk), never immigration, policing or anything that touches a family's status; "I changed my mind" is praised, never forced. Agent reads with the unit plan: sensitivity.
- **Host-teacher note.** Content used: social studies unit 2's deliberation and vote, and two sources on its local question. Language taught: a claim from a source, "I think ___ because ___", building on another's reason.

### Unit 4. Life cycles and forces

*What happens first, next, and why?* band days 58 to 76 (grade 3 days 58 to 76, weeks 12 to 16); 19 days: 6 Understanding, 3 Fluency, 7 Application, 2 end-of-unit assessment days and 1 respond day. Key language use: explain. Rows: g3-sc-explain, g3-si-explain.

- **Host.** S.cience grade 3 unit 3 (days 37 to 58; weeks 10 to 15), life cycles; science grade 3 unit 1 (days 1 to 16; weeks 1 to 4), balanced and unbalanced forces, retrieved
- **Arc.** Day 58 opens on the question and names the key language use. Day 59 retrieves the year before's row, then takes the science unit's life-cycle model apart (stages in order, each linked to the next) on the cause chain (2 to 3 stage). Day 60 is the Language Dive on the sentence form (sequence words with "so" ("First it is a ___. Next it ___, so ___")). Day 62 gives the talk move for SI Explain. Day 65 meets the second part, how a bigger push changes the swing's motion, from the unit 1 force test record. The class builds an explanation of one life cycle in steps with the teacher on day 63, students make an explanation of a life cycle and a force change, and how the group sorted it alone on day 69, the change of audience comes on day 70 (the explanation given to the group, then given to a grade 2 class as a short talk), and the self-check page on day 71 asks what a time word does in an explanation.
- **Why this order.** the model is taken apart before it is built with the teacher, and built with the teacher before anyone makes it alone; talk comes before writing on every day; a form is taught on an Understanding day before a Fluency day practices it. The host ends on school day 73; from day 74 the unit works from the class's own model.
- **Assessments.** No readiness check: day 59 retrieves g2-sc-explain, g2-si-explain (last used the year before, so retrieval). End-of-unit assessment days 74 and 75: read a new short page and order its stages; explain it to the teacher, and how the group checked its order; then write the explanation, on a short page on a plant's life cycle not studied, Curio Class's own and unseen. A prompt per part of each id; look-fors at each entry point. Response time: respond day 76, counted once. No mid-unit assessment (19 days, not over 25).
- **Help withdrawn.** Entry points 5 and 6 after day 69; 3 and 4 from day 71; 1 and 2 lose the cloze before day 74.
- **Candidate: California 3.3, the language-or-learning note on sequence words.** Kept, no day cost: the teacher note sits on day 60.
- **Candidate: PRIME Match.KLU, explain taught as its own use.** Kept, no day cost: day 58 names explain's job and stages before any content talk.
- **Sensitive ground.** Living things only: no family trees or "who you take after" prompts about a student's own family. Agent reads with the unit plan: sensitivity.
- **Host-teacher note.** Content used: science unit 3's life-cycle model and unit 1's force test record. Language taught: steps in order with time words and "so", "when the push is bigger", explaining a group's choice.

### Unit 5. Arrays and equal groups

*How did you solve it, and why does each step work?* band days 77 to 92 (grade 3 days 77 to 92, weeks 16 to 19); 16 days: 4 Understanding, 3 Fluency, 6 Application, 2 end-of-unit assessment days and 1 respond day. Key language use: explain. Rows: g3-ma-explain, g3-si-inform.

- **Host.** M.ath grade 3 unit 4 (days 62 to 77), area and the distributive idea, taught just before; math grade 3 unit 5 (days 78 to 91), multiplying and dividing larger numbers, alongside
- **Arc.** Day 77 opens on the question and names the key language use. Day 78 retrieves the year before's row, then takes a worked solution from the math unit apart (a solution in steps, each step a box) on the cause chain (2 to 3 stage, as steps). Day 79 is the Language Dive on the sentence form ("There are ___ rows of ___, so ___" and "This works because ___"). Day 81 gives the talk move for SI Inform (review; owned in unit 1). Day 83 meets the second part, the area model from math unit 4. The class builds a solution explained step by step with the teacher on day 82, students make steps for a new problem, each with why it works alone on day 86, the change of audience comes on day 87 (explained to a partner, then recorded as steps a classmate who was absent could follow), and the self-check page on day 88 asks why "so" is hard right after a number sentence.
- **Why this order.** the model is taken apart before it is built with the teacher, and built with the teacher before anyone makes it alone; talk comes before writing on every day; a form is taught on an Understanding day before a Fluency day practices it. Tight at 16 days, just before the mid-year check: its Fluency days keep to the forms it owns, and the respond day carries the review forms.
- **Assessments.** No readiness check: day 78 retrieves g2-ma-explain (last used the year before, so retrieval); day 81 retrieves g3-si-inform through use. End-of-unit assessment days 90 and 91: read a new worked solution with one step missing and say which step is missing; explain a new problem to the teacher; then write the steps, on a worked solution with one step missing, Curio Class's own and unseen. A prompt per part of each id; look-fors at each entry point. Response time: respond day 92, counted once. No mid-unit assessment (16 days, not over 25).
- **Help withdrawn.** Entry points 5 and 6 after day 86; 3 and 4 from day 88; 1 and 2 lose the cloze before day 90.
- **Candidate: PRIME Depth.LE, why each step works, not only what it is.** Kept, no day cost: "This works because ___" is the form of day 79 and a look-for in the end-of-unit assessment.
- **Candidate: California 5.27, why "so" is hard after a number sentence, with a remedy.** Kept, no day cost: the error note sits on day 88, where students judge their own steps.
- **Sensitive ground.** Word problems use school and market settings with no prices that rank families. Agent reads with the unit plan: sensitivity.
- **Host-teacher note.** Content used: math units 4 and 5, arrays, area models and multiplication and division problems. Language taught: steps with "so", "This works because ___", the facts of a problem shared first.

#### Grade 3 mid-year check (band days 93 and 94, respond day 95; grade 3 days 93 to 95, week 19)

After unit 5, as the frame's Course-level checks table sets it. It samples units 1 to 4 on new content; unit 5's end-of-unit record, taken just before, is carried unscored, so no item repeats that assessment. Day by day: Grade 3 mid-year check, day 1 (week 19): hear and read a new informational page and name its main idea and two details; hear a new page on a town decision and order its cause chain; write a grouped piece on the informational page. Students are heard one at a time: a sharing turn answered with a clarifying question, then a recount of a class event in three parts. Then read two short sources on a new local question and say which claim each supports; read a page on a new animal's life cycle and order its stages; write a short explanation of the town decision; groups of four reach a decision on the local question while the teacher listens, and the last students give their sharing turn and recount. The respond day groups students by form and entry point and feeds any move between entry points.

### Unit 6. Surviving where you live

*What is our claim, and what does the data show?* band days 96 to 113 (grade 3 days 96 to 113, weeks 20 to 23); 18 days: 5 Understanding, 3 Fluency, 7 Application, 2 end-of-unit assessment days and 1 respond day. Key language use: argue. Rows: g3-sc-argue, g3-si-explain.

- **Host.** S.cience grade 3 unit 4 (days 59 to 78; weeks 15 to 20), surviving where you live, just studied; science grade 3 unit 3, traits and the environment, retrieved
- **Arc.** Day 96 opens on the question and names the key language use. Day 97 retrieves the year before's row, then takes the science unit's habitat data apart (a claim, then two pieces of evidence from the data) on the claim chart (2 to 3 stage). Day 98 is the Language Dive on the sentence form ("Our claim is ___. The data shows ___. Another clue is ___."). Day 100 gives the talk move for SI Explain (review; owned in unit 4). Day 103 meets the second part, whether the environment affects a trait, from science unit 3's record. The class builds a survival claim with two pieces of evidence with the teacher on day 101, students make a survival claim from the unit's evidence, with two pieces of evidence alone on day 106, the change of purpose comes on day 107 (the claim argued in a group, then written as a card for a zoo or park habitat sign), and the self-check page on day 108 asks how "the data shows" is different from "I think".
- **Why this order.** the model is taken apart before it is built with the teacher, and built with the teacher before anyone makes it alone; talk comes before writing on every day; a form is taught on an Understanding day before a Fluency day practices it. The host ends on school day 98; the unit works from the host's own data (the frame's "just after").
- **Assessments.** No readiness check: day 97 retrieves g2-sc-argue, g3-sc-explain (last used the year before, so retrieval); day 100 retrieves g3-si-explain through use. End-of-unit assessment days 111 and 112: read new data and say which claim it supports; argue it to the teacher; then write the claim with two pieces of evidence, on data on an animal in a habitat not studied, Curio Class's own and unseen. A prompt per part of each id; look-fors at each entry point. Response time: respond day 113, counted once. No mid-unit assessment (18 days, not over 25).
- **Help withdrawn.** Entry points 5 and 6 after day 106; 3 and 4 from day 108; 1 and 2 lose the cloze before day 111.
- **Candidate: PRIME Breadth.ELD, argue on a second content area.** Kept, no day cost: the whole unit argues on science after unit 3 argued on social studies.
- **Candidate: Bar item 13, argue returns harder (data, not a source).** Kept, no day cost: day 97 names what is harder than unit 3.
- **Sensitive ground.** Organisms that do not survive are talked about plainly and gently; no human migration is compared to animal habitats. Agent reads with the unit plan: sensitivity.
- **Host-teacher note.** Content used: science unit 4's habitat data and unit 3's trait record. Language taught: a claim with two pieces of evidence, "the data shows", "another clue is".

### Unit 7. Fractions on the line

*Which fraction is greater, and how do you know?* band days 114 to 132 (grade 3 days 114 to 132, weeks 23 to 27); 19 days: 5 Understanding, 3 Fluency, 8 Application, 2 end-of-unit assessment days and 1 respond day. Key language use: argue. Rows: g3-ma-argue, g3-si-argue.

- **Host.** M.ath grade 3 unit 6 (days 92 to 114), comparing and equivalent fractions, just studied; math grade 3 unit 7 (days 117 to 133), line plots with fractions, alongside
- **Arc.** Day 114 opens on the question and names the key language use. Day 115 retrieves the year before's row, then takes two classmates' claims about a pair of fractions apart (a claim, its justification from a model, and a reply) on the claim chart (2 to 3 stage). Day 116 is the Language Dive on the sentence form (comparatives with "than" and "I claim ___ because the model shows ___"). Day 118 gives the talk move for SI Argue (review; owned in unit 3). Day 121 meets the second part, a classmate's claim to critique. The class builds a fraction claim with a justification from the number line with the teacher on day 119, students make a claim, its justification from a model, and a critique of a classmate's claim alone on day 125, the change of audience comes on day 126 (argued with a partner, then written as a reply to a made-up classmate who got it wrong), and the self-check page on day 127 asks what "than" does in a comparison.
- **Why this order.** the model is taken apart before it is built with the teacher, and built with the teacher before anyone makes it alone; talk comes before writing on every day; a form is taught on an Understanding day before a Fluency day practices it. 
- **Assessments.** No readiness check: day 115 retrieves g2-ma-argue (last used the year before, so retrieval); day 118 retrieves g3-si-argue through use. End-of-unit assessment days 130 and 131: read two new claims about a new fraction pair and say which the model supports; argue to the teacher; then write a claim with its justification and a critique, on two claims about a new fraction pair, Curio Class's own and unseen. A prompt per part of each id; look-fors at each entry point. Response time: respond day 132, counted once. No mid-unit assessment (19 days, not over 25).
- **Help withdrawn.** Entry points 5 and 6 after day 125; 3 and 4 from day 127; 1 and 2 lose the cloze before day 130.
- **Candidate: PRIME Depth.LE, critique taught as its own move.** Kept, no day cost: day 121 teaches the critique as its own move.
- **Candidate: California 4.1, the grade 2 drawing frame withdrawn.** Kept, no day cost: day 114 removes it for entry points 3 and 4.
- **Sensitive ground.** A critique is of the reasoning, never the classmate; made-up classmates only in written critiques. Agent reads with the unit plan: sensitivity.
- **Host-teacher note.** Content used: math unit 6's fraction comparisons and unit 7's line plots. Language taught: comparatives with "than", a claim justified from a model, a critique of reasoning.

#### Grade 3 year-end check (band days 133 and 134, respond day 135; grade 3 days 133 to 135, week 27)

After unit 7, as the frame's Course-level checks table sets it. It samples units 4, 5 and 6 on new content; unit 7's end-of-unit record, taken just before, is carried unscored, so no item repeats that assessment. Day by day: Grade 3 year-end check, day 1 (week 27): read a new force test record and a new worked multiplication solution; write an explanation of the force change; students are heard one at a time explaining why one step of the solution works and how they checked it. Then read new habitat data and write the claim it supports with two pieces of evidence; the last students are heard explaining a step and how they checked it. The respond day groups students by form and entry point and feeds any move between entry points.

### Unit 8. A story with a voice

*How does the character answer the problem?* band days 136 to 160 (grade 3 days 136 to 160, weeks 28 to 32); 25 days: 7 Understanding, 4 Fluency, 11 Application, 2 end-of-unit assessment days and 1 respond day. Key language use: narrate. Rows: g3-la-narrate, g3-si-narrate.

- **Host.** E.LA grade 3 unit 4 (days 120 to 156), its read-aloud story of a girl whose village gets a new well; narrative writing (ELA unit 2) and story parts (ELA unit 3) retrieved
- **Arc.** Day 136 opens on the question and names the key language use. Day 137 retrieves the year before's row, then takes one scene of the well story apart (problem, events and solution, mapped) on the story map (2 to 3 stage, problem, events and solution, finished). Day 138 is the Language Dive on the sentence form (quoted speech with "said" and "asked", in the past tense). Day 140 gives the talk move for SI Narrate. Day 144 meets the second part, a school event told with a beginning, middle and end and a feeling. The class builds a story with dialogue and a clear ending, planned on the story map with the teacher on day 141, students make a story of their own with dialogue and an ending alone on day 147, the change of audience comes on day 148 (the school event told to a partner who was there, then told to a visitor who was not), and the self-check page on day 153 asks what dialogue tells a reader that a plain sentence does not.
- **Why this order.** the model is taken apart before it is built with the teacher, and built with the teacher before anyone makes it alone; talk comes before writing on every day; a form is taught on an Understanding day before a Fluency day practices it. 
- **Assessments.** No readiness check: day 137 retrieves g2-la-narrate, g2-si-narrate (last used the year before, so retrieval); day 140 retrieves g3-si-narrate through use. End-of-unit assessment days 158 and 159: hear and read a new short story and map it; tell a school event to the teacher and retell the teacher's; then write a story with dialogue, on a short story, Curio Class's own and unseen. A prompt per part of each id; look-fors at each entry point. Response time: respond day 160, counted once. No mid-unit assessment (25 days, not over 25). The end-of-unit record and the year's sheet go on to the grade 4 teacher.
- **Help withdrawn.** Entry points 5 and 6 after day 147; 3 and 4 from day 153; 1 and 2 lose the cloze before day 158.
- **Candidate: PRIME Match.LE, the story's structure named.** Kept, no day cost: day 137 names problem, events and solution on the story map.
- **Candidate: Bar item 10, the change of audience.** Kept, no day cost: day 148, the event told to one who was there and one who was not.
- **Sensitive ground.** Own-story prompts: an invented character or a school event is always allowed; no prompt asks about a journey to this country. The well story's village is named and its people are not pitied. A story may be planned in the home language. Agent reads with the unit plan: sensitivity; spanish.
- **Host-teacher note.** Content used: ELA unit 4's read-aloud well story. Language taught: dialogue with "said" and "asked", the past tense, "at last" to an ending, a school event told in three parts.

## Grade 4 (band days 161 to 320, units 9 to 17)

#### Year map, grade 4

| Unit | Days (band) | Weeks | Key language use | Ids (owned or carried) | Sentence forms | Grows from |
|---|---|---|---|---|---|---|
| 9 The same amount | 161 to 177 | 1 to 4 | argue | MA.4-5.Argue.Interpretive (carried), MA.4-5.Argue.Expressive (carried), SI.4-12.Argue (owned) | "I claim ___. One reason is ___. Therefore, ___." | grade 3's fraction claims on a number line (unit 7) |
| 10 Our neighbors | 178 to 195 | 4 to 7 | argue | SS.4-5.Argue.Interpretive (carried), SS.4-5.Argue.Expressive (carried), SI.4-12.Inform (owned) | "My claim is ___. For example, the source says ___. Therefore, ___." | grade 3's claim from a source in the deliberation (unit 3) |
| 11 Animal defenses | 196 to 213 | 8 to 11 | inform | LA.4-5.Inform.Interpretive (carried), LA.4-5.Inform.Expressive (carried), SI.4-12.Inform (owned) | the definition sentence "A ___ is a ___ that ___" with "in addition" | grade 3's grouped piece with headings (unit 1) and ELA unit 1's informative writing |
| 12 Choose the path | 214 to 231 | 11 to 15 | narrate | LA.4-5.Narrate.Interpretive (carried), LA.4-5.Narrate.Expressive (carried), SI.4-12.Narrate (owned) | a time clause ("As soon as the door opened, ___") and noun groups with two describing words | grade 3's story with dialogue (unit 8) and the verse novel's theme (ELA unit 1) |
| 13 The changing land | 235 to 252 | 15 to 19 | explain | SC.4-5.Explain.Interpretive (carried), SC.4-5.Explain.Expressive (carried), SI.4-12.Explain (owned) | "as a result" and "which causes" joining causes | grade 3's life cycle and force explanation (unit 4) and science unit 2's energy model |
| 14 The canal debate | 253 to 269 | 19 to 22 | argue | LA.4-5.Argue.Interpretive (carried), LA.4-5.Argue.Expressive (carried), SI.4-12.Argue (owned) | "In my opinion, ___. One reason is ___. For example, ___. Therefore, ___." | grade 3's group decision (unit 3) and grouped facts (unit 1) |
| 15 Big numbers in parts | 270 to 286 | 22 to 26 | explain | MA.4-5.Explain.Interpretive (carried), MA.4-5.Explain.Expressive (carried), SI.4-12.Inform (owned) | "First I break ___ into ___. As a result, ___, which gives ___" | grade 3's array and area explanations (unit 5) |
| 16 Senses and structures | 287 to 302 | 26 to 29 | argue | SC.4-5.Argue.Interpretive (carried), SC.4-5.Argue.Expressive (carried), SI.4-12.Narrate (owned) | "Our claim is ___. The evidence is ___. This shows ___ because ___." | grade 3's habitat claims (unit 6) and science unit 3's code test |
| 17 Living with hazards | 306 to 320 | 30 to 32 | explain | SS.4-5.Explain.Interpretive (carried), SS.4-5.Explain.Expressive (carried), SI.4-12.Explain (owned) | "because of" with a noun group, "led to", "mattered more" | grade 3's level-of-government explanation (unit 2) and social studies unit 6's regions |

Earlier-grade rows each unit assumes, last use and treatment:

| Unit | Row | Last used | Treatment |
|---|---|---|---|
| 9 | g3-ma-argue | grade 3 | retrieval, day 162 |
| 9 | g3-si-argue | grade 3 | retrieval through use, day 163 |
| 10 | g3-ss-argue | grade 3 | retrieval, day 179 |
| 10 | g3-si-inform | grade 3 | retrieval through use, day 182 |
| 11 | g3-la-inform | grade 3 | retrieval, day 197 |
| 11 | g3-si-inform | grade 3 | retrieval, day 197 |
| 12 | g3-la-narrate | grade 3 | retrieval, day 215 |
| 12 | g3-si-narrate | grade 3 | retrieval, day 215 |
| 13 | g3-sc-explain | grade 3 | retrieval, day 236 |
| 13 | g3-si-explain | grade 3 | retrieval, day 236 |
| 14 | g3-si-argue | grade 3 | retrieval, day 254 |
| 14 | g3-la-inform | grade 3 | retrieval, day 254 |
| 14 | g4-si-argue | earlier this year | retrieval through use, day 257 |
| 15 | g3-ma-explain | grade 3 | retrieval, day 271 |
| 15 | g4-si-inform | earlier this year | retrieval through use, day 274 |
| 16 | g3-sc-argue | grade 3 | retrieval, day 288 |
| 16 | g4-si-narrate | earlier this year | retrieval through use, day 291 |
| 17 | g3-ss-explain | grade 3 | retrieval, day 307 |
| 17 | g4-si-explain | earlier this year | retrieval through use, day 310 |

### Unit 9. The same amount

*Are these fractions equal, and can you convince the group?* band days 161 to 177 (grade 4 days 1 to 17, weeks 1 to 4); 17 days: 5 Understanding, 3 Fluency, 6 Application, 2 end-of-unit assessment days and 1 respond day. Key language use: argue. Rows: g4-ma-argue, g4-si-argue.

- **Host.** M.ath grade 4 unit 2 (days 9 to 25), fraction equivalence and comparison; math grade 4 unit 1 (days 1 to 8), factors and multiples, runs first
- **Arc.** Day 161 opens on the question and names the key language use. Day 162 retrieves the year before's row, then takes a classmate's justification apart (a claim, a reason and a conclusion) on the claim chart (4 to 5 stage begun). Day 164 is the Language Dive on the sentence form ("I claim ___. One reason is ___. Therefore, ___."). Day 163 gives the talk move for SI Argue. Day 169 meets the second part, two fractions shown equivalent, or compared, with strips or a number line. The class builds a justification with a claim, a reason and "therefore" with the teacher on day 167, students make a justification of an equivalence, and a reply to a classmate's reasoning alone on day 171, the change of audience comes on day 172 (argued in the group, then written for a grade 3 student who thinks the bigger denominator means the bigger fraction), and the self-check page on day 173 asks what "therefore" tells a listener.
- **Why this order.** the model is taken apart before it is built with the teacher, and built with the teacher before anyone makes it alone; talk comes before writing on every day; a form is taught on an Understanding day before a Fluency day practices it. The routine is taught on days 1 to 3 and kept all year. Days 1 to 8 come before math's fractions unit (host day 9), so they retrieve grade 3's fraction claims and teach the routine and the compromise talk on math unit 1's factor puzzle (the frame's "If later" line). Tight at 17 days with the year's new routine: its Fluency days keep to the forms it owns, and the respond day carries the review forms.
- **Assessments.** No readiness check: day 162 retrieves g3-ma-argue (last used the year before, so retrieval); day 163 retrieves g3-si-argue through use. End-of-unit assessment days 175 and 176: read two new justifications for a new fraction pair and say which holds; argue to the teacher; then write a justification and a reply, on two justifications for a new fraction pair, Curio Class's own and unseen. A prompt per part of each id; look-fors at each entry point. Response time: respond day 177, counted once. No mid-unit assessment (17 days, not over 25).
- **Help withdrawn.** Entry points 5 and 6 after day 171; 3 and 4 from day 173; 1 and 2 lose the cloze before day 175.
- **Candidate: California 1.20, a named group routine.** Kept, no day cost: "plan, check, report" taught on days 161 to 163 and used every week.
- **Candidate: PRIME Breadth.KLU, two argue ids on one host.** Kept, no day cost: MA Argue and SI Argue meet in the group compromise on day 166 and in the end-of-unit talk task.
- **Sensitive ground.** Disagreeing politely is taught as a skill; no student is made to give way. Long-term English learners: "therefore" in writing is the look-for, since the social talk is already there. Agent reads with the unit plan: sensitivity.
- **Host-teacher note.** Content used: math unit 1's factor puzzle and unit 2's fraction equivalence. Language taught: "I claim ___. One reason is ___. Therefore, ___.", polite disagreement, a compromise.

### Unit 10. Our neighbors

*What does the research show, and does a second source agree?* band days 178 to 195 (grade 4 days 18 to 35, weeks 4 to 7); 18 days: 6 Understanding, 3 Fluency, 6 Application, 2 end-of-unit assessment days and 1 respond day. Key language use: argue. Rows: g4-ss-argue, g4-si-inform.

- **Host.** S.ocial studies grade 4 unit 2 (days 17 to 38), Canada and Mexico research, alongside; its own maps, photographs and records
- **Arc.** Day 178 opens on the question and names the key language use. Day 179 retrieves the year before's row, then takes one short source from the research unit on a question about Canada or Mexico apart (a claim and the source that holds it up) on the claim chart (4 to 5 stage). Day 180 is the Language Dive on the sentence form ("My claim is ___. For example, the source says ___. Therefore, ___."). Day 182 gives the talk move for SI Inform (review; owned in unit 11). Day 185 meets the second part, a second source on the same question, checked against the first. The class builds a claim from one source, then checked against a second with the teacher on day 183, students make a claim from two sources, citing both alone on day 188, the change of audience comes on day 189 (told to the group, then written for the class's research wall), and the self-check page on day 190 asks why a second source makes a claim stronger.
- **Why this order.** the model is taken apart before it is built with the teacher, and built with the teacher before anyone makes it alone; talk comes before writing on every day; a form is taught on an Understanding day before a Fluency day practices it. Social studies grade 4 unit 4's primary sources come later and are not used; the unit works from the research unit's own maps, photographs and records.
- **Assessments.** No readiness check: day 179 retrieves g3-ss-argue (last used the year before, so retrieval); day 182 retrieves g3-si-inform through use. End-of-unit assessment days 193 and 194: read two new short sources and say whether they agree; argue to the teacher; then write a claim citing both, on two short sources on a question about the border's rivers, Curio Class's own and unseen. A prompt per part of each id; look-fors at each entry point. Response time: respond day 195, counted once. No mid-unit assessment (18 days, not over 25).
- **Help withdrawn.** Entry points 5 and 6 after day 188; 3 and 4 from day 190; 1 and 2 lose the cloze before day 193.
- **Candidate: PRIME Match.ELD, a cited source as the argue form.** Kept, no day cost: day 180 teaches the citing sentence.
- **Candidate: Bar item 5, research language named.** Kept, no day cost: day 184 names the source kinds and the research words.
- **Sensitive ground.** Students from Mexico or Canada, or with family there, are never made the class's source or spokesperson; a student may share if they choose. No claim compares countries as better or worse. Agent reads with the unit plan: sensitivity; spanish.
- **Host-teacher note.** Content used: social studies unit 2's Canada and Mexico research and its sources. Language taught: a claim citing a source, checking one source against another, giving directions with roles.

### Unit 11. Animal defenses

*How is this text built, and what does that term mean?* band days 196 to 213 (grade 4 days 36 to 53, weeks 8 to 11); 18 days: 5 Understanding, 4 Fluency, 6 Application, 2 end-of-unit assessment days and 1 respond day. Key language use: inform. Rows: g4-la-inform, g4-si-inform.

- **Host.** E.LA grade 4 unit 2 (days 39 to 77), its informational book on animal defenses; ELA grade 4 unit 1 (days 1 to 38), informative writing and grammar, retrieved
- **Arc.** Day 196 opens on the question and names the key language use. Day 197 retrieves the year before's row, then takes one paragraph of the ELA unit's book on armor and camouflage apart (a section grouped by subtopic around a defined term) on the text map (4 to 5 stage, subtopics with a defined term). Day 199 is the Language Dive on the sentence form (the definition sentence "A ___ is a ___ that ___" with "in addition"). Day 198 gives the talk move for SI Inform. The class builds a section on one defense with a defined term with the teacher on day 202, students make a section on one defense, grouped by subtopic with a defined term alone on day 205, the change of audience comes on day 206 (the plan reported to the class, then the section written for the expert group's poster), and the self-check page on day 208 asks what a definition sentence does for a reader.
- **Why this order.** the model is taken apart before it is built with the teacher, and built with the teacher before anyone makes it alone; talk comes before writing on every day; a form is taught on an Understanding day before a Fluency day practices it. Days 36 to 38 come just before ELA's book opens (host day 39), so they retrieve ELA unit 1's informative writing (the frame's "If later" line).
- **Assessments.** No readiness check: day 197 retrieves g3-la-inform, g3-si-inform (last used the year before, so retrieval). End-of-unit assessment days 211 and 212: read a new short section and name its structure and its defined term; report a plan to the teacher; then write a section, on a short section on a defense not studied, Curio Class's own and unseen. A prompt per part of each id; look-fors at each entry point. Response time: respond day 213, counted once. No mid-unit assessment (18 days, not over 25).
- **Help withdrawn.** Entry points 5 and 6 after day 205; 3 and 4 from day 208; 1 and 2 lose the cloze before day 211.
- **Candidate: PRIME Depth.KLU, text structure named.** Kept, no day cost: day 201 names the structure and its signal words.
- **Candidate: California 1.15, word parts in the defined term.** Kept, no day cost: day 201.
- **Sensitive ground.** Animal defenses only; no student is asked to describe a time they had to defend themselves. Agent reads with the unit plan: sensitivity.
- **Host-teacher note.** Content used: ELA unit 2's book on animal defenses and unit 1's informative writing. Language taught: the definition sentence, signal words for structure, a plan reported and checked.

### Unit 12. Choose the path

*How does a scene slow down, and what did our group do?* band days 214 to 231 (grade 4 days 54 to 71, weeks 11 to 15); 18 days: 5 Understanding, 3 Fluency, 7 Application, 2 end-of-unit assessment days and 1 respond day. Key language use: narrate. Rows: g4-la-narrate, g4-si-narrate.

- **Host.** E.LA grade 4 unit 2 (days 39 to 77), its choose-your-own-adventure story; the verse novel's theme (ELA unit 1) retrieved
- **Arc.** Day 214 opens on the question and names the key language use. Day 215 retrieves the year before's row, then takes one passage of the adventure story apart (a scene with its key moment and the theme it shows) on the story map (4 to 5 stage). Day 216 is the Language Dive on the sentence form (a time clause ("As soon as the door opened, ___") and noun groups with two describing words). Day 218 gives the talk move for SI Narrate. The class builds one scene with dialogue and description, rehearsed aloud first with the teacher on day 219, students make one scene of their own with dialogue and description alone on day 223, the change of audience comes on day 224 (the recount told to the absent classmate, then the scene read aloud to another group), and the self-check page on day 226 asks what a noun group with two describing words does to a scene.
- **Why this order.** the model is taken apart before it is built with the teacher, and built with the teacher before anyone makes it alone; talk comes before writing on every day; a form is taught on an Understanding day before a Fluency day practices it. 
- **Assessments.** No readiness check: day 215 retrieves g3-la-narrate, g3-si-narrate (last used the year before, so retrieval). End-of-unit assessment days 229 and 230: read a new short adventure scene and say its theme and how it slows down; recount a group task to the teacher; then write a scene, on a short adventure scene, Curio Class's own and unseen. A prompt per part of each id; look-fors at each entry point. Response time: respond day 231, counted once. No mid-unit assessment (18 days, not over 25).
- **Help withdrawn.** Entry points 5 and 6 after day 223; 3 and 4 from day 226; 1 and 2 lose the cloze before day 229.
- **Candidate: PRIME Match.LE, noun groups named.** Kept, no day cost: day 216.
- **Candidate: California 3.5, the self-check page.** Kept, no day cost: day 226.
- **Sensitive ground.** Own-story prompts: an invented character is always allowed; the scene is the adventure's, not a student's own danger. Agent reads with the unit plan: sensitivity; spanish.
- **Host-teacher note.** Content used: ELA unit 2's adventure story and unit 1's verse novel. Language taught: time clauses, noun groups with two describing words, a recount for an absent classmate.

#### Grade 4 mid-year check (band days 232 and 233, respond day 234; grade 4 days 72 to 74, week 15)

After unit 12, as the frame's Course-level checks table sets it. It samples units 9, 10 and 11 on new content; unit 12's end-of-unit record, taken just before, is carried unscored, so no item repeats that assessment. Day by day: Grade 4 mid-year check, day 1 (week 15): read a new fraction justification and say whether it holds; read two new short sources on a question about a neighbor country's land and say whether they agree; write a claim citing both sources; students are heard one at a time reporting a plan and checking a partner's with "Do you mean ___?". Then read a new section on an animal defense and name its structure and defined term; write a section on it; groups of four reach a compromise on the fraction justification while the teacher listens, and the last students report their plan. The respond day groups students by form and entry point and feeds any move between entry points.

### Unit 13. The changing land

*How did the river do it, and why did our plan change?* band days 235 to 252 (grade 4 days 75 to 92, weeks 15 to 19); 18 days: 6 Understanding, 3 Fluency, 6 Application, 2 end-of-unit assessment days and 1 respond day. Key language use: explain. Rows: g4-sc-explain, g4-si-explain.

- **Host.** S.cience grade 4 unit 4 (days 57 to 73; weeks 15 to 19), weathering and erosion, alongside; science grade 4 unit 2, energy on the move, retrieved
- **Arc.** Day 235 opens on the question and names the key language use. Day 236 retrieves the year before's row, then takes the science unit's canyon model apart (a process, cause by cause) on the cause chain (4 to 5 stage). Day 237 is the Language Dive on the sentence form ("as a result" and "which causes" joining causes). Day 239 gives the talk move for SI Explain. Day 242 meets the second part, how energy moved in unit 2's ball test. The class builds an explanation of how a canyon formed with the teacher on day 240, students make an explanation of how a canyon formed and why the group's plan changed alone on day 245, the change of audience comes on day 246 (explained to the group, then written as a sign for a park trail), and the self-check page on day 247 asks what "which causes" adds that "and" does not.
- **Why this order.** the model is taken apart before it is built with the teacher, and built with the teacher before anyone makes it alone; talk comes before writing on every day; a form is taught on an Understanding day before a Fluency day practices it. 
- **Assessments.** No readiness check: day 236 retrieves g3-sc-explain, g3-si-explain (last used the year before, so retrieval). End-of-unit assessment days 250 and 251: read a new short page and order its cause chain; explain to the teacher; then write the explanation, on a short page on a beach changing over a year, Curio Class's own and unseen. A prompt per part of each id; look-fors at each entry point. Response time: respond day 252, counted once. No mid-unit assessment (18 days, not over 25).
- **Help withdrawn.** Entry points 5 and 6 after day 245; 3 and 4 from day 247; 1 and 2 lose the cloze before day 250.
- **Candidate: PRIME Depth.LE, linked causes.** Kept, no day cost: day 237.
- **Candidate: California 2.12, group talk guidance for a changed plan.** Kept, no day cost: day 239 carries the guidance, used again in the end-of-unit talk.
- **Sensitive ground.** Floods and land loss are named as the host names them; no student is asked about a disaster at home. Agent reads with the unit plan: sensitivity.
- **Host-teacher note.** Content used: science unit 4's canyon model and stream table, unit 2's ball test. Language taught: linked causes with "as a result" and "which causes", explaining a changed plan.

### Unit 14. The canal debate

*What is the author's reason, and what is mine?* band days 253 to 269 (grade 4 days 93 to 109, weeks 19 to 22); 17 days: 4 Understanding, 3 Fluency, 7 Application, 2 end-of-unit assessment days and 1 respond day. Key language use: argue. Rows: g4-la-argue, g4-si-argue.

- **Host.** E.LA grade 4 unit 3 (days 81 to 119), the Erie Canal debate, alongside
- **Arc.** Day 253 opens on the question and names the key language use. Day 254 retrieves the year before's row, then takes one paragraph of the 1816 memorial or the unit's opposing speech apart (the author's reasons, each with its evidence) on the text map of the author's facts (model in), growing into the claim chart. Day 255 is the Language Dive on the sentence form ("In my opinion, ___. One reason is ___. For example, ___. Therefore, ___."). Day 257 gives the talk move for SI Argue (review; owned in unit 9). The class builds one opinion paragraph with grouped reasons with the teacher on day 258, students make an opinion paragraph with grouped reasons, examples and a conclusion alone on day 262, the change of audience comes on day 263 (the opinion said to the group, then written as a letter to the 1816 legislature), and the self-check page on day 264 asks how "should" changes a sentence into an opinion.
- **Why this order.** the model is taken apart before it is built with the teacher, and built with the teacher before anyone makes it alone; talk comes before writing on every day; a form is taught on an Understanding day before a Fluency day practices it. 
- **Assessments.** No readiness check: day 254 retrieves g3-si-argue, g3-la-inform (last used the year before, so retrieval); day 257 retrieves g4-si-argue through use. End-of-unit assessment days 267 and 268: read a new short opinion and find its reasons and evidence; argue to the teacher; then write an opinion paragraph, on a short opinion on whether a town should build a bridge, Curio Class's own and unseen. A prompt per part of each id; look-fors at each entry point. Response time: respond day 269, counted once. No mid-unit assessment (17 days, not over 25).
- **Help withdrawn.** Entry points 5 and 6 after day 262; 3 and 4 from day 264; 1 and 2 lose the cloze before day 267.
- **Candidate: PRIME Breadth.LE, LA Argue first met.** Kept, no day cost: day 259 names it as the band's first LA Argue.
- **Candidate: Bar item 13, argue returns from math to a text.** Kept, no day cost: day 254 names what is harder than unit 9.
- **Sensitive ground.** The canal ran through Haudenosaunee lands, which the host names plainly; no claim treats the Oneida, Onondaga, Cayuga or Seneca Nations as an obstacle, and the opposing view is never the Nations' land against "progress". Agent reads with the unit plan: sensitivity.
- **Host-teacher note.** Content used: ELA unit 3's Erie Canal memorial and opposing speech. Language taught: an author's reasons found, an opinion paragraph with grouped reasons and "therefore".

### Unit 15. Big numbers in parts

*How does the method work, step by step?* band days 270 to 286 (grade 4 days 110 to 126, weeks 22 to 26); 17 days: 4 Understanding, 3 Fluency, 7 Application, 2 end-of-unit assessment days and 1 respond day. Key language use: explain. Rows: g4-ma-explain, g4-si-inform.

- **Host.** M.ath grade 4 unit 7 (days 96 to 110), multi-digit multiplication, taught just before; math grade 4 unit 8 (days 113 to 127), multi-digit division, alongside from day 113
- **Arc.** Day 270 opens on the question and names the key language use. Day 271 retrieves the year before's row, then takes a worked area-model solution apart (a method in steps a partner could use) on the cause chain (4 to 5 stage, as steps). Day 272 is the Language Dive on the sentence form ("First I break ___ into ___. As a result, ___, which gives ___"). Day 274 gives the talk move for SI Inform (review; owned in unit 11). Day 276 meets the second part, multi-digit division with place value. The class builds a multiplication method explained step by step with the teacher on day 275, students make a multi-digit method explained for a new problem alone on day 279, the change of audience comes on day 280 (explained to a partner, then recorded as a how-to card for a grade 3 class), and the self-check page on day 281 asks why partial products are hard to say.
- **Why this order.** the model is taken apart before it is built with the teacher, and built with the teacher before anyone makes it alone; talk comes before writing on every day; a form is taught on an Understanding day before a Fluency day practices it. 
- **Assessments.** No readiness check: day 271 retrieves g3-ma-explain (last used the year before, so retrieval); day 274 retrieves g4-si-inform through use. End-of-unit assessment days 284 and 285: read a new worked solution with an error and find the step; explain a new problem to the teacher; then write the method, on a worked solution with an error, Curio Class's own and unseen. A prompt per part of each id; look-fors at each entry point. Response time: respond day 286, counted once. No mid-unit assessment (17 days, not over 25).
- **Help withdrawn.** Entry points 5 and 6 after day 279; 3 and 4 from day 281; 1 and 2 lose the cloze before day 284.
- **Candidate: PRIME Depth.LE, a method explained for transfer.** Kept, no day cost: day 279, a new problem.
- **Candidate: California 5.27, why partial products are hard to say.** Kept, no day cost: day 281.
- **Sensitive ground.** Problems use school and community settings with no prices that rank families. Agent reads with the unit plan: sensitivity; spanish.
- **Host-teacher note.** Content used: math units 7 and 8, multi-digit multiplication and division. Language taught: steps with "as a result" and "which gives", a plan reported and checked.

### Unit 16. Senses and structures

*Which claim does our test support?* band days 287 to 302 (grade 4 days 127 to 142, weeks 26 to 29); 16 days: 4 Understanding, 3 Fluency, 6 Application, 2 end-of-unit assessment days and 1 respond day. Key language use: argue. Rows: g4-sc-argue, g4-si-narrate.

- **Host.** S.cience grade 4 unit 6 (days 94 to 117; weeks 24 to 30), senses and structures, alongside; science grade 4 unit 3, the coded-message test, retrieved
- **Arc.** Day 287 opens on the question and names the key language use. Day 288 retrieves the year before's row, then takes the science unit's results apart (a claim, its evidence and its reasoning) on the claim chart (4 to 5 stage). Day 289 is the Language Dive on the sentence form ("Our claim is ___. The evidence is ___. This shows ___ because ___."). Day 291 gives the talk move for SI Narrate (review; owned in unit 12). Day 293 meets the second part, which coded message worked best in unit 3's test. The class builds a structure claim with evidence and reasoning with the teacher on day 292, students make a structure claim from the class's tests alone on day 296, the change of audience comes on day 297 (argued to another group, then written for the science fair board), and the self-check page on day 298 asks how reasoning is different from evidence.
- **Why this order.** the model is taken apart before it is built with the teacher, and built with the teacher before anyone makes it alone; talk comes before writing on every day; a form is taught on an Understanding day before a Fluency day practices it. Tight at 16 days, before the year-end check: its Fluency days keep to the forms it owns, and the respond day carries the review forms.
- **Assessments.** No readiness check: day 288 retrieves g3-sc-argue (last used the year before, so retrieval); day 291 retrieves g4-si-narrate through use. End-of-unit assessment days 300 and 301: read new results and say which claim they support; argue to the teacher; then write the claim, on results on a plant structure not studied, Curio Class's own and unseen. A prompt per part of each id; look-fors at each entry point. Response time: respond day 302, counted once. No mid-unit assessment (16 days, not over 25). The end-of-unit record is carried unscored to the year-end check.
- **Help withdrawn.** Entry points 5 and 6 after day 296; 3 and 4 from day 298; 1 and 2 lose the cloze before day 300.
- **Candidate: PRIME Depth.LE, reasoning as its own part of a claim.** Kept, no day cost: day 289.
- **Candidate: Bar item 13, narrate returns harder.** Kept, no day cost: day 291, a test recount after unit 12's task recount.
- **Sensitive ground.** Senses: no student is asked about their own eyesight or hearing; students who are blind or deaf are never used as examples. Agent reads with the unit plan: sensitivity.
- **Host-teacher note.** Content used: science unit 6's structure tests and unit 3's code test. Language taught: claim, evidence and reasoning with "This shows ___ because ___", a test recounted in order.

#### Grade 4 year-end check (band days 303 and 304, respond day 305; grade 4 days 143 to 145, week 29)

After unit 16, as the frame's Course-level checks table sets it. It samples units 12 to 15 on new content; unit 16's end-of-unit record, taken just before, is carried unscored, so no item repeats that assessment. Day by day: Grade 4 year-end check, day 1 (week 29): read a new adventure scene and say its theme and how it slows down; read a new page on land changing and order its causes; write the explanation of the land change; students are heard one at a time recounting a group task for an absent classmate. Then read a new short opinion and find its reasons; read a new multi-digit solution and find the step with the error; write an opinion paragraph; students are heard explaining the corrected method and why their group changed its plan. The respond day groups students by form and entry point and feeds any move between entry points.

### Unit 17. Living with hazards

*What caused it, how did people respond, and what mattered more?* band days 306 to 320 (grade 4 days 146 to 160, weeks 30 to 32); 15 days: 4 Understanding, 3 Fluency, 5 Application, 2 end-of-unit assessment days and 1 respond day. Key language use: explain. Rows: g4-ss-explain, g4-si-explain.

- **Host.** S.ocial studies grade 4 unit 7 (days 137 to 160), peoples and hazards, alongside; social studies grade 4 unit 6, regions and resources, retrieved
- **Arc.** Day 306 opens on the question and names the key language use. Day 307 retrieves the year before's row, then takes the social studies unit's account of one region's hazard and its response apart (causes, a response, and one cause marked as mattering more) on the cause chain (4 to 5 stage, one cause marked as mattering more). Day 308 is the Language Dive on the sentence form ("because of" with a noun group, "led to", "mattered more"). Day 310 gives the talk move for SI Explain (review; owned in unit 13). Day 312 meets the second part, how a region's resources shape its life, from social studies unit 6. The class builds an explanation that weighs two causes with the teacher on day 311, students make an explanation of a hazard's causes and the response, with one cause weighed alone on day 314, the change of audience comes on day 315 (explained to the group, then written as a short page for a town's preparedness guide), and the self-check page on day 316 asks why "because of" needs a noun group after it.
- **Why this order.** the model is taken apart before it is built with the teacher, and built with the teacher before anyone makes it alone; talk comes before writing on every day; a form is taught on an Understanding day before a Fluency day practices it. Tight at 15 days, the year's last host window: its Fluency days keep to the forms it owns, and the respond day carries the review forms.
- **Assessments.** No readiness check: day 307 retrieves g3-ss-explain (last used the year before, so retrieval); day 310 retrieves g4-si-explain through use. End-of-unit assessment days 318 and 319: read a new short account and order its chain; explain to the teacher; then write the explanation, on a short account of a town preparing for a storm, Curio Class's own and unseen. A prompt per part of each id; look-fors at each entry point. Response time: respond day 320, counted once. No mid-unit assessment (15 days, not over 25). The end-of-unit record and the year's sheet go on to the grade 5 teacher.
- **Help withdrawn.** Entry points 5 and 6 after day 314; 3 and 4 from day 316; 1 and 2 lose the cloze before day 318.
- **Candidate: PRIME Breadth.ELD, explain on social studies.** Kept, no day cost: the whole unit.
- **Candidate: California 3.3, a language-or-learning note on noun groups after "because of".** Kept, no day cost: day 308.
- **Sensitive ground.** Some students and families have lived through a disaster or left one: the hazard is told through preparation and response, no student is asked to tell their own, and the teacher page names how to answer a student who chooses to. Agent reads with the unit plan: sensitivity; spanish.
- **Host-teacher note.** Content used: social studies unit 7's hazard account and unit 6's regions. Language taught: "because of" with a noun group, "led to", weighing which cause mattered more.

## Grade 5 (band days 321 to 480, units 18 to 25)

#### Year map, grade 5

| Unit | Days (band) | Weeks | Key language use | Ids (owned or carried) | Sentence forms | Grows from |
|---|---|---|---|---|---|---|
| 18 Starting over | 321 to 341 | 1 to 5 | narrate | LA.4-5.Narrate.Interpretive (owned), LA.4-5.Narrate.Expressive (owned), SI.4-12.Narrate (carried) | the past progressive with "while" and a time clause ("While the truck was pulling away, ___") | grade 4's scene with description and its recount (unit 12) |
| 19 Where a tree comes from | 342 to 366 | 5 to 10 | explain | SC.4-5.Explain.Interpretive (owned), SC.4-5.Explain.Expressive (owned), SI.4-12.Explain (carried), SC.4-5.Argue.Interpretive (owned), SC.4-5.Argue.Expressive (owned) | "The sun ___. As a result, ___, which causes ___" | grade 4's energy and erosion explanations (unit 13) and structure claims (unit 16) |
| 20 The rainforest | 367 to 385 | 10 to 13 | inform | LA.4-5.Inform.Interpretive (owned), LA.4-5.Inform.Expressive (owned), SI.4-12.Inform (carried) | relative clauses with "which" and "while" for comparing | grade 4's defined-term section (unit 11) |
| 21 Causes and a Constitution | 386 to 405 | 14 to 17 | explain | SS.4-5.Explain.Interpretive (owned), SS.4-5.Explain.Expressive (owned), SI.4-12.Inform (carried) | "so that no one branch ___" for purpose, with "as a result" and "which caused" | grade 4's hazard causes (unit 17) and social studies unit 3's causes |
| 22 Decimals at work | 409 to 425 | 18 to 21 | explain | MA.4-5.Explain.Interpretive (owned), MA.4-5.Explain.Expressive (owned), SI.4-12.Explain (carried) | "This step fits because ___, which means ___" | grade 4's multi-digit methods (unit 15) and math unit 4's fraction problems |
| 23 Leading change | 426 to 442 | 22 to 25 | argue | LA.4-5.Argue.Interpretive (owned), LA.4-5.Argue.Expressive (owned), SI.4-12.Argue (carried) | "This shows ___. Therefore, ___." and "should" for a recommendation | grade 4's opinion paragraph (unit 14) and its compromise talk (unit 9) |
| 24 Bigger or smaller | 443 to 457 | 25 to 28 | argue | MA.4-5.Argue.Interpretive (owned), MA.4-5.Argue.Expressive (owned), SI.4-12.Inform (carried) | "I claim ___. For example, ___. Therefore, ___." with "larger than" and "smaller than" | grade 4's equivalence justification (unit 9) |
| 25 Winning a right | 461 to 480 | 29 to 32 | argue | SS.4-5.Argue.Interpretive (owned), SS.4-5.Argue.Expressive (owned), SI.4-12.Narrate (carried) | "Both sources show ___. For example, ___. Therefore, ___ should ___." | grade 4's claim from two sources (unit 10) and social studies unit 3's sourcing (the Boston engraving and the testimony) |

Earlier-grade rows each unit assumes, last use and treatment:

| Unit | Row | Last used | Treatment |
|---|---|---|---|
| 18 | g4-la-narrate | grade 4 | retrieval, day 322 |
| 18 | g4-si-narrate | grade 4 | retrieval, day 322 |
| 19 | g4-sc-explain | grade 4 | retrieval, day 343 |
| 19 | g4-sc-argue | grade 4 | retrieval, day 343 |
| 19 | g4-si-explain | grade 4 | retrieval through use, day 346 |
| 20 | g4-la-inform | grade 4 | retrieval, day 368 |
| 20 | g4-si-inform | grade 4 | retrieval, day 368 |
| 21 | g4-ss-explain | grade 4 | retrieval, day 387 |
| 21 | g5-si-inform | earlier this year | retrieval through use, day 390 |
| 22 | g4-ma-explain | grade 4 | retrieval, day 410 |
| 22 | g4-si-explain | grade 4 | retrieval, day 410 |
| 23 | g4-la-argue | grade 4 | retrieval, day 427 |
| 23 | g4-si-argue | grade 4 | retrieval, day 427 |
| 24 | g4-ma-argue | grade 4 | retrieval, day 444 |
| 24 | g5-si-inform | earlier this year | retrieval through use, day 447 |
| 25 | g4-ss-argue | grade 4 | retrieval, day 462 |
| 25 | g5-si-narrate | earlier this year | retrieval through use, day 464 |

### Unit 18. Starting over

*How do the scenes join, and what was the key moment?* band days 321 to 341 (grade 5 days 1 to 21, weeks 1 to 5); 21 days: 6 Understanding, 4 Fluency, 8 Application, 2 end-of-unit assessment days and 1 respond day. Key language use: narrate. Rows: g5-la-narrate, g5-si-narrate.

- **Host.** E.LA grade 5 unit 1 (days 1 to 41), its novel read whole, alongside
- **Arc.** Day 321 opens on the question and names the key language use. Day 322 retrieves the year before's row, then takes the passage where two of the novel's chapters join apart (scenes joined across chapters, with the key moment marked) on the story map (4 to 5 stage, scenes or days with the key moment marked). Day 323 is the Language Dive on the sentence form (the past progressive with "while" and a time clause ("While the truck was pulling away, ___")). Day 325 gives the talk move for SI Narrate (carried; owned in grade 4). Day 329 meets the second part, a reflective ending ("Looking back, ___"). The class builds a narrative scene with pacing with the teacher on day 326, students make a narrative scene of their own with pacing and a reflective ending alone on day 332, the change of audience comes on day 333 (the recount told to a classmate who missed the week, then the scene read to a younger class), and the self-check page on day 335 asks what the past progressive does that the plain past does not.
- **Why this order.** the model is taken apart before it is built with the teacher, and built with the teacher before anyone makes it alone; talk comes before writing on every day; a form is taught on an Understanding day before a Fluency day practices it. 
- **Assessments.** No readiness check: day 322 retrieves g4-la-narrate, g4-si-narrate (last used the year before, so retrieval). End-of-unit assessment days 339 and 340: read a new short story in two scenes and say how they join; recount a group task to the teacher; then write a scene with a reflective ending, on a short story in two scenes, Curio Class's own and unseen. A prompt per part of each id; look-fors at each entry point. Response time: respond day 341, counted once. No mid-unit assessment (21 days, not over 25).
- **Help withdrawn.** Entry points 5 and 6 after day 332; 3 and 4 from day 335; 1 and 2 lose the cloze before day 339.
- **Candidate: PRIME Match.LE, the past progressive named with its job.** Kept, no day cost: day 323.
- **Candidate: California 1.26, all four domains.** Kept, no day cost: listening and reading on days 322 and 329, speaking on day 325, writing on day 332.
- **Sensitive ground.** the novel's family loses its home after a father's death and starts over in farm work in another state. The scene students write is invented, never their own move or loss; no prompt asks why a family moved; the teacher page names how to answer a student who chooses to share. The family note previews the loss and the move and says how to ask for the other text (a Curio Class passage on a move to a new school, written with the unit, carrying the same forms). Agent reads with the unit plan: sensitivity; spanish.
- **Host-teacher note.** Content used: ELA unit 1's novel. Language taught: the past progressive with "while", time clauses, a reflective ending, a recount across days.

### Unit 19. Where a tree comes from

*How did the energy get there, and what does the evidence show?* band days 342 to 366 (grade 5 days 22 to 46, weeks 5 to 10); 25 days: 7 Understanding, 5 Fluency, 10 Application, 2 end-of-unit assessment days and 1 respond day. Key language use: explain. Rows: g5-sc-explain, g5-si-explain, g5-sc-argue.

- **Host.** S.cience grade 5 unit 2 (days 18 to 41; weeks 5 to 10), food energy from the sun and plant matter, one shared host for both rows; science grade 5 unit 1, particles, retrieved
- **Arc.** Day 342 opens on the question and names the key language use. Day 343 retrieves the year before's row, then takes the science unit's food-web model apart (a mechanism, cause by cause) on the cause chain feeding the claim chart (4 to 5 stage). Day 344 is the Language Dive on the sentence form ("The sun ___. As a result, ___, which causes ___"). Day 346 gives the talk move for SI Explain (review; owned in unit 22). Day 348 meets the second part, that matter is made of particles too small to see, from unit 1's model. The class builds an explanation of where food energy comes from with the teacher on day 347, students make an explanation of where a tree's energy comes from alone on day 351, and the self-check page on day 353 asks how a claim is different from an explanation. Explain runs days 342 to 354; argue runs days 355 to 363: the plant-matter claim taken apart, its Language Dive, the soil claim answered in groups, built with the teacher, made alone (day 360), the change of audience (day 361) and a second self-check (day 362).
- **Why this order.** the model is taken apart before it is built with the teacher, and built with the teacher before anyone makes it alone; talk comes before writing on every day; a form is taught on an Understanding day before a Fluency day practices it. Science grade 5 unit 4's gravity is later and not used; the plant-matter argument meets the SC Argue ids and the gravity claim stays in science (frame, For the lead item 3).
- **Assessments.** No readiness check: day 343 retrieves g4-sc-explain, g4-sc-argue (last used the year before, so retrieval); day 346 retrieves g4-si-explain through use. End-of-unit assessment days 364 and 365: read a new short page and data and say what the data supports; explain and argue to the teacher; then write the explanation and the claim, on a short page and data on a seed grown in water, Curio Class's own and unseen. A prompt per part of each id; look-fors at each entry point. Response time: respond day 366, counted once. No mid-unit assessment (25 days, not over 25).
- **Help withdrawn.** Entry points 5 and 6 after day 351; 3 and 4 from day 353; 1 and 2 lose the cloze before day 364.
- **Candidate: PRIME Breadth.KLU, two uses on one host.** Kept, no day cost: explain on days 342 to 354, argue on days 355 to the end-of-unit assessment.
- **Candidate: California 2.9, new information controlled per lesson (explain first, then argue).** Kept, no day cost: the two halves do not overlap.
- **Sensitive ground.** Food and plants only; no student is asked what they eat at home. Agent reads with the unit plan: sensitivity.
- **Host-teacher note.** Content used: science unit 2's food web and plant-growth data, unit 1's particle model. Language taught: linked causes with "which causes", a claim with "for example" and "therefore", a process explained with "so that".

### Unit 20. The rainforest

*How is each text built, and which structure fits mine?* band days 367 to 385 (grade 5 days 47 to 65, weeks 10 to 13); 19 days: 6 Understanding, 3 Fluency, 7 Application, 2 end-of-unit assessment days and 1 respond day. Key language use: inform. Rows: g5-la-inform, g5-si-inform.

- **Host.** E.LA grade 5 unit 2 (days 42 to 80), the rainforest, its account of a canopy scientist's year in El Yunque and the federal forest pages, alongside; ELA unit 1's informative writing retrieved
- **Arc.** Day 367 opens on the question and names the key language use. Day 368 retrieves the year before's row, then takes one paragraph from the first of two ELA texts on the coquí frog apart (how one text compares and the other tells cause and effect) on the text map (4 to 5 stage, two texts side by side). Day 369 is the Language Dive on the sentence form (relative clauses with "which" and "while" for comparing). Day 371 gives the talk move for SI Inform (carried; owned in grade 4). Day 374 meets the second part, the second coquí text. The class builds an informative paragraph in a chosen structure with the teacher on day 372, students make an informative paragraph in the structure that fits, with precise words alone on day 378, the change of audience comes on day 379 (the progress report to the class, then the paragraph written for a forest visitors' guide), and the self-check page on day 380 asks how "which" packs two facts into one sentence.
- **Why this order.** the model is taken apart before it is built with the teacher, and built with the teacher before anyone makes it alone; talk comes before writing on every day; a form is taught on an Understanding day before a Fluency day practices it. 
- **Assessments.** No readiness check: day 368 retrieves g4-la-inform, g4-si-inform (last used the year before, so retrieval). End-of-unit assessment days 383 and 384: read two new short paragraphs and name each structure; report progress to the teacher; then write a paragraph, on two short paragraphs on one rainforest bird, Curio Class's own and unseen. A prompt per part of each id; look-fors at each entry point. Response time: respond day 385, counted once. No mid-unit assessment (19 days, not over 25).
- **Help withdrawn.** Entry points 5 and 6 after day 378; 3 and 4 from day 380; 1 and 2 lose the cloze before day 383.
- **Candidate: PRIME Depth.KLU, compared structures.** Kept, no day cost: day 374.
- **Candidate: Bar item 3, relative clauses at the sentence.** Kept, no day cost: day 369.
- **Sensitive ground.** El Yunque is in Puerto Rico, part of the United States; its people are named as the host names them; hurricanes are named only as the forest's. Agent reads with the unit plan: sensitivity; spanish.
- **Host-teacher note.** Content used: ELA unit 2's coquí texts and the forest pages. Language taught: compared structures, relative clauses with "which", "while" for comparing, a progress report summed up.

### Unit 21. Causes and a Constitution

*What led to it, and how does the plan share power?* band days 386 to 405 (grade 5 days 66 to 85, weeks 14 to 17); 20 days: 5 Understanding, 4 Fluency, 8 Application, 2 end-of-unit assessment days and 1 respond day. Key language use: explain. Rows: g5-ss-explain, g5-si-inform.

- **Host.** S.ocial studies grade 5 unit 5 (days 60 to 75), the Constitution, alongside to day 75, then just after; social studies grade 5 unit 3, the road to revolution, retrieved
- **Arc.** Day 386 opens on the question and names the key language use. Day 387 retrieves the year before's row, then takes the social studies page on the three branches apart (a structure of power, part by part, and causes weighed) on the cause chain (4 to 5 stage, one cause marked as mattering most). Day 388 is the Language Dive on the sentence form ("so that no one branch ___" for purpose, with "as a result" and "which caused"). Day 390 gives the talk move for SI Inform (review; carried, owned in grade 4). Day 393 meets the second part, the causes of the Revolution, from social studies unit 3. The class builds an explanation of what each branch does and why with the teacher on day 391, students make an explanation of the branches, and of the causes weighed in their own words alone on day 397, the change of audience comes on day 399 (explained to the group, then written as a museum label), and the self-check page on day 400 asks what "so that" tells about a purpose.
- **Why this order.** the model is taken apart before it is built with the teacher, and built with the teacher before anyone makes it alone; talk comes before writing on every day; a form is taught on an Understanding day before a Fluency day practices it. From day 76 the unit runs just after the host (host day 75), from its own pages and the class's chart.
- **Assessments.** No readiness check: day 387 retrieves g4-ss-explain (last used the year before, so retrieval); day 390 retrieves g5-si-inform through use. End-of-unit assessment days 403 and 404: read a new short page and order its chain; explain to the teacher; then write the explanation, on a short page on a made-up town charter that splits power three ways, Curio Class's own and unseen. A prompt per part of each id; look-fors at each entry point. Response time: respond day 405, counted once. No mid-unit assessment (20 days, not over 25). The end-of-unit record is carried unscored to the mid-year check.
- **Help withdrawn.** Entry points 5 and 6 after day 397; 3 and 4 from day 400; 1 and 2 lose the cloze before day 403.
- **Candidate: PRIME Breadth.ELD, explain on history.** Kept, no day cost: the whole unit.
- **Candidate: California 5.27, why noun groups like "taxation without representation" are hard, with a remedy.** Kept, no day cost: day 392.
- **Sensitive ground.** The Revolution is a war; violence is named plainly, never shown in detail. No student is asked about a war in a family's home country, or about citizenship. Agent reads with the unit plan: sensitivity; spanish.
- **Host-teacher note.** Content used: social studies unit 5's Constitution pages and unit 3's revolution causes. Language taught: "so that" for purpose, "which caused", noun groups unpacked, causes weighed.

#### Grade 5 mid-year check (band days 406 and 407, respond day 408; grade 5 days 86 to 88, week 18)

After unit 21, as the frame's Course-level checks table sets it. It samples units 18, 19 and 20 on new content; unit 21's end-of-unit record, taken just before, is carried unscored, so no item repeats that assessment. Day by day: Grade 5 mid-year check, day 1 (week 18): read a new two-scene story and say how the scenes join; read a new page and data on a plant, explain where its energy came from and say what the data supports; write a claim from the data with evidence and reasoning; students are heard one at a time recounting a project across days. Then read two new paragraphs on one topic and name each structure; write a paragraph in the structure that fits; groups give a progress report and another group sums it up while the teacher listens, and the last students give their recount. The respond day groups students by form and entry point and feeds any move between entry points.

### Unit 22. Decimals at work

*Why does each step fit the problem?* band days 409 to 425 (grade 5 days 89 to 105, weeks 18 to 21); 17 days: 5 Understanding, 3 Fluency, 6 Application, 2 end-of-unit assessment days and 1 respond day. Key language use: explain. Rows: g5-ma-explain, g5-si-explain.

- **Host.** M.ath grade 5 unit 7 (days 91 to 107), decimal operations, alongside from day 91; math grade 5 unit 4, fraction problems, retrieved
- **Arc.** Day 409 opens on the question and names the key language use. Day 410 retrieves the year before's row, then takes a worked decimal solution apart (a method in steps, each with its reason) on the cause chain (4 to 5 stage, as steps with reasons). Day 411 is the Language Dive on the sentence form ("This step fits because ___, which means ___"). Day 413 gives the talk move for SI Explain (carried; owned in grade 4). The class builds a decimal method explained step by step with reasons with the teacher on day 414, students make a decimal or fraction problem explained, and the group's choice alone on day 418, the change of audience comes on day 419 (explained to another group, then written as a how-to for a grade 4 class), and the self-check page on day 420 asks what "which means" adds after a step.
- **Why this order.** the model is taken apart before it is built with the teacher, and built with the teacher before anyone makes it alone; talk comes before writing on every day; a form is taught on an Understanding day before a Fluency day practices it. Days 89 and 90 come before math's decimal unit (host day 91), so they work the fraction problems, taught earlier (the frame's "If later" line).
- **Assessments.** No readiness check: day 410 retrieves g4-ma-explain, g4-si-explain (last used the year before, so retrieval). End-of-unit assessment days 423 and 424: read a new worked solution with one step out of place and fix the order; explain to the teacher; then write the steps with reasons, on a worked solution with one step out of place, Curio Class's own and unseen. A prompt per part of each id; look-fors at each entry point. Response time: respond day 425, counted once. No mid-unit assessment (17 days, not over 25).
- **Help withdrawn.** Entry points 5 and 6 after day 418; 3 and 4 from day 420; 1 and 2 lose the cloze before day 423.
- **Candidate: PRIME Depth.LE, why a step fits.** Kept, no day cost: day 411.
- **Candidate: California 5.25, a transfer note on the decimal comma.** Kept, no day cost: day 412, with the word cards.
- **Sensitive ground.** Money problems use school settings with no prices that rank families. Agent reads with the unit plan: sensitivity; spanish.
- **Host-teacher note.** Content used: math unit 7's decimal operations and unit 4's fraction problems. Language taught: "This step fits because ___, which means ___", a process explained and "why not" answered.

### Unit 23. Leading change

*Which reason supports which point, and so what?* band days 426 to 442 (grade 5 days 106 to 122, weeks 22 to 25); 17 days: 5 Understanding, 3 Fluency, 6 Application, 2 end-of-unit assessment days and 1 respond day. Key language use: argue. Rows: g5-la-argue, g5-si-argue.

- **Host.** E.LA grade 5 unit 3 (days 84 to 123), athletes who led change, its biography of Jackie Robinson and his 1949 testimony, alongside
- **Arc.** Day 426 opens on the question and names the key language use. Day 427 retrieves the year before's row, then takes one paragraph of the ELA unit's text where the author links a reason to its evidence apart (which reasons support which points) on the claim chart (4 to 5 stage). Day 428 is the Language Dive on the sentence form ("This shows ___. Therefore, ___." and "should" for a recommendation). Day 430 gives the talk move for SI Argue (carried; owned in grade 4). The class builds an opinion paragraph that links reasons to evidence with the teacher on day 431, students make an opinion paragraph with reasons linked to evidence alone on day 435, the change of audience comes on day 436 (the case made to the class, then the paragraph written for the school newsletter), and the self-check page on day 437 asks how "this shows" links evidence to a point.
- **Why this order.** the model is taken apart before it is built with the teacher, and built with the teacher before anyone makes it alone; talk comes before writing on every day; a form is taught on an Understanding day before a Fluency day practices it. 
- **Assessments.** No readiness check: day 427 retrieves g4-la-argue, g4-si-argue (last used the year before, so retrieval). End-of-unit assessment days 440 and 441: read a new short opinion and trace its reasons; make a case to the teacher; then write an opinion paragraph, on a short opinion on whether a school should name its gym for a local athlete, Curio Class's own and unseen. A prompt per part of each id; look-fors at each entry point. Response time: respond day 442, counted once. No mid-unit assessment (17 days, not over 25).
- **Help withdrawn.** Entry points 5 and 6 after day 435; 3 and 4 from day 437; 1 and 2 lose the cloze before day 440.
- **Candidate: PRIME Match.LE, linked reasons named.** Kept, no day cost: day 428.
- **Candidate: Bar item 13, argue returns harder.** Kept, no day cost: day 427 names what is harder than unit 14.
- **Sensitive ground.** Segregation and racism in the 1940s are named plainly, as the host does, and never role-played; no student argues for segregation in a "both sides" task. Agent reads with the unit plan: sensitivity; spanish.
- **Host-teacher note.** Content used: ELA unit 3's Jackie Robinson biography and testimony. Language taught: reasons linked to points with "this shows" and "therefore", "should", a case made for a plan.

### Unit 24. Bigger or smaller

*What happens when you scale, and how do we know?* band days 443 to 457 (grade 5 days 123 to 137, weeks 25 to 28); 15 days: 4 Understanding, 3 Fluency, 5 Application, 2 end-of-unit assessment days and 1 respond day. Key language use: argue. Rows: g5-ma-argue, g5-si-inform.

- **Host.** M.ath grade 5 unit 9 (days 119 to 134), scaling, alongside
- **Arc.** Day 443 opens on the question and names the key language use. Day 444 retrieves the year before's row, then takes two classmates' claims about multiplying by a fraction apart (a claim, an example, a conclusion and a critique) on the claim chart (4 to 5 stage). Day 445 is the Language Dive on the sentence form ("I claim ___. For example, ___. Therefore, ___." with "larger than" and "smaller than"). Day 447 gives the talk move for SI Inform (review; carried, owned in grade 4). The class builds a scaling claim with an example and "therefore" with the teacher on day 448, students make a scaling claim with a critique of another solution alone on day 451, the change of audience comes on day 452 (argued in the group, then written as a reply to a made-up classmate who thinks multiplying always makes bigger), and the self-check page on day 453 asks what a comparative does in a claim.
- **Why this order.** the model is taken apart before it is built with the teacher, and built with the teacher before anyone makes it alone; talk comes before writing on every day; a form is taught on an Understanding day before a Fluency day practices it. The row's shape-placement argument waits for math's hierarchy days (138 to 142) and comes back in unit 25, days 145 and 146. Tight at 15 days, before the year-end check: its Fluency days keep to the forms it owns, and the respond day carries the review forms.
- **Assessments.** No readiness check: day 444 retrieves g4-ma-argue (last used the year before, so retrieval); day 447 retrieves g5-si-inform through use. End-of-unit assessment days 455 and 456: read two new claims and say which holds; argue to the teacher; then write a claim with a critique, on two claims about scaling a recipe, Curio Class's own and unseen. A prompt per part of each id; look-fors at each entry point. Response time: respond day 457, counted once. No mid-unit assessment (15 days, not over 25). The end-of-unit record is carried unscored to the year-end check.
- **Help withdrawn.** Entry points 5 and 6 after day 451; 3 and 4 from day 453; 1 and 2 lose the cloze before day 455.
- **Candidate: PRIME Depth.LE, comparatives with their job in a claim.** Kept, no day cost: day 449.
- **Candidate: California 4.1, the grade 4 cloze withdrawn.** Kept, no day cost: day 443 removes it for entry points 3 and 4.
- **Sensitive ground.** Recipes use foods from several named cultures, none ranked. Agent reads with the unit plan: sensitivity.
- **Host-teacher note.** Content used: math unit 9's scaling. Language taught: a claim with "for example" and "therefore", comparatives, a critique, a progress report summed up.

#### Grade 5 year-end check (band days 458 and 459, respond day 460; grade 5 days 138 to 140, week 28)

After unit 24, as the frame's Course-level checks table sets it. It samples units 21, 22 and 23 on new content; unit 24's end-of-unit record, taken just before, is carried unscored, so no item repeats that assessment. Day by day: Grade 5 year-end check, day 1 (week 28): read a new page on a made-up charter and explain how it shares power; write the explanation; read a new decimal solution and say why a step fits; students are heard one at a time explaining a step and answering "why not ___?". Then read a new short opinion and trace its reasons to its points; write an opinion paragraph; groups make the case for a plan while the teacher listens, and the last students explain their step. The respond day groups students by form and entry point and feeds any move between entry points.

### Unit 25. Winning a right

*Do the sources agree, and what should we claim?* band days 461 to 480 (grade 5 days 141 to 160, weeks 29 to 32); 20 days: 5 Understanding, 3 Fluency, 9 Application, 2 end-of-unit assessment days and 1 respond day. Key language use: argue. Rows: g5-ss-argue, g5-si-narrate, g5-ma-argue.

- **Host.** S.ocial studies grade 5 unit 10 (days 147 to 160), researching civil rights, from day 147; social studies grade 5 unit 9 (days 127 to 142), after Reconstruction, just studied, for days 141 to 146; sourcing from social studies unit 3 retrieved
- **Arc.** Day 461 opens on the question and names the key language use. Day 462 retrieves the year before's row, then takes two sources from social studies unit 9 apart (a claim from two corroborated sources) on the claim chart (4 to 5 stage). Day 463 is the Language Dive on the sentence form ("Both sources show ___. For example, ___. Therefore, ___ should ___."). Day 464 gives the talk move for SI Narrate (review; carried, owned in grade 4). Day 467 meets the second part, two sources on one civil rights event from the research unit. The class builds a claim from corroborated sources with the teacher on day 469, students make a claim from research on a civil rights topic, answering another reading alone on day 472, the change of audience comes on day 473 (argued to the group, then written as part of the class's action letter), and the self-check page on day 474 asks what "both sources show" claims that "the source says" does not. Days 465 and 466 are the MA Argue return the frame places here: shape placements in the hierarchy defended with "every" and "some", after math teaches the hierarchy (math days 138 to 142), with an exit ticket on day 466 filed with unit 24's record.
- **Why this order.** the model is taken apart before it is built with the teacher, and built with the teacher before anyone makes it alone; talk comes before writing on every day; a form is taught on an Understanding day before a Fluency day practices it. 
- **Assessments.** No readiness check: day 462 retrieves g4-ss-argue (last used the year before, so retrieval); day 464 retrieves g5-si-narrate through use. End-of-unit assessment days 478 and 479: read two new short sources and say whether they agree; argue to the teacher; then write a claim from both, on two short sources on a made-up town's fight to open its library to all, Curio Class's own and unseen. A prompt per part of each id; look-fors at each entry point. Response time: respond day 480, counted once. No mid-unit assessment (20 days, not over 25). The end-of-unit record and the year's sheet go on to the grade 6 teacher.
- **Help withdrawn.** Entry points 5 and 6 after day 472; 3 and 4 from day 474; 1 and 2 lose the cloze before day 478.
- **Candidate: PRIME Breadth.ELD, argue on history.** Kept, no day cost: the whole unit.
- **Candidate: Bar item 13, narrate returns harder.** Kept, no day cost: day 464, a recount across days of source work.
- **Sensitive ground.** Jim Crow laws, segregation and violence against Black Americans are named plainly, as the host does; no role-play, no "both sides" task on rights. Civil rights struggles of Latino, Asian American and Native peoples are named where the host names them; no student is asked about discrimination they or their family have faced. Agent reads with the unit plan: sensitivity; spanish.
- **Host-teacher note.** Content used: social studies units 9 and 10, after Reconstruction and civil rights research; math unit 10's shape hierarchy. Language taught: corroboration with "both sources show", "should", "every" and "some" in a shape claim.

## Course-level checks

| Check | Band days | Week of its year | After unit | Samples | Ids sampled |
|---|---|---|---|---|---|
| Grade 3 mid-year | 93, 94; respond 95 | 19 | 5 | units 1 to 4 | LA.2-3.Inform.Interpretive, LA.2-3.Inform.Expressive, SS.2-3.Explain.Interpretive, SI.K-3.Inform, SI.K-3.Narrate, SS.2-3.Argue.Interpretive, SS.2-3.Argue.Expressive, SC.2-3.Explain.Interpretive, SS.2-3.Explain.Expressive, SI.K-3.Argue |
| Grade 3 year-end | 133, 134; respond 135 | 27 | 7 | units 4, 5 and 6 | SC.2-3.Explain.Interpretive, SC.2-3.Explain.Expressive, MA.2-3.Explain.Interpretive, MA.2-3.Explain.Expressive, SI.K-3.Explain, SC.2-3.Argue.Interpretive, SC.2-3.Argue.Expressive |
| Grade 4 mid-year | 232, 233; respond 234 | 15 | 12 | units 9, 10 and 11 | MA.4-5.Argue.Interpretive, SS.4-5.Argue.Interpretive, SS.4-5.Argue.Expressive, SI.4-12.Inform, LA.4-5.Inform.Interpretive, LA.4-5.Inform.Expressive, MA.4-5.Argue.Expressive, SI.4-12.Argue |
| Grade 4 year-end | 303, 304; respond 305 | 29 | 16 | units 12 to 15 | LA.4-5.Narrate.Interpretive, SC.4-5.Explain.Interpretive, SC.4-5.Explain.Expressive, SI.4-12.Narrate, LA.4-5.Argue.Interpretive, LA.4-5.Argue.Expressive, MA.4-5.Explain.Interpretive, MA.4-5.Explain.Expressive, SI.4-12.Explain |
| Grade 5 mid-year | 406, 407; respond 408 | 18 | 21 | units 18, 19 and 20 | LA.4-5.Narrate.Interpretive, SC.4-5.Explain.Interpretive, SC.4-5.Argue.Interpretive, SC.4-5.Argue.Expressive, SI.4-12.Narrate, LA.4-5.Inform.Interpretive, LA.4-5.Inform.Expressive, SI.4-12.Inform |
| Grade 5 year-end | 458, 459; respond 460 | 28 | 24 | units 21, 22 and 23 | SS.4-5.Explain.Interpretive, SS.4-5.Explain.Expressive, MA.4-5.Explain.Interpretive, MA.4-5.Explain.Expressive, SI.4-12.Explain, LA.4-5.Argue.Interpretive, LA.4-5.Argue.Expressive, SI.4-12.Argue |

Every owned id is sampled on a course-level check day except these, each named with the reason (sequence-write rule 3). The check weeks are fixed off the core check weeks (the frame's "Weeks"), so each year's last unit, and the unit just before each check, is assessed by its end-of-unit assessment, and that record and the sheet go on to the next teacher:

- Grade 3, MA.2-3.Argue.Interpretive: unit 7's record is carried unscored to the check after it; checked on its end-of-unit assessment, days 130 and 131.
- Grade 3, MA.2-3.Argue.Expressive: unit 7's record is carried unscored to the check after it; checked on its end-of-unit assessment, days 130 and 131.
- Grade 3, LA.2-3.Narrate.Interpretive: unit 8 follows the year-end check; checked on its end-of-unit assessment, days 158 and 159.
- Grade 3, LA.2-3.Narrate.Expressive: unit 8 follows the year-end check; checked on its end-of-unit assessment, days 158 and 159.
- Grade 5, LA.4-5.Narrate.Expressive: the check's 30 minutes hold the talk and one written task a day, and the frame's table names the interpretive items for this unit; checked on its end-of-unit assessment, days 339 and 340.
- Grade 5, SC.4-5.Explain.Expressive: the check's 30 minutes hold the talk and one written task a day, and the frame's table names the interpretive items for this unit; checked on its end-of-unit assessment, days 364 and 365.
- Grade 5, MA.4-5.Argue.Interpretive: unit 24's record is carried unscored to the check after it; checked on its end-of-unit assessment, days 455 and 456.
- Grade 5, MA.4-5.Argue.Expressive: unit 24's record is carried unscored to the check after it; checked on its end-of-unit assessment, days 455 and 456.
- Grade 5, SS.4-5.Argue.Interpretive: unit 25 follows the year-end check; checked on its end-of-unit assessment, days 478 and 479.
- Grade 5, SS.4-5.Argue.Expressive: unit 25 follows the year-end check; checked on its end-of-unit assessment, days 478 and 479.

Grade 4's carried content ids are sampled on its checks as practice toward grade 5, not as owner claims. A check never repeats a task form given in the two weeks before it (the grade 3 year-end habitat item asks for the claim in the student's own words, since unit 7 asked students to choose between two claims). Collect once: each check's talk task is heard once per student, about a minute each over the two days, with groups heard about two minutes each; no check sits within ten days of the end-of-unit talk record it would repeat, since that record is carried, not heard again. Minute budgets plan for 30 students.

## Newcomer strand

A 20-day on-ramp beside each year, outside its 160 days, taught in an added period with the ELD teacher (Cory, 2026-11-26, Desk q-frames-scope-1), with a short catch-up card set for the unit language missed. Grade 3 works the four SI K-3 ids and both LA 2-3 Inform ids; grades 4 and 5 work the four SI 4-12 ids and both LA 4-5 Inform ids. Content is the school day itself and the current host unit's pictures. It is not in days.csv. Its outline, the same in each year with that year's ids and routine:

| Strand days | Content | Ids worked | Look-for |
|---|---|---|---|
| 1 to 5 | Names, greetings, the room and its objects, asking for help ("Can you help me?", "Where is ___?") | SI Inform | asks for help with a frame |
| 6 to 10 | Routines and the timetable: what happens first, next and last in the school day | SI Narrate; SI Inform | tells the day in order with a time word |
| 11 to 15 | The year's talk routine with a partner on the current host unit's pictures; naming and grouping what is in a picture | SI Explain; LA Inform (both modes) | names a picture's main idea with the word bank |
| 16 to 20 | Agreeing and choosing ("I like ___ because ___"), then a short spoken and labeled piece on a host picture | SI Argue; LA Inform (both modes) | gives one reason; labels a picture |

A newcomer joins the class's current unit at entry points 1 and 2 when the teacher judges the strand's look-fors "seen" on two days in a row, or on the school's own check. A newcomer who needs letters and sounds uses the ELA K to 2 foundational rows with a note; ELD does not teach phonics. The strand and its family notes get their own sensitivity read before use, and no strand prompt asks how a student came, a family's status or whether English is spoken at home.

## Shorter path

- **A year about 10 days short.** Ten fold-in days a year, each a Fluency day that teaches nothing new, drafts nothing and holds no assessment: its rehearsal moves into the first five minutes of the next teaching day, and each saves 25 minutes net (the 30-minute lesson less the 5-minute opener). Every owned id keeps its teaching days and its end-of-unit assessment; the tight units (5, 9, 16, 17, 24) lose none.
  - Grade 3: day 8 (unit 1); day 14 (unit 1); day 18 (unit 1); day 29 (unit 2); day 47 (unit 3); day 66 (unit 4); day 104 (unit 6); day 122 (unit 7); day 143 (unit 8); day 149 (unit 8). Ten days, 250 minutes net; the year runs on 150 days.
  - Grade 4: day 186 (unit 10); day 192 (unit 10); day 203 (unit 11); day 207 (unit 11); day 210 (unit 11); day 221 (unit 12); day 225 (unit 12); day 243 (unit 13); day 260 (unit 14); day 277 (unit 15). Ten days, 250 minutes net; the year runs on 150 days.
  - Grade 5: day 328 (unit 18); day 334 (unit 18); day 349 (unit 19); day 354 (unit 19); day 375 (unit 20); day 394 (unit 21); day 398 (unit 21); day 416 (unit 22); day 433 (unit 23); day 471 (unit 25). Ten days, 250 minutes net; the year runs on 150 days.
- **A shorter period** (20 minutes in place of 30): every day keeps the talk and the form; on an Application day the written part finishes in the next day's first ten minutes, and the exit ticket moves to the next day's opener; end-of-unit and course-level check days keep their reading and writing parts whole and spread the talk task over the respond day as well.
- **A left-out unit** (STANDARD.md section 3, the shared leave-out and swap rule): the course page and the unit's family note name the ids not claimed that year. Where a later unit uses a model card a left-out unit carried (the cause chain, claim chart, text map or story map at its stage), that later unit teaches the card's one-step form in its first ten minutes and claims none of the left-out unit's parts (the leave-out bridge rule, DESK-ANSWERS 2026-11-26). A swapped host text keeps the unit's ids met. A family may ask for the other text where a host is about migration, war or loss (unit 18 names it).
- **The newcomer strand** sits outside the 160 days, in its added period, so no shorter path cuts it.

## Sources and what is not loaded

- The host units' texts and records are the host courses' own (credited there); ELD names the page or passage each unit takes apart and writes its own scaffolds and each end-of-unit assessment's new content, searched first in docs/ and data/ so it is unseen. The Language Dive routine is adapted from EL Education K-5 Language Arts, 2017 edition (CC BY 4.0), credited on each day that uses it. No base text and no source map (the frame: no open ELD course exists).
- Not loaded: the printed expectation lists of the WIDA ELD Standards Framework, 2020 edition. Every owned id's parts were planned from data/standards/wida-2020.txt and the frame (frame, For the lead item 7); the days that name an id's parts in our words (units 7 and 23) lean on that unloaded check, and the whole course's "every part of every id" claim waits on it.

## For the lead

1. **The C11 gate.** STANDARD.md section 6 and the frame's For the lead item 1 say the scope and sequence waits until C11 passes in two core subjects' probe and guard units. This scope was written on the lead's 2026-11-26 brief ("do the rest of the scopes and sequences"); the unit plans, days and newcomer strand still wait for the gate. Cory or the lead should confirm the brief lifts the gate for scopes, and record it.
2. **Frame "None" cells.** Units 10, 14, 15, 16 and 17 have "None" in Owned standards (grade 4 owns only the SI 4-12 ids), so sequence.py prints "standard None is on no day" for each. A frame fix (an empty cell, or the carried ids marked `~`) would clear the notes; nothing is missing.
3. **Expectation lists (frame item 7).** Applying the second-model read's function list per unit waits for the printed lists. When they are loaded, the added functions fit inside the existing days (the Language Dive, W and self-check days carry them); no unit changes length.
4. **Mid-year checks sample a unit's row before its owner unit only once:** grade 3's mid-year talk hears SI K-3 Narrate, taught in unit 2 as the frame's review use before unit 8 owns it. It is taught on band day 24 first, so the check claims only what a day taught.

## Not done here

Item writing, answer keys, section plans and the newcomer strand's days come with the unit plans (PRODUCTION-PATH step 4).

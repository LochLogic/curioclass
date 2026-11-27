# Scope and sequence: English Language Development, grades 9 to 12

> **Held on C11 (Cory 2026-11-26, Desk q-eld-scope-1).** A draft, written before the ELD C11 gate passed (docs/courses/eld/STANDARD.md section 6). It has had no expert read or fix pass; the read, fix, unit plans and days wait until C11 passes, and the read then runs on this draft.

Course `english-language-development-grades-9-to-12` (catalog id `eld-9-12`), grades 9 to 12, a band course of four grade years; draft 2026-11-26. 640 course days, 160 a year: one 45-minute protected ELD period a day, five a week, 32 weeks (data/plans/frames.csv). The days live in data/plans/english-language-development-grades-9-to-12/days.csv; this page holds the judgment. It changes none of the frame's 36 units, owned rows or day counts.

## How to read the days

- **Years and day numbers.** Grade 9 is course days 1 to 160, grade 10 days 161 to 320, grade 11 days 321 to 480, grade 12 days 481 to 640. The `day` column runs 1 to 640; every other day number on this page and in the notes is a day of the year, as the frame gives them (grade 10 day 84 is course day 244). Host course days are the host's own.
- **school_day.** The course meets every school day, so `school_day` = day - 160 x (grade - 9), filled on every row, and week = (school_day - 1) // 5 + 1 within the year. Every check falls in the weeks the frame and the table at the end of docs/courses/CALENDAR.md give: weeks 17 and 32 in grades 9, 10 and 11, weeks 16 and 32 in grade 12. Grades 9 to 12 have no stagger rule but the finals week (CALENDAR.md rule 4), and week 32 is the finals week.
- **Standards.** English language development standards (WIDA 2020, data/standards/wida-2020.txt), ids and our own words only. Grade 12 owns the 18 cluster 9-12 ids (LA Narrate, Inform and Argue; MA, SC and SS Explain and Argue, each Interpretive and Expressive). Grades 9, 10 and 11 carry the same ids ("carried; owned in grade 12"), and the `codes` column lists them on the days that work them, in the same form. Every year carries the four SI 4-12 ids, owned in grade 4. A day lists the Interpretive id where students listen, read or view, and the Expressive id where they speak, write or label a diagram.
- **Every day.** Each lesson has structured talk with frames before any writing, in the year's one talk routine (grade 9 'point, build, ask', grade 10 'point, source, sum up', grade 11 'point, objection, answer', grade 12 'propose, concede, hold'), taught in week 1 of the year's first unit. Each day ends with an exit ticket a student cannot pass without the day's form (one or two sentences, said or written), seen against two or three look-fors on the teacher's paper sheet (seen or not yet). No scores are stored.
- **Kinds** follow GLOSSARY "teaching day" and APPROACH "Kinds of day in ELD": Understanding first shows a form, a text's structure, a model or a talk move; Fluency is oral rehearsal, sentence combining and word work on forms already shown, and drafts nothing; Application uses the forms in talk and then writing (every day that drafts, revises or reads a second text with the forms is Application); Check is an end-of-unit or course-level check day; Respond reteaches what the sheet shows not yet. Fluency is 103 of the 532 teaching days, about a fifth, as the frame asks for high school.
- **Entry points.** Three (levels 1 and 2, 3 and 4, 5 and 6), the same task on the same content at each, help changed, never the task. Help comes off on named days in every unit: levels 5 and 6 lose the sentence frame after the first independent piece (the day the note names); levels 3 and 4 lose it on the self-check day, before the end-of-unit task; levels 1 and 2 keep the word bank and lose the cloze on that same day. Each year's rows remove one more frame for levels 3 and 4, so in grade 12 they work from the model alone from day 1 of every unit. Newcomer, long-term English learner and English learner with disabilities notes come with each unit plan (bar item 5); the teacher page carries the line on telling a language need from a learning need.
- **Base text and sources.** No base text and no source map (the frame: ELD places no base units). Texts are the host units' own; EL Education's Language Dive routine (K-5 Language Arts, 2017 edition, CC BY 4.0) is credited on each day that uses it. Sources a day leans on that are not loaded: the WIDA framework's printed 9-12 pages (the owner-year parts named on grade 12 days are the frame's reading, For the lead below); the Chronicling America report for unit 24 (named below, not opened); and every "Curio Class's own" unseen text, which the unit plan writes and checks unused in docs/ and data/ (section plans and items.csv too) before it is written in.
- **Home language and families.** Talk or plan in the home language before English, cognates and false friends on the word cards, Spanish notes first (APPROACH "Home languages"). Every unit sends a family note in English and Spanish before day 1; a student 18 or over gets it themselves. No student translates for another, the class or a family.
- **Paper path.** Every day runs on paper, cards and talk; the optional replay tool, word deck and passage audio each have the teacher reading aloud twice beside them. No tool records a voice or writing.

## Earlier rows and how each opens (rule 2)

Counted by grade number. Every row a unit assumes was last taught the year before (grade 8 for grade 9, in English Language Development, grades 6 to 8, units 18 to 26) or earlier the same year, so each opens as a retrieval task inside a day and no unit needs a readiness check (none is placed). The ten-minute retrieval task sits on each unit's second day, after day 1's hook; the `retrieves` column names the rows. Each unit's first Fluency day on sentence combining also spends three minutes on the form of the unit before (practice that returns, also in `retrieves`). A student who joins without the earlier year meets the retrieval task at entry points 1 and 2 with the earlier model on the card; a newcomer takes the strand first.

| Row | Last taught | Opens in | Day (of the year) | Treatment |
|---|---|---|---|---|
| g8-la-narrate | grade 8 | unit 1 | 2 | retrieval (the year before) |
| g8-si-narrate | grade 8 | unit 1 | 2 | retrieval (the year before) |
| g8-sc-explain | grade 8 | unit 2 | 26 | retrieval (the year before) |
| g8-si-explain | grade 8 | unit 2 | 26 | retrieval (the year before) |
| g9-sc-explain | grade 9 | unit 3 | 44 | retrieval (earlier this year) |
| g8-sc-argue | grade 8 | unit 4 | 62 | retrieval (the year before) |
| g8-si-argue | grade 8 | unit 4 | 62 | retrieval (the year before) |
| g9-sc-argue | grade 9 | unit 5 | 85 | retrieval (earlier this year) |
| g9-ma-argue | grade 9 | unit 6 | 101 | retrieval (earlier this year) |
| g8-la-inform | grade 8 | unit 7 | 118 | retrieval (the year before) |
| g8-si-inform | grade 8 | unit 7 | 118 | retrieval (the year before) |
| g9-si-explain | grade 9 | unit 8 | 133 | retrieval (earlier this year) |
| g9-la-inform | grade 9 | unit 9 | 146 | retrieval (earlier this year) |
| g9-sc-explain | grade 9 | unit 10 | 2 | retrieval (the year before) |
| g9-si-explain | grade 9 | unit 10 | 2 | retrieval (the year before) |
| g9-si-inform | grade 9 | unit 10 | 5 | retrieval inside the SI review day (the year's own row comes later) |
| g9-ss-explain | grade 9 | unit 11 | 18 | retrieval (the year before) |
| g9-ma-argue | grade 9 | unit 12 | 32 | retrieval (the year before) |
| g9-la-narrate | grade 9 | unit 13 | 48 | retrieval (the year before) |
| g9-si-narrate | grade 9 | unit 13 | 48 | retrieval (the year before) |
| g9-la-argue | grade 9 | unit 14 | 64 | retrieval (the year before) |
| g9-si-argue | grade 9 | unit 14 | 64 | retrieval (the year before) |
| g9-ma-explain | grade 9 | unit 15 | 85 | retrieval (the year before) |
| g9-si-explain | grade 9 | unit 15 | 85 | retrieval (the year before) |
| g10-ma-argue | grade 10 | unit 16 | 102 | retrieval (earlier this year) |
| g9-la-inform | grade 9 | unit 17 | 120 | retrieval (the year before) |
| g9-si-inform | grade 9 | unit 17 | 120 | retrieval (the year before) |
| g9-ss-argue | grade 9 | unit 18 | 142 | retrieval (the year before) |
| g10-la-narrate | grade 10 | unit 19 | 2 | retrieval (the year before) |
| g10-si-narrate | grade 10 | unit 19 | 2 | retrieval (the year before) |
| g10-la-inform | grade 10 | unit 20 | 18 | retrieval (the year before) |
| g10-si-inform | grade 10 | unit 20 | 18 | retrieval (the year before) |
| g10-sc-explain | grade 10 | unit 21 | 36 | retrieval (the year before) |
| g10-si-explain | grade 10 | unit 21 | 36 | retrieval (the year before) |
| g10-si-explain | grade 10 | unit 21 | 39 | retrieval inside the SI review day (the year's own row comes later) |
| g10-la-argue | grade 10 | unit 22 | 50 | retrieval (the year before) |
| g10-si-argue | grade 10 | unit 22 | 50 | retrieval (the year before) |
| g10-ss-explain | grade 10 | unit 23 | 64 | retrieval (the year before) |
| g10-si-explain | grade 10 | unit 23 | 64 | retrieval (the year before) |
| g10-ss-argue | grade 10 | unit 24 | 85 | retrieval (the year before) |
| g10-sc-argue | grade 10 | unit 25 | 98 | retrieval (the year before) |
| g10-ma-explain | grade 10 | unit 26 | 112 | retrieval (the year before) |
| g10-ma-argue | grade 10 | unit 27 | 134 | retrieval (the year before) |
| g11-la-narrate | grade 11 | unit 28 | 2 | retrieval (the year before) |
| g11-si-narrate | grade 11 | unit 28 | 2 | retrieval (the year before) |
| g11-ss-explain | grade 11 | unit 29 | 18 | retrieval (the year before) |
| g11-si-explain | grade 11 | unit 29 | 21 | retrieval inside the SI review day (the year's own row comes later) |
| g11-sc-explain | grade 11 | unit 30 | 35 | retrieval (the year before) |
| g11-si-inform | grade 11 | unit 30 | 38 | retrieval inside the SI review day (the year's own row comes later) |
| g11-ma-explain | grade 11 | unit 31 | 51 | retrieval (the year before) |
| g11-si-explain | grade 11 | unit 31 | 51 | retrieval (the year before) |
| g11-ss-argue | grade 11 | unit 32 | 66 | retrieval (the year before) |
| g11-si-argue | grade 11 | unit 32 | 66 | retrieval (the year before) |
| g11-la-inform | grade 11 | unit 33 | 82 | retrieval (the year before) |
| g11-si-inform | grade 11 | unit 33 | 82 | retrieval (the year before) |
| g11-ma-argue | grade 11 | unit 34 | 102 | retrieval (the year before) |
| g11-sc-argue | grade 11 | unit 35 | 120 | retrieval (the year before) |
| g11-la-argue | grade 11 | unit 36 | 138 | retrieval (the year before) |

Host rows the frame retrieves (bio-dna-to-protein, alg1-correlation-causation, wh1-geography-shapes-contact and the rest named in each unit) are retrieved on the same day 2, in the note; they are other courses' rows, so they are not in the `retrieves` column.

## Grade 9 (course days 1 to 160)

Grade 9 carries the 18 cluster 9-12 ids for the first time and moves every model from the 6 to 8 stage to the 9 to 12 stage. Its hosts: ELA grade 9, Algebra I, Biology and World History I. Talk routine: 'point, build, ask'.

| Unit | Days of the year | Course days | Weeks | Key language use | Ids (cluster 9-12) | Kinds U/F/A/C/R |
|---|---|---|---|---|---|---|
| 1. Telling it out of order | 1 to 24 | 1 to 24 | 1 to 5 | narrate | LA Narrate (both modes), carried | 6/5/10/2/1 |
| 2. Code and energy | 25 to 42 | 25 to 42 | 5 to 9 | explain | SC Explain (both modes), carried | 5/3/7/2/1 |
| 3. Showing each step | 43 to 60 | 43 to 60 | 9 to 12 | explain | MA Explain (both modes), carried | 4/3/8/2/1 |
| 4. Moose, wolves and evidence | 61 to 80 | 61 to 80 | 13 to 16 | argue | SC Argue (both modes), carried | 6/3/8/2/1 |
| 5. Steady or snowballing | 84 to 99 | 84 to 99 | 17 to 20 | argue | MA Argue (both modes), carried | 4/2/7/2/1 |
| 6. Judging the case for later start times | 100 to 116 | 100 to 116 | 20 to 24 | argue | LA Argue (both modes), carried | 4/2/8/2/1 |
| 7. How an idea unfolds | 117 to 131 | 117 to 131 | 24 to 27 | inform | LA Inform (both modes), carried | 5/2/5/2/1 |
| 8. New ways of knowing | 132 to 144 | 132 to 144 | 27 to 29 | explain | SS Explain (both modes), carried | 3/2/5/2/1 |
| 9. Where power comes from | 145 to 157 | 145 to 157 | 29 to 32 | argue | SS Argue (both modes), carried | 3/2/5/2/1 |

### Unit 1. Telling it out of order (days 1 to 24, weeks 1 to 5)

*How does a writer move a story through time, and how do we tell one event two ways?* Host: ELA grade 9 unit 1's suspense stories (ELA days 1 to 22). Ids: WIDA.ELD-LA.9-12.Narrate, Interpretive and Expressive (carried; owned in grade 12); SI: g9-si-narrate (the unit's own SI row).

**Arc.** Day 1 hooks on the question and names narrate openly (what it is for, where the host asks for it, its stages). Day 2 opens with the retrieval task, then takes apart one passage of 'The Cask of Amontillado' (1846), told by a narrator looking back. Day 3 is a Language Dive on past and past perfect against the narrator's present ('Even now, ___. Back then, ___.'), and day 6 adds reflective 'looking back, I'. Day 5 teaches the SI move (recount one event (orientation day, a team meeting) for a peer and then for an adult, and say what changed). Day 7 builds a narrative scene with one time shift with the teacher; day 10 is the first independent piece; day 9 reads the opening of 'The Monkey's Paw' from the same ELA unit, read for where its time moves; day 14 applies the forms to it; day 13 is a seminar on the host content. Day 15 changes the audience (the event told to a peer, then the same event told to an adult), and day 21 is the talk-about-language and self-check day (what 'had' does to time).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed. On the host calendar: Day 9: If later: ELA's narrative writing opens on ELA day 23, so the scene uses ELD's own frame and model scene; the Odyssey is not used. Longer units (here 24 days) add a second host passage, a stage-labeling day, a seminar and peer reading, by the row's load (an LA row weighs most).

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 2). No mid-unit assessment (24 days, not over 25). End-of-unit assessment on days 22 and 23: the interpretive part on a new short passage with a flashback, invented by Curio Class for practice: mark where time shifts; the talk task (recount a new event for a named adult), heard in seminars of three; the writing task, a scene with one time shift. Response time: respond day 24.

**Candidate cells.** California 1.26, all four domains in the unit: kept, 0 added days (listening and reading day 2, speaking day 5, writing day 10). PRIME Match.LE, one interpretive item on the new passage: kept, 0 added days (day 22).

**Sensitive ground and home language.** Sensitive: the host stories hold a murder and a son's death; the family note (English and Spanish) previews loss and how to ask for another story; ELD uses the Poe passage for its structure, not its crime. Own-story prompts: an invented character or a chosen place is always allowed. Home language: cognates for the word cards; the home language is never wrong, the task is choosing for the listener. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, ELA grade 9 unit 1's suspense stories (ELA days 1 to 22); language taught, narrate with past and past perfect against the narrator's present ('Even now, ___. Back then, ___.') and reflective 'looking back, I'.

### Unit 2. Code and energy (days 25 to 42, weeks 5 to 9)

*How does a cell's structure explain what it does?* Host: Biology unit 3's photosynthesis pages (Biology days 26 to 43). Ids: WIDA.ELD-SC.9-12.Explain, Interpretive and Expressive (carried; owned in grade 12); SI: g9-si-explain (the unit's own SI row).

**Arc.** Day 25 hooks on the question and names explain openly (what it is for, where the host asks for it, its stages). Day 26 opens with the retrieval task, then takes apart a short labeled explanation from the biology pages (the order of DNA bases to a protein; chloroplasts to stored sugar). Day 27 is a Language Dive on cause verbs (codes for, results in) and hedging (may, suggests), and day 30 adds dense noun groups ('the sequence of bases in the gene'). Day 29 teaches the SI move (explain one's own reasoning in seminar ('My reasoning was that ___, which suggests ___') and ask a partner what led to theirs). Day 31 builds an explanation of one mechanism on a cause chain, citing the class's seedling data and naming one limit with the teacher; day 34 is the first independent piece; day 33 reads Biology unit 2's DNA model (retrieved) beside the chloroplast diagram; day 37 applies the forms to it; day 36 is a seminar on the host content. Day 38 changes the audience (the mechanism explained to a classmate, then the same mechanism written as a caption for a hallway poster), and day 39 is the talk-about-language and self-check day (how 'may' and 'suggests' change what the writer claims).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed.

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 26). No mid-unit assessment (18 days, not over 25). End-of-unit assessment on days 40 and 41: the interpretive part on a new labeled diagram of a cell process not studied (Curio Class's own): order its steps; the talk task (explain one step in a seminar), heard in seminars of three; the writing task, the written explanation of the step. Response time: respond day 42.

**Candidate cells.** PRIME Depth.ELD, a cause verb taught as a feature with a job: kept, 0 added days (day 27). Bar item 4, asking a partner to explain: kept, 0 added days (day 29, the reasoning-turn day).

**Sensitive ground and home language.** No task asks about a student's own body or health. Home language: proteína and protein, estructura and structure are cognates. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, Biology unit 3's photosynthesis pages (Biology days 26 to 43); language taught, explain with cause verbs (codes for, results in) and hedging (may, suggests) and dense noun groups ('the sequence of bases in the gene').

### Unit 3. Showing each step (days 43 to 60, weeks 9 to 12)

*Why is each step of a solution true, and what does the line tell us?* Host: Algebra I unit 2's equations (its last days) and unit 3's fitted lines (Algebra I days 18 to 59). Ids: WIDA.ELD-MA.9-12.Explain, Interpretive and Expressive (carried; owned in grade 12); SI: g9-si-narrate (an SI review use).

**Arc.** Day 43 hooks on the question and names explain openly (what it is for, where the host asks for it, its stages). Day 44 opens with the retrieval task, then takes apart a worked solution of a linear equation from the Algebra I pages. Day 45 is a Language Dive on 'Since ___, it follows that ___', and day 48 adds 'The intercept means ___' and 'The slope tells us ___'. Day 47 uses again the SI move (recount, in order, how a group solved a problem, for an adult who was not there). Day 49 builds a step-by-step justification, and what a fitted line's slope and intercept mean in the data's own words with the teacher; day 52 is the first independent piece; day 51 reads Algebra I unit 3's fitted line on a class data set; day 55 applies the forms to it; day 54 is a seminar on the host content. Day 56 changes the audience (a solution explained to a partner, then the same solution written for a student who was absent), and day 57 is the talk-about-language and self-check day (what 'therefore' and 'it follows that' promise the reader).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed. On the host calendar: Day 47: From here the fitted lines of Algebra I unit 3 (days 47 to 59) run alongside.

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 44). No mid-unit assessment (18 days, not over 25). End-of-unit assessment on days 58 and 59: the interpretive part on a new worked solution with one unjustified step: supply the reason; the talk task (explain the slope of a new fitted line in a seminar), heard in seminars of three; the writing task, the written justification. Response time: respond day 60.

**Candidate cells.** PRIME Match.ELD.2-5, the math standard's own key language use: kept, 0 added days (days 43 to 45). Bar item 3, the sentence dimension ('since, it follows that'): kept, 0 added days (day 45).

**Sensitive ground and home language.** Numbers and methods stay within Algebra I units 2 and 3. Home language: equivalente and equivalent, operación inversa and inverse operation are cognates; a student may talk the steps through in the home language first. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, Algebra I unit 2's equations (its last days) and unit 3's fitted lines (Algebra I days 18 to 59); language taught, explain with 'Since ___, it follows that ___' and 'The intercept means ___' and 'The slope tells us ___'.

### Unit 4. Moose, wolves and evidence (days 61 to 80, weeks 13 to 16)

*What has kept the island's moose from eating everything, and how sure can we be?* Host: Biology unit 5's island moose and wolf surveys (Biology days 58 to 75). Ids: WIDA.ELD-SC.9-12.Argue, Interpretive and Expressive (carried; owned in grade 12); SI: g9-si-argue (the unit's own SI row).

**Arc.** Day 61 hooks on the question and names argue openly (what it is for, where the host asks for it, its stages). Day 62 opens with the retrieval task, then takes apart two short claims about why the moose population held or crashed. Day 63 is a Language Dive on concession ('Although ___, the evidence suggests ___'), and day 66 adds hedging modals (may, might) and 'That changes my view because ___'. Day 65 teaches the SI move (in seminar, state a view, build on or question others, and change one's view when given a good reason). Day 67 builds a claim argued from several lines of the island data (moose counts, wolf counts, winter severity), with one limitation of the surveys and an answered rebuttal with the teacher; day 70 is the first independent piece; day 69 reads the winter severity record beside the wolf counts; day 74 applies the forms to it; day 73 is a seminar on the host content. Day 75 changes the audience (the claim argued in seminar, then the same claim written as a short letter to a park ranger), and day 77 is the talk-about-language and self-check day (how 'may' and 'clearly' change a claim's strength).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed. Longer units (here 20 days) add a second host passage, a stage-labeling day, a seminar and peer reading, by the row's load (an LA row weighs most).

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 62). No mid-unit assessment (20 days, not over 25). End-of-unit assessment on days 78 and 79: the interpretive part on a new two-species data set (Curio Class's own, invented for practice): pick the claim it supports; the talk task (argue a claim in a seminar), heard in seminars of three; the writing task, the claim written with a limit. Response time: respond day 80.

**Candidate cells.** Bar item 10, a change of purpose (seminar to letter): kept, 0 added days (day 75, the change-of-audience day). PRIME Breadth.KLU, the year's first argue: kept, 0 added days (days 61 to 80).

**Sensitive ground and home language.** No task asks about hunting or a family's land use. If later: common ancestry (Biology unit 7) is not taught yet, so the unit argues about ecosystem stability only, and the host-teacher note tells biology the claim chart is ready for its unit 7. Home language: limitación and limitation are cognates; a view may be planned in the home language first. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, Biology unit 5's island moose and wolf surveys (Biology days 58 to 75); language taught, argue with concession ('Although ___, the evidence suggests ___') and hedging modals (may, might) and 'That changes my view because ___'.

### Unit 5. Steady or snowballing (days 84 to 99, weeks 17 to 20)

*Does the data show a cause, and is it growing by steps or by percents?* Host: Algebra I unit 5's linear and exponential growth (Algebra I days 84 to 107). Ids: WIDA.ELD-MA.9-12.Argue, Interpretive and Expressive (carried; owned in grade 12); SI: g9-si-argue (an SI review use).

**Arc.** Day 84 hooks on the question and names argue openly (what it is for, where the host asks for it, its stages). Day 85 opens with the retrieval task, then takes apart two claims about one data set from the Algebra I pages. Day 86 is a Language Dive on 'The data shows ___, but it does not prove ___', and day 89 adds concession and hedging on a data claim. Day 88 uses again the SI move (build on a partner's claim in seminar and question it). Day 90 builds a claim argued from a table and graph, with a critique of another claim using the definitions with the teacher; day 93 is the first independent piece; day 92 reads a second table that grows by a constant ratio; day 94 applies the forms to it. Day 95 changes the audience (the claim to a partner, then the same claim written as a reply to a news headline that overclaims), and day 96 is the talk-about-language and self-check day (why 'does not prove' is stronger than 'is not true').

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed.

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 85). No mid-unit assessment (16 days, not over 25). End-of-unit assessment on days 97 and 98: the interpretive part on a new table and two claims: judge which the data supports; the talk task (argue in a seminar), heard in seminars of three; the writing task, the claim and a critique. Response time: respond day 99.

**Candidate cells.** PRIME Breadth.LE, argue on a second content standard: kept, 0 added days (days 84 to 99). Bar item 13, argue returns harder: kept, 0 added days (the SI review day names what is harder).

**Sensitive ground and home language.** Data sets are invented for practice or from the host; numbers stay within Algebra I units 3 and 5. Home language: correlación and correlation, causalidad and causation are cognates. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, Algebra I unit 5's linear and exponential growth (Algebra I days 84 to 107); language taught, argue with 'The data shows ___, but it does not prove ___' and concession and hedging on a data claim.

### Unit 6. Judging the case for later start times (days 100 to 116, weeks 20 to 24)

*Is the argument for a later school start a strong one?* Host: ELA grade 9 unit 6's op-ed and government page on teen sleep (ELA days 100 to 116). Ids: WIDA.ELD-LA.9-12.Argue, Interpretive and Expressive (carried; owned in grade 12); SI: g9-si-argue (an SI review use).

**Arc.** Day 100 hooks on the question and names argue openly (what it is for, where the host asks for it, its stages). Day 101 opens with the retrieval task, then takes apart one paragraph of the unit's op-ed or government page on teen sleep. Day 102 is a Language Dive on concession ('Although ___, ___'), and day 105 adds hedging modals (may, might) and a precise claim. Day 104 uses again the SI move (disagree politely in seminar and give the reason). Day 106 builds one argument paragraph with a precise claim and an answered counterclaim with the teacher; day 109 is the first independent piece; day 108 reads the second source in ELA's sleep unit; day 111 applies the forms to it; day 110 is a seminar on the host content. Day 112 changes the audience (the paragraph written for the class, then the same paragraph cut to a two-sentence comment to the school board), and day 113 is the talk-about-language and self-check day (aunque and although are not cognates, so the word card carries the word).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed.

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 101). No mid-unit assessment (17 days, not over 25). End-of-unit assessment on days 114 and 115: the interpretive part on a new short opinion piece on a school schedule question (Curio Class's own): mark its claim and a weak reason; the talk task (argue in a seminar), heard in seminars of three; the writing task, the argument paragraph. Response time: respond day 116.

**Candidate cells.** Bar item 12, students judge their own claim's precision on the self-check: kept, 0 added days (day 113, the self-check day).

**Sensitive ground and home language.** Teen sleep: no task asks about a student's own sleep, work hours or home. Home language: aunque and although are not cognates; the word card carries although. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, ELA grade 9 unit 6's op-ed and government page on teen sleep (ELA days 100 to 116); language taught, argue with concession ('Although ___, ___') and hedging modals (may, might) and a precise claim.

### Unit 7. How an idea unfolds (days 117 to 131, weeks 24 to 27)

*How did Darwin's island birds come to differ, and how does the writer build the explanation?* Host: ELA grade 9 unit 7's island birds texts (ELA days 117 to 130). Ids: WIDA.ELD-LA.9-12.Inform, Interpretive and Expressive (carried; owned in grade 12); SI: g9-si-inform (the unit's own SI row).

**Arc.** Day 117 hooks on the question and names inform openly (what it is for, where the host asks for it, its stages). Day 118 opens with the retrieval task, then takes apart one passage of the unit's Darwin or US government text where an idea unfolds. Day 119 is a Language Dive on relative and contrast clauses ('which', 'whereas'), and day 122 adds nominalization ('the development of the beak'). Day 121 teaches the SI move (sum up a seminar's main points for a classmate who missed it, and ask a teacher for information in a formal register ('I was wondering whether ___')). Day 123 builds one analytical paragraph that traces how an idea develops with the teacher; day 125 is the first independent piece; day 126 applies the forms to it. Day 127 changes the audience (the seminar summed up aloud for one classmate, then the same summary written as a note to the teacher), and day 128 is the talk-about-language and self-check day (what 'whereas' does that 'but' does not).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed.

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 118). No mid-unit assessment (15 days, not over 25). End-of-unit assessment on days 129 and 130: the interpretive part on a new short informational passage on another island species (Curio Class's own, from public sources): trace its idea; the talk task (sum up a short seminar), heard in seminars of three; the writing task, the analytical paragraph. Response time: respond day 131.

**Candidate cells.** Bar item 3, the text, sentence and word dimensions in one unit: kept, 0 added days (days 118 to 119). PRIME Depth.LE: kept, 0 added days (both modes on the same passage, days 118 and 125).

**Sensitive ground and home language.** Species threats are read as context only. Home language: seminario and seminar, analizar and analyze are cognates; notes in any language. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, ELA grade 9 unit 7's island birds texts (ELA days 117 to 130); language taught, inform with relative and contrast clauses ('which', 'whereas') and nominalization ('the development of the beak').

### Unit 8. New ways of knowing (days 132 to 144, weeks 27 to 29)

*What made the Scientific Revolution happen when and where it did?* Host: World History I unit 9's Scientific Revolution (World History I days 126 to 137). Ids: WIDA.ELD-SS.9-12.Explain, Interpretive and Expressive (carried; owned in grade 12); SI: g9-si-explain (an SI review use).

**Arc.** Day 132 hooks on the question and names explain openly (what it is for, where the host asks for it, its stages). Day 133 opens with the retrieval task, then takes apart a short sourced account of one discovery of the 1600s. Day 134 is a Language Dive on 'In the context of ___, ___ contributed to ___. This may ___.', with weighing words (most, mainly) with a reason beside it. Day 136 uses again the SI move (explain in seminar why one factor counts most). Day 137 builds an explanation of the change on a weighted cause chain, citing sources and naming a limit with the teacher; day 139 is the first independent piece. Day 140 changes the audience (the explanation to a partner, then the same explanation written as a museum label), and day 141 is the talk-about-language and self-check day (how 'mainly' changes a list into a ranking).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed. Tight at 13 days (the frame): Fluency stays on the forms the unit owns, and review forms go to the respond day.

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 133). No mid-unit assessment (13 days, not over 25). End-of-unit assessment on days 142 and 143: the interpretive part on a new short account of one discovery (Curio Class's own, sourced): weigh its factors; the talk task (explain in a seminar), heard in seminars of three; the writing task, the written explanation. Response time: respond day 144.

**Candidate cells.** PRIME Breadth.LE, explain on the social studies standard: kept, 0 added days (days 132 to 144).

**Sensitive ground and home language.** Sensitive: the geography host is about migration and conquest, so the unit leads with the Scientific Revolution and retrieves geography only as routes of ideas; no student is asked about their own family's movement; the family note previews the topic. Home language: contexto and context, revolución and revolution are cognates. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, World History I unit 9's Scientific Revolution (World History I days 126 to 137); language taught, explain with 'In the context of ___, ___ contributed to ___. This may ___.' and weighing words (most, mainly) with a reason.

### Unit 9. Where power comes from (days 145 to 157, weeks 29 to 32)

*Where should a government's power come from, according to the sources, and do historians agree?* Host: World History I unit 10's reason, rights and rulers (World History I days 138 to 155). Ids: WIDA.ELD-SS.9-12.Argue, Interpretive and Expressive (carried; owned in grade 12); SI: g9-si-inform (an SI review use).

**Arc.** Day 145 hooks on the question and names argue openly (what it is for, where the host asks for it, its stages). Day 146 opens with the retrieval task, then takes apart two short sources of the period and one historian's view. Day 147 is a Language Dive on 'My thesis is ___. The source suggests ___', with 'Historian ___ argues ___' beside it. Day 149 uses again the SI move (sum up two historians' positions side by side for a classmate). Day 150 builds a thesis written and defended with sourced evidence, corroborating two sources and naming a limit with the teacher; day 152 is the first independent piece. Day 153 changes the audience (the thesis defended in seminar, then the same thesis written for a history fair panel), and day 154 is the talk-about-language and self-check day (why 'argues' is different from 'says').

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed. Tight at 13 days (the frame): Fluency stays on the forms the unit owns, and review forms go to the respond day.

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 146). No mid-unit assessment (13 days, not over 25). End-of-unit assessment on days 155 and 156: the interpretive part on a new pair of short sources (Curio Class's own selection, public domain; checked unused in docs/ and data/, including section plans and items.csv, before it is written in): pick the claim they corroborate; the talk task (defend a thesis in a seminar), heard in seminars of three; the writing task, the written thesis with evidence. Response time: respond day 157.

**Candidate cells.** PRIME Depth.KLU, the stages of a historical argument named: kept, 0 added days (day 146).

**Sensitive ground and home language.** Who was left out of the period's rights is studied as history; no student is asked to speak for a group. Home language: tesis and thesis, interpretación and interpretation are cognates. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, World History I unit 10's reason, rights and rulers (World History I days 138 to 155); language taught, argue with 'My thesis is ___. The source suggests ___' and 'Historian ___ argues ___'.

### Grade 9 course-level checks

- **Grade 9 mid-year check** (days 81 and 82, respond day 83, week 17), after unit 4: samples units 1, 2, 3 on new content (a read and heard short passage with a flashback (mark the time shift), a new labeled diagram of a cell process (order its steps) and a new worked solution with one step unjustified (supply the reason)), then a reasoning turn on one item, heard in a seminar of three and a short written scene opening or step justification. Unit 4's end-of-unit record is carried unscored, not collected again; because the check comes right after that assessment, its items come from the earlier units only, and no task form from unit 4's last two weeks repeats.
- **Grade 9 year-end check** (days 158 and 159, respond day 160, week 32), after unit 9: samples units 4, 5, 6, 7, 8 on new content (a new data set with two claims (pick and qualify one), a new opinion paragraph (mark its concession), a new informational passage (trace its idea) and a new short sourced account (weigh a factor)), then a seminar talk task and one written argument or explanation paragraph. Unit 9's end-of-unit record is carried unscored, not collected again; because the check comes right after that assessment, its items come from the earlier units only, and no task form from unit 9's last two weeks repeats.

## Grade 10 (course days 161 to 320)

Grade 10 carries the same ids at a harder text or task and picks up each grade 9 row. Its hosts: ELA grade 10, Geometry, Chemistry and World History II. Talk routine: 'point, source, sum up'.

| Unit | Days of the year | Course days | Weeks | Key language use | Ids (cluster 9-12) | Kinds U/F/A/C/R |
|---|---|---|---|---|---|---|
| 10. Why the table predicts | 1 to 16 | 161 to 176 | 1 to 4 | explain | SC Explain (both modes), carried | 4/2/7/2/1 |
| 11. Mills and empires | 17 to 30 | 177 to 190 | 4 to 6 | explain | SS Explain (both modes), carried | 5/2/4/2/1 |
| 12. Proving it | 31 to 46 | 191 to 206 | 7 to 10 | argue | MA Argue (both modes), carried | 5/2/6/2/1 |
| 13. Two ways to begin | 47 to 62 | 207 to 222 | 10 to 13 | narrate | LA Narrate (both modes), carried | 5/2/6/2/1 |
| 14. The funeral speeches | 63 to 80 | 223 to 240 | 13 to 16 | argue | LA Argue (both modes), carried | 5/3/7/2/1 |
| 15. Modeling real things | 84 to 100 | 244 to 260 | 17 to 20 | explain | MA Explain (both modes), carried | 5/2/7/2/1 |
| 16. Earth's thermostat | 101 to 118 | 261 to 278 | 21 to 24 | argue | SC Argue (both modes), carried | 4/3/8/2/1 |
| 17. Two sources on one problem | 119 to 140 | 279 to 300 | 24 to 28 | inform | LA Inform (both modes), carried | 6/4/9/2/1 |
| 18. What should be tried next? | 141 to 157 | 301 to 317 | 29 to 32 | argue | SS Argue (both modes), carried | 4/2/8/2/1 |

### Unit 10. Why the table predicts (days 1 to 16, weeks 1 to 4)

*Why do elements in one column act alike?* Host: Chemistry unit 1's periodic patterns (Chemistry days 1 to 16). Ids: WIDA.ELD-SC.9-12.Explain, Interpretive and Expressive (carried; owned in grade 12); SI: g9-si-inform (an SI review use).

**Arc.** Day 1 hooks on the question and names explain openly (what it is for, where the host asks for it, its stages). Day 2 opens with the retrieval task, then takes apart the chemistry unit's short explanation of why lithium, sodium and potassium react more strongly down the column. Day 3 is a Language Dive on 'More ___ contributes to ___, which results in ___', and day 6 adds dense noun groups ('the attraction between the nucleus and the outer electron'). Day 5 uses again the SI move (give a short briefing on the lab's safety routine to a new student and answer one question). Day 7 builds a particle-level explanation of the pattern on a cause chain, citing the class's data table and naming one limit with the teacher; day 10 is the first independent piece; day 9 reads the class data table from the chemistry unit; day 11 applies the forms to it. Day 12 changes the audience (the pattern explained to a partner, then the same pattern written as a caption on a class periodic table), and day 13 is the talk-about-language and self-check day (why a dense noun group can carry a whole cause).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed.

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 2). No mid-unit assessment (16 days, not over 25). End-of-unit assessment on days 14 and 15: the interpretive part on a new explanation of a different column (Curio Class's own): order its causes; the talk task (explain in a seminar), heard in seminars of three; the writing task, the written explanation. Response time: respond day 16.

**Candidate cells.** California 1.26, all four domains: kept, 0 added days (days 2, 5, 7 and 10). PRIME Match.ELD.2-5: kept, 0 added days (days 1 to 16).

**Sensitive ground and home language.** No demonstration in ELD. If later: reaction rates (Chemistry unit 6) come in weeks 15 to 18 and are not used; levels 1 and 2 use the cloze "Down the column, ___ goes up, so ___." in place of the row's rate cloze. Home language: periódico and periodic, colisión and collision are cognates. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, Chemistry unit 1's periodic patterns (Chemistry days 1 to 16); language taught, explain with 'More ___ contributes to ___, which results in ___' and dense noun groups ('the attraction between the nucleus and the outer electron').

### Unit 11. Mills and empires (days 17 to 30, weeks 4 to 6)

*What did industrialization lead to, and how did it feed empire?* Host: World History II units 2 and 3, the Industrial Revolution and the causes of imperialism (World History II days 16 to 39). Ids: WIDA.ELD-SS.9-12.Explain, Interpretive and Expressive (carried; owned in grade 12); SI: g10-si-explain (begun here, taught in full later in the year).

**Arc.** Day 17 hooks on the question and names explain openly (what it is for, where the host asks for it, its stages). Day 18 opens with the retrieval task, then takes apart a short sourced account of factory work and one of an imperial motive. Day 19 is a Language Dive on 'Over time, ___ contributed to ___, which resulted in ___', and day 22 adds time links (by then, as a result, in turn). Day 21 teaches the SI move (explain to a partner why the class chose one cause as the strongest (unit 15 teaches the two-listener explanation in full)). Day 23 builds an explanation of how industrialization contributed to imperialism on a weighted cause chain, citing sources and naming a limit with the teacher; day 25 is the first independent piece. Day 26 changes the audience (the explanation in seminar, then the same explanation written as a timeline caption), and day 27 is the talk-about-language and self-check day (how 'in turn' shows one cause feeding the next).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed. On the host calendar: Day 27: World History II unit 3 (imperialism) opens on day 27 of its course; from here the imperial motive source is used. Tight at 14 days (the frame): Fluency stays on the forms the unit owns, and review forms go to the respond day.

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 18). No mid-unit assessment (14 days, not over 25). End-of-unit assessment on days 28 and 29: the interpretive part on a new short account (Curio Class's own, sourced) of one industry's raw material and its source abroad: order the causes; the talk task (explain in a seminar), heard in seminars of three; the writing task, the written explanation. Response time: respond day 30.

**Candidate cells.** PRIME Breadth.LE, explain on a second content standard: kept, 0 added days (days 17 to 30).

**Sensitive ground and home language.** Sensitive: the imperialism host is about colonial rule, which some families lived under; the family note previews it and offers the Industrial Revolution host alone; no student is asked to speak for a country or a people. Home language: industrialización and industrialization, imperialismo and imperialism are cognates. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, World History II units 2 and 3, the Industrial Revolution and the causes of imperialism (World History II days 16 to 39); language taught, explain with 'Over time, ___ contributed to ___, which resulted in ___' and time links (by then, as a result, in turn).

### Unit 12. Proving it (days 31 to 46, weeks 7 to 10)

*How few facts make two triangles the same, and how do we say why?* Host: Geometry unit 2's congruence criteria and parallelogram proofs (Geometry days 27 to 45). Ids: WIDA.ELD-MA.9-12.Argue, Interpretive and Expressive (carried; owned in grade 12); SI: g10-si-argue (begun here, taught in full later in the year).

**Arc.** Day 31 hooks on the question and names argue openly (what it is for, where the host asks for it, its stages). Day 32 opens with the retrieval task, then takes apart a partner's or a model proof from the Geometry pages. Day 33 is a Language Dive on 'Since ___, it follows that ___', and day 36 adds 'Although ___, ___' for the critique. Day 35 teaches the SI move (question a partner's reason politely in seminar (unit 14 teaches the several-source seminar in full)). Day 37 builds a congruence or parallelogram proof (given, statements, reasons, conclusion), presented, and a critique of a partner's with the teacher; day 40 is the first independent piece; day 39 reads a parallelogram proof from the same unit; day 41 applies the forms to it. Day 42 changes the audience (the proof presented to the class, then the same proof written for a student who missed the lesson), and day 43 is the talk-about-language and self-check day (what 'it follows that' promises and when it is false).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed.

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 32). No mid-unit assessment (16 days, not over 25). End-of-unit assessment on days 44 and 45: the interpretive part on a new proof with one missing or wrong reason: fix it; the talk task (present a short proof in a seminar), heard in seminars of three; the writing task, the written proof. Response time: respond day 46.

**Candidate cells.** PRIME Depth.ELD, 'it follows that' as a feature with a job: kept, 0 added days (day 33).

**Sensitive ground and home language.** Methods stay within Geometry units 1 and 2. Home language: definición and definition are cognates; demostrar and prove are not, so the word card carries prove. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, Geometry unit 2's congruence criteria and parallelogram proofs (Geometry days 27 to 45); language taught, argue with 'Since ___, it follows that ___' and 'Although ___, ___' for the critique.

### Unit 13. Two ways to begin (days 47 to 62, weeks 10 to 13)

*How do two stories use structure and voice, and how can we shape a scene for an effect?* Host: ELA grade 10 unit 3's stories under colonial rule (ELA days 46 to 60), with Frankenstein (ELA unit 1) retrieved. Ids: WIDA.ELD-LA.9-12.Narrate, Interpretive and Expressive (carried; owned in grade 12); SI: g10-si-narrate (the unit's own SI row).

**Arc.** Day 47 hooks on the question and names narrate openly (what it is for, where the host asks for it, its stages). Day 48 opens with the retrieval task, then takes apart the opening of Frankenstein (letters before the story) beside the opening of Tagore's 'The Postmaster'. Day 49 is a Language Dive on 'In contrast to ___, ___ begins with ___, which creates ___', and day 52 adds tone words. Day 51 teaches the SI move (recount a club's or class's term for a formal audience (a visitor) beside an informal one). Day 53 builds a scene that uses structure for an effect, and a formal recount (opening, events, highlight, close) with the teacher; day 56 is the first independent piece; day 55 reads a second story from the same ELA unit, read for its opening; day 57 applies the forms to it. Day 58 changes the audience (the recount to a visitor, then the same recount to a friend), and day 59 is the talk-about-language and self-check day (what a formal opening does for a visitor that a friend does not need).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed.

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 48). No mid-unit assessment (16 days, not over 25). End-of-unit assessment on days 60 and 61: the interpretive part on two new short openings (Curio Class's own): name each structure's effect; the talk task (recount a new event for a visitor in a seminar), heard in seminars of three; the writing task, the scene. Response time: respond day 62.

**Candidate cells.** Bar item 10, formal and informal audience: kept, 0 added days (day 58, the change-of-audience day). PRIME Depth.KLU: kept, 0 added days (stages of the formal recount named on day 51).

**Sensitive ground and home language.** Sensitive: the host stories show people living under colonial rule; the family note previews it and offers another story from the ELA unit; no student is asked to speak for a country. Own-scene prompts follow APPROACH "Sensitive ground". Home language: contraste and contrast, efecto and effect are cognates. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, ELA grade 10 unit 3's stories under colonial rule (ELA days 46 to 60), with Frankenstein (ELA unit 1) retrieved; language taught, narrate with 'In contrast to ___, ___ begins with ___, which creates ___' and tone words.

### Unit 14. The funeral speeches (days 63 to 80, weeks 13 to 16)

*Was Brutus right, and how do the speeches move the crowd?* Host: ELA grade 10 unit 4's Julius Caesar (ELA days 61 to 85). Ids: WIDA.ELD-LA.9-12.Argue, Interpretive and Expressive (carried; owned in grade 12); SI: g10-si-argue (the unit's own SI row).

**Arc.** Day 63 hooks on the question and names argue openly (what it is for, where the host asks for it, its stages). Day 64 opens with the retrieval task, then takes apart one paragraph of Brutus's and one of Antony's funeral speech. Day 65 is a Language Dive on 'While ___ is true, ___ matters more because ___', and day 68 adds boosting modals (clearly, must). Day 67 teaches the SI move (hold a seminar on the play and Plutarch's account (two sources), citing reasons and summing up where the group agrees). Day 69 builds one argument paragraph that weighs two counterclaims with the teacher; day 72 is the first independent piece; day 71 reads Plutarch's account of the same moment; day 75 applies the forms to it; day 74 is a seminar on the host content. Day 76 changes the audience (the claim argued in seminar, then the same claim written as a program note for an audience), and day 77 is the talk-about-language and self-check day (how 'clearly' and 'must' push a listener).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed.

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 64). No mid-unit assessment (18 days, not over 25). End-of-unit assessment on days 78 and 79: the interpretive part on a new short speech passage (Curio Class's own selection, public domain; checked unused in docs/ and data/, including section plans and items.csv, before it is written in): mark its rebuttal; the talk task (argue in a seminar on two sources), heard in seminars of three; the writing task, the argument paragraph. Response time: respond day 80.

**Candidate cells.** PRIME Breadth.KLU, argue across LA and SS this year: kept, 0 added days (named in day 63's host note). Bar item 4, summing up agreement: kept, 0 added days (day 69).

**Sensitive ground and home language.** An assassination is studied as drama; no role play of violence. If later: evaluating arguments returns in ELA unit 7; this unit judges the speeches' reasoning on its own. Home language: retórica and rhetoric are cognates. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, ELA grade 10 unit 4's Julius Caesar (ELA days 61 to 85); language taught, argue with 'While ___ is true, ___ matters more because ___' and boosting modals (clearly, must).

### Unit 15. Modeling real things (days 84 to 100, weeks 17 to 20)

*How did you model it, and why that way?* Host: Geometry unit 5's modeling objects and density (Geometry days 82 to 102), with unit 4's right triangles retrieved. Ids: WIDA.ELD-MA.9-12.Explain, Interpretive and Expressive (carried; owned in grade 12); SI: g10-si-explain (the unit's own SI row).

**Arc.** Day 84 hooks on the question and names explain openly (what it is for, where the host asks for it, its stages). Day 85 opens with the retrieval task, then takes apart a short worked modeling task (a tank, a log) from the Geometry pages. Day 86 is a Language Dive on 'Assuming ___, the object is modeled by ___, which results in ___', and day 89 adds 'I decided on ___' and 'I went with ___'. Day 88 teaches the SI move (explain a choice made on the modeling task to the teacher and then to peers, choosing words for each listener). Day 90 builds an explanation of how a real object was modeled or a right-triangle problem solved, so a partner could use the method with the teacher; day 93 is the first independent piece; day 92 reads a right-triangle problem from Geometry unit 4 (retrieved); day 95 applies the forms to it; day 94 is a seminar on the host content. Day 96 changes the audience (the choice explained to the teacher, then the same choice explained to peers), and day 97 is the talk-about-language and self-check day (how 'assuming' warns the listener).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed.

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 85). No mid-unit assessment (17 days, not over 25). End-of-unit assessment on days 98 and 99: the interpretive part on a new modeling task (Curio Class's own): name its assumption; the talk task (explain a choice in a seminar), heard in seminars of three; the writing task, the written explanation. Response time: respond day 100.

**Candidate cells.** Bar item 10, two listeners: kept, 0 added days (day 96, the change-of-audience day). PRIME Match.ELD.2-5: kept, 0 added days (days 84 to 100).

**Sensitive ground and home language.** Methods stay within Geometry units 4 and 5. Home language: densidad and density are cognates; triángulo rectángulo and right triangle are close. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, Geometry unit 5's modeling objects and density (Geometry days 82 to 102), with unit 4's right triangles retrieved; language taught, explain with 'Assuming ___, the object is modeled by ___, which results in ___' and 'I decided on ___' and 'I went with ___'.

### Unit 16. Earth's thermostat (days 101 to 118, weeks 21 to 24)

*What do the data say about Earth's feedbacks, and where are they limited?* Host: Chemistry unit 5's thermal equilibrium (retrieved) and unit 9's Earth feedbacks (Chemistry days 113 to 130). Ids: WIDA.ELD-SC.9-12.Argue, Interpretive and Expressive (carried; owned in grade 12); SI: g10-si-argue (an SI review use).

**Arc.** Day 101 hooks on the question and names argue openly (what it is for, where the host asks for it, its stages). Day 102 opens with the retrieval task, then takes apart two short claims about a heating or cooling result from Chemistry unit 5. Day 103 is a Language Dive on 'Although ___, the data shows ___. However, it is limited because ___', and day 106 adds 'clearly' against 'suggests'. Day 105 uses again the SI move (answer a rebuttal in seminar without dropping the claim). Day 107 builds a claim argued from the data, with its limits weighed and a rebuttal answered with the teacher; day 109 is the first independent piece; day 112 reads one claim about Arctic sea ice from Chemistry unit 9; day 113 applies the forms to it; day 111 is a seminar on the host content. Day 114 changes the audience (the claim argued in seminar, then the same claim written as a short reply to a reader's letter), and day 115 is the talk-about-language and self-check day (why 'is limited because' makes a claim stronger, not weaker).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed. The second host opens on day 113, and the days that read it sit on or after that day. Chemistry opens unit 9 today: the Arctic sea ice claim is used from here; the days before argued from Chemistry unit 5's thermal equilibrium data (retrieved).

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 102). No mid-unit assessment (18 days, not over 25). End-of-unit assessment on days 116 and 117: the interpretive part on a new small data set (invented for practice): pick the supported claim; the talk task (argue in a seminar), heard in seminars of three; the writing task, the claim written with a limit. Response time: respond day 118.

**Candidate cells.** PRIME Depth.PLD, the same data task at three entry points: kept, 0 added days (day 109, the first independent application day).

**Sensitive ground and home language.** Climate data can worry students: the unit names what people are doing and keeps to the host's data. Home language: equilibrio and equilibrium are cognates. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, Chemistry unit 5's thermal equilibrium (retrieved) and unit 9's Earth feedbacks (Chemistry days 113 to 130); language taught, argue with 'Although ___, the data shows ___. However, it is limited because ___' and 'clearly' against 'suggests'.

### Unit 17. Two sources on one problem (days 119 to 140, weeks 24 to 28)

*What do two sources say about rising seas, and how do we join them?* Host: ELA grade 10 unit 6's founding texts on liberty (ELA days 112 to 127), then unit 7's rising seas sources (ELA days 128 to 155). Ids: WIDA.ELD-LA.9-12.Inform, Interpretive and Expressive (carried; owned in grade 12); SI: g10-si-inform (the unit's own SI row).

**Arc.** Day 119 hooks on the question and names inform openly (what it is for, where the host asks for it, its stages). Day 120 opens with the retrieval task, then takes apart two of ELA unit 6's founding texts on liberty, already read. Day 121 is a Language Dive on 'Whereas ___, ___. Both ___', and day 124 adds 'Regarding ___, ___' and quotations worked in ('the report states that'). Day 123 teaches the SI move (give a short briefing on a school event and answer audience questions not planned for). Day 125 builds one informative paragraph that synthesizes two sources, with a short quotation worked into a sentence with the teacher; day 127 is the first independent piece; day 128 reads one passage from each of ELA unit 7's sources (a government sea-level report and a news piece); day 132 applies the forms to it; day 131 is a seminar on the host content. Day 133 changes the audience (the briefing to the class, then the paragraph written for a town newsletter), and day 137 is the talk-about-language and self-check day (what 'nonetheless' tells a reader about the next sentence).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed. The second host opens on day 128, and the days that read it sit on or after that day. ELA opens unit 7 today: the sea-level report and the news piece are used from here; the days before synthesized two of ELA unit 6's founding texts on liberty, already read. Longer units (here 22 days) add a second host passage, a stage-labeling day, a seminar and peer reading, by the row's load (an LA row weighs most).

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 120). No mid-unit assessment (22 days, not over 25). End-of-unit assessment on days 138 and 139: the interpretive part on two new short sources (Curio Class's own selection, US government works; checked unused in docs/ and data/, including section plans and items.csv, before it is written in): mark where they agree; the talk task (brief a small group and answer a question), heard in seminars of three; the writing task, the synthesis paragraph. Response time: respond day 140.

**Candidate cells.** Bar item 3, the text dimension (ordering two sources): kept, 0 added days (day 120). PRIME Breadth.LE: kept, 0 added days (LA inform on two text types).

**Sensitive ground and home language.** No task asks whether a student's home or family is at risk from flooding. Home language: sintetizar and synthesize, información and information are cognates. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, ELA grade 10 unit 6's founding texts on liberty (ELA days 112 to 127), then unit 7's rising seas sources (ELA days 128 to 155); language taught, inform with 'Whereas ___, ___. Both ___' and 'Regarding ___, ___' and quotations worked in ('the report states that').

### Unit 18. What should be tried next? (days 141 to 157, weeks 29 to 32)

*Which effort has done most on one global problem, and what do historians and the evidence say?* Host: World History II unit 11's research argument (World History II days 145 to 157), with unit 4's 1919 peace retrieved. Ids: WIDA.ELD-SS.9-12.Argue, Interpretive and Expressive (carried; owned in grade 12); SI: g10-si-narrate (an SI review use).

**Arc.** Day 141 hooks on the question and names argue openly (what it is for, where the host asks for it, its stages). Day 142 opens with the retrieval task, then takes apart two historians' short views of the 1919 peace (retrieved from World History II unit 4). Day 143 is a Language Dive on 'Although ___ argues ___, the evidence suggests ___', and day 146 adds 'Historians disagree about ___'. Day 145 uses again the SI move (recount the research path for a formal audience (what was asked, found and changed)). Day 147 builds a research claim that weighs interpretations and names a limit with the teacher; day 150 is the first independent piece; day 149 reads two sources on one global problem from World History II unit 11; day 152 applies the forms to it; day 151 is a seminar on the host content. Day 153 changes the audience (the claim in seminar, then the same claim written as a short brief for a school club), and day 154 is the talk-about-language and self-check day (why 'disagree about' is different from 'are wrong about').

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed. The second host opens on day 145, and the days that read it sit on or after that day. World History II opens unit 11 today: the global-problem sources are used from here; the days before retrieved the 1919 interpretations.

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 142). No mid-unit assessment (17 days, not over 25). End-of-unit assessment on days 155 and 156: the interpretive part on two new short interpretations (Curio Class's own): name the difference; the talk task (argue in a seminar), heard in seminars of three; the writing task, the written claim. Response time: respond day 157.

**Candidate cells.** PRIME Depth.KLU, a research argument's stages: kept, 0 added days (day 142).

**Sensitive ground and home language.** Sensitive: the 1919 peace is about war and its aftermath; the family note previews it. Global-problem picks are from several, and refugee crises are one choice, never the set topic. Home language: the false friend eventualmente (possibly, not eventually) is named. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, World History II unit 11's research argument (World History II days 145 to 157), with unit 4's 1919 peace retrieved; language taught, argue with 'Although ___ argues ___, the evidence suggests ___' and 'Historians disagree about ___'.

### Grade 10 course-level checks

- **Grade 10 mid-year check** (days 81 and 82, respond day 83, week 17), after unit 14: samples units 10, 11, 12, 13 on new content (a new particle-level explanation (order the causes), a new account of an industry (sort causes over time), a new proof with a wrong reason and two new story openings (name each effect)), then a small-seminar talk task and a short written explanation or scene. Unit 14's end-of-unit record is carried unscored, not collected again; because the check comes right after that assessment, its items come from the earlier units only, and no task form from unit 14's last two weeks repeats.
- **Grade 10 year-end check** (days 158 and 159, respond day 160, week 32), after unit 18: samples units 14, 15, 16, 17 on new content (a new speech passage (mark the rebuttal), a new modeling task (name the assumption), a new small data set (claim and limit) and two new short sources (synthesize)), then a seminar talk task and one written synthesis or argument paragraph. Unit 18's end-of-unit record is carried unscored, not collected again; because the check comes right after that assessment, its items come from the earlier units only, and no task form from unit 18's last two weeks repeats.

## Grade 11 (course days 321 to 480)

Grade 11 carries the ids again and picks up each grade 10 row. Its hosts: ELA grade 11, Algebra II, Physics and US History I. Talk routine: 'point, objection, answer'.

| Unit | Days of the year | Course days | Weeks | Key language use | Ids (cluster 9-12) | Kinds U/F/A/C/R |
|---|---|---|---|---|---|---|
| 19. Stories that refuse to settle | 1 to 16 | 321 to 336 | 1 to 4 | narrate | LA Narrate (both modes), carried | 5/2/6/2/1 |
| 20. What did they ask us to trust? | 17 to 34 | 337 to 354 | 4 to 7 | inform | LA Inform (both modes), carried | 5/3/7/2/1 |
| 21. Where will it be? | 35 to 48 | 355 to 368 | 7 to 10 | explain | SC Explain (both modes), carried | 4/2/5/2/1 |
| 22. Founding promises | 49 to 62 | 369 to 382 | 10 to 13 | argue | LA Argue (both modes), carried | 5/2/4/2/1 |
| 23. Free labor and a breaking Union | 63 to 80 | 383 to 400 | 13 to 16 | explain | SS Explain (both modes), carried | 5/3/7/2/1 |
| 24. Failed or overthrown? | 84 to 96 | 404 to 416 | 17 to 20 | argue | SS Argue (both modes), carried | 3/2/5/2/1 |
| 25. Light, two ways | 97 to 110 | 417 to 430 | 20 to 22 | argue | SC Argue (both modes), carried | 4/2/5/2/1 |
| 26. Things that go around | 111 to 132 | 431 to 452 | 23 to 27 | explain | MA Explain (both modes), carried | 5/4/10/2/1 |
| 27. How sure is sure? | 133 to 157 | 453 to 477 | 27 to 32 | argue | MA Argue (both modes), carried | 5/5/12/2/1 |

### Unit 19. Stories that refuse to settle (days 1 to 16, weeks 1 to 4)

*How does a writer's structure keep us in doubt, and how do we look back on our own story?* Host: ELA grade 11 unit 1's stories built on doubt (ELA days 1 to 16). Ids: WIDA.ELD-LA.9-12.Narrate, Interpretive and Expressive (carried; owned in grade 12); SI: g11-si-narrate (the unit's own SI row).

**Arc.** Day 1 hooks on the question and names narrate openly (what it is for, where the host asks for it, its stages). Day 2 opens with the retrieval task, then takes apart the turn in 'An Occurrence at Owl Creek Bridge' (1890) where the story's time breaks. Day 3 is a Language Dive on 'Looking back, I realize ___' and 'At first I thought ___', and day 6 adds 'My role was to ___. As a result, ___'. Day 5 teaches the SI move (recount an experience for an interview-style question (a time you worked on a team) in three parts: situation, action, result). Day 7 builds a reflective narrative scene, personal or invented, with a chosen structure with the teacher; day 10 is the first independent piece; day 9 reads a second story from the same ELA unit, read for where its structure withholds; day 11 applies the forms to it. Day 12 changes the audience (the recount to an interviewer, then the same recount to a friend), and day 13 is the talk-about-language and self-check day (why an interviewer wants 'my role was' and a friend does not).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed.

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 2). No mid-unit assessment (16 days, not over 25). End-of-unit assessment on days 14 and 15: the interpretive part on a new short passage with a structural break (Curio Class's own): name the choice; the talk task (give an interview recount in a seminar), heard in seminars of three; the writing task, the reflective scene. Response time: respond day 16.

**Candidate cells.** Bar item 12, the self-check on reflective language: kept, 0 added days (day 13, the self-check day). PRIME Depth.KLU: kept, 0 added days (the interview stages named on day 5).

**Sensitive ground and home language.** Sensitive: Owl Creek Bridge is a hanging in the Civil War; the family note previews loss, and ELD uses the passage for its structure. A student may speak as an invented applicant; no task asks about documents, aid eligibility or a family's situation. Home language: reflexión and reflection, estructura and structure are cognates. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, ELA grade 11 unit 1's stories built on doubt (ELA days 1 to 16); language taught, narrate with 'Looking back, I realize ___' and 'At first I thought ___' and 'My role was to ___. As a result, ___'.

### Unit 20. What did they ask us to trust? (days 17 to 34, weeks 4 to 7)

*How does an essay make its point clear, and how do we ask an office for information?* Host: ELA grade 11 unit 2's essays (ELA days 17 to 34). Ids: WIDA.ELD-LA.9-12.Inform, Interpretive and Expressive (carried; owned in grade 12); SI: g11-si-inform (the unit's own SI row).

**Arc.** Day 17 hooks on the question and names inform openly (what it is for, where the host asks for it, its stages). Day 18 opens with the retrieval task, then takes apart one paragraph of 'Self-Reliance' and one of 'Civil Disobedience'. Day 19 is a Language Dive on 'Most sources agree that ___. One source adds ___', and day 22 adds polite modals ('Could you tell me ___?', 'I am calling about ___'). Day 21 teaches the SI move (request and give information in a formal setting (a meeting with a counselor, a call to an office), with greeting, reason, question and thanks). Day 23 builds an informative paragraph that synthesizes several sources (the two essays and a short reference entry) for a named reader with the teacher; day 26 is the first independent piece; day 25 reads a short reference entry on the two writers; day 29 applies the forms to it; day 28 is a seminar on the host content. Day 30 changes the audience (the request made by phone (role-played as an invented caller), then the same request written as an email), and day 31 is the talk-about-language and self-check day (what a reference entry gives a reader that an essay does not).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed.

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 18). No mid-unit assessment (18 days, not over 25). End-of-unit assessment on days 32 and 33: the interpretive part on a new short essay passage (Curio Class's own selection, public domain; checked unused in docs/ and data/, including section plans and items.csv, before it is written in): outline its structure; the talk task (make a formal request in a short role-played call), heard in seminars of three; the writing task, the synthesis paragraph. Response time: respond day 34.

**Candidate cells.** Bar item 4, the language of asking: kept, 0 added days (days 21 and 30). PRIME Breadth.LE: kept, 0 added days (several sources).

**Sensitive ground and home language.** A student may speak as an invented applicant; no call asks about documents or a family's situation. Home language: the false friend realizar (carry out) is named. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, ELA grade 11 unit 2's essays (ELA days 17 to 34); language taught, inform with 'Most sources agree that ___. One source adds ___' and polite modals ('Could you tell me ___?', 'I am calling about ___').

### Unit 21. Where will it be? (days 35 to 48, weeks 7 to 10)

*How can people predict an orbit years ahead?* Host: Physics unit 3's orbits (Physics days 31 to 46). Ids: WIDA.ELD-SC.9-12.Explain, Interpretive and Expressive (carried; owned in grade 12); SI: g10-si-explain (an SI review use).

**Arc.** Day 35 hooks on the question and names explain openly (what it is for, where the host asks for it, its stages). Day 36 opens with the retrieval task, then takes apart the physics unit's explanation of how gravity's pull sets a spacecraft's path. Day 37 is a Language Dive on 'As ___ increases, ___ decreases, because ___ is proportional to ___', and day 40 adds 'which allows' clauses. Day 39 uses again the SI move (explain a school procedure (signing up for a test) to a younger student). Day 41 builds an explanation of an orbit with the mathematical model in words and a labeled diagram, naming one limit with the teacher; day 43 is the first independent piece. Day 44 changes the audience (the orbit explained to a partner, then the same orbit written for a planetarium sign), and day 45 is the talk-about-language and self-check day (what 'is proportional to' says that 'goes with' does not).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed.

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 36). No mid-unit assessment (14 days, not over 25). End-of-unit assessment on days 46 and 47: the interpretive part on a new short explanation of a moon's orbit (Curio Class's own): order its causes; the talk task (explain in a seminar), heard in seminars of three; the writing task, the written explanation. Response time: respond day 48.

**Candidate cells.** PRIME Match.ELD.2-5, a mathematical model said in words: kept, 0 added days (day 37).

**Sensitive ground and home language.** If later: wave technologies (Physics unit 6) come in weeks 16 to 19 and are not used. Home language: órbita and orbit are cognates; señal and signal look alike but the card carries signal. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, Physics unit 3's orbits (Physics days 31 to 46); language taught, explain with 'As ___ increases, ___ decreases, because ___ is proportional to ___' and 'which allows' clauses.

### Unit 22. Founding promises (days 49 to 62, weeks 10 to 13)

*How well does a founding text argue, and how do we make a case to someone who can say no?* Host: ELA grade 11 unit 3's covenant and consent texts (ELA days 35 to 55). Ids: WIDA.ELD-LA.9-12.Argue, Interpretive and Expressive (carried; owned in grade 12); SI: g11-si-argue (the unit's own SI row).

**Arc.** Day 49 hooks on the question and names argue openly (what it is for, where the host asks for it, its stages). Day 50 opens with the retrieval task, then takes apart one paragraph of Common Sense (1776). Day 51 is a Language Dive on 'It is clear that ___' against 'It may be that ___', and day 54 adds 'We understand that ___. In return, ___'. Day 53 teaches the SI move (make a case to an adult (a club request, a class change) and answer objections in a formal register). Day 55 builds one argument paragraph for a chosen audience, adjusting tone, and a request case with claim, reasons, an answered objection and an ask with the teacher; day 57 is the first independent piece. Day 58 changes the audience (the same claim for a classmate, then the same claim for the principal), and day 59 is the talk-about-language and self-check day (how 'must' and 'may' change who will listen).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed. On the host calendar: Day 56: ELA grade 11 unit 3 ends on ELA day 55; from here the unit runs just after its host, on the passage already read.

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 50). No mid-unit assessment (14 days, not over 25). End-of-unit assessment on days 60 and 61: the interpretive part on a new short founding-era passage (Curio Class's own selection, public domain; checked unused in docs/ and data/, including section plans and items.csv, before it is written in): name its audience; the talk task (make a case to a teacher playing the adult), heard in seminars of three; the writing task, the argument paragraph. Response time: respond day 62.

**Candidate cells.** Bar item 10, two audiences: kept, 0 added days (day 58, the change-of-audience day). PRIME Depth.ELD: kept, 0 added days (modals as tone-setting features, day 51).

**Sensitive ground and home language.** Winthrop's sermon is a historical source; no student states a belief. If later: ELA's Douglass unit (unit 5) comes later; this unit's rhetoric is Paine's. Home language: audiencia and audience, objeción and objection are cognates. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, ELA grade 11 unit 3's covenant and consent texts (ELA days 35 to 55); language taught, argue with 'It is clear that ___' against 'It may be that ___' and 'We understand that ___. In return, ___'.

### Unit 23. Free labor and a breaking Union (days 63 to 80, weeks 13 to 16)

*What changed and what stayed the same, and why did the sections pull apart?* Host: US History I unit 4's market revolution (US History I days 51 to 71) and unit 5's sectional crisis (from day 72). Ids: WIDA.ELD-SS.9-12.Explain, Interpretive and Expressive (carried; owned in grade 12); SI: g11-si-explain (the unit's own SI row).

**Arc.** Day 63 hooks on the question and names explain openly (what it is for, where the host asks for it, its stages). Day 64 opens with the retrieval task, then takes apart short sourced accounts of mill work and of the cotton economy. Day 65 is a Language Dive on 'While ___ changed, ___ continued', and day 68 adds 'The first step is ___, which allows ___'. Day 67 teaches the SI move (explain a process (applying for a summer program) to a younger student and to an adult). Day 69 builds an explanation of how the market revolution sharpened sectional tension on a weighted cause chain, citing sources and naming a limit with the teacher; day 71 is the first independent piece; day 72 reads a short sourced account of the sectional crisis from US History I unit 5; day 75 applies the forms to it; day 74 is a seminar on the host content. Day 76 changes the audience (the process to a ninth grader, then the same process to a parent's friend (invented)), and day 77 is the talk-about-language and self-check day (how 'while' lets one sentence hold two times).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed. The second host opens on day 72, and the days that read it sit on or after that day. US History I opens unit 5 today: the sectional crisis account is used from here.

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 64). No mid-unit assessment (18 days, not over 25). End-of-unit assessment on days 78 and 79: the interpretive part on a new short sourced account (Curio Class's own): sort change from continuity; the talk task (explain in a seminar), heard in seminars of three; the writing task, the written explanation. Response time: respond day 80.

**Candidate cells.** PRIME Breadth.LE, explain on the social studies standard: kept, 0 added days (days 63 to 80).

**Sensitive ground and home language.** Sensitive: the sectional crisis host is about slavery and the coming war; the family note previews it and offers the market revolution host alone; slavery is never role-played, and no student is asked to speak for a group. Applicant prompts allow an invented applicant. Home language: continuidad and continuity, tensión and tension are cognates. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, US History I unit 4's market revolution (US History I days 51 to 71) and unit 5's sectional crisis (from day 72); language taught, explain with 'While ___ changed, ___ continued' and 'The first step is ___, which allows ___'.

### Unit 24. Failed or overthrown? (days 84 to 96, weeks 17 to 20)

*Did Reconstruction fail, or was it overthrown, and how reliable is the source that says so?* Host: US History I unit 5's argument writing on Reconstruction (US History I days 72 to 92). Ids: WIDA.ELD-SS.9-12.Argue, Interpretive and Expressive (carried; owned in grade 12); SI: g11-si-argue (an SI review use).

**Arc.** Day 84 hooks on the question and names argue openly (what it is for, where the host asks for it, its stages). Day 85 opens with the retrieval task, then takes apart two short sources on Reconstruction, one of them a period newspaper report from Chronicling America. Day 86 is a Language Dive on reporting verbs (claims, reports, admits) with hedging, with 'Although the report claims ___, ___ suggests ___' beside it. Day 88 uses again the SI move (answer an objection to a source's reliability in seminar). Day 89 builds a historical argument that corroborates and names a bias with the teacher; day 91 is the first independent piece. Day 92 changes the audience (the claim in seminar, then the same claim written as a short note to a museum about its exhibit text), and day 93 is the talk-about-language and self-check day (why 'admits' and 'claims' report the same words differently).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed. Tight at 13 days (the frame): Fluency stays on the forms the unit owns, and review forms go to the respond day.

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 85). No mid-unit assessment (13 days, not over 25). End-of-unit assessment on days 94 and 95: the interpretive part on a new pair of short sources (Curio Class's own selection; checked unused in docs/ and data/, including section plans and items.csv, before it is written in): judge one claim's reliability; the talk task (argue in a seminar), heard in seminars of three; the writing task, the written argument. Response time: respond day 96.

**Candidate cells.** PRIME Depth.KLU, sourcing as part of argue: kept, 0 added days (day 86).

**Sensitive ground and home language.** Sensitive: Reconstruction's overthrow includes racial violence, taught from sources and never role-played; the family note previews it. News picks avoid immigration enforcement. If later: news reading in US History I unit 9 comes in weeks 28 to 31; this unit judges a period newspaper only. Home language: fiable and reliable are not cognates, so the card carries reliable. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, US History I unit 5's argument writing on Reconstruction (US History I days 72 to 92); language taught, argue with reporting verbs (claims, reports, admits) with hedging and 'Although the report claims ___, ___ suggests ___'.

### Unit 25. Light, two ways (days 97 to 110, weeks 20 to 22)

*Is light a wave or a particle, and does a published claim about radiation hold up?* Host: Physics unit 7's wave-particle question and published claims (Physics days 93 to 106). Ids: WIDA.ELD-SC.9-12.Argue, Interpretive and Expressive (carried; owned in grade 12); SI: g11-si-inform (an SI review use).

**Arc.** Day 97 hooks on the question and names argue openly (what it is for, where the host asks for it, its stages). Day 98 opens with the retrieval task, then takes apart two short published claims about radiation's effects (a government health page and an invented ad). Day 99 is a Language Dive on 'That claim might ___, although ___', and day 102 adds 'A reliable source would ___'. Day 101 uses again the SI move (write a short request to an agency for the data behind a claim). Day 103 builds an argument on whether light behaves as a wave or a particle in a given result, answering a rebuttal with the teacher; day 105 is the first independent piece. Day 106 changes the audience (the judgment in seminar, then the same judgment written as a reply on a class question board), and day 107 is the talk-about-language and self-check day (how 'might' keeps a judgment fair).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed.

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 98). No mid-unit assessment (14 days, not over 25). End-of-unit assessment on days 108 and 109: the interpretive part on a new short published claim (invented for practice): judge it; the talk task (argue in a seminar), heard in seminars of three; the writing task, the written argument. Response time: respond day 110.

**Candidate cells.** PRIME Depth.PLD: kept, 0 added days (day 105, the same claim task at three entry points). Bar item 13, argue returns on a new standard: kept, 0 added days (named on day 97).

**Sensitive ground and home language.** No task asks about a student's own medical tests. Home language: the false friend actual (current) is named. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, Physics unit 7's wave-particle question and published claims (Physics days 93 to 106); language taught, argue with 'That claim might ___, although ___' and 'A reliable source would ___'.

### Unit 26. Things that go around (days 111 to 132, weeks 23 to 27)

*How did you build the model, and how far can it be trusted?* Host: Algebra II unit 6's periodic modeling (Algebra II days 113 to 136), with unit 5's combined models retrieved. Ids: WIDA.ELD-MA.9-12.Explain, Interpretive and Expressive (carried; owned in grade 12); SI: g11-si-explain (an SI review use).

**Arc.** Day 111 hooks on the question and names explain openly (what it is for, where the host asks for it, its stages). Day 112 opens with the retrieval task, then takes apart a short worked model of a periodic data set (tide heights or daylight hours) from the Algebra II pages. Day 113 is a Language Dive on 'The model suggests ___, but it may ___', and day 116 adds dense noun groups ('the period of the daylight model'). Day 115 uses again the SI move (explain the model to a younger student and then to the teacher). Day 117 builds an explanation of how a function or periodic model was built and its limits with the teacher; day 120 is the first independent piece; day 119 reads a second periodic data set from the Algebra II unit; day 124 applies the forms to it; day 123 is a seminar on the host content. Day 125 changes the audience (the model explained to a younger student, then the same model explained to the teacher), and day 129 is the talk-about-language and self-check day (what 'may' does at the end of a model's explanation).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed. On the host calendar: Day 111: Algebra II is in its unit 5 check and respond days (110 to 112): the hook uses the tide picture and unit 5's combined models (retrieved). Day 112: One day ahead of the host: the worked periodic model is read for its language only (amplitude, period and midline named, not computed); the math is Algebra II's from its day 113. Longer units (here 22 days) add a second host passage, a stage-labeling day, a seminar and peer reading, by the row's load (an LA row weighs most).

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 112). No mid-unit assessment (22 days, not over 25). End-of-unit assessment on days 130 and 131: the interpretive part on a new periodic data set (public source, credited): name its model's parts; the talk task (explain a model in a seminar), heard in seminars of three; the writing task, the written explanation with a limit. Response time: respond day 132.

**Candidate cells.** PRIME Match.ELD.2-5: kept, 0 added days (days 111 to 132).

**Sensitive ground and home language.** Methods stay within Algebra II units 5 and 6. Home language: amplitud and amplitude, periódico and periodic are cognates. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, Algebra II unit 6's periodic modeling (Algebra II days 113 to 136), with unit 5's combined models retrieved; language taught, explain with 'The model suggests ___, but it may ___' and dense noun groups ('the period of the daylight model').

### Unit 27. How sure is sure? (days 133 to 157, weeks 27 to 32)

*Is the result significant, and what does the margin of error allow us to say?* Host: Algebra II unit 7's significance and margin of error (Algebra II days 137 to 157). Ids: WIDA.ELD-MA.9-12.Argue, Interpretive and Expressive (carried; owned in grade 12); SI: g11-si-narrate (an SI review use).

**Arc.** Day 133 hooks on the question and names argue openly (what it is for, where the host asks for it, its stages). Day 134 opens with the retrieval task, then takes apart two short reports of one survey or experiment. Day 135 is a Language Dive on 'The result might ___, although ___', and day 138 adds 'Within the margin of error, ___'. Day 137 uses again the SI move (recount how the class ran its own small study, for a reader who must judge it). Day 139 builds an argument on whether a result is significant and what its margin of error allows, naming a limitation with the teacher; day 142 is the first independent piece; day 141 reads a simulation result from Algebra II unit 7; day 146 applies the forms to it; day 145 is a seminar on the host content. Day 147 changes the audience (the claim in seminar, then the same claim written as a letter to a school newspaper about a poll), and day 154 is the talk-about-language and self-check day (why 'within the margin of error' can make two different numbers the same).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed. On the host calendar: Day 133: If later: days 133 to 136 come before Algebra II opens unit 7, so they read study reports for their language (who was asked, how many); the inference work starts day 137. The second host opens on day 137, and the days that read it sit on or after that day. Algebra II opens unit 7 today: the inference work (significance and margin of error) starts here. Longer units (here 25 days) add a second host passage, a stage-labeling day, a seminar and peer reading, by the row's load (an LA row weighs most).

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 134). No mid-unit assessment (25 days, not over 25). End-of-unit assessment on days 155 and 156: the interpretive part on a new short poll report (invented for practice): judge its claim; the talk task (argue in a seminar), heard in seminars of three; the writing task, the written argument. Response time: respond day 157.

**Candidate cells.** PRIME Depth.KLU, claims with stated uncertainty: kept, 0 added days (day 135).

**Sensitive ground and home language.** Polls are on school topics, never on immigration. Methods stay within Algebra II unit 7. Home language: significativo and significant, margen de error and margin of error are cognates. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, Algebra II unit 7's significance and margin of error (Algebra II days 137 to 157); language taught, argue with 'The result might ___, although ___' and 'Within the margin of error, ___'.

### Grade 11 course-level checks

- **Grade 11 mid-year check** (days 81 and 82, respond day 83, week 17), after unit 23: samples units 19, 20, 21, 22 on new content (a new passage with a structural break (name the choice), a new essay passage (outline its structure), a new orbit explanation (order its causes) and a new founding-era passage (name its audience)), then an interview recount or a case to an adult and a short written synthesis or argument paragraph. Unit 23's end-of-unit record is carried unscored, not collected again; because the check comes right after that assessment, its items come from the earlier units only, and no task form from unit 23's last two weeks repeats.
- **Grade 11 year-end check** (days 158 and 159, respond day 160, week 32), after unit 27: samples units 23, 24, 25, 26 on new content (a new account (sort change from continuity), a new pair of sources (judge one claim's reliability), a new published claim (judge it) and a new periodic data set (name its model's parts)), then a seminar talk task and one written explanation or argument. Unit 27's end-of-unit record is carried unscored, not collected again; because the check comes right after that assessment, its items come from the earlier units only, and no task form from unit 27's last two weeks repeats.

## Grade 12 (course days 481 to 640)

Grade 12 is the owner year of cluster 9-12: every grade 12 unit names, in our words, every part of its owned ids, and its end-of-unit task samples every part (a prompt per interpretive part, each expressive stage scored). Levels 3 and 4 work from the model alone. Its hosts: ELA grade 12, US Government and Politics (fall) and Economics (spring, not used), and for math and science a shared host with each student's own course (the frame's Grade 12 hosts). Talk routine: 'propose, concede, hold'.

| Unit | Days of the year | Course days | Weeks | Key language use | Ids (cluster 9-12) | Kinds U/F/A/C/R |
|---|---|---|---|---|---|---|
| 28. The personal statement | 1 to 16 | 481 to 496 | 1 to 4 | narrate | LA Narrate (both modes), owned | 4/2/7/2/1 |
| 29. Ambition against ambition | 17 to 33 | 497 to 513 | 4 to 7 | explain | SS Explain (both modes), owned | 4/2/8/2/1 |
| 30. The water you drink | 34 to 49 | 514 to 529 | 7 to 10 | explain | SC Explain (both modes), owned | 4/2/7/2/1 |
| 31. Method and plan | 50 to 64 | 530 to 544 | 10 to 13 | explain | MA Explain (both modes), owned | 5/2/5/2/1 |
| 32. Policy in the news | 65 to 77 | 545 to 557 | 13 to 16 | argue | SS Argue (both modes), owned | 4/2/4/2/1 |
| 33. Defining the terms | 81 to 100 | 561 to 580 | 17 to 20 | inform | LA Inform (both modes), owned | 6/3/8/2/1 |
| 34. Is it justified? | 101 to 118 | 581 to 598 | 21 to 24 | argue | MA Argue (both modes), owned | 4/3/8/2/1 |
| 35. Can the model be trusted? | 119 to 136 | 599 to 616 | 24 to 28 | argue | SC Argue (both modes), owned | 4/3/8/2/1 |
| 36. The senior argument | 137 to 157 | 617 to 637 | 28 to 32 | argue | LA Argue (both modes), owned | 4/3/11/2/1 |

### Unit 28. The personal statement (days 1 to 16, weeks 1 to 4)

*How does a writer turn one moment into who they became, and how do we tell it to a reader who decides?* Host: ELA grade 12 unit 1's narrative writing and seminar (ELA days 1 to 15). Ids: WIDA.ELD-LA.9-12.Narrate, Interpretive and Expressive (owned here); SI: g12-si-narrate (the unit's own SI row).

**Arc.** Day 1 hooks on the question and names narrate openly (what it is for, where the host asks for it, its stages). Day 2 opens with the retrieval task, then takes apart Twain's 'Two Views of the Mississippi' (1883). Day 3 is a Language Dive on tense shifts on purpose and 'I came to see ___', with 'At the time, I was responsible for ___' beside it. Day 5 teaches the SI move (recount an experience for a college, job or program interview, then retell it in an email). Day 6 builds a polished narrative for a real reader (a personal statement, or a story on a chosen topic, real or invented) with the teacher; day 8 is the first independent piece. Day 9 changes the audience (the interview aloud, then the same experience as an email), and day 10 is the talk-about-language and self-check day (how a tense shift on purpose tells a reader the writer has changed). The writing evidence is a product: draft on day 11, the teacher's written feedback on day 12, revision on day 13.

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed.

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 2). No mid-unit assessment (16 days, not over 25). End-of-unit assessment on days 14 and 15: the interpretive part on a new short reflective passage (Curio Class's own selection, public domain; checked unused in docs/ and data/, including section plans and items.csv, before it is written in): name its turning point and tone; the talk task (answer an interview question in a seminar), heard in seminars of three; the writing evidence is the revised piece from day 13. Every part is sampled: interpretive (how the writer orients the reader; how the structure (before and after) builds meaning; where the turning point sits; how tone and the closing reflection carry the meaning), each with its own prompt; expressive (orient the reader; develop events with chosen detail; build to a turning point; shape structure and tone for that reader; close on a resolution or reflection; revise voice after feedback), each scored. Response time: respond day 16.

**Candidate cells.** PRIME Match.LE, every part of the owned ids sampled in the end-of-unit task: kept, 0 added days (days 13 to 15). Bar item 10: kept, 0 added days (day 9, the change-of-audience day).

**Sensitive ground and home language.** No student is asked or nudged to write about migration, loss or hardship; an invented applicant and an invented story are always allowed; the teacher reads drafts privately. Home language: the home language may carry the plan; revisar and revise are cognates. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, ELA grade 12 unit 1's narrative writing and seminar (ELA days 1 to 15); language taught, narrate with tense shifts on purpose and 'I came to see ___' and 'At the time, I was responsible for ___'.

### Unit 29. Ambition against ambition (days 17 to 33, weeks 4 to 7)

*How do checks and balances work, and what limits each branch?* Host: US Government and Politics unit 3's federalism (days 16 to 22) and unit 4's checks and balances (from day 23). Ids: WIDA.ELD-SS.9-12.Explain, Interpretive and Expressive (owned here); SI: g11-si-explain (an SI review use).

**Arc.** Day 17 hooks on the question and names explain openly (what it is for, where the host asks for it, its stages). Day 18 opens with the retrieval task, then takes apart a short sourced account of federalism dividing power (US Government and Politics unit 3). Day 19 is a Language Dive on '___ is limited by ___', and day 22 adds 'When ___, ___ results'. Day 21 uses again the SI move (explain to a partner which check matters most and why). Day 23 builds an explanation of how checks and balances limit power with the teacher; day 26 is the first independent piece; day 25 reads a short sourced account of one real check (a veto and its override, a court ruling on a law); day 28 applies the forms to it; day 27 is a seminar on the host content. Day 29 changes the audience (the system to a partner, then the same system written as a civics fair handout), and day 30 is the talk-about-language and self-check day (why 'is limited by' puts the check first in the reader's mind).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed. The second host opens on day 23, and the days that read it sit on or after that day. US Government and Politics opens unit 4 today: the branches and a real check are used from here; the days before explained how federalism divides power.

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 18). No mid-unit assessment (17 days, not over 25). End-of-unit assessment on days 31 and 32: the interpretive part on a new short account of one check (Curio Class's own, sourced): map its causes; the talk task (explain in a seminar), heard in seminars of three; the writing task, the written explanation. Every part is sampled: interpretive (the parts of the system; the causes and their order; how the writer frames them), each with its own prompt; expressive (introduce the system and its context; set out the weighted causes with evidence from the sources; close on what the system cannot do, naming a limit), each scored. Response time: respond day 33.

**Candidate cells.** PRIME Depth.ELD, 'is limited by' as a feature with a job: kept, 0 added days (day 19).

**Sensitive ground and home language.** Cases are chosen from several and kept balanced across parties; no student is asked their family's views. Levels 1 and 2 use the cloze 'When one branch ___, another branch can ___.' in place of the row's demand cloze, since Economics is not used. Home language: equilibrio de poderes is the Spanish name; rama and branch, veto and veto are close. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, US Government and Politics unit 3's federalism (days 16 to 22) and unit 4's checks and balances (from day 23); language taught, explain with '___ is limited by ___' and 'When ___, ___ results'.

### Unit 30. The water you drink (days 34 to 49, weeks 7 to 10)

*How does a lake's bloom reach a city's tap?* Host: Environmental Science unit 3's water quality (days 34 to 51), shared; Earth and Space Science unit 3 (Cascadia's earthquake) for its students; Physics unit 3 (grade 11 orbits, retrieved) for a student in no grade 12 science. Ids: WIDA.ELD-SC.9-12.Explain, Interpretive and Expressive (owned here); SI: g11-si-inform (an SI review use).

**Arc.** Day 34 hooks on the question and names explain openly (what it is for, where the host asks for it, its stages). Day 35 opens with the retrieval task, then takes apart the environmental science pages on the 2014 Toledo water event. Day 36 is a Language Dive on '___ is driven by ___', and day 39 adds '___ contributes to ___, which may ___'. Day 38 uses again the SI move (give an orientation to younger students on the school's water fountain test). Day 40 builds an explanation of the system, then the same kind of explanation on the student's own course's system with the teacher; day 43 is the first independent piece; day 42 reads each student's own course system (water quality, the earthquake system, or orbits); day 44 applies the forms to it. Day 45 changes the audience (the explanation to a partner, then the same explanation written as a public notice), and day 46 is the talk-about-language and self-check day (how 'is driven by' and 'contributes to' weigh a cause differently).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed.

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 35). No mid-unit assessment (16 days, not over 25). End-of-unit assessment on days 47 and 48: the interpretive part on a new short system account (Curio Class's own, from public sources): map its causes; the talk task (explain in a seminar), heard in seminars of three; the writing task, the written explanation. Every part is sampled: interpretive (the system's parts; the chain of causes from farm nutrients to tap; the evidence behind each link), each with its own prompt; expressive (introduce the event; model the relationships on a weighted cause chain; develop the explanation with the host's evidence; name its limits), each scored. Response time: respond day 49.

**Candidate cells.** PRIME Breadth.LE, the shared host plus each student's own course: kept, 0 added days (days 42 and 44).

**Sensitive ground and home language.** No task asks whether a student's home water is safe. Levels 1 and 2 use the cloze '___ contributes to ___ because ___.' with a labeled model of their own course's system. Home language: circulación and circulation, sistema and system are cognates. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, Environmental Science unit 3's water quality (days 34 to 51), shared; Earth and Space Science unit 3 (Cascadia's earthquake) for its students; Physics unit 3 (grade 11 orbits, retrieved) for a student in no grade 12 science; language taught, explain with '___ is driven by ___' and '___ contributes to ___, which may ___'.

### Unit 31. Method and plan (days 50 to 64, weeks 10 to 13)

*How did the method get from the question to the answer, and what is your plan?* Host: Statistics unit 10's investigation plan (retrieved), shared; Calculus related rates (retrieved); Precalculus unit 4 (alongside); Algebra II unit 5 (grade 11, retrieved) for a student in no grade 12 math. Ids: WIDA.ELD-MA.9-12.Explain, Interpretive and Expressive (owned here); SI: g12-si-explain (the unit's own SI row).

**Arc.** Day 50 hooks on the question and names explain openly (what it is for, where the host asks for it, its stages). Day 51 opens with the retrieval task, then takes apart a worked statistical investigation plan from the Statistics pages. Day 52 is a Language Dive on purpose clauses ('in order to', 'so that'), and day 55 adds 'My plan is to ___. One option is ___'. Day 54 teaches the SI move (explain a plan, one's own or an invented student's, for a project, a program or the year after high school, in talk and then in a short written statement). Day 56 builds a method explained from goal to conclusion, then a method from the student's own course, and a plan statement with the teacher; day 58 is the first independent piece; day 59 applies the forms to it. Day 60 changes the audience (the plan to a counselor (the teacher), then the same plan in writing), and day 61 is the talk-about-language and self-check day (how 'so that' and 'in order to' turn a list of steps into a method).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed.

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 51). No mid-unit assessment (15 days, not over 25). End-of-unit assessment on days 62 and 63: the interpretive part on a new short worked method (Curio Class's own): name its key step; the talk task (explain a method in a seminar, then state a plan for an invented student (goal, next steps, reasons and one other option)), heard in seminars of three; the writing task, the method explanation and the plan statement (SI look-fors recorded apart from the MA look-fors). Every part is sampled: interpretive (the goal; each step and why it comes where it does; two methods for the same question compared), each with its own prompt; expressive (introduce the question; describe and justify each step; describe the data or model; conclude with what the result means and which step matters most), each scored. Response time: respond day 64.

**Candidate cells.** PRIME Match.ELD.2-5, explain across four math courses: kept, 0 added days (day 59, the own-course application day).

**Sensitive ground and home language.** A student may plan as an invented student; no task asks about documents, aid eligibility or a family's situation. Methods stay within each student's own course. Home language: método and method, opción and option are cognates. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, Statistics unit 10's investigation plan (retrieved), shared; Calculus related rates (retrieved); Precalculus unit 4 (alongside); Algebra II unit 5 (grade 11, retrieved) for a student in no grade 12 math; language taught, explain with purpose clauses ('in order to', 'so that') and 'My plan is to ___. One option is ___'.

### Unit 32. Policy in the news (days 65 to 77, weeks 13 to 16)

*Which side of one policy debate has the stronger case, and how do we lead the talk?* Host: US Government and Politics unit 8's policy debates (days 64 to 71). Ids: WIDA.ELD-SS.9-12.Argue, Interpretive and Expressive (owned here); SI: g12-si-argue (the unit's own SI row).

**Arc.** Day 65 hooks on the question and names argue openly (what it is for, where the host asks for it, its stages). Day 66 opens with the retrieval task, then takes apart two short sourced positions on one policy. Day 67 is a Language Dive on 'I propose ___', 'That is a fair point, but ___', 'I still believe ___', with 'One trade-off is ___' beside it. Day 69 teaches the SI move (lead a short discussion and argue for a proposal, conceding a point and holding the main claim). Day 70 builds an argument for one side, and a proposal led in discussion with the teacher; day 72 is the first independent piece. Day 73 changes the audience (the proposal to a student council, then the same proposal written as a letter to a local official), and day 74 is the talk-about-language and self-check day (why conceding a point can make the main claim stronger).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed. On the host calendar: Day 72: The government course moves to its unit 8 check (day 72); the positions already read stay in use. Tight at 13 days (the frame): Fluency stays on the forms the unit owns, and review forms go to the respond day.

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 66). No mid-unit assessment (13 days, not over 25). End-of-unit assessment on days 75 and 76: the interpretive part on two new short positions (Curio Class's own, sourced): judge their evidence; the talk task (lead a short discussion), heard in seminars of three; the writing task, the written argument. Every part is sampled: interpretive (each claim; its evidence; what it concedes; whether the sources corroborate), each with its own prompt; expressive (introduce the claim and its context; develop it with evidence from sources; answer the counterargument; name a trade-off and a limit; conclude), each scored. Response time: respond day 77.

**Candidate cells.** PRIME Depth.KLU: kept, 0 added days (the stages named on day 66). Bar item 4, leading a discussion: kept, 0 added days (days 69 and 75).

**Sensitive ground and home language.** Topics are chosen from several; immigration or enforcement policy is never put to a class vote, and no student is asked to argue a side that touches their family. Home language: política (both policy and politics) is named. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, US Government and Politics unit 8's policy debates (days 64 to 71); language taught, argue with 'I propose ___', 'That is a fair point, but ___', 'I still believe ___' and 'One trade-off is ___'.

### Unit 33. Defining the terms (days 81 to 100, weeks 17 to 20)

*How does a formal text define what it means, and how do we write and ask in a formal register?* Host: ELA grade 12 unit 5's Du Bois and Woolf (ELA days 72 to 82) and unit 6's public words (from ELA day 87). Ids: WIDA.ELD-LA.9-12.Inform, Interpretive and Expressive (owned here); SI: g12-si-inform (the unit's own SI row).

**Arc.** Day 81 hooks on the question and names inform openly (what it is for, where the host asks for it, its stages). Day 82 opens with the retrieval task, then takes apart one section of Du Bois's The Souls of Black Folk (1903, chapter 1). Day 83 is a Language Dive on '___ refers to ___' and '___ is defined as ___', and day 86 adds 'Would it be possible to ___?'. Day 85 teaches the SI move (write and say a formal message for an adult setting (an email to a teacher, a request to an office)). Day 87 builds one informative section that defines, synthesizes and concludes, and a formal message with the teacher; day 90 is the first independent piece; day 89 reads a speech from ELA unit 6's public words; day 94 applies the forms to it; day 93 is a seminar on the host content. Day 95 changes the audience (the term explained to a classmate, then the email to an office), and day 97 is the talk-about-language and self-check day (how 'refers to' and 'is defined as' differ in what they promise).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed. On the host calendar: Day 81: If later: days 81 to 86 take Du Bois apart before ELA opens unit 6 on ELA day 87 (ELA is in its unit 5 check on days 83 to 86). The second host opens on day 87, and the days that read it sit on or after that day. ELA opens unit 6 today: its public speeches are used from here as the second source. Longer units (here 20 days) add a second host passage, a stage-labeling day, a seminar and peer reading, by the row's load (an LA row weighs most).

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 82). No mid-unit assessment (20 days, not over 25). End-of-unit assessment on days 98 and 99: the interpretive part on a new short formal passage (Curio Class's own selection, public domain; checked unused in docs/ and data/, including section plans and items.csv, before it is written in): name how it defines its term; the talk task (make the formal request aloud to the teacher, who plays the office), heard in seminars of three; the writing task, the section and the formal email. Every part is sampled: interpretive (how it defines a term; how its structure develops the idea; how its formal register works), each with its own prompt; expressive (introduce and define terms; synthesize two or more sources with quotations worked in; keep a formal register; conclude), each scored. Response time: respond day 100.

**Candidate cells.** PRIME Match.LE, every part of the owned ids: kept, 0 added days (days 98 and 99). Bar item 3, Latin-root cognates at the word dimension: kept, 0 added days (day 84).

**Sensitive ground and home language.** Du Bois writes of race and exclusion: taught as a text, and no student is asked to speak for a group. A student 18 or over may write the formal email in their own name. Home language: definir and define, sintetizar and synthesize are cognates. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, ELA grade 12 unit 5's Du Bois and Woolf (ELA days 72 to 82) and unit 6's public words (from ELA day 87); language taught, inform with '___ refers to ___' and '___ is defined as ___' and 'Would it be possible to ___?'.

### Unit 34. Is it justified? (days 101 to 118, weeks 21 to 24)

*What does the test let us conclude, and on what assumptions?* Host: Statistics unit 7's testing a proportion (days 93 to 116), shared; Calculus unit 4, Precalculus unit 3 and Algebra II unit 7 (grade 11) retrieved for their students. Ids: WIDA.ELD-MA.9-12.Argue, Interpretive and Expressive (owned here); SI: g12-si-narrate (an SI review use).

**Arc.** Day 101 hooks on the question and names argue openly (what it is for, where the host asks for it, its stages). Day 102 opens with the retrieval task, then takes apart two short conclusions from one test. Day 103 is a Language Dive on 'We can conclude ___, assuming ___', and day 106 adds 'Although ___, this might ___'. Day 105 uses again the SI move (recount in an email how a test was run so its limits show). Day 107 builds an argued conclusion with its assumptions and limits, then one from the student's own course with the teacher; day 110 is the first independent piece; day 109 reads each student's own course argue unit; day 113 applies the forms to it; day 112 is a seminar on the host content. Day 114 changes the audience (the conclusion in seminar, then the same conclusion written as a short report for a school club that ran a survey), and day 115 is the talk-about-language and self-check day (how 'assuming' opens a door for a critic).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed.

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 102). No mid-unit assessment (18 days, not over 25). End-of-unit assessment on days 116 and 117: the interpretive part on a new short test report (invented for practice): judge its conclusion; the talk task (argue in a seminar), heard in seminars of three; the writing task, the written argument. Every part is sampled: interpretive (each conclusion's claim; its assumptions; whether the evidence is strong enough), each with its own prompt; expressive (state a precise claim; name the assumptions; justify it from the evidence; answer a critique; conclude with its limits), each scored. Response time: respond day 118.

**Candidate cells.** PRIME Depth.PLD, one task at three entry points across four courses: kept, 0 added days (day 113, the own-course application day).

**Sensitive ground and home language.** Survey topics are school topics, never immigration. Methods stay within each student's own course. Home language: concluir and conclude are cognates; suposición and assumption are close. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, Statistics unit 7's testing a proportion (days 93 to 116), shared; Calculus unit 4, Precalculus unit 3 and Algebra II unit 7 (grade 11) retrieved for their students; language taught, argue with 'We can conclude ___, assuming ___' and 'Although ___, this might ___'.

### Unit 35. Can the model be trusted? (days 119 to 136, weeks 24 to 28)

*Does a simple climate model explain the ice record, and what is the trade-off in an energy choice?* Host: Earth and Space Science unit 7's climate model test (days 107 to 123), shared; Environmental Science unit 4 and Physics unit 7 (grade 11) retrieved for their students. Ids: WIDA.ELD-SC.9-12.Argue, Interpretive and Expressive (owned here); SI: g12-si-argue (an SI review use).

**Arc.** Day 119 hooks on the question and names argue openly (what it is for, where the host asks for it, its stages). Day 120 opens with the retrieval task, then takes apart two short claims about whether a simple model matches the Greenland ice-core record. Day 121 is a Language Dive on 'Although ___, the evidence clearly ___', and day 124 adds 'One trade-off is ___'. Day 123 uses again the SI move (concede a fair point about uncertainty and hold the claim). Day 125 builds an argued claim with evidence, a trade-off, limits and a rebuttal, then one from the student's own course (an energy choice's trade-off for environmental science) with the teacher; day 128 is the first independent piece; day 127 reads each student's own course claim (the energy transition, or the wave-particle question); day 131 applies the forms to it; day 130 is a seminar on the host content. Day 132 changes the audience (the claim in seminar, then the same claim written as a public comment to a town energy board), and day 133 is the talk-about-language and self-check day (how 'clearly' after 'although' keeps the claim standing).

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed. On the host calendar: Day 124: Earth and Space Science closes unit 7 on its day 123; from here the unit runs just after its host on the record already read.

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 120). No mid-unit assessment (18 days, not over 25). End-of-unit assessment on days 134 and 135: the interpretive part on a new short model-and-data pair (invented for practice): judge the claim; the talk task (argue in a seminar), heard in seminars of three; the writing task, the written argument. Every part is sampled: interpretive (each claim; the evidence each uses; the other explanation it must answer), each with its own prompt; expressive (introduce the claim; support it with evidence and reasoning; weigh a trade-off and the uncertainty; answer a rebuttal; conclude), each scored. Response time: respond day 136.

**Candidate cells.** PRIME Breadth.KLU, argue on the science standard in the owner year: kept, 0 added days (days 119 to 136).

**Sensitive ground and home language.** Climate content can worry students: the unit names what people are doing and keeps to the host's evidence. Home language: incertidumbre and uncertainty share a root but look different, so the word card carries it. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, Earth and Space Science unit 7's climate model test (days 107 to 123), shared; Environmental Science unit 4 and Physics unit 7 (grade 11) retrieved for their students; language taught, argue with 'Although ___, the evidence clearly ___' and 'One trade-off is ___'.

### Unit 36. The senior argument (days 137 to 157, weeks 28 to 32)

*How does a speech concede and rebut, and how do we answer the strongest objection to our own claim?* Host: ELA grade 12 unit 8's senior research project (ELA days 125 to 160). Ids: WIDA.ELD-LA.9-12.Argue, Interpretive and Expressive (owned here); SI: g12-si-argue (an SI review use).

**Arc.** Day 137 hooks on the question and names argue openly (what it is for, where the host asks for it, its stages). Day 138 opens with the retrieval task, then takes apart one paragraph of Roosevelt's First Inaugural Address (1933, retrieved from ELA unit 6). Day 139 is a Language Dive on 'Granted, ___. Nevertheless, ___', and day 142 adds 'Admittedly ___, but ___'. Day 141 uses again the SI move (defend the paragraph's claim in a short panel). Day 143 builds one argument paragraph for the student's senior project's real audience with the teacher; day 145 is the first independent piece; day 148 applies the forms to it. Day 146 changes the audience (the claim for the class panel, then the same claim for the project's real reader), and day 154 is the talk-about-language and self-check day (how 'granted' and 'admittedly' differ in how much they give away). The writing evidence is a product: draft on day 150, the teacher's written feedback on day 151, revision on day 152.

**Why this order.** The model is taken apart before it is built with the teacher and made alone (bar item 9); each form is shown in the host text before it is rehearsed; talk comes before writing every day; the change of audience follows the first independent piece, so students have something to change and can say what they changed.

**Assessments.** No readiness check (every assumed row was taught the year before or earlier this year; retrieval on day 138). No mid-unit assessment (21 days, not over 25). End-of-unit assessment on days 155 and 156: the interpretive part on a new short speech paragraph (Curio Class's own selection, public domain; checked unused in docs/ and data/, including section plans and items.csv, before it is written in): mark its concession and rebuttal; the talk task (defend a claim in a seminar), heard in seminars of three; the writing evidence is the revised piece from day 152. Every part is sampled: interpretive (its claim; how it concedes; how it rebuts; how its evidence and appeals reach its audience), each with its own prompt; expressive (introduce the claim in context; develop it with evidence; concede a point; rebut the strongest objection; conclude; revise once after written feedback), each scored. Response time: respond day 157.

**Candidate cells.** PRIME Depth.KLU: kept, 0 added days (the stages named on day 137). California 3.5, the student's own judgment of their progress over four years on the self-check: kept, 0 added days (day 154, the self-check day).

**Sensitive ground and home language.** Senior project questions are the student's own: no student is nudged toward migration, loss or hardship. Home language: conceder and concede are cognates; refutación and rebuttal are close. The unit's fresh sensitivity read, and the Spanish read of its family note, come with the unit plan.

**Host-teacher note** (bar item 14): content used, ELA grade 12 unit 8's senior research project (ELA days 125 to 160); language taught, argue with 'Granted, ___. Nevertheless, ___' and 'Admittedly ___, but ___'.

### Grade 12 course-level checks

- **Grade 12 mid-year check** (days 78 and 79, respond day 80, week 16), after unit 32: samples units 28, 29, 30, 31 on new content (a new reflective passage (turning point and tone), a new account of a check (map its causes), a new system account (map its causes) and a new worked method (name its key step), each at the owner year's demand with no sentence frame for levels 3 and 4), then an interview answer or a plan and a short written narrative opening or explanation. Unit 32's end-of-unit record is carried unscored, not collected again; because the check comes right after that assessment, its items come from the earlier units only, and no task form from unit 32's last two weeks repeats.
- **Grade 12 year-end check** (days 158 and 159, respond day 160, week 32), after unit 36: samples units 32, 33, 34, 35 on new content (two new short policy positions (judge their evidence), a new formal passage (how it defines its term), a new test report (judge its conclusion) and a new model-and-data pair (judge the claim), at the owner year's demand), then a seminar talk task and one written argument or formal section. Unit 36's end-of-unit record is carried unscored, not collected again; because the check comes right after that assessment, its items come from the earlier units only, and no task form from unit 36's last two weeks repeats.

## Course-level checks

| Check | Days of the year | Course days | Week | Units sampled | Ids sampled (cluster 9-12, both modes, plus SI) |
|---|---|---|---|---|---|
| Grade 9 mid-year | 81, 82; respond 83 | 81 to 83 | 17 | 1, 2, 3 | LA Narrate, SC Explain, MA Explain; SI Explain |
| Grade 9 year-end | 158, 159; respond 160 | 158 to 160 | 32 | 4, 5, 6, 7, 8 | SC Argue, MA Argue, LA Argue, LA Inform, SS Explain; SI Argue |
| Grade 10 mid-year | 81, 82; respond 83 | 241 to 243 | 17 | 10, 11, 12, 13 | SC Explain, SS Explain, MA Argue, LA Narrate; SI Narrate |
| Grade 10 year-end | 158, 159; respond 160 | 318 to 320 | 32 | 14, 15, 16, 17 | LA Argue, MA Explain, SC Argue, LA Inform; SI Argue |
| Grade 11 mid-year | 81, 82; respond 83 | 401 to 403 | 17 | 19, 20, 21, 22 | LA Narrate, LA Inform, SC Explain, LA Argue; SI Argue |
| Grade 11 year-end | 158, 159; respond 160 | 478 to 480 | 32 | 23, 24, 25, 26 | SS Explain, SS Argue, SC Argue, MA Explain; SI Explain |
| Grade 12 mid-year | 78, 79; respond 80 | 558 to 560 | 16 | 28, 29, 30, 31 | LA Narrate, SS Explain, SC Explain, MA Explain; SI Explain |
| Grade 12 year-end | 158, 159; respond 160 | 638 to 640 | 32 | 32, 33, 34, 35 | SS Argue, LA Inform, MA Argue, SC Argue; SI Argue |

Each check runs as the frame sets it: the teacher reads each new text aloud once and students read it again; the writing task goes to the whole class; the talk task is heard in seminars of three, about six minutes a group, while the others write, so each of 30 students is heard once over the two days. The respond day groups students by form and entry point (at most four groups). Every check comes right after its unit's end-of-unit assessment, so its items come from the earlier units and that unit's record is carried, not collected again.

**Owned codes on a check.** The 18 owned ids are grade 12's. Sixteen are sampled on a grade 12 check: LA Narrate, SS Explain, SC Explain and MA Explain (both modes) at mid-year; SS Argue, LA Inform, MA Argue and SC Argue (both modes) at year-end. WIDA.ELD-LA.9-12.Argue.Interpretive and WIDA.ELD-LA.9-12.Argue.Expressive are not: unit 36 is the band's last unit and ends on day 157, right before the year-end check, which draws from the earlier units so it does not repeat the assessment just given (the frame's stated cost). They are assessed in full by unit 36's end-of-unit task (every part, with the revised paragraph as the writing evidence) and sampled in carried form on the grade 9, 10 and 11 checks (grade 9 year-end, grade 10 year-end and grade 11 mid-year). The same cost falls on units 9 (SS Argue), 18 (SS Argue) and 27 (MA Argue) in their years; each is checked again the next year through the matching unit's retrieval and that year's check.

## Shorter path

Nothing assessed and no owned part is cut on any path below: end-of-unit days, respond days, course-level checks, the retrieval days and every first teaching of a form stay.

**A shorter period** (30 to 40 minutes, where a school has less time). The talk set-up and the exit ticket stay every day. A Fluency day keeps its oral rehearsal and drops the word sort to the next day's opening (5 minutes); an Application day keeps the talk and moves the writing past the first two sentences to the next day's opening; a Language Dive takes one sentence, not two. End-of-unit and check days keep their parts and spread the seminars over a third day where the period is under 35 minutes, taken from the unit's next fold-in day below.

**A year about 10 days short.** Each year names ten fold-in days, none assessed and none a first teaching: each one's core (about 8 minutes of rehearsal or one rewritten sentence) moves into the next day's opening, so each saves 45 minutes of class time and costs the next day 8, a net of 37 minutes. Ten a year save 10 course days (450 minutes, 370 net), so a year of 150 days holds every unit's assessed and owned work against the frame's 160.

- Grade 9: day 11 (unit 1, word work, into the next day's opening); day 16 (unit 1, talk-task rehearsal, into the self-check day's rehearsal); day 17 (unit 1, second independent piece, into the next day's talk round); day 18 (unit 1, peer read, into the self-check day's revision); day 19 (unit 1, sentence building, into the next day's opening); day 20 (unit 1, second change of purpose, into the change-of-audience day's last minutes); day 35 (unit 2, word work, into the next day's opening); day 53 (unit 3, word work, into the next day's opening); day 71 (unit 4, word work, into the next day's opening); day 76 (unit 4, peer read, into the self-check day's revision). Ten days, 45 minutes each.
- Grade 10: day 73 (unit 14, word work, into the next day's opening); day 74 (unit 14, seminar on the host content, into the change-of-audience day's talk round); day 94 (unit 15, seminar on the host content, into the change-of-audience day's talk round); day 110 (unit 16, word work, into the next day's opening); day 111 (unit 16, seminar on the host content, into the change-of-audience day's talk round); day 129 (unit 17, word work, into the next day's opening); day 130 (unit 17, stage labeling, into the first independent piece's planning, on the model); day 134 (unit 17, talk-task rehearsal, into the self-check day's rehearsal); day 135 (unit 17, second independent piece, into the next day's talk round); day 136 (unit 17, peer read, into the self-check day's revision). Ten days, 45 minutes each.
- Grade 11: day 126 (unit 26, talk-task rehearsal, into the self-check day's rehearsal); day 127 (unit 26, second independent piece, into the next day's talk round); day 128 (unit 26, peer read, into the self-check day's revision); day 143 (unit 27, word work, into the next day's opening); day 148 (unit 27, talk-task rehearsal, into the self-check day's rehearsal); day 149 (unit 27, second independent piece, into the next day's talk round); day 150 (unit 27, peer read, into the self-check day's revision); day 151 (unit 27, sentence building, into the next day's opening); day 152 (unit 27, second change of purpose, into the change-of-audience day's last minutes); day 153 (unit 27, small-group conferences, into the self-check day's revision). Ten days, 45 minutes each.
- Grade 12: day 27 (unit 29, seminar on the host content, into the change-of-audience day's talk round); day 91 (unit 33, word work, into the next day's opening); day 92 (unit 33, stage labeling, into the first independent piece's planning, on the model); day 96 (unit 33, peer read, into the self-check day's revision); day 108 (unit 34, review-form rehearsal, into the next day's opening); day 111 (unit 34, word work, into the next day's opening); day 112 (unit 34, seminar on the host content, into the change-of-audience day's talk round); day 126 (unit 35, review-form rehearsal, into the next day's opening); day 129 (unit 35, word work, into the next day's opening); day 130 (unit 35, seminar on the host content, into the change-of-audience day's talk round). Ten days, 45 minutes each.

**Seniors who leave early** (the frame, Grade 12 calendar). The year-end check and its respond day move to the seniors' last three days, and unit 36 folds up to 5 days in this order, never its end-of-unit assessment, its draft, feedback and revision days or its respond day: its Fluency days on review forms (days 144 and 147), the second change-of-audience day (day 153) and the second independent application days (days 148 and 149). A school whose seniors leave more than 5 days early places the 160 days so they end on the seniors' last day (CALENDAR.md).

**A left-out or swapped unit** (STANDARD section 3; Cory 2026-11-21). A school or family may swap a host text, keeping the unit's ids met; a unit whose host is about migration, war or loss (units 1, 8, 11, 13, 18, 19, 23, 24) previews it in the family note and says how to ask for the other text. A left-out unit's family note and the course page name the ids not claimed that year. Leave-out bridge: where a later unit uses a model a left-out unit introduced (the story map, unit 1; the cause chain, unit 2; the claim chart, unit 4; the text map, unit 7), that unit teaches the model's one-step form in its first ten minutes and claims none of the left-out unit's parts.

## Newcomer strand (20 days beside each year, outside the 160)

An added period with the ELD teacher, not a side table (Cory 2026-11-26, Desk q-frames-scope-1). A newcomer arriving at any point takes it, then joins the class's current unit at entry points 1 and 2 with the short catch-up card set for that unit. It works the four SI 4-12 ids and both WIDA.ELD-LA.9-12.Inform ids (Interpretive and Expressive) only. Its content is the school day and the current host unit's pictures and diagrams; each year uses its own grade's host unit, and grade 12 adds the formal email on day 18. A newcomer who needs early reading also uses the ELA K to 2 foundational rows, with a note. No day asks how a student came, a family's status or a parent's work; a student may speak about an invented student throughout. The strand gets its own sensitivity read before use.

| Strand day | What it is for | Ids |
|---|---|---|
| 1 | Greetings, names and asking for help ("Can you help me, please?") | SI Inform |
| 2 | Reading a class schedule: times, rooms, teachers, with picture cards | LA Inform Interpretive |
| 3 | Asking where a room is and giving one direction back | SI Inform |
| 4 | The locker, the lunch line and the bus: steps in order with first, then, last | SI Explain |
| 5 | Classroom words and the talk routine's first frame, said with a partner | SI Inform |
| 6 | Reading a picture-backed school notice: what, when, where | LA Inform Interpretive |
| 7 | Asking a teacher a question in class and saying "I do not understand ___" | SI Inform |
| 8 | Telling what I did today in the simple past, in order | SI Narrate |
| 9 | The counselor's office: making an appointment, greeting, reason, thanks | SI Inform |
| 10 | Reading the current host unit's labeled diagram with the teacher | LA Inform Interpretive |
| 11 | Naming the diagram's parts aloud and labeling a copy | LA Inform Expressive |
| 12 | Saying what I prefer and why, with because | SI Argue |
| 13 | Agreeing and disagreeing politely in a pair | SI Argue |
| 14 | Explaining a school procedure (signing in late, the fire drill route) to a partner | SI Explain |
| 15 | Writing a short caption for a host picture from a word bank | LA Inform Expressive |
| 16 | Telling a short school event in order for a classmate | SI Narrate |
| 17 | Reading a short host page with the teacher and pointing to the main idea | LA Inform Interpretive |
| 18 | Three sentences about the host topic from a word bank (grade 12: a short formal email to a teacher) | LA Inform Expressive; SI Inform |
| 19 | Strand look-fors: a short talk turn and a caption, seen or not yet on the paper sheet, no scores | all six ids |
| 20 | Joining the class: the catch-up card set for the current unit, a first turn in the class routine at entry points 1 and 2 | SI and the current unit's ids |

A student moves to entry points 1 and 2 when the teacher judges the strand's look-fors seen on two days in a row, or on the school's own check (STANDARD section 2).

## Leans on the calendar

Every host unit was checked against data/plans/calendar.csv (2026-11-26): each host runs on the course days the frame cites. The units that run just after or a little ahead of their host carry the frame's bridge in the day's note: unit 3 (Algebra I unit 2 ends day 46; unit 3 joins its last days and runs on with unit 3 of Algebra I), unit 8 (World History I unit 9 ends day 137), unit 16 (Chemistry unit 9 from day 113), unit 17 (ELA grade 10 unit 7 from day 128), unit 18 (World History II unit 11 from day 145), unit 20 (e11-info-structure used ahead of ELA grade 11 unit 3, day 35), unit 22 (ELA grade 11 unit 3 ends day 55), unit 23 (US History I unit 5 from day 72), unit 24 (US History I unit 5's argument days), unit 26 (Algebra II is in its unit 5 check and respond on days 110 to 112, so day 111 works on unit 5's models and day 112 reads the periodic model for its language one day ahead), unit 27 (Algebra II unit 7 from day 137), unit 29 (US Government unit 4 from day 23), unit 32 (US Government unit 8 ends day 71, its check day 72), unit 33 (ELA grade 12 unit 6 from day 87) and unit 35 (Earth and Space Science unit 7 ends day 123).

## For the lead

1. **End-of-unit days moved inside four units (frame wording to fix).** The frame puts the end-of-unit assessment of units 4, 14 and 23 on days 76 and 77 with the respond day 78, and unit 32's on days 73 and 74 with respond day 75, which would leave two teaching days after each unit's assessment and before the mid-year check, with nothing named for them. The frame lets the scope and sequence move days within a year, so here every unit closes the same way: units 4, 14 and 23 assess on days 78 and 79 and respond on day 80; unit 32 assesses on days 75 and 76 and responds on day 77. The frame's unit cells and its Course-level checks table ("Unit 4's end-of-unit record (days 76 and 77)", "Unit 32's end-of-unit record (days 73 and 74)") should read the new days. Unit days, order and owned rows are unchanged.
2. **Owner-year parts not yet checked against the printed pages** (frame item 2). The parts named on grade 12 days and in their end-of-unit tasks are the frame's reading; when the WIDA pages are opened, the goals and notes of units 28 to 36 are edited in place with them.
3. **Unit 24's newspaper pick.** The frame asks the scope and sequence to name it: a period report of the 1877 withdrawal of federal troops from the South Carolina or Louisiana statehouse, from Chronicling America (Library of Congress). The exact issue and page are not opened here; the unit plan writer picks and checks them as a browser check at grade close, checks the page unused in docs/ and data/, and keeps the frame's rules (no role play, the family note's preview).
4. **SI review rows from the year before.** Units 10, 21, 29 and 30 use an SI move whose own-year row is taught later in the year (g10-si-inform in unit 17, g11-si-explain in unit 23, g12-si-explain in unit 31, g12-si-inform in unit 33), so the review day retrieves the year before's row (in `retrieves`). Units 11 and 12 begin g10-si-explain and g10-si-argue, listed in `skills` there, and units 15 and 14 teach them in full. No frame change needed; recorded so the reads see it was chosen.
5. **Carried ids in `codes`.** Grades 9 to 11 list the carried cluster 9-12 ids in `codes` without the progression's `~`, and this page says once they are carried. If the gate or the skeleton should mark carried codes, the lead picks the form.
6. **Rule 2 check for ELD.** scripts/sequence.py's rule 2 notes and scripts/unit_skeleton.py cover the four core subjects only, so no script counted this course's retrieval; it was counted by hand from data/progressions/eld.csv (the table above).
7. **The frame's item 1 (C11 gate).** This scope was written on the after-core brief (Cory, "do the rest of the scopes and sequences", 2026-11-26); the unit plans, days and newcomer strand materials still wait as the frame says.


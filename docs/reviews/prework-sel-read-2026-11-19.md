# Social and emotional learning pre-work: cold read, 2026-11-19

Read as the curriculum expert (docs/agents/EXPERT.md) with the SEL lens (docs/agents/lenses/sel.md). I did not write these
drafts. Nothing was edited but this file. Confidence is Firm, Likely or Judgment call on each finding. Anything that rests
on my memory is marked "from memory". No outside source was opened (none was asked for), so nothing here rests on the
framework page or the criteria paper themselves.

## What I read

AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/sel.md; docs/ADOPTION-BAR-SUBJECTS.md (pass rule, C1 to C16, part 9,
the SEL row of "Before a scope and sequence", the sources table); docs/courses/sel/STANDARD.md and APPROACH.md;
data/standards/casel-5.txt; docs/APPROACH.md; docs/courses/UNIT-PLAN.md; docs/courses/health/APPROACH.md (finished page,
for comparison); docs/reviews/prework-computer-science-read-2026-11-19.md (format only). For stale-note and ownership
checks only: scripts/standards.py lines 90 to 140; scripts/progression.py lines 51 to 112 (STD_FILES, code_grades);
docs/PRODUCTION-PATH.md lines 118 to 130 (layer 4 rule); data/courses.csv line 41 and data/subjects.csv line 11;
docs/COURSES-STATUS.md SEL rows; one-line id existence checks in data/progressions/ela.csv and social-studies.csv for the
rows STANDARD.md section 7 names.

## Verdict

The standard is sound as a list: all 40 ids are real, unique, in our own words, and the counts match everywhere, and every
one of the 13 grade years teaches each of the 40 exactly once as a unit's own. The biggest risk is that it is not yet
usable for a progression: layer 4 requires every standard to be owned by exactly one grade, the draft gives every
sub-skill thirteen owners and no per-grade depth, and scripts/progression.py has no SEL support at all. The one change that
matters most is a settled ownership and depth rule (finding 1 and 2), plus a full eleven-field block in APPROACH.md
(finding 4), which today fills about half the slots and sends two fields to the wrong place.

## What I counted (so nobody has to again)

| Check | Result |
|---|---|
| Ids in casel-5.txt | 40, no duplicates; 40 distinct wordings; none under 15 characters |
| By competency | Self-Awareness 9, Self-Management 7, Social Awareness 8, Responsible Decision-Making 7, Relationship Skills 9 (matches file header and STANDARD.md short codes SA1 to SA9, SM1 to SM7, SO1 to SO8, RD1 to RD7, RS1 to RS9) |
| Grade table | 13 grade years (K to 12), each lists all 40 codes once, none missing, none repeated, none outside the set |
| Units per grade | 6 each |
| Ids per unit | K 5/4/5/5/9/12; G1 4/4/6/7/7/12; G2 5/5/5/5/9/11; G3 5/5/6/5/7/12; G4 5/6/6/7/7/9; G5 5/6/5/8/7/9; G6 5/6/4/7/6/12; G7 6/5/5/7/6/11; G8 5/6/6/6/5/12; G9 6/5/5/6/6/12; G10 4/5/6/5/8/12; G11 5/8/5/7/6/9; G12 5/6/6/8/7/8 |
| Unit 6 | holds 8 to 12 ids in every grade year, 11 or 12 in nine of the 13 |
| Validator | scripts/standards.py reads casel-5.txt (LISTED, lines 96 to 105; lookup at line 137), so a full id such as CASEL.Self-Awareness.3 is valid now |
| Cross-subject ids named in STANDARD.md section 7 | the ELA discussion rows and the four social studies rows exist in the progression files |

## Findings, most serious first

### 1. Layer 4 needs one owning grade per standard; SEL has thirteen, and no gate or rule bridges them

- **Where:** STANDARD.md section 3 ("every grade teaches all 40", "taught once and only once as a unit's own"); docs/PRODUCTION-PATH.md lines 121 to 125 ("every skill id is owned by exactly one grade", "every standard owned by one grade or excluded"); scripts/progression.py (STD_FILES and code_grades have no SEL entry; `~CODE` marks a row that applies a standard another row owns).
- **What is wrong:** The progression is the layer between the standard and the scope and sequence. For health, PE and computer science it gives a span or band, one owner grade, and `~` rows elsewhere. For SEL the page makes placement a property of the grade-year table and never says which grade owns or deepens a sub-skill. A progression writer has three bad options: 40 rows with no sensible owner, 520 owned rows the gate will reject as duplicates, or an invented rule. Two writers will pick differently.
- **Cost:** The progression cannot be written, or is written two ways. Everything downstream (the 13 frames, readiness checks that "name skill ids an earlier grade owns") inherits the gap.
- **Fix (add to STANDARD.md section 3, ours, untested):**

> **Ownership.** The progression has one owned row per sub-skill per band, so 40 ids by four bands is 160 owned rows. A band's owner year is its last grade (K, 5, 8, 12), the year the sub-skill is met at the band's full depth (see the depth ladder); the other years of the band carry the id as `~ID`, each with a one-line note on how that year differs. The grade-year table stays the placement, and every year still teaches all 40 once. Each row's `assumes` names the same sub-skill in the band before.

  Add `sel` to STD_FILES and ANCHOR in scripts/progression.py, with a code_grades rule that treats the four bands as spans, as health does. Confidence: Firm that a rule is missing; the 160-row form is a Judgment call (see For Cory 1).

### 2. Depth grows by band in one paragraph, but no per-sub-skill ladder exists, and grades within a band differ only by theme

- **Where:** STANDARD.md section 3 opening paragraph (picture-book scene, named strategy with reasons, choice under pressures, plan the student designs and judges); the three-grade bands K to 2, 3 to 5, 6 to 8; lens "Errors reviewers catch" (a grade year that repeats another year of its band with the same cases and the same depth).
- **What is wrong:** The depth sentence is one line for the whole standard. A writer cannot tell what SA6 or RS5 looks like in grade 4 as opposed to grade 3 or 5. Within a band the table varies the year theme and the unit grouping, but the depth is stated once for three grades. The same code can end up as the same case at the same depth three years running, which is the lens's first error and the bar's "a band taught the same way every year" fail.
- **Cost:** C1 (taught at the depth the wording asks) and C4 (each idea rests on the last) cannot be traced for any id.
- **Fix (add to STANDARD.md section 3 a ladder; example text, ours, untested):**

> **Depth ladder, by competency and band.** K to 2: a picture or story moment, one or two pictured steps, said aloud or acted with a teacher; the skill is named. 3 to 5: a named strategy with three or four steps and a reason, used on an invented case and then a planned class moment. 6 to 8: the strategy chosen among options, weighed against real pressures (friends, online, time), with a reason in writing. 9 to 12: a plan the student designs for an invented or chosen situation, with the trade-offs, and a judgement of how well it worked. Within a band: the first year uses cases from the school day, the second adds a second person's point of view, the third adds a cost or a pressure. Each sub-skill's `~` row names which of the three it is in that year.

  Also state what SO6 and SO8 are in grades 3 and 4 (the placement notes say "playground fairness in K to 2" and "unfair rules of the past from grade 5", so grades 3 and 4 have no stated case). Confidence: Firm.

### 3. The last unit of nearly every year is a catch-all, and the minutes cannot teach it

- **Where:** STANDARD.md section 2 (64 sessions, six units) and section 3 table.
- **What is wrong:** By my arithmetic (ours, untested): 64 sessions over six units is about ten to eleven sessions a unit. Take about three of those for the readiness item, end-of-unit assessment and respond day, and a unit has about eight teaching sessions. Unit 6 holds 12 ids in nine of the 13 grade years and 8 to 11 in the rest: one session or less per id, against 4 to 6 ids (about two sessions each) in units 1 to 4. Unit names make it worse. K "Good choices" carries all seven RD ids plus SM4 to SM7 and SO8; grade 8 "Making a difference" carries SA7, SA9, SM4, SM6, SM7, RS4, RS7, RS9, RD3, RD6, RD7 and SO8, across all five competencies, under a title that names one. The short path (32 sessions) makes it worse again: it says "named sessions to drop" and names none.
- **Cost:** Self-management and relationship skills must be practised by doing (item 5). One session per id leaves no rehearsal day, so the unit becomes talk about skills, the common failure in the lens. A planner who sees 12 ids will cut rehearsal first.
- **Fix:** Cap each unit at 8 ids and move the remainder forward into units 1 to 4, which hold 4 to 6. Where an id is better met late, keep it in unit 6 as a `~` return and not as "first taught". Name the 32-session short path's dropped sessions in each frame (ours: the second Application session in each unit). Confidence: Likely.

### 4. APPROACH.md fills about half the slots, and two of its field numbers are wrong

Compared with the health and computer science pages and UNIT-PLAN.md fields 1 to 10 (unit) and 1 to 11 (section):

| Slot | Verdict | Note |
|---|---|---|
| Unit 1 header | Filled | sessions by kind, sessions a week and minutes |
| Unit 2 standards, what is carried | Part | ids, skill names, cue words named; no rule for the model, the day it is withdrawn or the day the student first does it alone |
| Unit 3 where it sits | Missing | no builds-on, handoff strength or comes-back; the one link to the grade's core courses (bar item 9) has no field |
| Unit 4 readiness | Filled | one scenario item, ten-minute reteach |
| Unit 5 end-of-unit assessment | Filled | rehearsal plus scenario items with two samples; see finding 8 for the self-referential ids |
| Unit 6 error register | Filled | two good examples |
| Unit 7 response allocation | Missing | how the check is marked (teacher-judged by look-fors, so no hands-up self-marking), how groups come from the class sheet, the cap on respond-day groups |
| Unit 8 tools and supplies | Part | scene cards and stories only; no statement of what a tool may or may not do (C15), and no statement that no tool collects feelings |
| Unit 9 family note | Wrong place | the family activity is put in "Section field 10"; it belongs in unit field 9 |
| Unit 10 sources | Missing | no sources table, no read-status (finding 11), no logic-model line (C16) |
| Section 1 before you teach, sensitive topics | Filled | |
| Section 2 where it sits | Missing | |
| Section 3 checks | Filled | |
| Section 4 expected errors | Missing | wrong example beside right one, the day shown, what to do if many made it |
| Section 5 what is carried | Missing | the step card or cue: who holds the model each day, the day it is withdrawn (C7) |
| Section 6 days | Part | calm start in K to 5 only; no rule for how other days open, or that teaching comes before trying in K to 5 |
| Section 7 talk and writing | Filled | |
| Section 8 practice that returns | Missing | the page lists the principle ("Comes back") but fills no field; the health page does |
| Section 9 supports | Part | frames and a quiet option; see finding 6 |
| Section 10 two rooms | Wrong | the page puts the carry-out cue here; field 10 is "Two rooms" (a parent teaching one child at home; one projector). The cue has no home |
| Section 11 not in this section | Missing | |
| Pacing | Missing from the page | in STANDARD.md section 2 only |

- **Cost:** C7 (door-adjacent), C10, C11, C14, C15, C16 each lose a slot, and the carry-out cue (bar item 10) is written into the wrong field of every plan.
- **Fix (replace "What SEL adds to the unit and section plan fields" with a full block):** keep the existing lines that are right; add the missing ones in these words (ours, untested):

> **Unit field 3:** builds on (the same sub-skill one year before, handoff strong or weak); leads to; comes back; and the one link to this grade's core courses a teacher may use (an ELA discussion routine, a social studies civics row), named by its row id.
> **Unit field 7:** the end-of-unit rehearsal is judged by the teacher against the look-fors, so nothing is hands-up self-marked. Groups for the respond day come from the class sheet's "not yet" cells by step, capped at four; others rehearse in pairs from the step card. Marking time is stated as minutes a student times the class.
> **Unit field 9:** the family note, in English and Spanish: the skill's name and steps, the words the class uses, and one thing to try at home (the family activity).
> **Section field 4:** each expected error as a wrong example beside a right one (for example an I-statement that blames), with the day it is shown and the five to ten minute response if many made it.
> **Section field 5:** what is carried is the skill's step card. The teacher holds the model on the first session; pairs hold the card on the second; the card is withdrawn on the first Application session, which the plan names; the check is taken without it. K to 2 use the same steps as three or four pictured words said aloud.
> **Section field 6:** each day opens with a calm start routine or a retrieval question on an earlier skill, five minutes at most. In K to 5, new skills are taught before they are tried.
> **Section field 8:** practice that returns: one earlier skill, named, rehearsed for three minutes with its card.
> **Section field 10:** a parent teaching one child at the table: the skill rehearsed with the adult playing the other part; one projector: the scene card shown and acted by volunteers. The carry-out cue for the school day goes in field 5, as part of what is carried.
> **Pacing:** as STANDARD.md section 2.

  Confidence: Firm.

### 5. Bar part 9, items 1 to 13: answers on the pages

| Item | Answered? | Where, and what is lacking |
|---|---|---|
| 1 All five areas | Yes | STANDARD section 3 (every area every year) |
| 2 Sequence per grade | Yes | STANDARD section 3; progression owed (finding 1) |
| 3 For every student, in school hours | Part | Section 2 gives the session and the advisory period. "For every student" has no answer on a page: C10 supports are missing (finding 6) |
| 4 Sequenced | Part | the table sequences units; no depth ladder (finding 2) |
| 5 Active practice | Yes | STANDARD section 3 and APPROACH "Shows it, then has every student do it"; protect with finding 3 |
| 6 Focused and explicit | Yes | set time in section 2; "teaches one skill by name" in APPROACH |
| 7 Adult guidance, carry beyond the lesson | Part | adult guidance yes (before you teach); the carry-out cue is in the wrong field (finding 4) |
| 8 States no study | Yes | APPROACH "Where the evidence is thin"; the course-page line and logic model (C16) are not on the page |
| 9 One link to the grade's core courses | No | STANDARD section 7 names leans at course level; the approach has no unit field for it and the grade table does not name a link per unit |
| 10 Carry it out | Part | said, but in the wrong field |
| 11 Sessions a year, fidelity checklist, class record, no ratings of children | Part | sessions and class record yes; no page defines the teacher's fidelity checklist or says where it sits (unit field 8 or a course page) |
| 12 Equity within the promises | Part | Spanish family notes yes; bias as noticing own snap judgements yes (section 4 D); student voice in class and school life has no unit or session placement; neither is in APPROACH |
| 13 Before you teach | Yes | APPROACH section field 1 |

No item is wholly unanswered except 9; 3, 7, 10, 11 and 12 are part answers. Confidence: Firm.

### 6. The supports slot is thin: English learners, access, reading load, extension, check accommodations

- **Where:** APPROACH.md section field 9 (frames, picture cues, a quiet option); bar C10 and C11.
- **What is wrong:** One line. Nothing says which words are taught in depth (feelings words and words with more than one meaning: calm, cool down, stand up, pressure, mean, fair, bully), nothing separates a language gap from a content gap in a key, nothing on reading load, extension on the same skill, or check accommodations. The quiet option (rehearse with the teacher or in writing) is good and should be written as a rule that no student must speak aloud.
- **Cost:** C10 and C11 would fail; they are scored, and a part pass count over three fails the course.
- **Fix (add as a section, ours, untested):**

> **Supports.** English learners: each unit names six to eight words taught in depth with a picture, including feelings words and words with two meanings (cool down, stand up, pressure, mean), and a sentence frame for each skill step ("When you ___, I feel ___. I would like ___."). A key line says: the right step shown in the home language, pointing or acting is a language gap; a wrong step is a content gap. Access: no student must speak aloud or be watched while rehearsing; any rehearsal can be done in writing, with a card, or with the teacher. Reading load: students read a scene card of at most five short sentences alone (K to 2: read aloud, pictured). Check accommodations: read aloud, oral answer, scribe, extra time. Extension, same skill: a harder or less familiar invented case, or a skill returned in another setting, never the next grade's skill.

  Confidence: Firm.

### 7. Sensitive ground: no therapy, screening or group blame found; four places need a rule

I found nothing in sections 5 of STANDARD.md or in APPROACH.md that screens, rates a child's feelings, or assigns guilt to a group. The values rule and "noticing your own snap judgements on invented cases" are applied correctly, and no clinical word is used of a child. Four places still need a sentence:

- **a. Role play of refusal and standing up.** STANDARD section 5.3 forbids casting a child as victim or perpetrator, but RS6 (say no to pressure) and RS9 (speak up for others) cannot be rehearsed without someone applying the pressure or the unkind act. The health page solves it ("The teacher or a card plays the pressure; no student plays a person who pressures"); this page does not. Fix: add that sentence to section 5.3 and to APPROACH section field 7. Confidence: Firm.
- **b. The line with health and mental health.** Units named "Stress and strong feelings" (G6), "Stress, focus and rest" (G8), "Stress and coping" (G9), "Relationships that are good for me" (G9), "Healthy boundaries" (G10) and "Help, support and pressure" (G11) sit next to mental health, dating and sexual health. Section 5.4 and the placement note on RS6 say those topics are health's, but the unit titles and cases are not bounded. Fix: add a rule that a unit's invented cases use school, friend, family-chore, sport and online settings only; no case names self-harm, a diagnosis, dating, sex or a substance; the teacher note names the health unit by name. Consider retitling "Healthy boundaries" to "Saying no, setting limits" (a Judgment call). Confidence: Likely.
- **c. Personal sub-skills.** SA1 (groups you belong to: family, culture) and SA2 (strengths from your culture and languages) invite a child to disclose identity. Section 5.2 covers disclosure in general; the placement notes do not repeat it for these two. Fix: add "SA1 and SA2 use an invented character first; a child may share or make one up; a family or culture is never asked about by name in a check". Confidence: Likely.
- **d. SO6 at grades 3 and 4.** See finding 2: the safe case is "playground fairness" and "settled history from grade 5", with nothing stated between. Confidence: Likely.

### 8. Four sub-skills are personal in the standard's own wording, and the bar wants a check item for each

- **Where:** casel-5.txt SA3 (notice what you are feeling), SA4 (tell the truth, act on values), SA7 (believe you can), SA9 (find your interests and purpose); STANDARD.md section 5.1 (checks score a skill, never a feeling or trait); C1, C8 (every standard has a check item).
- **What is wrong:** C1 fails any standard with no check item. These four are about the child's inside. Section 5.1 forbids scoring them. The APPROACH examples (name the feeling, pick a fair next step) can be done on a character, which works for SA3 but not for SA7 or SA9, which are beliefs and interests.
- **Fix (add to STANDARD.md section 5.1; Judgment call, see For Cory 2):** state how each is checked as a skill on an invented case or a plan the student keeps: SA3, name a character's feeling and the clue; SA4, choose the true action in a case and say what it costs; SA7, name two steps a character could take and one place to ask for help; SA9, a private list the student keeps, checked only for "seen" that the steps were followed, never for content. Say the course never records a student's answer to SA7 or SA9. Confidence: Judgment call.

### 9. The class sheet and "no ratings of individual children" pull against each other

- **Where:** APPROACH.md "Daily evidence" (paper class sheet "seen / not yet", never kept as student data); bar part 9 item 11 ("the class record of skill checks; no ratings of individual children"); STANDARD.md section 4C ("behaviour ratings of individual children are not collected").
- **What is wrong:** A class sheet with a mark per child is a rating per child, even if it is of a skill step. The pages never say that the sheet scores a step seen on one occasion and not the child, nor how long the sheet is kept. "Never kept as student data" and "a paper sheet of per-student marks" are the same object.
- **Fix:** Add one line to APPROACH "Daily evidence": the sheet holds "seen / not yet" per step on one named day, is the teacher's own working paper, is not shared outside the class, and is thrown away at the end of the unit (ours). Item 11 then reads "no behaviour ratings". Confidence: Likely.

### 10. Words: none quoted, but six lines sit close to the source and the "SAFE" label is borrowed

- **Method:** I compared casel-5.txt with the source page's sub-skill list from memory (the page was not opened, so this is a memory comparison). Neither STANDARD.md nor APPROACH.md quotes a CASEL sentence, graphic or product name; both name CASEL only as the source in internal pages, which the terms allow.
- **Lines that read as near paraphrase of a short phrase (from memory):** RD2 ("weighing information, data and facts" keeps the source's trio of nouns); RD6 (the same three settings, "yourself, your family and your community"); RD7 ("you, other people, your community and its institutions"); RS9 ("speak up for others whose rights are not being respected"); SO6 ("some expectations have been unfair" for the source's "unjust"); SM4 ("for yourself and with a group" for "personal and collective"). All are phrases of a few words, not sentences, so this is a Judgment call, but a cheap reword removes the question.
- **Suggested rewords (ours):** RD2, "Choose after checking what the facts and numbers say"; RD6, "Think about how you help or hurt the people close to you and the people around you"; RD7, "Weigh who is affected by a choice, near and far, and what rules or groups it touches"; RS9, "Stand up for someone who is being treated unfairly".
- **"SAFE":** APPROACH.md uses it ("in the SAFE sense") and the lens credits it to a source. From memory it is a label from a 2011 review and a registry criteria paper, not CASEL's alone; either way it is a named acronym that a family or teacher page should not carry. Keep it in internal pages only and write the four features in plain words on any page a teacher reads.
- **"CASEL" in unit fields:** APPROACH "Unit field 2: the CASEL sub-skill ids" is fine for a planning document; the unit plan is teacher-facing, so say "the sub-skill ids (our own words)" on the page itself. Judgment call.

### 11. Read-status of the sources is three different things, and APPROACH.md carries no sources

- **Where:** bar part 9 "design criteria read in full by the writer and the expert"; the bar's sources table ("Writer, pp 23 to 25; expert, pp 21 to 27"); STANDARD.md section 1 ("pp 1 to 3 and 20 to 35 in full") and section 4 ("pp 23 to 35"); lens ("pp 1 to 3 and 20 to 35"); APPROACH "Where the evidence is thin" (meta-analyses found gains in skills, behaviour and attainment); lens (meta-analyses: abstracts only; EEF read; mindset reviews from the writer's knowledge).
- **What is wrong:** C13 fails "a research claim rests on a source nobody read". The pages give four different page ranges for one paper and say "in full" in the bar. APPROACH states what the meta-analyses found, which the lens says rests on abstracts. "Short mindset lessons have mixed results" is not marked from memory, though the lens says it is.
- **Fix:** Pick one range and update the bar, section 1 and the lens to match (the section 1 range is the most specific). In APPROACH add a closing "Evidence and sources" section as the health page has: what was read, how much, what is from memory, no claim of effect, and a one-line pointer to the course-level logic model (C16). Mark the mindset line "from memory". Confidence: Firm.

### 12. A school may leave out any unit, but every year teaches every id

- **Where:** STANDARD.md section 5.6 ("each SEL unit can be left out without breaking the course"); lens error ("a unit a school could not leave out without breaking later units"); the grade table, where each id is first taught in exactly one unit per year.
- **What is wrong:** If a school leaves out a unit, its ids are not taught that year, which is a C1 fail for that school, and later units' readiness checks may lean on it. The page does not say what a course page then states, nor how a unit's readiness check avoids leaning on a left-out unit.
- **Fix:** Add: "A school that leaves a unit out is told which sub-skill ids that year no longer teaches; later units never assume it (a readiness item is on the previous year's owner row, not the same year's earlier unit), and the course page says the course then does not claim those ids that year." Confidence: Likely.

### 13. Stale notes

- **casel-5.txt, header line 10** ("scripts/standards.py does not read this file; its CLOSED regex accepts only the five competency codes") and **STANDARD.md section 1, "For the lead"**: both stale. scripts/standards.py now builds LISTED from casel-5.txt (lines 96 to 105) and returns a valid code at line 137, so `CASEL.Self-Awareness.3` passes. The CLOSED pattern for the five competency codes is kept for data/modules.csv and is not a problem. Replace both with: "scripts/standards.py reads this file as an id list (valid as listed); the five competency codes in data/modules.csv remain valid." This is also the answer to the "Owed to the lead" item in the header table.
- **data/courses.csv line 41** and **data/subjects.csv line 11** still read "Light shelf; not a build priority" while the bar and Cory's 2026-11-15 rule say every course is finished to the bar and SEL is four courses with 13 grade-year frames. courses.csv has one row (`sel-k12`); docs/COURSES-STATUS.md counts four. State which is the authority, or add the four rows (a catalogue decision, For Cory 3).
- **STANDARD.md section 4 verdict** says the design half "is not enough alone in three places (B, C, D)"; section 4 lists five gaps (A to E) and all five were adopted. Change "three" to "five" or drop the parenthesis.
- **Bar part 9, items 9 to 13** are tagged [I] (from the instrument). They are additions of our own (STANDARD.md section 4); tag them [O].
- **STANDARD.md header**, "Core subjects come first: nothing here starts a frame or a scope and sequence", is true; keep.
- **casel-5.txt header lines 6 to 8** record the wording being removed on 2026-11-11 and added in our words on 2026-11-16; line 7 ("read the sub-skills on the source page") is superseded by line 8 and can be dropped.
- **ADOPTION-BAR-SUBJECTS.md status line**: "Not read by the expert since revision" is out of date (the SEL part has been through this read). Not mine to rewrite; flagged.

Confidence: Firm for each (checkable by reading two lines side by side).

### 14. Time and the course grain: minutes are a range, and the catalogue grain differs from the frame grain

- **Where:** STANDARD.md section 2 ("about 20 minutes in K to 2, 30 minutes in 3 to 8, 30 to 45 minutes in 9 to 12").
- **What is wrong:** C2 asks for a stated period length per lesson. "30 to 45 minutes" is a range, so a day-count and an assessment-minutes gate cannot be computed for grades 9 to 12. "About 20" has the same fault.
- **Fix:** State one number per band (ours: 20, 30, 30, 40) and say the frame may change it with a reason, as the health page does. Confidence: Likely.

### 15. What else would stop a planner

- **Course list and gate grain.** A progression and a plan.py course exist per course; the catalogue has one SEL course and the standard says 13 grade-year frames under four. State what plan.py's course id is (`sel-k-2`, one frame per grade year, or per-grade ids) before data/plans/sel/ is created. Confidence: Likely.
- **The two units that start each K year.** K unit 1 "Hello, our class" holds RS1, RS2, RS8, SO2, SA1; the first days of K cannot lean on any readiness check, and C4 "each idea rests on the last" needs a statement for K that the first unit assumes nothing. Add one line. Confidence: Likely.
- **Cross-subject leans.** STANDARD.md section 7 names real ids and the leans are sound; it still says "to check when health's frames are written". Rows exist, so the check is a one-line gate. No action beyond noting it.

## What is right and should not be touched

- The 40 ids, their order and their own-words lines, and the header's licence stance (ids and our own words only).
- Every grade covering all 40, taught once as a unit's own, with return in practice; this answers the bar's "two of five areas" and "same every year" fails and Cory's "smaller means fewer minutes, never fewer units".
- STANDARD.md section 5 as a whole: nothing personal collected or scored, no disclosure asked, SEL is not therapy, hard facts plain at the right age, no product or rating words. This is the best-written part of either page.
- Practising by doing for self-management and relationship skills, and by reflection for the other three.
- The kinds-of-day table and the "Where the evidence is thin" paragraph's stance (no claim that these courses work).
- Short codes SA/SM/SO/RS/RD for the planner, and the transition-year themes.

## Not checked

- The CASEL framework page and the criteria paper: not reopened, so the memory comparison in finding 10 is unverified.
- docs/reviews/sel-open-material-2026-11-16.md, FOUNDATION.md, BASELINE rules and DESK-ANSWERS: not read for this pass, so the values rule is taken from the lens and STANDARD.md.
- scripts/unitplan.py and scripts/plan.py: not read.
- Whether the SEL frames, tools or TOOL-ASKS exist: no data/plans/sel folder or progression file was seen.
- Anything about Spanish family notes beyond the decision recorded in the pages.

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| SEL ownership is one owned row per sub-skill per band (owner is the band's last grade), `~` rows in the other years | Fits the layer 4 gate and the ELA band-code convention; the grade table stays the placement | STANDARD.md section 3 |
| Unit cap of 8 ids; extra ids move forward as `~` returns | Rehearsal needs about two sessions an id | STANDARD.md section 3 table |
| One period length per band (20, 30, 30, 40) | C2 needs one number | STANDARD.md section 2 |
| Carry-out cue is part of "what is carried" (section field 5); family activity is unit field 9 | The current field numbers point at "Two rooms" | APPROACH.md |
| Refusal and upstander role play: the teacher or a card plays the pressure | Matches the health page's rule | STANDARD.md section 5.3; APPROACH.md |
| Reword RD2, RD6, RD7, RS9 | Remove the near-paraphrase question | data/standards/casel-5.txt |
| Class sheet kept to one named day and discarded at the end of the unit | Reconciles item 11 with promise 2 | APPROACH.md "Daily evidence" |

## For Cory

1. **Ownership form (finding 1).** The layer 4 gate wants one owner per standard. Recommended: 160 owned rows (40 ids by four bands), owner the band's last grade, `~` in the other years. The alternative is changing the gate for SEL so that each id is owned once per grade year (520 rows). Which?
2. **The four personal sub-skills (finding 8).** SA3, SA4, SA7 and SA9 can only be checked as a skill on an invented case or a plan the student keeps and never reads back. Recommended: yes, and the course page says SA7 and SA9 are practised and not scored. Or leave SA7 and SA9 as untested standards and mark the part pass in C1?
3. **Catalogue grain (finding 13 and 15).** `data/courses.csv` has one SEL row marked "Light shelf"; the bar and the frames say four courses. Recommended: replace the row with four band rows and drop "Light shelf". Yes or no?
4. **A school leaving out a unit (finding 12).** Recommended: allowed, and the course page states which ids the school then does not claim for that year. Or does the course ask that every SEL id be kept?
5. **"Healthy boundaries" title (finding 7b).** Recommended: retitle to "Saying no, setting limits" so the unit does not read as dating or sexual health. Yes or no?
6. **Your yes on the approach page**, once findings 4 to 6 and 9 to 11 are in. It stays a draft until then.

## Fixes applied (2026-11-20)

1. STANDARD section 3: ownership rule written as the recommended 160-row form (owner years 2, 5, 8, 12), marked pending on Cory; scripts/progression.py left untouched.
2. STANDARD section 3: depth ladder by band and within a band added; SO6 and SO8 stated for grades 3 and 4.
3. STANDARD section 3: unit cap of 8 sub-skills; the 13 grade tables rebalanced by moving excess ids into units 1 to 5 (chosen by competency fit, so unit names may need a read); short path names its dropped sessions (section 2).
4. APPROACH: every unit and section field now filled, family note moved to unit field 9, carry-out cue to section field 5, two rooms to field 10, pacing line added.
5. Answered by the additions in 4, 6, 8 and 9 (item 9 link, fidelity checklist, student voice, carry-out cue); no separate edit.
6. APPROACH section field 9: supports written in full.
7. a, c: role-play and SA1/SA2 rules added (STANDARD sections 3 and 5). b: case-settings rule added; the "Healthy boundaries" retitle written as recommended and pending. d: see 2.
8. STANDARD section 5.1: the four checks written as recommended, pending on Cory.
9. APPROACH "Daily evidence": class sheet kept to one named day and discarded at unit end.
10. casel-5.txt RD2, RD6, RD7, RS9, SO6, SM4 reworded; "SAFE" removed from APPROACH; "CASEL" wording in APPROACH unit field 2 changed to "sub-skill ids, in our own words".
11. One page range (pp 1 to 3 and 20 to 35) in STANDARD; APPROACH has an Evidence and sources section and the mindset line marked from memory. The bar and the lens still carry other ranges: not in scope here.
12. STANDARD section 5.6: leave-out rule written as recommended, pending on Cory.
13. Stale validator notes fixed in casel-5.txt and STANDARD section 1; casel-5.txt line 7 dropped; "three" changed to "five". Left: data/courses.csv and subjects.csv (pending, STANDARD section 2), bar item tags and bar status line (not our pages).
14. STANDARD section 2: 20, 30, 30, 40 minutes, a frame may change it with a reason.
15. Catalogue and plan.py course grain written as recommended, pending (section 2); kindergarten unit 1 assumes nothing (unit rules); cross-subject lean note reworded.

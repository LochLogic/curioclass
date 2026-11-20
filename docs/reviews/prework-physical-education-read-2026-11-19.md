# Physical education pre-work: cold read, 2026-11-19

Read as the curriculum expert (docs/agents/EXPERT.md). I did not write these drafts. Nothing was edited but this file.
Confidence is "likely" unless a line says otherwise. Anything about PE practice that rests on my memory is marked
"from memory"; no outside source was opened (none was asked for).

## What I read

AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/physical-education.md; docs/ADOPTION-BAR-SUBJECTS.md (pass rule,
shared core, part 4, "Before a scope and sequence" PE row); docs/courses/physical-education/STANDARD.md and
APPROACH.md; docs/standards-notes/pe-2014-to-2024.md; docs/reviews/physical-education-open-material-2026-11-16.md;
row L46 of data/plans/later.csv; data/standards/shape-pe-2024.txt (header, all ids, counted); docs/APPROACH.md
(principles); docs/courses/UNIT-PLAN.md (rules, field lists). For stale-note checks only: the SHAPE lines of
scripts/standards.py and scripts/progression.py, docs/PRODUCTION-PATH.md step 1, and the "own words" line of
docs/courses/health/STANDARD.md. Not read: the PECAT PDF, SHAPE pages, any outside source.

## Verdict

The standard file is sound as a list (edition right, 210 ids, every per-span count in the header matches the file,
numbering contiguous, no duplicates), and the PE rules for the learning environment are well chosen. But the standard
is not yet usable by a planner, because no indicator has any wording at all, and the grade-outcome rule disagrees with
the ownership rule the progression gate already enforces. The approach page covers the bar's PE part well but leaves
out several shared-core approach rows (model fading, English learners, reading load, the two rooms, cost, safety, no
effect claim) and has one unsafe line about injured students. Fix findings 1 to 5 before asking for Cory's yes.

## Findings, most serious first

### 1. The 210 indicators have no wording, so a planner cannot write a grade outcome from the repo

- **Where:** data/standards/shape-pe-2024.txt; STANDARD.md sections 2 and 3; UNIT-PLAN.md rule 15.
- **What is wrong:** The file is ids only (right, the source is all rights reserved). STANDARD.md names four standard
  themes and says "our own words". But nothing in the repo says what SHAPE.S1.5.14 or SHAPE.S2.8.9 asks. A progression
  writer must reopen the publisher's page for every id, and each writer will paraphrase differently. Health made the
  same choice (health STANDARD.md line 39 says outcomes are written in our own words) and the same gap exists there.
  UNIT-PLAN rule 15 ("the standard's verb is quoted exactly") cannot be followed for PE: the verb may not be quoted.
- **Why it matters:** Bar criterion 1 (outcome, content and assessment for every standard in every grade) cannot be
  traced if no one can see what each indicator holds. Same indicator, three paraphrases, three different days. C1 is a
  door criterion.
- **Fix:** Add a working file `data/standards/shape-pe-2024-words.txt`: id, tab, one line in Curio Class's own words
  (our paraphrase, marked "ours, not the publisher's"), written once from the free page by one writer and read by a
  second. Add to STANDARD.md section 2: "Indicator wording is never copied. Our one-line paraphrases live in
  shape-pe-2024-words.txt; a plan states each verb in our own words and cites the id." Add a PE line to UNIT-PLAN rule
  15: "Physical education: name the indicator by id and state its action in our own words; the verb cannot be quoted
  (all rights reserved)." Confidence: firm that something is missing; the paraphrase file is a judgment call on form.

### 2. The grade-outcome rule contradicts the ownership rule the gate already enforces

- **Where:** STANDARD.md section 3 rules 1, 2 and 5; scripts/progression.py `code_grades` (lines 82 to 88).
- **What is wrong:** Four separate problems.
  1. Rule 2 says each indicator is "placed in at least one year of the band and fully met by the band's last year."
     The gate says a SHAPE indicator is owned by the span's last grade (grade 2, 5, 8 or 12) and worked toward, written
     `~CODE`, in any earlier grade. Read the gate's way, every K to 2 indicator is owned in grade 2, so K and grade 1
     have nothing owned. That cannot be what a planner means by "one outcome per standard per grade".
  2. The gate's comment says the rule was "added 2026-11-19" to the PE STANDARD.md. STANDARD.md has no such text
     (it is dated 2026-11-16 and says "toward", not `~`).
  3. For high school, rule 5 has years 1 and 2 meeting the span's indicators. The gate would make grade 12 the owner
     of all 9 to 12 indicators, so a grade 9 course that fully teaches one still does not own it.
  4. The rule is written as a scope and sequence rule. The progression (layer 4) is where each indicator is placed in a
     grade first (PRODUCTION-PATH step 1: one row per skill, one grade owns it). No progression row exists for PE yet
     and the rule never mentions one.
- **Why it matters:** A writer cannot obey both texts. The first progression will fail the gate or be built to the
  gate and teach nothing owned until grade 2.
- **Fix:** Replace rules 1 and 2 with: "A progression row owns an indicator in the grade where the student first meets
  it as a pattern and can show it in a stated setting (progression owner, any grade of the span). Grades after it in
  the span carry it as `~CODE` (used in new settings). Grades before it, if they prepare it, carry `~CODE`. Every
  indicator has exactly one owner grade and is shown as met no later than the span's last grade. Every standard
  (S1 to S4) has a stated outcome in every grade, each naming at least one owned or `~` indicator." Then either change
  progression.py to "owner may be any grade of the span, the last grade is the deadline" for PE and health, or keep
  its rule and say so in STANDARD.md in the gate's words. This is a call on one number-level rule; I recommend the
  first, because under the gate's rule a K to 2 child owns nothing until grade 2. Update the comment's date and
  location either way. For high school add: "9 to 12 indicators have an owner grade 9 to 12 in the course
  progression; years 3 and 4 own the choice and plan indicators (S4)."

### 3. The approach page omits shared-core approach rows (C7, C10, C11, C13, C14, C16)

- **Where:** APPROACH.md throughout; docs/APPROACH.md principles 3, 9; UNIT-PLAN section plan fields 5, 9, 10.
- **What is wrong:** See the table in the next section. In plain terms: nothing says who holds the model each day and the
  day it is withdrawn (C7 fails-if "no day is named for withdrawing the model"); nothing for English learners, reading
  load, or access beyond equipment (C10, C11); there is no "two rooms" (a parent with one child, one screen) answer
  for a subject built on partners, groups and a shared space (C14); no stated cost, class size or teacher knowledge
  (C14); no source list or note on how much of each source was read, inside the approach page (C13); no statement that
  the course has not been tried with children and no logic model owed (C16).
- **Why it matters:** C7, C10, C11, C13, C14 and C16 together are more than the three part-passes the pass rule allows,
  and C14 is a door criterion. The shared page says a subject page only fills slots; these are slots.
- **Fix (wording to add to APPROACH.md):**
  - *Who holds the model:* "The model is the teacher's demonstration with the cue card. A student holds it with a cue
    card or partner. Each unit plan names the day the cue card goes away (the student performs and names the cues from
    memory). New skills are first tried with the teacher watching, never first met in a game."
  - *English learners and reading load:* "Each unit names the movement words (cues, body parts, direction words) taught
    with a picture or demonstration and a sentence frame, such as 'My step is with the ___ foot.' Reading load: task
    cards are picture-led, with read-aloud on the card for grades K to 2. A student who is slow to say the cue can show
    it; the check marks movement and understanding separately, so a language gap is not marked as a skill gap."
  - *Two rooms:* "One child at home: partner tasks use a parent or sibling or a wall, a target, or the child's own
    count against yesterday; no team games are needed. One projector or none: every day runs from a printed cue card,
    and the screen only shows a skill picture."
  - *Cost and room:* "Needs a clear space about the size of a room, a few soft balls or rolled socks, a rope or string,
    and a line (tape, string or chalk). Nothing to buy. Class of thirty: stations in groups of three to four, one item
    per pair. The teacher needs no special training; each unit's cue card says what to look for."
  - *Evidence:* "Course pages say the course has not been tried with children and claim no effect on fitness or
    health. A one-page logic model is owed at the course level."
  - *Sources:* a short list of sources with how much of each was read (the appropriate practice guidelines, pages 1 to
    12 and 22 to 25; PECAT K to 5 overview and standard 1 tables), copied from STANDARD.md 4 and 3.
- Confidence: firm (the missing rows are named in the bar).

### 4. One line in APPROACH.md is unsafe, and safety content has no home

- **Where:** APPROACH.md "Supports": "A student with a short-term injury has a moving or a helping role, never a seat
  on the bench." Also bar criterion 4 (fitness and safety content is accurate).
- **What is wrong:** A student under a medical restriction (a clinician's or family's instruction to rest an injury or a
  head knock, a cast, a bad asthma day) may need to sit. "Never a seat" overrides that. STANDARD.md 5 hands individual
  conditions to "the school nurse and families", so the approach contradicts the standard note. Separately, the page
  has no safety content: no clear-space rule for throwing, striking and ropes, a surface rule for hard floors and wet
  grass, a heat and water-break rule, a footwear note, or a check of equipment. Hard surfaces and heat are in the lens's
  "unsafe space" list and nowhere in the approach.
- **Why it matters:** The first is a possible harm to a child. The second means bar criterion 4 has nothing to check a
  plan against, and C3a (accuracy) needs the safety statements to be sourced.
- **Fix:** Replace the line with: "A student with a short-term injury has a role that fits what the family or the
  school nurse has said they may do: a moving task for the parts that are fine, a helping or observing role (cue
  watcher, scorekeeper of the student's own count) otherwise. If they have been told to rest, they rest and the
  teacher gives a seated role. Nobody is sent to the bench as a punishment." Add a "Safe space" block to the page:
  "Each unit lists: the clear-space size (arm's length all round, and a throwing direction everyone faces); the
  surface (soft or hard) and what to change on a hard floor or wet grass; a water break in warm weather; the equipment
  checked before the lesson. Safety facts are sourced; a fact with no source is marked 'from memory'." The lens's list
  gives the content.

### 5. The daily evidence cannot show growth against the student's own earlier work

- **Where:** APPROACH.md "The daily evidence", "Kinds of day: Check"; bar criterion 7.
- **What is wrong:** The teacher marks one cue for a rotating group "so every student is seen at least once a unit."
  One observation per unit is one point, not growth. The Check day says "growth against the student's own earlier
  check", but no earlier check is defined, and no baseline exists at the start of a unit. Conduct (criterion 7 asks for
  skill, knowledge and conduct) has a self-assessment but no rule on what conduct is judged against, which is the
  usual road to grading on effort, dress or attendance. Closure by "thumbs scale on a self-check" is also visible to
  the class and could be read as public rank.
- **Why it matters:** C8 fails if a doing subject is checked by recall alone, and criterion 7 needs growth to be
  measurable. As drafted, the teacher can record growth for no student.
- **Fix:** Add to the Check day and the evidence section: "Each unit opens with a baseline: the unit's first skill day
  has a short watch of the unit's main cue for the whole class in rotating groups, recorded met, partly or not yet.
  The Check day repeats the same cue, so each student has two marks and the growth is the change. Conduct is marked
  against the unit's stated behaviors (taking turns, using equipment safely, helping a partner), taken from the S3
  indicators, never against dress, attendance or effort alone." Change the thumbs scale to "held privately (a card on
  the desk, a mark on the student's own sheet)."

### 6. Motor skill order: sound as a reference, thin as a rule

- **Where:** STANDARD.md section 3 rule 3.
- **What is wrong:** The order quoted (underhand throw, catch, hand and foot dribble, kick, short striking and rope in K;
  weight transfer in 1; overhand throw, jog, long striking in 2) is a curriculum table's order, and it matches my
  memory of the 2014 outcomes, so it is reasonable by age, and "reference, not wording" is the right label. Four gaps.
  (a) It names only manipulative and jumping skills. Locomotor patterns (hop, gallop, skip, slide), balance, rolling
  and the first dance and gymnastics skills are all S1 span K to 2 indicators and have no order. (b) Overhand throwing
  is placed at grade 2 only; children usually throw overhand by kindergarten (from memory), so K to 1 should work
  "toward" it as a pattern with the cue "step with the opposite foot" before grade 2 expects it. (c) Continuous hand
  dribbling and a continuous self-turned rope in K are later developing skills (from memory); the K outcome should be
  "attempts" or "toward". (d) Nothing covers 3 to 12; the rule says "for the order within K to 5".
- **Why it matters:** A progression writer can place the manipulative skills but is on their own for locomotor, rhythm,
  gymnastics and every grade after 5. Criterion 2 is a bar line.
- **Fix:** Add to rule 3: "Order inside each span follows pattern, then conditions, then combination. Locomotor
  patterns and balance come first in K and 1, before manipulatives that need them; weight transfer follows locomotor
  control. A skill the PECAT tables first expect in a grade is owned there, and the grade before it carries it as
  `~CODE` (toward). Grades 3 to 12 are ordered by the planner from the 6 to 8 and 9 to 12 tables (L46) and the
  appropriate practice guidelines; mark each order as 'from the tool', 'from memory' or 'ours, untested'."

### 7. The five-to-four map is usable for S1 and S2, not yet for the rest

- **Where:** docs/standards-notes/pe-2014-to-2024.md "How to use it".
- **What is wrong:** The note maps standards only and says outcomes are not mapped. PECAT's tables are coded by older
  outcomes (S3.E1 and so on). For older standards 3, 4 and 5 the planner "has to split by hand", but no per-outcome
  list exists, and the tables read for L46 will each need that split. Left as is, each band's planner invents a
  different split and the same PECAT finding lands under different 2024 standards.
- **Why it matters:** The PECAT tables are the only evidence of grade placement for grade 3 to 12 skill order.
- **Fix:** Add a short rule to "How to use it": "Where an older outcome is of a skill (kicking, dribbling) it goes to S1.
  Where it is about knowing a concept or a fitness fact it goes to S2. Where it is about working with others it goes to
  S3. Where it is about self-management, personal fitness plans or choosing activity it goes to S4. A planner who
  splits an older outcome records the choice in the band's table." No new table is needed now.

### 8. Pacing and minutes stated thinly

- **Where:** APPROACH.md "Pacing"; lens "Sources" (about 150 and 225 minutes, from memory).
- **What is wrong:** The page says K to 5 is 2 to 3 sessions a week and gives no session length. The lens says the
  recommended weekly minutes are about 150 for elementary (from memory). Two to three sessions of 30 minutes is 60 to
  90 minutes, which is below the figure the lens quotes. Nothing says so. The approach also asks for at least half of
  each lesson in moderate to vigorous activity without saying how short a session can be and still have a warm-up,
  focus, cool-down and closure.
- **Fix:** Add one honest line: "Curio Class plans two to three sessions a week (session length stated in each frame);
  this is below the weekly minutes professional bodies recommend (from memory, 150 in elementary). Families and
  schools can add free play and walks; the course does not claim to meet the recommendation." Fits C16.

## The bar and the approach, criterion by criterion

Met = the line shows it. Part = something is there but a fails-if or a row is not answered. Missed = not found.

### PE part, criteria 1 to 8

| # | Verdict | Where, and what is lacking |
|---|---|---|
| 1 Outcome, content, assessment for every standard in every grade | Part | STANDARD 3 rules 1 and 4 state it. Unusable until findings 1 and 2 are fixed. |
| 2 Motor skills built in order | Part | STANDARD 3 rule 3, APPROACH "Practice that returns". K to 5 manipulative order only (finding 6). |
| 3 Most of the class moving most of the time | Met | APPROACH "Every day ... at least half ... moderate to vigorous"; Fluency "No lines"; STANDARD 4 "Activity time". |
| 4 Fitness and safety content accurate | Part | STANDARD 4 "Fitness testing". No safety content, no source rule for safety facts (finding 4). |
| 5 Gym, field or small room; weather, class size, little equipment | Part | APPROACH "Space and equipment ... low-equipment version and a wet-weather version". Class size not stated. |
| 6 Adaptation in every lesson | Met | APPROACH "Supports": "Every lesson has an adaptation ... equipment size, distance, speed, rules, roles." |
| 7 Skill, knowledge, conduct; growth against own earlier work | Part | APPROACH "Check" names all three and growth. No baseline, no conduct rule (finding 5). |
| 8 No exercise as punishment, no elimination | Met | APPROACH "Supports" last bullet; STANDARD 4 "Learning environment" and "Competition". Appropriate practice is now read in part, so the bar's "nobody here has read them" is stale. |

### Fails-if list

| Condition | Verdict | Line |
|---|---|---|
| A year of games with no outcomes | Met | STANDARD 3 rule 4; APPROACH "What a PE unit carries": the grade outcome per standard. |
| Long lines and waiting | Met | APPROACH Fluency "No lines"; STANDARD 4 "Activity time". |
| Grading on dress or attendance | Part | STANDARD 4 "Grading" forbids it; APPROACH has no grading rule of its own, and the conduct check is open (finding 5). |
| Fitness tests used as grades | Met | APPROACH "Fitness ... never graded"; STANDARD 4. |

### Shared core rows that point at layer 3

| Row | Verdict | Where, and what is lacking |
|---|---|---|
| C7 Taught, then faded, and returning | Part | "Practice that returns" and the "Understanding ... then tried at once" day show returning and teaching first. No model holder and no withdrawal day (finding 3). |
| C10 Every learner works on the content | Part | "Supports" keeps the goal and names adaptations. No extension on the same standard, no reading load, no hook list (finding 3). |
| C11 English learners inside the lesson | Missed | No line on EL words, frames or telling a language gap from a skill gap. |
| C13 Approach explained, families told | Part | STANDARD 4 says what was read and how much. APPROACH has no source list and no family note slot; the family note belongs to unit finish, but the approach should name it. |
| C14 Ordinary room; time, space, supplies, cost, knowledge | Part | Space, equipment and wet weather stated. No cost, class size, teacher knowledge, paper path or two rooms. |
| C16 Honest about evidence | Missed | No logic model owed and no "not tried with children" statement in the PE docs (finding 3). The shared page may hold the course-wide line; the PE page should point to it. |

## Questions 4 and 5

### The approach page against the section plan slots

- **Kinds of day:** Filled. Understanding, fluency, application, check and respond match UNIT-PLAN rule 11 ("in the
  subject page's words"). One ambiguity: a day's "closure" is part of every day but the Check day's evidence and the
  teacher's mark are not tied to one field, so a writer may put the mark in field 3 or field 6. Say: "The teacher's
  mark goes in field 3 as the day's evidence."
- **Daily evidence:** Filled, but see finding 5.
- **Space and equipment:** Filled under unit field 2, but the section plan has no matching field (UNIT-PLAN section
  fields 1 to 11 have field 5 "what a room with nothing does" and unit field 8 "supplies"). The approach page says space
  goes in unit field 2 and the bar says "section plan fills ... space, equipment and the adaptation". Say once where
  it lives: "Space and equipment: unit field 8 (supplies) and section field 5 (what a room with nothing does)."
- **Adaptations:** Filled and good. Needs the injury fix.
- **Contradictions and unclear wording:**
  - "A tool ... may run a timer or music track for a lesson with a stated purpose" is consistent with UNIT-PLAN rule 14.
  - "Practices (section field 1)" is right; the field is "Standards and practices" and the PE page uses it for cues.
    Fine, but say "cues take the place of math's practices".
  - "A tool may ... collect no fitness data": the sentence says "may not ... collect fitness data about them" and
    "Fitness: the student keeps their own record". Make explicit that the record is on paper or on the device only.
  - "Understanding ... then tried at once" and docs/APPROACH.md principle 4 agree (teach first). Good.
  - Check day lists three kinds of check in one sentence. A writer will do one. Say "each unit's check has a skill
    task and a knowledge task, and conduct is marked once in the unit."
- **What a progression writer still needs:** (1) own-words indicator list (finding 1); (2) the owner and `~` rule
  (finding 2); (3) the older-outcome tag rule (finding 7); (4) the locomotor, balance and dance order and the rest of
  the PECAT tables (finding 6 and L46); (5) the dance and health hand-off table, since STANDARD 6 says the course pages
  "name each other" but no dance or PE-health split exists in the repo and a progression must record the
  `cross_subject` links.

### L46: before progression or only before scopes?

L46 says "Before the PE scopes" and recommends doing it as the first job of PE's frame work. The bar row and
STANDARD.md both say each band's planner reads the rest. These do not line up (finding 9 below). My reading: it is
needed before the PE **progression** for the strands the tables cover, not only before scopes. The progression is the
layer that fixes which grade owns each skill (PRODUCTION-PATH step 1: one grade owns each skill id), and the
PECAT grade tables are exactly the only evidence in hand for grade placement. The K to 5 overview and standard 1 tables
are read, so the K to 5 motor order can start. It is not enough for K to 5 S2 to S4 (movement knowledge, fitness,
responsible behavior, valuing: older standards 2 to 5), nor for 6 to 8 and 9 to 12 at all. So: read the K to 5 tables
for older standards 2 to 5 before the K to 5 progression is reconciled, and read the 6 to 8 and 9 to 12 tables before
those bands' progressions. A scope that leans on a progression that did not use them inherits the gap. Confidence:
likely; reasonable people might let the scope and sequence writer read the tables, as the bar says. If the progression
writer is the band's planner, the two readings come to the same job.

## Finding 9: stale notes

Lines that say something is not done, or give a wrong fact, now that the repo shows otherwise:

- STANDARD.md section 1: "scripts/standards.py checks `SHAPE.S[1-4]` by pattern; it does not check span or number."
  scripts/standards.py line 109 now checks the span (2, 5, 8 or 12) and allows one or two digits for the number. It still
  does not check that the number exists. Change to: "checks the standard (1 to 4), the span (2, 5, 8 or 12) and a
  one or two digit number; it does not check that the number exists in the file."
- pe-2014-to-2024.md "What was checked": "Not reopened today: PECAT itself (the CDC addresses we tried returned 'not
  found')" and "taken from docs/reviews/standards-currency-2026-11-11.md". PECAT was read in part on 2026-11-16
  (STANDARD.md 3) and the keying to the 2013 five is confirmed there. Update the line to "PECAT 2019 read in part
  2026-11-16 (K to 5 overview and standard 1 tables); keying to the five confirmed."
- ADOPTION-BAR-SUBJECTS.md part 4: "(preliminary analyses and directions read; grade tables not read)" and criterion
  8 "nobody here has read them" are out of date: the K to 5 overview and standard 1 tables, and the appropriate
  practice guidelines pages 1 to 12 and 22 to 25, were read 2026-11-16. The "Not read by the expert since revision"
  status line and "Rests on" paragraph need the same update.
- later.csv L46: "Its grade tables are still unread" and "the PE and health keying rests on the earlier report" are
  stale: the K to 5 overview and standard 1 tables are read for PE. It also still says "had returned 404" and
  "curl is refused, read in a browser", which STANDARD.md does not repeat. Restate the remaining work: K to 5
  standards 2 to 5 tables, 6 to 8 and 9 to 12 tables, and the health keying. Also resolve the timing conflict: L46 says
  "before the PE scopes" and "first job of PE's frame work", the bar row says "read by each band's planner", and
  STANDARD.md says the same. Pick one wording (see the L46 section above).
- STANDARD.md header table, "(Also) Outcome for each standard by grade ... Rule written": fine, but its section 3 is
  now out of step with scripts/progression.py (finding 2).
- scripts/progression.py comment: cites "health and PE STANDARD.md, added 2026-11-19". Neither file contains that
  text as of this read (finding 2).
- The lens header calls the approach page "(draft)" and says the standard is reviewed "with CDC's PECAT 2019": correct
  as written. No change.

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| The owner of a PE indicator is the grade where the student first shows it, in any grade of the span; the span's last grade is the deadline | Under the gate's current rule K and grade 1 own nothing | docs/courses/physical-education/STANDARD.md section 3, scripts/progression.py `code_grades` |
| Use `~CODE` as the one mark for "toward" | It is what the progression gate reads; "toward" in prose is not checkable | STANDARD.md section 3 |
| Paraphrase file for the 210 ids at one line each, written once and read by a second agent | Avoids three paraphrases of one indicator | data/standards/shape-pe-2024-words.txt (new) |
| Baseline watch on a unit's first skill day, repeat on the Check day | Two points make growth; one does not | APPROACH.md "daily evidence" |
| Conduct marked against the unit's stated behaviors from S3, not effort, dress or attendance | Criterion 7 and the grading rule | APPROACH.md "daily evidence" |
| Closure self-check held privately | Public thumbs could read as rank | APPROACH.md |
| Injured student's role depends on family or nurse guidance; rest is allowed | Safety; STANDARD.md 5 already hands conditions to the nurse and families | APPROACH.md "Supports" |
| The older-outcome tag rule (skill to S1, concept to S2, others to S3, self-management and choice to S4) | Same finding lands under one 2024 standard whichever planner reads | docs/standards-notes/pe-2014-to-2024.md |
| Locomotor and balance order before manipulatives in K and 1 | Manipulatives need locomotor control (from memory) | STANDARD.md section 3 rule 3 |
| Overhand throw: K and grade 1 toward, grade 2 owned; continuous dribble and rope in K "attempts" | Developmentally typical order (from memory); matches "reference, not wording" | STANDARD.md section 3 rule 3 |
| Teacher's mark is the day's evidence in section field 3 | One home for it | APPROACH.md |
| Where space and equipment live: unit field 8 and section field 5 | The section plan has no field named for it | APPROACH.md |
| Cue cards in place of math's practices in section field 1 | A PE section has no practices list | APPROACH.md |
| L46 read split by band: K to 5 older standards 2 to 5 before the K to 5 progression is reconciled; 6 to 8 and 9 to 12 before those bands | Progression is where grade placement is decided | data/plans/later.csv L46 |
| Stale lines as listed in finding 9 | Repo shows the work is done | STANDARD.md, pe-2014 note, ADOPTION-BAR-SUBJECTS.md part 4, later.csv L46 |

## For Cory

- **Session length and weekly minutes:** the plan (2 to 3 sessions a week in elementary) is below the minutes
  professional bodies recommend (from memory, 150 a week). Do you want the course to say so openly (my recommendation),
  or plan a third and fourth short session so it can meet it? That is a scope call.
- **Whether the approach page gets your yes** once findings 1 to 5 are fixed. It is a draft that is not in force.
- **Where the PE progression is read:** by the same people who read health's, or a separate PE read, since both depend
  on the same PECAT tables (L46). People and money call; I have no view on who.

(Nothing here changes a course's audience or money.)

## What is right and should not be touched

- The standard file itself (ids, counts, contiguous numbering, header note on reuse terms).
- STANDARD.md section 4 (the appropriate practice points in our own words) and section 5 (what is left out).
- The "Kinds of day" list, the no-lines, no-elimination, no-public-picks rules, and "A tool may ... may not".
- The "reference, not wording" use of the PECAT order and the split rows of the five-to-four map.
- The scout's verdict that no open PE base text fits: PE is written fresh.

## What I could not judge

- Whether the 210 ids match the live SHAPE page (no web access asked). The file's internal counts are consistent.
- Whether the K to 5 order is as I recall it from the 2014 outcomes (from memory); PECAT tables not opened.
- Anything about 6 to 12 skill order.

# Expert read: unit plans of Grade 1: Leaders, Helpers and Communities

Course `social-studies-grade-1`, units 1 to 8 (s01.md to s08.md). Cold read, 2026-11-14, per
docs/pipeline/briefs/plan-read.md. I did not write these plans. Of the Codex write notes I read only each note's
"expert attention" line.

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/agents/lenses/social-studies.md, docs/GLOSSARY.md,
  docs/pipeline/briefs/plan-read.md, the social studies part of docs/ADOPTION-BAR-SUBJECTS.md (items 1 to 14 and
  "Fails if"), docs/courses/social-studies/STANDARD.md.
- In full: docs/courses/social-studies-grade-1/frame.md, s01.md to s08.md; data/plans/social-studies-grade-1/days.csv
  (96 rows); the K and grade 1 rows of data/progressions/social-studies.csv; scope-and-sequence.md (readiness and
  checks parts).
- Earlier reads, for REPEAT tags and settled rules: docs/reviews/plan-social-studies-kindergarten-2026-11-14.md
  (its "Settled by the expert" table is applied here, not re-argued), docs/reviews/sequence-social-studies-grade-1-2026-11-14.md.
- scripts/unit_skeleton.py (field 5's assessment filter, line 870).
- Gates: `plan.py check` passes the course (0 failures). No em dashes in any plan.
- Web checks this run: the C3 PDF (NCSS, rev. 2017), indicators D1.2 to D1.4, D2.Civ.6, D2.His.9, D2.Eco.9, D4.6,
  D4.7 (K-2); the two NPS pages unit 1 uses (Cabrillo group volunteering, Padre Island Trashbusters); news of Dolores
  Huerta's death (October 28, 2026) and her March 2026 statements about Cesar Chavez; the Supreme Court's June 30,
  2026 birthright citizenship ruling; the Navajo Nation Council's structure.

## Course verdict

The eight plans are careful and close to the bar on coverage, sourcing and values: every Massachusetts part and
owned C3 indicator has an item with a meets and a does-not sample, every unit has a fresh source for its assessment,
invented material is labelled as invented everywhere, the informed action in unit 7 is the class's own, and the
Pledge, citizenship and family-privacy cautions are right. The biggest risk is the same as kindergarten's: units 1 to
7 ignore the settled K to 2 exit format (only unit 8 uses it), and units 1 to 5 and 7 load each child's spoken
evidence into one 30-minute assessment day that one teacher cannot run. The one change that matters most is to carry
unit 8's two-part exit and rotation pattern, and unit 6's spread observation, into units 1 to 7; after it, two
current facts must go in before the sensitivity agent runs: Dolores Huerta died on October 28, 2026 (unit 3), and the
Supreme Court upheld birthright citizenship on June 30, 2026 (unit 7).

Finding counts: course-wide 2 serious, 1 moderate, 2 minor, plus 1 skeleton finding; unit 1, 1 moderate, 2 minor;
unit 2, 1 moderate; unit 3, 1 serious, 1 minor; unit 4, none of its own (C1, C2, C3 apply); unit 5, 1 moderate,
1 minor; unit 6, 1 moderate, 2 minor; unit 7, 1 moderate, 1 minor; unit 8, 1 moderate, 1 minor.

## Course-wide findings

### C1. Units 1 to 7 do not use the settled K to 2 exit format (serious)

LAYER plan. REPEAT yes (kindergarten read C1; settled there).
- **What is wrong.** Every exit row in s01 to s07 is a spoken, often multi-part question for each child, for
  example s01 day 8: "name a goal, two duties and who could assign them. Explain each duty's help"; s02 day 17:
  "Name a helpful source kind, explain using today's evidence, and point to a dated classroom experience on our
  calendar. Is it past, present or future?"; s04 day 41 asks four things. Thirty six-year-olds cannot each answer
  these aloud in the last minutes of a 30-minute day. s08 alone adopts the settled format ("Daily exit tickets, two
  parts").
- **Why it matters.** The section writer copies these into the days; the teacher hears four children, and every
  "a miss changes the next day's opening" rule fires on no evidence.
- **Fix.** In s01 to s07, field 5, replace the paragraph that begins "**Daily exit tickets.**" with s08's paragraph
  that begins "**Daily exit tickets, two parts.**" (through "...tracks paper and spoken evidence separately."),
  keeping each unit's own sentences on withholding cases. Then give each exit row's answer cell a first sentence
  "Mark: ..." that offers two pictures, the row's answer and its likely miss, for every child to circle; the row's
  existing question becomes the spoken why for the day's rotating six. Rows whose task is already on paper keep it as
  the mark part (s02 days 11 and 13, calendar placement; s03 day 29 and s04 day 39, the written or dictated claim;
  s05 day 52, the sketch map). Rows that say "Items ... supply the day's evidence" stay as they are.

### C2. The end-of-unit observation days cannot hear thirty children (serious)

LAYER plan. REPEAT yes (kindergarten read 1.1 and 4.1, the same kind: a day asked to carry more than it holds).
- **What is wrong.** s01 day 9 gives "twenty for individual drawn or dictated responses, and five for spoken claims"
  for six items, five of them spoken; s02 day 17 asks the teacher to "listen to each child's own yesterday, today and
  tomorrow sentences" inside the day's claim lesson; s03 day 30 gives ten minutes for every pair's question-and-answer
  exchange (item 4) and pushes "unheard exchanges" into day 31's opening; s04 day 40, s05 day 54 and s07 day 79 each
  put four to six multi-part spoken items into 15 plus 10 minutes. The frame asks for "an observation task with a
  short drawn or dictated piece spread over the unit's last lessons", which s06 (days 62 to 67) and s08 (days 87 to
  90) do and the others do not.
- **Why it matters.** The record sheet ends up full of "insufficient evidence", and day N+1's response teaches to
  the children who happened to be heard.
- **Fix** (I settle the pattern; see the table). In each of s01, s02, s03, s04, s05 and s07, field 5, the
  administration paragraph: every item gets a paper part that every child does (circle, match, place or draw), and
  its spoken part is heard in five groups of six during the assessment day's independent minutes (about three
  minutes a group) or, for items on skills already taught, from the rotating six in supported work on the two days
  before. Exact sentence to add after the timing sentence: "Every child does each item's paper part. The spoken parts
  are heard group by group, six children at a time, while the others draw; a child not heard is heard from the
  rotation on the respond day's fresh try, never by a whole-class wait." Specific moves: s02, item 2's tense evidence
  comes from the rotation on days 12 to 17, not from every child on day 17; s03, item 4's exchange is done in pairs
  inside each group of six; s01, item 6's spoken claim is heard inside the groups.

### C3. Native content leans on one nation in three units (moderate)

LAYER plan. REPEAT yes (kindergarten read 5.4, "anchors on Aquinnah everywhere").
- **What is wrong.** The Cherokee Nation is the Native example in unit 3 (Mankiller, required), unit 4 (day 37,
  elected offices and terms) and unit 6 (Tahlequah as a "way of living", day 60's living nation and language). Bar
  C12 fails if "one group carries all the examples"; the lens asks Native nations to be shown as varied ("do not
  generalize one nation's system", as s04 itself says).
- **Why it matters.** A child meets "Native nation" as "Cherokee Nation" three times and one other nation once
  (Lenape, unit 5).
- **Fix** (settled, see the table). s04 day 37 uses the Navajo Nation: an elected President and Vice President and a
  Council of 24 delegates, each elected for four years (it held an election on November 3, 2026), named by office
  only. s04, field 6 contrast G and field 10 "Production references": replace the Cherokee government pages with the
  Navajo Nation's own pages (navajo-nsn.gov, navajonationcouncil.org); exit day 37's last sentence becomes "Then use
  the Navajo Nation government summary to name its elected offices and their four-year terms". days.csv day 37 goal:
  "(a tribal chair or chief)" becomes "(a tribal chair, chief or president)". Unit 6 keeps the Cherokee Nation (see
  6.1 for Tahlequah).

### C4. Tennessee rows say "not retried" (minor)

LAYER process. REPEAT yes (kindergarten read C2).
- **Fix.** Each comparison table's Tennessee row in s01 to s08: "Blocked; not retried ..." becomes "Not yet compared;
  the 2024 PDF on tn.gov refuses automated reading." The load itself is the structure pass's (kindergarten item 4).

### C5. The voice is clipped (minor)

LAYER plan. REPEAT yes (kindergarten read C3).
- **What is wrong.** Field 2's teaching bullets and field 7 read as notes: "Model pay vocabulary on 81, source
  comparisons on 84, forgone alternatives on 86 and a reasoned claim on 87" (s08); "Legal adults-only Barnette
  syllabus read" (s06); "Step back during day 8's task" (s01); "A sorts roles; B connects deeds and reasons; C
  sequences" (s03).
- **Fix.** No edit now; the section writer writes each move as one full sentence with who does what ("On day 86 the
  teacher models naming the next best thing given up").

### C6. The skeleton still drops the K to 2 `observe` assessment and the one-section U fields (skeleton)

LAYER skeleton. REPEAT yes (kindergarten structure items 1 and 2, not yet applied).
- scripts/unit_skeleton.py line 870 still filters `('end', 'mid')`; every grade 1 writer patched field 5 by hand
  ("The data row says `observe`, not `end`"). Exit tables again sit in field 5 for want of U3. See "For the
  structure pass".

## Unit 1. Our groups (days 1 to 10)

### 1.1 The start-of-year check duplicates the retrieval tasks and cannot run as written (moderate)

LAYER plan. REPEAT yes (kindergarten read 1.2, settled there).
- **What is wrong.** Field 4: "Use ten minutes a few days before opening", three one-to-one oral items on
  kindergarten rows. Course day 1 is school day 2, so there are no "few days before"; thirty oral answers do not fit
  ten minutes; and all three rows were used the year before, so by rule they are retrieval tasks (sequence-write rule
  2; scope-and-sequence "Readiness"), which s01 already holds on days 1, 3 and 6. The kindergarten course hands its
  record to the grade 1 teacher (kindergarten days.csv day 64), and s01 never uses it.
- **Why it matters.** The check either eats day 1 or does not happen, and the gap blocks it selects (A on day 2, B on
  day 4, C on day 7) fire on nothing.
- **Fix.** s01 field 4, replace the paragraph after "**Given:**" and its first line with: "The start-of-year check,
  defined here. Grade 1 assumes only kindergarten rows, used the year before, so it is not a test and not a separate
  sitting. Before day 1 the teacher reads the kindergarten record sheet passed on at the end of kindergarten, where
  there is one. During days 1 to 3 the teacher notes three access look-fors for each child on the record sheet: asks
  or shows a wonder, gives any reason for a rule, says what a class job does; and how each child prefers to answer
  (speech, home language, pointing, drawing). No score bars entry." Keep the item table as the look-fors, and the gap
  blocks, now fed by the day 1, 3 and 6 retrieval tasks.

### 1.2 D1.3.K-2 is given a part it does not have (minor)

LAYER plan. REPEAT new.
- **What is wrong.** Field 2 paraphrases D1.3.K-2 as "Construct smaller questions and identify the facts and
  concepts each needs"; the indicator is only "identify facts and concepts associated with a supporting question"
  (C3, rev. 2017, read this run). Item 2's part column then tests "construct". Making the link between supporting and
  compelling questions is D1.4.K-2, which no grade 1 day cites.
- **Fix.** s01 field 2: the D1.3 line becomes "**D1.3.K-2.** Identify facts and concepts associated with a supporting
  question. Parts: identify facts; identify concepts. Writing the supporting questions is the course's own row
  (ss1-supporting-questions)." Item 2's part cell: "Identify facts and concepts (questions written as the row's
  practice)". D1.4.K-2 goes to the structure pass.

### 1.3 Item 2's does-not sample is not a child's likely answer (minor)

- s01 item 2: "Is music nice? Is music nice? I need music." becomes "Is the show fun? Do I like it?" (A: questions a
  preference cannot answer and needs no fact).

## Unit 2. Clues from the past (days 11 to 19)

### 2.1 No source about "our school" is planned, so day 16 cannot do its goal (moderate)

LAYER plan. REPEAT new.
- **What is wrong.** The compelling question and day 16's goal are about "the school or town", but every then source
  is from somewhere else (Johnston's Washington classrooms about 1899, an Iowa bus caption of 1928). The plan says so
  itself ("Another school's photograph cannot establish our school's history"). The question is still answerable as
  a method question (which kinds of source would tell us), so the inquiry holds, but day 16's "then and now of the
  school or town" becomes another school then against ours now.
- **Why it matters.** Bar item 1 fails if "its question is answered without the unit's content"; here the risk is the
  reverse, children learning that another school's photograph is our past (the plan's own error D).
- **Fix.** s02 field 10, after the "Secondary text" paragraph, add: "Our own school first. Where the school office,
  the district's website or the town's own records hold a dated photograph or record of this school or town, the
  teacher prints it for day 16 beside the Johnston photograph. Where none can be found without a library visit,
  day 16 compares Johnston's classroom with today's classroom drawing and names what a photograph of our own school
  would add; the class's answer to the compelling question is then the kinds of source it would look for." Field 2,
  "Closing": add "The answer may be a plan of which sources to find."

## Unit 3. Leaders (days 20 to 31)

### 3.1 Dolores Huerta died on October 28, 2026, and the plan gives the teacher nothing on Chavez (serious)

LAYER plan and data. REPEAT new.
- **What is wrong.** s03 links "Huerta's community memorial" but nowhere tells the teacher she has died; days.csv day
  24 and the frame describe her only as organizing "from 1962 on". Huerta died on October 28, 2026, at 96 (AARP,
  WTTW, Courthouse News). The settled swap from Cesar Chavez rests on Huerta's own March 2026 statement that Chavez
  sexually abused her (OPB, March 18, 2026), yet the plan has no teacher note for the child who names Chavez (schools,
  streets and a state holiday carry his name), and its study list names no source on the 2026 statements; its
  "Chicano historians" line points to a paid book.
- **Why it matters.** The NPS Huerta page and older summaries speak of her in the present tense; a writer will copy
  that. Without a note, a teacher asked "What about Cesar Chavez?" has to improvise on child abuse allegations in
  front of six-year-olds.
- **Fix.** days.csv day 24 note, add at the start: "Dolores Huerta (1930 to 2026) died on October 28, 2026; taught in
  the past tense." s03 field 2, "Limits", add: "Huerta is taught in the past tense (1930 to 2026). She and Cesar Chavez
  started the farm workers' union together; if a child names him, the teacher says so in one sentence and that this
  class studies Huerta's work. Nothing about the 2026 statements is taught at this age." s03 field 10, the
  sensitivity paragraph: replace "accessible scholarship from the contributors to Mario T. Garcia's Huerta reader
  ... paid book excluded" with "Huerta's March 2026 statements as reported (for one, OPB, 2026-03-18) and an obituary
  of record (October 2026), to judge the teacher note on Chavez; and a free article by a Chicano historian the agent
  names".

### 3.2 Exit 23 models emancipation as opening a path (minor)

LAYER plan. REPEAT new.
- **What is wrong.** Day 23's exit analogue for Lincoln is "a council leader signed a rule opening a public path".
  Read beside the day's Emancipation Proclamation it makes ending slavery parallel to opening a path.
- **Fix.** s03 day 23 exit: replace the invented case with "An invented record says a town leader asked the council
  to build a school, and builders and families worked for a year to open it. What action and quality might you
  investigate? Ask one question about the builders or families."

## Unit 4. Choosing together (days 32 to 41)

No finding of its own. C1 and C2 apply (day 40 holds four multi-part spoken items in 25 minutes); C3 moves day 37
to the Navajo Nation. What is right: made-up candidates whose deeds are on cards, the tie rule, the election and
vote distinction kept apart, and eligibility kept apart from belonging.

## Unit 5. Maps and places (days 44 to 55)

### 5.1 "The two living nations" leaves out the Munsee people of the place itself (moderate)

LAYER plan. REPEAT new.
- **What is wrong.** Field 6 contrast H: "show the two living nations' government pages" (Delaware Nation and the
  Delaware Tribe of Indians, both in Oklahoma). The Lenape of the Manhattan area were Munsee-speaking, and the
  Stockbridge-Munsee Community in Wisconsin, a federally recognized nation, includes their descendants; Munsee and
  Delaware nations also live in Ontario. From memory; the agent should confirm on the nations' own pages.
- **Why it matters.** "Two" reads as all; the lens asks for Native nations named by their own names and shown as
  more than one people today.
- **Fix.** s05 field 6, contrast H: "show the two living nations' government pages" becomes "show government pages of
  Lenape nations today, among them the Delaware Nation and the Delaware Tribe of Indians in Oklahoma and the
  Stockbridge-Munsee Community in Wisconsin". s05 field 10, "Production references": add the Stockbridge-Munsee
  Community's own history page, and add it to the sensitivity agent's study.

### 5.2 Day 52's local water may not exist (minor)

- Item 5 asks for "a documented local park with water"; many schools have none nearby and the plan bars travel. Add
  to s05 field 8: "Where no local place has water, the teacher uses a supplied photograph set of a small park with a
  pond, labelled as another place."

## Unit 6. One country, many people (days 56 to 68)

### 6.1 Tahlequah sits among "ways of living around the world" (moderate; a judgment call)

LAYER plan. REPEAT new.
- **What is wrong.** Days 56 to 58 compare Tahlequah, Sapporo and Singapore under MA.1.T2.5 ("different parts of
  the world"). Setting the Cherokee Nation's capital beside Japan and Singapore invites six-year-olds to file Cherokee
  people as foreign, the framing the lens and the frame ("no exotic framing") warn against; day 60 then teaches the
  same nation as part of American diversity. Two of the three places are also in Asia.
- **Fix** (settled, see the table). Days 56 to 58 use Sapporo, Singapore and Nairobi, Kenya (cool highland weather,
  two seasons of rain, English and Swahili). The Cherokee Nation stays on day 60 as a living nation inside the United
  States, with its language school. s06 field 2 hook, field 10 production references and items 1 and 2 keep their
  shape with Nairobi in Tahlequah's teaching place (the held-out items already use Sapporo and Singapore views
  different from teaching; give Nairobi's teaching views the same rule). The sensitivity study adds Nairobi's city
  government pages and Kenya's ministry of education pages. If a reader prefers to keep Tahlequah, the minimum fix
  is to place it on the United States map on day 56 and say aloud "a city in our own country, the capital of the
  Cherokee Nation".

### 6.2 The bald eagle's current legal status is missing (minor)

LAYER plan. REPEAT yes (kindergarten read 5.7; settled: current official facts for symbols).
- s06 field 6 contrast D, add: "Since December 2024 the bald eagle has been the national bird by law."

### 6.3 Town data arrives as percentages (minor)

- Census QuickFacts gives percentages, which grade 1 cannot read. s06 field 10, "Local evidence": add "Show each
  figure as a ten-square strip with the shaded squares counted, and the words 'some' or 'many'; no percent sign."

## Unit 7. Helping our community (days 69 to 80)

### 7.1 Birthright citizenship was decided this year, and the plan does not say so (moderate)

LAYER plan. REPEAT new.
- **What is wrong.** Day 69 teaches "people born in the United States are citizens" (MA.1.T1.9). In 2025 an executive
  order tried to narrow this; on June 30, 2026 the Supreme Court held it unconstitutional (Trump v. Barbara, 6 to 3).
  s07 cites Plyler only, and says "Citizenship source attempted: ... blocked; anchor paraphrase controls this draft".
- **Why it matters.** Values rule (a): side with the higher court. A teacher who has followed the news needs the
  current law in one line, and the sensitivity agent should read it.
- **Fix.** s07 field 2, "Limits", add: "Teacher background: people born in the United States are citizens under the
  Fourteenth Amendment; the Supreme Court upheld this on June 30, 2026 (Trump v. Barbara). Not taught as a dispute at
  this age." s07 field 10: replace "Citizenship source attempted: federal naturalization brochure blocked; anchor
  paraphrase controls this draft" with "Citizenship: the Fourteenth Amendment (National Archives transcript) and the
  Supreme Court's June 30, 2026 opinion in Trump v. Barbara, teacher background." Add the opinion to the sensitivity
  study list.

### 7.2 Kindergarten's talk rules get no retrieval task (minor)

LAYER data. REPEAT new.
- ss1-community-problems assumes ssk-talk-together, a row from the year before not retrieved earlier this year, and
  days.csv holds no retrieval note in unit 7 (field 4 says "Given: none"). days.csv day 72 note: prepend "Retrieval
  task: kindergarten's talk rules and two points of view (ssk-talk-together)." s07 field 4 then gets one retrieval
  row: "72 | ssk-talk-together | After the hook: 'One friend wants the quiet corner, one wants to talk about a book.
  Say what each wants and why.' A child who names only one side joins a five-minute two-sides sort during the day's
  first teaching minutes." The same data gap in unit 5 (ssk-maps-globes, which s05 already retrieves on day 46): add
  "Retrieval task: kindergarten's maps and globes (ssk-maps-globes)" to days.csv day 46's note.

## Unit 8. Earning, buying and saving (days 81 to 93)

### 8.1 Day 87 holds the only teaching of MA.1.T4.8 and four observations (moderate)

LAYER plan. REPEAT yes (kindergarten settled rule: observations never take the only teaching minutes of a new skill).
- **What is wrong.** Field 5: "items 1 to 3 on 87 after prior teaching, item 4 after teaching on 87". Day 87 is the
  only day that teaches values-based buying, and in 30 minutes it must also observe employment, goods and services,
  and opportunity cost.
- **Fix** (settled, see the table). s08 field 5, replace "items 1 to 3 on 87 after prior teaching, item 4 after
  teaching on 87, item 5 after teaching on 88, item 6 after teaching on 89 and item 7 after teaching on 90" with
  "item 1 on 83, item 2 on 85, item 3 on 87, item 4 on 88, item 5 on 89, item 6 on 90, items 7 and 8 on 92, each the
  day after its teaching and inside supported work". Field 7 marking: "ten teacher minutes after each day 87 to 90"
  becomes "ten teacher minutes after each of days 83, 85 and 87 to 90".

### 8.2 No named study list for the sensitivity agent (minor)

- s08 is the only unit without a "Sensitivity study owed" paragraph. Add at the end of field 10: "Sensitivity study
  owed: the two community sources above first, then the federal Money as You Grow page, and one school-facing source
  on teaching money to children in poverty that the agent names. Check family privacy, shame about means, unpaid care
  as work and the optional share jar."

## Settled by the expert

| Choice | Reason, in one line | File it touches |
|---|---|---|
| K to 2 exit format in s01 to s07 (applies the kindergarten settlement): every child marks a picture, a rotating six give the spoken why | Unit 8 already does it; thirty spoken answers do not fit two minutes | s01 to s07 field 5 |
| End-of-unit spoken parts heard in five groups of six on the assessment day or from the rotation on the two days before | One teacher, 30 minutes | s01, s02, s03, s04, s05, s07 field 5 |
| Grade 1 start-of-year check = the kindergarten record plus three access look-fors noted in days 1 to 3, no separate sitting | All assumed rows are the year before; retrieval already covers them | s01 field 4 |
| Unit 4 day 37's Native government example is the Navajo Nation | Three of four Native examples were one nation | s04 fields 5, 6, 10; days.csv day 37 goal |
| Unit 6's three places are Sapporo, Singapore and Nairobi; the Cherokee Nation stays on day 60 | Keeps a Native nation out of "around the world" and spreads the continents | s06 fields 2, 5, 10; days.csv day 56 note unchanged (it names no place) |
| Unit 8 observations moved to the day after each teaching day | MA.1.T4.8's only teaching day keeps its minutes | s08 fields 5 and 7 |
| Huerta taught in the past tense; Chavez named in one sentence as co-founder if a child asks, the 2026 statements not taught | Current fact; grade and life experience (values rule d) | s03 field 2; days.csv day 24 note |
| Day 23 exit analogue: a leader asks for a school to be built | The path case paralleled emancipation | s03 field 5 |
| Town data as ten-square strips, no percent | Grade 1 has no percent | s06 field 10 |

## For the fixer (exact edits, in order)

1. s01 to s07, field 5: the exit paragraph and each exit row's "Mark:" sentence (C1).
2. s01, s02, s03, s04, s05, s07, field 5: the administration sentence and the specific moves (C2).
3. s01: field 4 start-of-year paragraph (1.1); field 2 D1.3 line and item 2's part cell (1.2); item 2's does-not
   sample (1.3).
4. s02 field 10 "Our own school first" paragraph and field 2 closing sentence (2.1).
5. s03 field 2 Limits Huerta sentence, field 10 sensitivity study replacement (3.1); day 23 exit (3.2).
6. s04 day 37 to the Navajo Nation: field 5 exit 37, field 6 contrast G, field 10 references and study list (C3).
7. s05 field 6 contrast H and field 10 references and study (5.1); field 8 water stand-in (5.2).
8. s06: Nairobi in Tahlequah's place in fields 2, 5 (teaching views only), 6 and 10, Cherokee kept on day 60
   (6.1); field 6 bald eagle line (6.2); field 10 town data strips (6.3).
9. s07 field 2 teacher background and field 10 citizenship sources (7.1); field 4 retrieval row (7.2).
10. s08 field 5 observation days and field 7 marking (8.1); field 10 sensitivity study (8.2).
11. days.csv: day 24 note (3.1); day 37 goal (C3); day 46 note (7.2); day 72 note (7.2). Then bring each changed
    row into the matching plan's "Day list" table by hand (do not rerun the skeleton over written plans).
12. s01 to s08, each Tennessee row's wording (C4).

## For the structure pass

1. scripts/unit_skeleton.py line 870: add `'observe'` to the assessment filter, labelled "End-of-unit assessment
   (observation)". Kindergarten structure item 1, still open; every grade 1 writer patched it. REPEAT.
2. The one-section unit and its U fields (kindergarten structure item 2), still open. REPEAT.
3. A written K to 2 exit and observation default (kindergarten structure item 3). Grade 1 shows why it must live in a
   file the writer reads: one of eight writers found the settlement, seven did not. Put it in UNIT-PLAN.md's social
   studies fill or the plan brief's "Settled" line for K to 2. REPEAT.
4. data/progressions/social-studies.csv, ss1-supporting-questions: add D1.4.K-2 (make connections between supporting
   and compelling questions), the indicator the row actually teaches, and cite it on days.csv days 1 and 21. New.
5. Retrieval notes: plan.py could flag a K row in a grade 1 progression row's `assumes` that has no "Retrieval task"
   note anywhere in the course (caught here by hand: ssk-talk-together, ssk-maps-globes). New.
6. The plan brief's sensitivity line could ask each writer to search the news for the people a unit names
   (Huerta's death came 17 days before these plans were written). New.

## For Cory

None.

## What is right and should not be touched

- Every invented case, record and picture is labelled invented; every real source carries its rights line and what
  was read of it.
- Unit 3's honest limits: Tubman's helpers and agency, the Proclamation's limits, collective action with each
  leader; an unstudied leader (Jane Addams) for the assessment.
- Unit 4's made-up candidates, eligibility kept apart from belonging, "accepting a result" never meaning silence.
- Unit 6's Pledge and songs as study, never performance, under Barnette; the record kept apart from later meanings.
- Unit 7's status privacy, the look-back six school days after the action, and "limited or no improvement is an
  acceptable conclusion".
- Unit 8's two-part exits and spread observation, the optional share jar, unpaid care counted as work.

## What I could not judge

- The Johnston photographs (loc.gov refuses automated reading) and so whether s02's sample answers match them; the
  plan already says to inspect before production.
- The Sapporo and Singapore views (not yet chosen).
- Tennessee's grade 1 lines (blocked).

## Sources

- [C3 Framework, NCSS, rev. 2017](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf): indicator wordings, 1.2 and the D4 checks.
- [NPS, Cabrillo group volunteering](https://www.nps.gov/cabr/getinvolved/group-volunteering.htm) and [NPS, Trashbusters](https://www.nps.gov/articles/000/impacts-beyond-the-beach-trashbusters-and-their-shared-mission.htm): unit 1's sources confirmed (H. Marquez photo, Coastal Trail caption, updated March 22, 2025).
- [AARP obituary](https://www.aarp.org/events-history/dolores-huerta-obit-united-farm-workers/), [WTTW](https://news.wttw.com/node/55318), [Courthouse News](https://www.courthousenews.com/dolores-huerta-influential-labor-leader-feminist-and-civil-rights-icon-dies-at-96/): Huerta's death, 3.1.
- [OPB, 2026-03-18](https://www.opb.org/article/2026/03/18/cesar-chavez-accused-of-sexually-abusing-labor-rights-leader-dolores-huerta): Huerta's statements on Chavez, 3.1.
- [WHYY](https://whyy.org/articles/supreme-court-upholds-birthright-citizenship/), [Semafor](https://semafor.com/article/06/30/2026/supreme-court-rejects-trumps-birthright-citizenship-executive-order): Trump v. Barbara, June 30, 2026, 7.1.
- [Navajo Nation Council, about](https://www.navajonationcouncil.org/about-us-and-history/): 24 delegates, four-year terms, C3.
- From memory, not fetched: the Stockbridge-Munsee Community's Munsee descent (5.1); the bald eagle national bird law,
  December 2024 (confirmed in the kindergarten read); Nairobi's climate and languages (6.1).

Confidence: C1, C2 likely (classroom arithmetic, settled in kindergarten); 3.1 and 7.1 firm on the facts, judgment on
the wording; C3, 6.1 judgment calls; 5.1 likely; 1.1, 8.1 likely; 1.2 firm.

## For the source list

- doloreshuerta.org and nps.gov/people pages are readable; news sites carry the October 2026 obituary.
- navajonationcouncil.org and navajo-nsn.gov are the Navajo Nation's own pages for unit 4.

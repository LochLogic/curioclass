# Expert read: the English language development progression, K to 12 (2026-11-21)

A cold read of data/progressions/eld.csv by the curriculum expert (docs/agents/EXPERT.md), with a fresh sensitivity
read for students learning English, their families and teachers. Edits nothing but this report.

## What was read

- docs/agents/EXPERT.md, docs/agents/lenses/eld.md, docs/RUBRIC-ELD.md (all), docs/ADOPTION-BAR-SUBJECTS.md part 10
  (items 1 to 14, Fails if, Unsupported, Scope and sequence states).
- The layer above, in full: docs/courses/eld/STANDARD.md (168 lines) and docs/courses/eld/APPROACH.md (169 lines).
- data/progressions/eld.csv: 162 rows (K 10, grade 1 11, grades 2 and 3 12 each, grades 4 to 12 13 each), every row
  and every field. data/progressions/eld-edges.md. data/standards/wida-2020.txt (104 ids).
- Every cross_subject target (248 distinct host rows, discussion and seminar rows aside) looked up in
  data/progressions/ela.csv, math.csv, science.csv and social-studies.csv: the row's grade and the opening of its notes.
- `python -X utf8 scripts/progression.py check eld`: 162 rows, 0 failures. `python -X utf8 scripts/stale.py check` on
  eld.csv, eld-edges.md, STANDARD.md and APPROACH.md: 0 failures. plan.py not run (brief). No reconcile report exists.
- Earlier progression reads in docs/reviews/ (science and social studies, 2026-11-13), section headings only, to set
  REPEAT. No ELD course page or earlier ELD review was opened.

## Verdict

The skeleton is sound: all 104 ids are owned once, every `assumes` and `hands_on` runs one grade at a time, every
host row exists at the stated grade, the first-appearance rule (a new key language use builds on the year-before SI
row) is applied where APPROACH says, and every `~` row has its own task sentence. The biggest risk is that, under
each task sentence, the rows are one stock text per owned id: the entry points, words and models are copied
verbatim into every carried year (54 entry-point texts and 56 word lists for 162 rows), the entry points often give
the lower levels an easier task rather than more help, and 75 of 75 math, science and social studies rows name the
content but no form of English. The one change that matters most is to rewrite each row's entry points as one shared
task with per-level support and a named withdrawal, and to add a "Forms:" sentence that grows by cluster (findings 1
and 2); without both, a frame writer builds ELD units that read as content lessons with easier work for newcomers,
which bar part 10 fails outright.

## Findings, most serious first

### 1. Entry points change the task, not the help, and are copied into every carried year (serious; firm)

LAYER progression. REPEAT new.

- **What is wrong.** Bar item 2 says every entry point does the same task on the same content at the same thinking
  demand, and "Fails if" lists "a lower entry point given an easier task". Many rows give levels 5 and 6 a thinking
  step levels 1 and 2 never take:
  - g2-ss-argue: the host (social-studies:ss2-two-accounts) is comparing two accounts; levels 1 and 2 "choose a side
    and point to a source", only 5 and 6 "compare two sources".
  - The whole SS Explain chain, g4-ss-explain to g12-ss-explain: 1 and 2 "order cause-and-effect cards", 5 and 6
    "explain several causes and weigh them". Weighing is the thinking demand of the host.
  - The SS Argue chain g4 to g12: only 5 and 6 "corroborate sources". The MA Argue chain g4 to g12: only 5 and 6
    "critique another solution". The SC Argue chain: only 5 and 6 "answer another claim".
- **Copied text.** The "Entry points" sentence of every `~` row is its owner's word for word: 54 distinct texts in
  162 rows. SI 4-12 carries one text through nine grades, so the text no longer fits the task:
  - g12-si-inform: the task is an email to a teacher or an office; 5 and 6 "summarize the plan for a new group member".
  - g12-si-explain: the task is a plan for after high school; 5 and 6 "explain a change of plan".
  - g10-si-narrate: the task is a formal club report; 1 and 2 "retell a shared group event from picture notes".
  - g3-ss-explain (plain error): the host is levels of government, but 3 and 4 "say how people use or change a
    place", copied from g2-ss-explain.
- **The stock line.** The "In grade N ..." line on SI rows is one sentence for all four SI rows of a grade (for
  example "In grade 7 group roles and lab routines add structured turns" on all four grade 7 SI rows). It shows
  how the grade differs; it does not show how that key language use differs.
- **Cost.** A frame writer copies these into unit field 5 and section field 9. Newcomers get a matching task while
  classmates analyze. That is the failure the bar names, and a PRIME reader would mark it down under Depth.PLD (b).
- **Fix.** Rewrite each row's entry points in one pattern: "Entry points (all [the one task]): levels 1 and 2 with
  [support]; 3 and 4 with [support]; 5 and 6 with [support], [what is withdrawn]." The language each level produces
  may differ, but the task may not. Three rewrites to model the rest on:
  - g2-ss-argue: "Entry points (all compare the two accounts and state a claim from them): levels 1 and 2 with both
    accounts read aloud and pictured, a two-column picture chart (both say, only one says), the frame 'Both say ___.
    I think ___.' and talk in the home language first; 3 and 4 with the claim chart and 'Both accounts say ___, but
    ___. I think ___ because the source says ___.'; 5 and 6 with the claim chart only, frame withdrawn, adding 'one
    account says ___ while the other ___'."
  - g7-ss-explain: "Entry points (all explain two causes of Rome's fall and say which mattered more): levels 1 and 2
    with pictured cause cards on the cause chain and 'One cause was ___. This led to ___. ___ mattered more.'; 3 and
    4 with the cause chain and frames using 'because of', 'as a result' and 'led to'; 5 and 6 with the cause chain
    only, joining causes with 'not only ... but also' and 'the main reason was'."
  - g12-si-inform: "Entry points (all write a short request to a school office and then say it aloud): levels 1 and
    2 with a model message to copy and change, a bank of request phrases and a rehearsal with the teacher; 3 and 4
    with frames for greeting, request and thanks ('I am writing to ask about ___. Could you ___?'); 5 and 6 with no
    frame, writing the same request once for a classmate and once for an office."
  - g3-ss-explain: replace the 3 and 4 clause with "say what one level of government does and why, with 'so' and
    'because'".

### 2. The content rows name content, not language, and the LA rows restate ELA (serious; firm)

LAYER progression. REPEAT new.

- **What is wrong.** Bar item 3 says each form is taught as a feature that does a named job, at all three
  dimensions (whole text, sentence, word or phrase). Item 13 says earlier forms return. No form appears in any
  math, science or social studies task sentence (0 of 75 rows). Only about 8 of 35 LA rows and 8 of 52 SI rows name
  one (for example g2-la-narrate "then, after and finally", g5-la-argue "therefore and for example").
- **Examples.** g7-sc-explain ("explain photosynthesis and how cells use food ... from the science unit") and
  g9-ss-explain are content objectives. The LA rows set the ELA product at every level: g8-la-argue ("delineate and
  evaluate an argument ... write an argument that cites credible sources and answers counterclaims") is RI.8.8 and
  W.8.1 restated, and g5-la-narrate is RL.5.5 and W.5.3. STANDARD section 5 says ELD "does not reteach ELA".
- **What the gate cannot see.** The `words` column is mostly content or topic words, so it cannot carry this.
- **Cost.** Without a form per row, item 13 (forms return and grow) cannot be checked at the scope and sequence, and
  a writer fills the ELD period with the host lesson again. That is the lens's "ELA lesson repeated".
- **Fix.** Add one sentence to every row's notes, after the task: "Forms: [text level]; [sentence level]; [word
  level]." Grow it along the ladder below (settled by the expert, from memory of functional-grammar practice and the
  three dimensions in RUBRIC-ELD; a frame may swap within a cell). `~` rows take the lower half of their cluster's
  cell and owner years take the whole cell.
  - **Narrate.**
    - K to 1: past tense of common verbs; time words; "and then".
    - 2 to 3: irregular past; said-words and dialogue marks; then, after, finally.
    - 4 to 5: time clauses (when, while, as soon as); describing noun groups; past progressive.
    - 6 to 8: past perfect for flashback; point-of-view pronouns kept steady; varied dialogue tags.
    - 9 to 12: tense shifts on purpose; reflective language ("looking back, I"); tone words.
  - **Inform.**
    - K to 1: "This is / it has / they can"; labels.
    - 2 to 3: topic sentence; general present ("Frogs lay eggs"); also, another, for example.
    - 4 to 5: definition sentences ("A ___ is a ___ that ___"); relative clauses; in addition, for instance.
    - 6 to 8: classifying ("can be divided into", "types of"); formal register with no "you"; section transitions.
    - 9 to 12: synthesis ("both sources", "whereas"); nominalization; quotations worked into a sentence.
  - **Explain.**
    - K to 1: "when ___, ___"; because.
    - 2 to 3: first, next, so; present tense for how things work.
    - 4 to 5: as a result, which causes; one process noun (erosion).
    - 6 to 8: passive voice for processes ("water is heated"); nominalization (evaporation); if ... then.
    - 9 to 12: dense noun groups; cause verbs (results in, contributes to); hedging (may, suggests).
  - **Argue.**
    - K to 3 (SI): "I think ___ because"; "I agree with ___ because".
    - 2 to 3: claim plus "the data shows" or "the source says".
    - 4 to 5: grouped reasons; for example, therefore; should.
    - 6 to 8: reporting verbs (claims, argues, states); "Some people think ___. However, ___"; according to.
    - 9 to 12: concession ("Although ___, ___"); hedging and boosting modals; rebuttal moves; evaluative words.
- **A model LA rewrite**, g8-la-argue task: "Students take apart one paragraph of the ELA unit's argument: how the
  writer brings in a counterclaim ('Some argue that ... However, ...') and which reporting verbs carry the sources.
  They then build one paragraph that answers a counterclaim, with the teacher first and then alone. The full essay
  stays in ELA." Each LA row names the one paragraph or passage ELD takes from the ELA text, and what stays in ELA.

### 3. Scaffolds are never withdrawn in the data (serious; firm)

LAYER progression. REPEAT new.

- **What is wrong.** Bar item 3 and California 4.1 (STANDARD section 4) want scaffolds withdrawn as proficiency
  grows, and the lens lists "a frame that is never withdrawn" as an error. In the data, "sentence frame" and "word
  bank" sit in model_in and model_out of nearly every row from K to grade 12 (323 and 321 mentions), and
  model_in equals model_out in 158 of 162 rows. Only g4-la-narrate names a withdrawal point ("the frame comes off
  for levels 5 and 6 by mid-unit"). About 18 rows say "without the frame" for 5 and 6, and a few say "thins" with
  no point named.
- **A second fault.** A sentence frame and a word bank are scaffolds, not models. Listing them as models hides the
  four real models and makes the model chain look continuous when nothing grows.
- **Cost.** A writer reads "sentence frame" as a model that every grade 12 unit carries in and out, and C7's
  withdrawal day is never planned.
- **Fix.** Remove "sentence frame" and "word bank" from model_in and model_out in all 162 rows; they belong in unit
  field 2 ("what is carried, and the day each is withdrawn"). Add to each row's entry-point sentence (finding 1)
  what comes off and when. The default, settled below: for 5 and 6 the frame comes off after the first application
  day; for 3 and 4 before the end-of-unit writing task; 1 and 2 keep the word bank and lose the cloze frame before
  the check. Each `~` row also says which support its owner year no longer gives (for example g2-la-inform: "the
  linking-word frame is gone for 3 and 4 in grade 3").

### 4. The four models do not grow (moderate; firm)

LAYER progression. REPEAT yes (the social studies read of 2026-11-13 named model gaps).

- **What is wrong.** The six model names have no gap in the chain, because each is present K to 12 (story map 51
  mentions, text map 81, cause chain 95, claim chart 111). That is the problem: each name means the same thing in K
  and grade 12, and no row says what the model adds. There is one small inconsistency in K: k-si-inform carries
  "sentence frame" in model_in, but nothing introduces it before K; k-si-narrate leaves model_in empty.
- **Fix.** Keep the names, so the gate's chain holds, and put the stage in the owner-year row's notes ("Model:
  ..."), settled below:
  - claim chart: K to 1 a picture vote chart (choice and one reason); 2 to 3 claim and reason with its source; 4 to
    5 claim, grouped reasons, evidence; 6 to 8 adds a counterclaim and response; 9 to 12 adds rebuttal and the
    limits of the evidence.
  - cause chain: two linked boxes; then a chain with "so"; then branching causes; then a mechanism with an
    unseen step; then weighted, multi-factor causes.
  - story map: three pictures; then problem and solution; then theme, scenes and pacing; then point of view and
    episodes; then structure across time.
  - text map: topic and facts; then grouped parts with headings; then the text's structure (cause, compare,
    sequence); then sections building a central idea; then two or more sources synthesized.

  Also empty k-si-inform model_in.

### 5. Words do not grow, and some do not fit the grade (moderate; firm)

LAYER progression. REPEAT new.

- **What is wrong.** There are 56 word lists for 162 rows: every carried row repeats its owner's list. SI K-3 gives
  grade 3 "this is; it has; color; big; small; show" (g3-si-inform), below a grade 3 sharing time with clarifying
  questions. SI 4-12 gives grades 4 to 12 the same five words. g12-si-narrate, an interview recount, has "after
  that; meanwhile; finally; our group; at first". g12-si-inform, messages to offices, has "the task is; step; plan;
  role".
- **Fix.** Each row's words fit its own task, keeping at most half of the year before. Replacements (settled):
  - g3-si-inform: "I learned that; for example; also; What do you mean by; Can you say more about"
  - g8-si-inform: "brief; the main steps are; first of all; any questions; to clarify"
  - g11-si-inform: "I would like to ask about; Could you tell me; appointment; I am calling about; thank you for"
  - g12-si-narrate: "at the time; I was responsible for; as a result; I learned; looking back"
  - g12-si-inform: "I am writing to ask; regarding; would it be possible; I would appreciate; please let me know"
  - g12-si-explain: "my plan is to; the main reason; in order to; one option is; so that"
  - g12-si-argue: "I propose; I understand that; however; that is a fair point, but; I still believe"

  Apply the same rule to the SI rows of grades 5 to 11 and to the LA, MA, SC and SS `~` rows: each adds two to four
  words its own task needs.

### 6. Sensitive ground: cases a teacher, family or student could reasonably object to (moderate; firm on the rule, judgment on wording)

LAYER progression. REPEAT new. The rule is APPROACH.md, "Sensitive ground". The Narrate rows already carry the
"one of several prompts, invented character allowed" note, and that should stay. These rows need more:

- **k-ss-inform.** The host (social-studies:ssk-jobs-helping) includes a home job, and talk about community jobs
  drifts quickly into "What does your mom or dad do?". APPROACH forbids asking about a parent's work. Add: "Teacher
  note: no task asks what a family member does for work; students describe helpers from the unit's pictures,
  visitors and class jobs."
- **g4-ss-argue.** The host (social-studies:ss4-canada-mexico-research) researches a country's people and
  languages. A student from Mexico must not be made the class expert, asked for family knowledge, or asked to
  translate a source. Add: "Teacher note: a student from the country studied is never made the class expert or
  asked to translate; they choose their topic like everyone else."
- **g2-ss-argue.** The host's worked example is "two newcomers' memories of one ship arrival". That is a migration
  text in a class of English learners, and the row's conditional note does not say that this host is one. Add:
  "Teacher note: the host's example pair is about newcomers arriving; the family note previews it and offers the
  host's other pair (two reports of a town flood); no student is asked about their own arrival."
- **All 25 SS rows** carry the same conditional "when the host unit is about migration, war or loss" line, including
  econ-markets-prices and ss3-levels-of-government. The progression already knows which hosts are sensitive.
  - Name the topic where it is: ss4-disasters-response (disaster and loss: students who lived through a hurricane,
    flood or earthquake), ss5-revolution-causes (war), ss7-rome-fall (invasion), wh1-geography-shapes-contact
    (migration and conquest), wh2-imperialism-causes (colonial rule, which some families lived under),
    us1-sectional-crisis (slavery and the coming war), and us1-news-reading (news may touch immigration
    enforcement: pick pieces on other topics, or offer one of several).
  - Drop the line where it is not, so the warning keeps its force.
- **g11-si-inform, g11-si-explain, g12-si-narrate, g12-si-explain.** Counselor meetings, applying for a program,
  college or job interviews, and a plan for after high school can touch work authorization, aid eligibility and
  family situation. APPROACH bars asking about immigration status, and a real plan cannot be required. Replacement
  for g12-si-explain: "Students explain a plan, their own or an invented student's, for a project, a program or the
  year after high school, and the reasons for it, in talk and in a short written statement." Add to all four:
  "Teacher note: a student may speak as an invented applicant; no task asks about documents, aid eligibility or a
  family's situation."
- **g12-la-narrate.** "A personal statement" invites the hardship essay that immigrant students are often steered
  toward. Replace with "a personal statement or a story on a topic the student chooses, real or invented", and add:
  "Teacher note: no student is asked or nudged to write about migration, loss or hardship."
- **g9-si-inform, g9-si-argue, g11 SI rows (register).** "A formal register for adults" can be read as informal
  English or the home language being wrong. Add to the g9 SI rows: "Teacher note: informal English and the home
  language are not wrong; the task is choosing for the listener."
- **g1-sc-inform.** "How a young animal is like its parent" is fine about animals. Add a short note that the
  lesson does not extend to "How are you like your parents?" (students apart from a parent, in foster care or
  adopted).
- **No row uses the home language at all.** "Home language", "cognate" and "Spanish" appear in no row, while bar
  item 6 is planned in every unit. This belongs to unit plans, but each owner-year row should carry one line of
  home-language help (for example g8-sc-explain: "Home language: Spanish cognates for process nouns, such as
  evaporación and evaporation"). Without it, item 6 has no anchor at the progression.

### 7. Three cross_subject leans do not ask for the row's key language use (moderate; firm)

LAYER progression. REPEAT yes (the social studies read of 2026-11-13 found leans naming the wrong skill).

All 248 host rows exist at the stated grade. These three do not ask for the language:

- **g4-sc-argue lean `science:s4-energy-resources`.** The host is 4-ESS3-1, "obtain and combine information to
  describe": that is Inform, not Argue. Replace it with `science:s4-information-codes (comparing solutions)`
  (4-PS4-3 with 3-5-ETS1-2, generate and compare solutions), and change the task clause "which energy resource has
  fewer effects" to "which way of sending a coded message works best, from the class's tests".
  science:s4-hazard-solutions also fits, but it brings disaster ground (finding 6), so it was not picked.
- **g11-sc-argue lean `science:phys-big-bang-evidence`.** The host is HS-ESS1-2, "construct an explanation". Replace
  it with `science:phys-em-radiation-effects (judging published claims)` (HS-PS4-4, evaluate claims in published
  materials), and change "the evidence for the Big Bang" to "whether a published claim about radiation's effects
  holds up". In g12-sc-argue, change the fallback from phys-big-bang-evidence to
  `science:phys-wave-particle-light (if no grade 12 science course)`.
- **SI Narrate leans, grades 6 to 12.** The leans on e6-present-claims, e7-present-salient, e8-present-reasoning,
  e9-sl-presentation, e10-sl-presentation, e11-presentation and e12-presentation are labelled "(telling and
  describing aloud)", but those rows present claims and findings. Relabel them "(presenting in order to an
  audience)" and keep them: a recount for listeners who were not there is the nearest ELA row. The recount itself
  is ELD's own SI use.

### 8. Stale notes in the settled page (minor; firm)

LAYER process. REPEAT yes (stale notes in the science and social studies reads of 2026-11-13).

- **STANDARD.md, the owed table.** The row reads "Progression gate support | Owed: scripts/progression.py has no ELD
  entry yet". It has one (`'eld': ['wida-2020.txt']`, ELD_CLUSTER and ELD_SI, added 2026-11-21), and `check eld`
  passes. Rewrite it as "Done 2026-11-21: scripts/progression.py checks ELD with the cluster-to-grade map and the
  owner rule in section 2".
- **STANDARD.md section 2, Ownership, last sentence.** "The gate then needs ELD in scripts/progression.py: ..."
  should become "scripts/progression.py holds ELD: the standards file, the anchor, and a cluster-to-grade map beside
  the span map, with the owner rule above."
- **Not edited here.** STANDARD is a settled page and this read edits nothing; the caller applies both rewrites.

### 9. Pace in grades 4 and 5 is tight at 30 minutes (minor; judgment call)

LAYER progression. REPEAT new.

- **Counts.** Rows per grade are even: K 10, grade 1 11, grades 2 and 3 12, grades 4 to 12 13. Content rows,
  which each need a unit, are K 6, grade 1 7, grades 2 and 3 8, grades 4 to 12 9. The four SI rows ride inside
  them.
- **Days per content unit.** Over 160 days that is about 27, 23, 20, 20 and 18 days.
- **Grades 4 and 5.** Eighteen days of 30 minutes is about 9 hours. In that time a unit must take a model apart,
  build one together, have students write alone, change the audience, check, and respond. That is tight, and
  newcomer days are already outside the frame. Grades 6 to 12 at 45 minutes (about 13.5 hours) fit.
- **Fix (settled below).** The grade 4 and 5 frames may run two rows on one host unit where the hosts share a core
  unit (MA Explain with MA Argue, or SC Explain with SC Argue). Add to g4-ma-explain and g4-sc-explain: "A frame may
  pair this row with the Argue row of the same standard on one host unit."
- **Grade 12 math hosts.** These assume Statistics, but the math progression also offers Calculus and Precalculus.
  "If no grade 12 math course" leaves a calculus student without a host. This goes to Cory (below).

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Entry points written as one shared task plus per-level support and withdrawal (finding 1 pattern) | Bar item 2 and "Fails if" | data/progressions/eld.csv, notes of all 162 rows |
| g3-ss-explain 3 and 4 clause: "say what one level of government does and why, with 'so' and 'because'" | Copied text did not fit the host | data/progressions/eld.csv |
| "Forms:" sentence in notes (no new column), on the ladder in finding 2 | Keeps the schema and the gate; makes item 13 checkable | data/progressions/eld.csv |
| Sentence frame and word bank removed from model_in and model_out; withdrawal default: 5 and 6 after the first application day, 3 and 4 before the end-of-unit writing task, 1 and 2 keep the word bank | Scaffolds are not models; C7 and California 4.1 | data/progressions/eld.csv |
| Model stages per band as in finding 4, in owner-year notes; k-si-inform model_in emptied | Models grow, and the names stay for the gate | data/progressions/eld.csv |
| Word replacements in finding 5; each row adds two to four words its own task needs | Words fit the task and the grade | data/progressions/eld.csv |
| Sensitivity notes and replacements in finding 6 (k-ss-inform, g4-ss-argue, g2-ss-argue, g11 and g12 SI rows, g12-la-narrate, g9 SI register note, g1-sc-inform); SS conditional line named per host or dropped | APPROACH "Sensitive ground"; disaster read as loss | data/progressions/eld.csv |
| One home-language line per owner-year row | Bar item 6 anchored at the progression | data/progressions/eld.csv |
| g4-sc-argue host to science:s4-information-codes; g11-sc-argue host to science:phys-em-radiation-effects; g12-sc-argue fallback to phys-wave-particle-light | The hosts must ask for Argue | data/progressions/eld.csv |
| SI Narrate grade 6 to 12 presentation leans relabelled "(presenting in order to an audience)" | The label misdescribed the host | data/progressions/eld.csv |
| Grade 4 and 5 frames may pair a standard's Explain and Argue rows on one host unit | 18 days of 30 minutes is tight | data/progressions/eld.csv (g4-ma-explain, g4-sc-explain notes) |
| STANDARD owed-table row and section 2 gate sentence rewritten as done | Stale | docs/courses/eld/STANDARD.md |

## For Cory

{"q": "In the English language development progression, the grade 12 math rows (g12-ma-explain, g12-ma-argue) use the Statistics course as the host, with an Algebra II row as the fallback 'if no grade 12 math course'. The math progression also has grade 12 Calculus and Precalculus, so a grade 12 English learner in Calculus or Precalculus has no host from their own class. Should those students get their own host rows, which adds Calculus and Precalculus content to what grade 12 ELD draws on, or fall back to the Algebra II rows they took a year earlier?", "options": ["Name one Calculus and one Precalculus host per grade 12 math row, so every grade 12 student's ELD uses their own math class", "Keep Statistics as the host and widen the fallback to any student not in Statistics (Algebra II rows)"], "pick": "Name one Calculus and one Precalculus host per grade 12 math row, so every grade 12 student's ELD uses their own math class"}

## Lens checklist (progression layer)

| Line (docs/agents/lenses/eld.md, "Errors reviewers catch", course frame and scope and sequence) | Mark |
|---|---|
| Units built on word lists or grammar drills with no content | Met: every row has a host. The opposite risk (content with no form) is finding 2 |
| One level for all, or levels that change the content rather than the help | Missed: levels change the task (finding 1) |
| A WIDA id the file does not hold | Met (gate: all 104 ids, no extras) |
| No entry and exit points, or a course that stands in for ELA | Entry points missed (finding 1); exit is the school's (bar, Unsupported); LA rows lean toward restating ELA (finding 2) |
| ELA pairing missing for an LA unit, or host core unit missing for MA, SC, SS | Met: every LA row names ELA rows and every content row names hosts; three hosts do not fit (finding 7) |
| Talk planned with frames | Met at the progression: every row names a partner or group exchange |
| Home language as a resource | Missed at the progression: no row names it (finding 6, last item) |
| Newcomers, long-term English learners, English learners with disabilities | Not applicable at this layer (unit notes); the newcomer strand sits outside the file, as edges.md says |
| Language need or learning need | Not applicable at this layer (teacher page) |

## What is right and should not be touched

- **Ownership and coverage.** Ownership by cluster's last grade, SI 4-12 owned in grade 4, and full coverage of the
  104 ids (settled, STANDARD section 2).
- **First appearances.** The first-appearance `assumes` (g1-ss-argue, g2-ma-explain, g2-ma-argue, g2-sc-argue,
  g2-ss-explain, g4-la-argue) follow APPROACH unit field 3 exactly, with a reason in each note.
- **Task sentences.** Every `~` row's task sentence is its own and harder than the year before. Examples: SI
  Narrate moves from a class event (K) to an absent classmate (grade 4), a newsletter (grade 8), a peer then an
  adult (grade 9) and an interview then an email (grade 12). LA Argue moves from finding reasons (grade 4) to
  judging sufficiency (grade 7). Keep these.
- **SI tasks.** SI rows are about classroom life, not the student's private life, which is the right default for
  this population.
- **The Narrate note.** The Narrate teacher note ("one of several prompts; an invented character or a chosen place
  is always allowed") is on every Narrate row.
- **Grade 12 fallbacks.** The fallbacks for science, and for math within its limit, are a good pattern.

## What it could not judge

- Whether each host row's own wording meets the language demand beyond the opening of its notes: 248 hosts were
  checked for grade and for the general ask, not read in full.
- The WIDA Language Expectations' own wording (all rights reserved, not in the repository), so the rows cannot be
  checked against the expectation behind each id, only against its standard, cluster, key language use and mode.
- Whether the host units the SS rows name are sensitive in their actual texts: that waits for the SS unit plans and
  their sensitivity reads.

## Sources

- docs/RUBRIC-ELD.md (WIDA PRIME 2020, read in full by its writer, 2026-11-16): Depth.PLD (b), same thinking demand
  at every level; Depth.LE, forms as features doing a function; Breadth.KLU and Breadth.LE, growth across the year.
- docs/courses/eld/STANDARD.md section 4 (California criteria map, Program Type 5, read in full 2026-11-16): 4.1
  scaffolds withdrawn; 5.27 why a skill is hard.
- docs/courses/eld/APPROACH.md, "Sensitive ground": the rule behind finding 6.
- From memory, no page cited: functional-grammar practice for English learners (the form ladder in finding 2);
  English Learner Success Forum guidance on scaffolds that are withdrawn; National Academies 2017 on content-based
  language teaching. Each is a starting point, and the ladder is marked settled by the expert, not sourced.

## For the source list

None new.

## Fix pass (2026-11-21)

Applied to data/progressions/eld.csv (162 rows, rewritten through the csv module, CRLF kept) and two sentences of
docs/courses/eld/STANDARD.md. The progression check gives 0 failures. data/progressions/eld-edges.md needed no change,
because the new grade 12 hosts sit in the rows' cross_subject column.

- **1. Entry points.** All 162 rows now name one shared task, with help for levels 1 and 2, 3 and 4, and 5 and 6,
  and what is withdrawn and when (the default settled above). Each was written per row and year; no two are word for
  word the same. The g3-ss-explain copy error is fixed.
- **2. Forms.** Every row (162) has a "Forms:" sentence on the ladder above, growing by cluster. All 35 LA rows now
  take apart one paragraph or passage of the ELA text and name the language; the full ELA task stays in ELA.
- **3 and 4. Models.** Sentence frame and word bank are gone from model_in and model_out on every row. model_out
  differs from model_in on 11 rows where a tool is faded or grows into its next stage (the four K SI rows,
  g1-ss-argue, g2-ma-explain, g2-ma-argue, g2-sc-explain, g2-sc-argue, g2-ss-explain, g4-la-argue). "Model:" lines
  name the band's stage on owner-year rows and on the SI rows where a band starts. The models rule in the check passes.
- **5. Words.** Each row's words fit its task, using the replacements above; all 162 lists differ and none keeps
  more than half of the year before.
- **6. Sensitivity.** The general migration, war or loss line was taken off all SS rows; a named note now sits only
  on the sensitive hosts (g4, g5, g7, g9, g10 and g11 SS Explain, g11 SS Argue), plus g12-ss-argue (immigration
  policy is never put to a class vote), which this read did not list. The invented applicant is allowed on six
  grade 11 and 12 SI rows, the register note is on seven grade 9 and 11 SI rows, and g12-la-narrate lets the student
  choose the topic, real or invented. Every row (162) has a home-language line, and none asks a student to translate
  or to act as the class expert. The teacher notes for k-ss-inform, g1-sc-inform, g2-ss-argue and g4-ss-argue use
  the wording above.
- **7. Hosts.** g4-sc-argue now uses science:s4-information-codes; g11-sc-argue uses science:phys-em-radiation-effects;
  the g12-sc-argue fallback is science:phys-wave-particle-light. Tasks are updated to match.
- **8. STANDARD.** The owed-table row and the section 2 Ownership sentence now say the check supports ELD since
  2026-11-21 and the progression passes it. Nothing else on that page changed.
- **9. Pace.** The grade 4 and 5 MA, SC and SS Explain rows (6 rows) say a frame may pair them with the same
  grade's Argue row on one host unit.
- **For Cory, settled by the lead (2026-11-21), the reader's pick.** g12-ma-explain adds math:calc-related-rates
  and math:pc-trig-equations, and g12-ma-argue adds math:calc-mean-value-extrema and math:pc-exp-log-models, beside
  Statistics; the Algebra II fallback stays for a student in no grade 12 math course.

# English language development pre-work: second-model cold read, 2026-11-20

> Filed by the lead 2026-11-20. Gemini 4 Neon (medium effort) in Antigravity, pasted by Cory from S:/CurioClass-gemini/ (prompt 10 to 18 for this subject), after it passed calibration (docs/reviews/calibration-*-gemini-2026-11-20.md). Its saved report is S:/CurioClass-gemini/reports/prework-eld-read.md; text unchanged here except wording the repository checks flag.

Read as the curriculum expert (docs/agents/EXPERT.md) with the English language development (ELD) lens
(docs/agents/lenses/eld.md), as a stage 1 pre-work check (docs/COURSE-RUN.md, stage 1). I did not write these drafts.
Nothing in S:\CurioClass was edited; this report is saved to S:\CurioClass-gemini\reports\prework-eld-read.md.
Confidence is Firm, Likely or Judgment call on each finding. Anything resting on memory is marked "from memory".
The earlier first-model read (docs/reviews/prework-eld-read-2026-11-20.md) was not opened until all findings below were
written; the comparison sits in "Against the first read".

## What I read

AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/eld.md; docs/FOUNDATION.md; docs/APPROACH.md;
docs/PRODUCTION-PATH.md (lines 100 to 160, layer 4 rule); docs/COURSE-RUN.md (stage 1); docs/agents/decisions/BASELINE.md
(rules 20 to 30); docs/courses/UNIT-PLAN.md (full); docs/ADOPTION-BAR-SUBJECTS.md (pass rule, C1 to C16, part 10 items
1 to 14, fails-if, unsupported, standards, the ELD row of "Before a scope and sequence in this subject", and the sources
table); docs/RUBRIC-ELD.md; docs/courses/eld/STANDARD.md and docs/courses/eld/APPROACH.md; data/standards/wida-2020.txt
(all 104 ids); docs/reviews/eld-open-material-2026-11-16.md; docs/courses/health/APPROACH.md and
docs/courses/sel/APPROACH.md (finished examples, for comparison); docs/reviews/prework-sel-read-2026-11-19.md (report
shape); docs/pipeline/briefs/sensitivity-read.md; data/courses.csv (ELD rows, lines 46 to 49); data/subjects.csv (ELD
row, line 12); docs/COURSES-STATUS.md (summary and ELD rows, lines 203 to 206); scripts/progression.py (lines 45 to 130,
STD_FILES, ANCHOR, SPAN, code_grades); scripts/standards.py (lines 80 to 142); targeted slices of
data/progressions/ela.csv (kindergarten, grade 1, grade 5, grade 6, grade 9, grade 10) to verify the ELA lean ids
without dumping the whole file. Opened only after all findings were written: docs/reviews/prework-eld-read-2026-11-20.md.

Outside sources checked via web search (2026-11-20):
- WIDA English Language Development Standards Framework, 2020 Edition, official reference code grammar, grade-level
  clusters, and representative Language Expectation codes across SI, LA, MA, SC and SS at
  https://wida.wisc.edu/sites/default/files/resource/WIDA-ELD-Standards-Framework-2020.pdf (via search results; the local
  PDF was not opened directly).
- WIDA copyright and reuse policy at https://wida.wisc.edu/policies (via search results).
- California Department of Education, Designated ELD instructional time guidance (Title 5 CCR section 11300(a) and CDE
  FAQ) at https://www.cde.ca.gov/sp/ml/isfaqs.asp (via search results).
- Arizona Department of Education, Structured English Immersion (SEI) models and A.R.S. section 15-756.01 (120 minutes
  K to 5, 100 minutes 6 to 12) at https://www.azed.gov/oelas/sei-models (via search results).
- Rhode Island Department of Education (RIDE), Regulations Governing the Education of Multilingual Learners (45 minute
  instructional period floor, 1 to 3 periods by level) at https://ride.ri.gov/instruction-assessment/multilingual-learners
  (via search results).
- Montana Office of Public Instruction (OPI), English Learner Guidance for School Districts (local district flexibility,
  no statewide 45 to 135 minute mandate) at https://opi.mt.gov/Educators/Teaching-Learning/English-Learners (via search
  results).

## Verdict

The standard id file is sound: all 104 WIDA 2020 reference codes are unique, follow the framework's published code
grammar, match every stated count, and keep Curio Class strictly in our own words. The biggest risk is that three
post-read edits in STANDARD.md and APPROACH.md leave a progression or unit writer with contradictory or gate-failing
rules: an internal contradiction between 104 owned rows and two mode ids per row (which yields 56 owned rows), a
handoff rule ("one cluster earlier") that skips grades inside multi-grade clusters and breaks on six first-appearance
key language uses, and a section-plan field block that puts student language goals into Section field 2 ("Where it
sits") while dropping reading load, check accommodations and same-standard extension from Section field 9. The one
change that matters most is fixing the ownership, handoff and section-plan field rules together (findings 1, 2 and 3)
before ELD's progression gate is coded or any progression row is written.

## What I counted (so nobody has to again)

| Check | Result |
|---|---|
| Ids in data/standards/wida-2020.txt | 104 data lines (lines 11 to 114), 0 duplicates |
| By standard | SI 8 (K-3 x 4, 4-12 x 4, no mode suffix); LA 30 (15 pairs); MA 20 (10 pairs); SC 24 (12 pairs); SS 22 (11 pairs); total 8 + 96 = 104 |
| By cluster (non-SI) | K 12, 1 14, 2-3 16, 4-5 18, 6-8 18, 9-12 18 |
| Prominent KLUs with no earlier-cluster predecessor in same standard | 6 non-K pairs: ELD-SS.1.Argue, ELD-MA.2-3.Explain, ELD-MA.2-3.Argue, ELD-SC.2-3.Argue, ELD-SS.2-3.Explain, ELD-LA.4-5.Argue (plus all K ids) |
| Clusters containing `Inform` in non-SI standards | K and 1: LA, MA, SC, SS. Clusters 2-3, 4-5, 6-8, 9-12: ELD-LA only (MA, SC and SS have Explain and Argue only) |
| Counts stated across docs | 104 codes, 5 standards, 4 key language uses, 6 content clusters + 2 SI spans agree across wida-2020.txt, STANDARD.md and APPROACH.md |
| Validator (scripts/standards.py) | Loads wida-2020.txt into LISTED (lines 97, 104, 137 to 138); all 104 full ids validate; coarse codes WIDA.ELD-1 to 5 and WIDA.Narrate/Inform/Explain/Argue validate via CLOSED (line 116) |
| Progression gate (scripts/progression.py) | No `eld` entry in STD_FILES, ANCHOR or code_grades |
| Catalogue (data/courses.csv) | 4 band rows already live (lines 46 to 49): `eld-k-2`, `eld-3-5`, `eld-6-8`, `eld-9-12` ("one frame per grade year (Cory, 2026-11-21)") |
| ELA lean ids spot-checked in data/progressions/ela.csv | Core writing and discussion families exist (`ek-narrate`, `e1-narrative`..`e5-narrative`, `e6-narrative-writing`..`e8-narrative-writing`, `e9-w-narrative`..; same for informative, opinion/argument, discussion/seminar); `ELD-LA Argue (from 4-5)` mistakenly cites K to 3 opinion rows (`ek-opinion` to `e3-opinion`) |
| Dose as stated | "about 30 minutes in K to 5 and 45 minutes in 6 to 12, 160 days" (about 80 and 120 hours a year) |

## Findings, most serious first

### 1. Ownership rule contradicts itself on row count (104 vs 56 owned rows), mislabels SI K-3 as an exception, and scripts/progression.py still lacks ELD support

- **Where:** docs/courses/eld/STANDARD.md section 2, "Ownership" (lines 70 to 78); scripts/progression.py (`STD_FILES`, `ANCHOR`, `code_grades`, lines 51 to 130).
- **What is wrong:** Line 70 states "The ELD progression has one owned row per id in data/standards/wida-2020.txt, 104 in all", while lines 75 to 76 state "A row names the Interpretive id and the Expressive id as two ids, so the gate counts both." Pairing Interpretive and Expressive on one row produces 48 content-area owned rows plus 8 SI owned rows = 56 owned rows (covering all 104 ids), not 104 owned rows. Second, line 74 calls both social and instructional ranges "the exception", but SI K-3 owned by grade 3 with `~` in K to 2 follows the general last-grade rule; only SI 4-12 (owned by grade 4, carried as `~` in grades 5 to 12) is an exception. Third, scripts/progression.py still has no `eld` entry in `STD_FILES`, `ANCHOR` or `code_grades`, so the progression gate cannot run on ELD.
- **Cost:** Two progression writers will produce incompatible CSVs (56 owned rows vs 104 owned rows), and the progression gate cannot check ELD until `scripts/progression.py` is updated.
- **Fix (replace the "Ownership" bullet in docs/courses/eld/STANDARD.md section 2, lines 70 to 78, with this text; ours, untested):**

> - **Ownership** (settled by the expert reader, 2026-11-20, revised; ours, untested). The ELD progression covers all
>   104 ids in data/standards/wida-2020.txt across 56 owned rows: 8 SI rows (one id each) and 48 content-area rows
>   (each naming the Interpretive id and the Expressive id of the same standard, cluster and key language use as two
>   semicolon-separated ids in the standard column, so the gate counts all 104 ids). No id is excluded. A cluster's
>   owner year is its last grade: K for K, 1 for 1, 3 for 2-3, 5 for 4-5, 8 for 6-8, 12 for 9-12, and 3 for SI K-3.
>   The other grades of the cluster carry the row's ids as `~ID`, each with a one-line note on how that year differs
>   (a harder text or task, or the next key language use added). SI 4-12 is the one exception to the last-grade rule,
>   because upper-elementary students need that social and instructional language as soon as they enter grade 4: SI
>   4-12 is owned by grade 4 and carried as `~` in grades 5 to 12. The gate needs `eld` added to scripts/progression.py:
>   `'eld': ['wida-2020.txt']` in `STD_FILES`, `'eld': 'wida-2020.txt'` in `ANCHOR`, and a `code_grades` branch mapping
>   clusters `K` (`['K']`, `['K']`), `1` (`['1']`, `['1']`), `2-3` (`['3']`, `['2', '3']`), `4-5` (`['5']`, `['4', '5']`),
>   `6-8` (`['8']`, `['6', '7', '8']`), `9-12` (`['12']`, `['9', '10', '11', '12']`), `K-3` (`['3']`, `['K', '1', '2', '3']`),
>   and `4-12` (`['4']`, `['4', '5', '6', '7', '8', '9', '10', '11', '12']`).

- **Confidence:** Firm.

### 2. Unit field 3 handoff rule ("one cluster earlier") skips grades inside multi-grade clusters and breaks for six first-appearance key language uses

- **Where:** docs/courses/eld/APPROACH.md, Unit field 3 (line 47); data/standards/wida-2020.txt.
- **What is wrong:** APPROACH.md Unit field 3 says `builds on (the same key language use one cluster earlier, handoff strong or weak)`. That fails in two ways. First, ELD has 13 grade-year frames (one per grade, K to 12). Inside multi-grade clusters (`2-3`, `4-5`, `6-8`, `9-12`), grade 3 builds on grade 2 (not grade 1), grade 5 builds on grade 4 (not grade 3), grades 7 and 8 build on grades 6 and 7, and grades 10 to 12 build on grades 9 to 11. Pointing "one cluster earlier" skips intermediate grades, which fails the continuity rule. Second, six content-area cluster-by-KLU pairs appear for the first time in their cluster with no earlier same-standard, same-KLU code: `ELD-SS.1.Argue` (SS K has Inform only), `ELD-MA.2-3.Explain` and `ELD-MA.2-3.Argue` (MA 1 has Inform only), `ELD-SC.2-3.Argue` (SC 1 has Inform and Explain only), `ELD-SS.2-3.Explain` (SS 1 has Inform and Argue only), and `ELD-LA.4-5.Argue` (LA 2-3 has Narrate and Inform only). In addition, Kindergarten has no earlier grade or cluster.
- **Cost:** Progression and unit writers will either skip grades in `assumes`/`hands_on` handoffs (tripping the progression gate's skipped-grade check) or reference nonexistent predecessor codes for newly introduced KLUs.
- **Fix (replace Unit field 3 in docs/courses/eld/APPROACH.md, lines 47 to 50, with this text; ours, untested):**

> - Unit field 3 (where it sits): builds on (the prior grade's row for the same standard and key language use, handoff
>   strong or weak; where a key language use first appears in a content standard, namely `ELD-SS.1.Argue`,
>   `ELD-MA.2-3.Explain`, `ELD-MA.2-3.Argue`, `ELD-SC.2-3.Argue`, `ELD-SS.2-3.Explain` and `ELD-LA.4-5.Argue`, it builds
>   on the prior grade's `ELD-SI` row for that key language use plus the prior grade's `Inform` or `Explain` row in the
>   same content standard; Kindergarten unit 1 assumes nothing); leads to (the next grade's row); comes back in; the host
>   core unit and, for LA, the ELA rows it pairs with (STANDARD section 5); and the two-line note the ELD teacher can
>   share with the host teacher: the content used and the language taught (bar item 14).

- **Confidence:** Firm.

### 3. APPROACH.md misplaces the student language goal in Section field 2 and drops three required C10/UNIT-PLAN slots from Section field 9 (plus minor omissions in Unit fields 2 and 5 and Section fields 1, 3 and 5)

- **Where:** docs/courses/eld/APPROACH.md (lines 45 to 85); docs/courses/eld/STANDARD.md section 4 (line 113); docs/courses/UNIT-PLAN.md (unit fields 1 to 10, section fields 1 to 11); docs/ADOPTION-BAR-SUBJECTS.md (C8, C10, C14, C15, part 10 item 11).
- **What is wrong:** Checking every field against UNIT-PLAN.md:
  - **Section field 2 (placement fault):** UNIT-PLAN.md defines Section field 2 as "Where it sits" (what comes just before and just after, the readiness items it uses, and where its own results go). APPROACH.md puts "the language goal, stated for students" into Section field 2 and drops "where its own results go"; STANDARD.md line 113 also sends California 5.7 ("Language goals stated for each lesson, with a progression") to Section field 2. Per UNIT-PLAN.md, the section's share of the standard sits in **Section field 1** ("Standards and practices"), and each day's goal in student words sits in **Section field 6** ("Days: Goal, in student words").
  - **Section field 9 (three C10 slots dropped):** UNIT-PLAN.md Section field 9 requires English learners, Access (disabilities), **Check accommodations**, **Reading load**, and **Extension on the same standard**. APPROACH.md Section field 9 names entry points, newcomers, long-term English learners, English learners with disabilities and home language helps, but drops reading load (C10 explicitly fails an empty reading load field), check accommodations (also missing from Unit field 5), and extension on the same standard (C10 explicitly fails a course with no extension on the same standard). Compare docs/courses/health/APPROACH.md (lines 111 to 114) and docs/courses/sel/APPROACH.md (lines 88 to 95), both of which fill all three.
  - **Unit field 5 (interpretive mode omitted):** Unit field 5 names "a talk task and a writing task at each entry point" (both expressive), with no interpretive check (listening, reading or viewing), even though bar part 10 item 11 requires both interpretive and expressive modes in every unit and every non-SI standard has an Interpretive id.
  - **Smaller slot omissions:** Unit field 2 omits limits and the day carried frames are withdrawn (UNIT-PLAN field 2); Section field 1 omits the section's share of the unit's standard ids and limits; Section field 3 omits the unit assessment item numbers this section owns; Section field 5 omits the ideal instrument verdict and what a room with nothing does (paper path, C14/C15).
- **Cost:** Every ELD section plan written from APPROACH.md will place daily student goals under the wrong field number and fail C10 (reading load and extension) and C8/bar item 11 (interpretive check and check accommodations).
- **Fix (replace these bullets in docs/courses/eld/APPROACH.md, and update docs/courses/eld/STANDARD.md line 113; ours, untested):**

> - Unit field 2: the ELD standard ids the unit plans to (our own words for each, both modes named); the key language
>   use; the forms and words taught; limits (what is out of scope for this cluster and unit); what is carried (frames,
>   word cards) and the day the frame is withdrawn.
> - Unit field 5 (end-of-unit assessment): an interpretive prompt on a new grade-level text or task of the same kind,
>   followed by a talk task and a writing task at each entry point, with look-fors and two sample answers per level
>   (meets / does not). Names check accommodations (read aloud, large print, a scribe, an oral answer, extra time) and
>   says how a student moves to the next entry point.
> - Section field 1: the section's share of the unit's ELD standard ids (our own words) and limits; before you teach:
>   the form explained for the teacher, a note on how Spanish does the same thing (other home languages: see "Home
>   languages" below), a line on telling a language need apart from a learning disability, any sensitive ground the
>   section touches, and the school's reporting route if a student discloses harm.
> - Section field 2 (where it sits): what comes just before and just after in the unit; the readiness items it uses;
>   and where its own results go.
> - Section field 3: the numbers of the unit assessment items this section owns; the day's evidence as above, with
>   look-fors per level.
> - Section field 5 (what is carried, and instruments): the model sentence or passage, who holds it each day, and the
>   day the frame is withdrawn; any key-moment tool with its ideal-instrument verdict and link to TOOL-ASKS.md; and what
>   a room with nothing does (paper path).
> - Section field 6 (days): one row a day with the day's language goal in student words, kind of day, how it opens, the
>   content read or done, who holds what is carried, tool by part (or "None"), work by hand, and the day's evidence.
> - Section field 9 (supports and extension): the three entry points; newcomer notes; long-term English learner notes;
>   notes for English learners with disabilities (access: no student must speak aloud or be watched rehearsing; oral,
>   written, card or teacher options); home language helps; reading load (how much a student reads alone and what is read
>   aloud or supported with audio/visuals); check accommodations (read aloud, large print, scribe, oral answer, extra
>   time); and extension on the same standard (a harder text, an added audience shift or a deeper form analysis on the
>   same language goal, never the next grade's standard).

  In docs/courses/eld/STANDARD.md line 113, change `Section field 2` to `Section field 1 (section goal) and Section field 6 (daily goal in student words)`.
- **Confidence:** Firm.

### 4. Pacing cites an inaccurate Montana time figure ("45 to 135 minutes by level") and leaves K to 5 minutes as "about 30"

- **Where:** docs/courses/eld/APPROACH.md, "Pacing" (lines 122 to 130); docs/courses/eld/STANDARD.md section 2 (line 59).
- **What is wrong:** Web search against official state department pages confirms three of the four statements in "Pacing" and contradicts the fourth:
  - Federal guidance: no fixed minute mandate (from memory, consistent with Title VI / OCR guidance requiring sufficient time to overcome language barriers).
  - California: confirmed, no statewide minimum minute count (CDE FAQ / Title 5 CCR section 11300(a), https://www.cde.ca.gov/sp/ml/isfaqs.asp).
  - Arizona: confirmed, 120 minutes a day in K to 5 and 100 minutes a day in 6 to 12 under A.R.S. section 15-756.01 (https://www.azed.gov/oelas/sei-models).
  - Rhode Island: confirmed, a 45 minute instructional period as a floor, with 1 to 3 periods (45 to 135 minutes) by proficiency level under RIDE regulations (https://ride.ri.gov/instruction-assessment/multilingual-learners).
  - **Montana:** contradicted. Montana Office of Public Instruction (https://opi.mt.gov/Educators/Teaching-Learning/English-Learners) does NOT set a statewide 45 to 135 minute mandate; districts set service minutes locally based on student need. The "45 to 135 minutes" figure matches Rhode Island's 1 to 3 period structure, not Montana.
  Second, "about 30 minutes in K to 5" uses a hedged word ("about") where C2 asks for a stated period length per lesson so day-count and assessment-minutes gates can compute cleanly (compare docs/reviews/prework-sel-read-2026-11-19.md, finding 14).
- **Cost:** Publishing an unverified and inaccurate state mandate violates C3 (facts and figures accurate with sources), and "about 30" leaves period length ambiguous for gates.
- **Fix (replace the "Pacing" paragraph in docs/courses/eld/APPROACH.md, lines 122 to 130, with this text):**

> Settled 2026-11-16 (Cory, Desk card q-later-sel-eld): a protected period of 30 minutes in K to 5 and 45 minutes in 6
> to 12, 160 days (80 and 120 hours a year). No national body sets a figure for ELD time (federal guidance sets none,
> from memory). California sets no statewide minimum (California Department of Education, Instructional Services FAQ,
> Title 5 CCR section 11300(a), checked 2026-11-20), and Montana leaves service minutes to local districts (Montana OPI
> English Learner Guidance, checked 2026-11-20). States that publish a daily floor set it higher: Arizona requires 120
> minutes a day in K to 5 and 100 minutes in 6 to 12 (A.R.S. section 15-756.01, Arizona Department of Education SEI
> models, checked 2026-11-20), and Rhode Island sets a 45 minute period as a floor, scaling from 1 to 3 periods (45 to
> 135 minutes) by proficiency level (RIDE Multilingual Learner regulations, checked 2026-11-20). So the course page
> says Curio Class's period is the protected core of a student's English language development and not a replacement for
> the school's own program or for more time where a state or district asks for it. Each band frame may change the
> minutes with a reason. Cory kept these minutes (2026-11-21).

  In docs/courses/eld/STANDARD.md line 59, change `about 30 minutes in K to 5 and a 45 minute period in 6 to 12` to `30 minutes in K to 5 and 45 minutes in 6 to 12`.
- **Confidence:** Firm.

### 5. Sensitive-ground rules are not carried into the unit and section plan fields that touch them, and there is no leave-out/swap rule or at-home hotline pointer

- **Where:** docs/courses/eld/APPROACH.md, "Sensitive ground" (lines 98 to 111), Unit field 5 (lines 53 to 54), Unit field 9 (lines 62 to 63), Section field 1 (lines 66 to 68), Section field 7 (line 77).
- **What is wrong:** The "Sensitive ground" section itself is well written, but four places that touch sensitive ground do not carry its rules:
  1. **Section field 1** names "any sensitive ground the section touches" but omits the school's reporting route if a student discloses harm (compare docs/courses/sel/APPROACH.md line 73).
  2. **Unit field 9 (family note)** omits a preview and opt-out/alternative-text note when a host unit's text touches migration, war or loss, even though "Sensitive ground" requires a sensitivity read of family notes and those host texts.
  3. **Unit field 5 and Section field 7** omit the rule that any talk or writing prompt about family, home or "where you are from" must offer an invented-character or chosen-place option and never ask about immigration status or home language use.
  4. **No leave-out or swap rule and no at-home hotline:** Neither STANDARD.md nor APPROACH.md says how a school or parent opts out of a sensitive host text (such as migration, war or loss) without breaking the unit's language goal, and the at-home disclosure line ("at home, a child's disclosure is not handled alone") omits the national child abuse hotline by purpose (which docs/courses/health/APPROACH.md lines 105 to 106 include).
- **Cost:** Writers filling unit plans, section plans and family notes will miss the reporting route, opt-out preview or invented-character option on sensitive host texts.
- **Fix (add to docs/courses/eld/APPROACH.md; ours, untested):**
  - In **Unit field 5** and **Section field 7**, add: `Any prompt about family, home or "where you are from" offers an invented character or a place the student chooses, and never asks about immigration status, how a family came, or whether the family speaks English at home.`
  - In **Unit field 9 (family note)**, add: `When a host text touches migration, war or loss, the family note previews the topic and states how a family may opt out for the alternative text (in a school through the school; at home the parent decides).`
  - In **Section field 1**, include the reporting route (already included in the pasteable fix for finding 3 above).
  - In **"Sensitive ground"**, replace the last sentence of the first paragraph (lines 106 to 107) with: `If a student tells you something about their home, listen, do not promise secrecy, follow the school's duty to report, and tell the student who the next adult is; for a parent teaching at home, the teacher page names the national child abuse hotline by purpose and says a child's disclosure is not handled alone. Where a host text touches migration, war or loss, the unit names a neutral alternative text on the same language goal so a student or family may opt out without losing the ELD standard.`
- **Confidence:** Firm.

### 6. STANDARD.md section 5 (ELA lean) points ELD-LA Argue (from 4-5) to K to 3 opinion rows that have no ELD-LA Argue standard, and drops hyphens on several ELA ids

- **Where:** docs/courses/eld/STANDARD.md section 5 (lines 131 to 135), checked against data/progressions/ela.csv.
- **What is wrong:** Line 133 pairs `ELD-LA Argue (from 4-5)` with `Opinion writing in K to 5 (ek-opinion to e5 opinion)`. In data/standards/wida-2020.txt, `ELD-LA` has no `Argue` expectation in K, 1 or 2-3; `ELD-LA.4-5.Argue` starts in grade 4, so its ELA opinion lean is grades 4 and 5 only (`e4-opinion` and `e5-opinion`), not `ek-opinion` to `e3-opinion`. In addition, several id strings omit hyphens or grade prefixes (`e5 opinion` vs `e5-opinion`, `e1 to e5 narrative` vs `e1-narrative` to `e5-narrative`, `e1 to e5 informative` vs `e1-informative` to `e5-informative`, `argument-writing` vs `e6-argument-writing` to `e8-argument-writing`, `e10 to e12 seminar` vs `e10-sl-seminar`, `e11-seminar`, `e12-seminar`).
- **Cost:** A writer or script checking cross-subject leans in K to 3 will either look for a nonexistent `ELD-LA.K.Argue` code or fail an exact-id lookup.
- **Fix (replace rows 1 to 4 of the table in docs/courses/eld/STANDARD.md section 5, lines 131 to 134, with this text):**

> | ELD-LA Narrate | Narrative writing (`ek-narrate`, `e1-narrative` to `e5-narrative`, `e6-narrative-writing` to `e8-narrative-writing`, `e9-w-narrative`, `e10-w-narrative`, `e11-narrative`, `e12-narrative`) and the reading-literature rows |
> | ELD-LA Inform | Informative writing (`ek-inform`, `e1-informative` to `e5-informative`, `e6-informative-writing` to `e8-informative-writing`, `e9-w-informative`, `e10-w-informative`, `e11-informative`, `e12-informative`) and the reading-informational rows |
> | ELD-LA Argue (from 4-5) | Opinion writing in grades 4 and 5 (`e4-opinion`, `e5-opinion`) and argument writing from grade 6 (`e6-argument-writing` to `e8-argument-writing`, `e9-w-argument`, `e10-w-argument`, `e11-argument`, `e12-argument`) |
> | ELD-SI (all four uses) | Speaking and listening: the discussion rows (`ek-discussion` to `e5-discussion`, `e6-collab-discussion` to `e8-collab-discussion`, `e9-sl-discussion`, `e10-sl-seminar`, `e11-seminar`, `e12-seminar`) and the presenting rows |

- **Confidence:** Firm.

### 7. Newcomer strand's "cluster's Inform only" exists only in ELD-LA from cluster 2-3 up, and its 20-day calendar slot is ambiguous

- **Where:** docs/courses/eld/STANDARD.md section 2, "Newcomer strand" (lines 79 to 81); data/standards/wida-2020.txt.
- **What is wrong:** Line 79 says the newcomer strand is "the first 20 days of each band, on the SI ids and the cluster's Inform only." Two problems: first, in clusters `2-3`, `4-5`, `6-8` and `9-12`, `ELD-MA`, `ELD-SC` and `ELD-SS` have NO `Inform` code in wida-2020.txt (only `ELD-LA.<cluster>.Inform` and `ELD-SI.<range>.Inform` exist; `MA`, `SC` and `SS` have `Inform` only in K and 1). Saying "the cluster's Inform only" without naming `ELD-LA` invites a 3-5, 6-8 or 9-12 writer to look for nonexistent math, science or social studies Inform codes. Second, "the first 20 days of each band" does not say whether the 20 days replace unit 1 inside a 160-day grade frame for newcomers or sit as a standalone 20-day on-ramp alongside the 160-day frame (so newcomers who enter mid-year or at day 1 know how they join unit 1).
- **Cost:** Frame writers in 3 to 5, 6 to 8 and 9 to 12 may mis-tag standards or miscount the 160-day calendar.
- **Fix (replace the "Newcomer strand" bullet in docs/courses/eld/STANDARD.md section 2, lines 79 to 81, with this text; calendar placement is Question for Cory 1):**

> - **Newcomer strand** (settled by the expert reader, ours, untested): a 20-day on-ramp per band (placed beside the
>   160-day grade frame, not cutting into its 160 days, so a newcomer arriving at any point in the year can take it
>   before joining the class's current unit). It runs on the band's `ELD-SI` ids and `ELD-LA.<cluster>.Inform` (plus
>   `ELD-MA`, `ELD-SC` and `ELD-SS` Inform in K and grade 1 only, where those codes exist). A student moves to entry
>   points 1 and 2 when the teacher judges the strand's look-fors "seen" on two days in a row, or on the school's own
>   check where there is one.

- **Confidence:** Likely.

### 8. Stale catalogue, approval, bar-sync, mode-wording and public-naming notes across ELD pre-work files

- **Where:** docs/courses/eld/STANDARD.md (lines 16, 51, 68 to 69, 97, 108); docs/ADOPTION-BAR-SUBJECTS.md (lines 487, 570); docs/RUBRIC-ELD.md (lines 3, 26); docs/courses/eld/APPROACH.md (lines 45, 87); docs/COURSES-STATUS.md (lines 203 to 206).
- **What is wrong:**
  1. **Catalogue already updated (stale text):** STANDARD.md line 51 still says `data/courses.csv has one ELD track row (eld-k12, "WIDA grade clusters")` and line 68 says `The catalogue (data/courses.csv) then replaces eld-k12 with four band rows...`. `data/courses.csv` lines 46 to 49 already hold `eld-k-2`, `eld-3-5`, `eld-6-8`, `eld-9-12`.
  2. **Approach approval already granted (stale text):** STANDARD.md line 16 says `Draft for Cory's yes` and ADOPTION-BAR-SUBJECTS.md line 570 says `Owed: the approach page's yes`, while APPROACH.md line 3 records `Approved by Cory 2026-11-21 (Desk q-prework-open-2)`. ADOPTION-BAR-SUBJECTS.md line 570 also omits the 2026-11-20 cold read and the still-owed `scripts/progression.py` gate support.
  3. **English learners with disabilities missing from bar item 5 and STANDARD section 3:** STANDARD.md section 4 (line 107) proposed adding "English learners with disabilities" to bar item 5, and APPROACH.md (lines 79 to 80) and the ELD lens (lines 27 to 28, 50) already include it, but ADOPTION-BAR-SUBJECTS.md part 10 item 5 (line 487) and STANDARD.md section 3 (line 97) still name only "newcomers and long-term English learners".
  4. **"All four modes" vs two modes / four domains:** STANDARD.md section 4 (line 108) writes `adopt "all four modes in every unit" as a check` (using "modes" for California's four language domains: listening, speaking, reading, writing, whereas WIDA 2020 defines two modes, interpretive and expressive), and APPROACH.md line 87 writes `talk and writing both in every unit` (both expressive, omitting listening/reading/viewing).
  5. **RUBRIC-ELD.md stale read status:** RUBRIC-ELD.md line 3 says "Not yet read by the curriculum expert" and line 26 says the 2020 Framework pages were not opened, while APPROACH.md line 140 says Appendix C was read in full on 2026-11-20.
  6. **"WIDA ids" in teacher-facing Unit field 2 (Judgment call):** APPROACH.md line 45 says `the WIDA ids the unit plans to`. Per STANDARD.md lines 34 to 35 and AGENTS.md line 25, teacher-facing unit plans should say `the ELD standard ids` (matching the SEL cold read's precedent on "CASEL").
  7. **COURSES-STATUS.md (generated):** lines 203 to 206 still list `shared page only` in the Approach column for all four ELD courses (and repeat "grades K to 2, grades K to 2" in the course name); needs `scripts/course_status.py` re-run once changes settle.
- **Cost:** Contradictory status and bar lines cause writers and reviewers to check against outdated rules or miss English learners with disabilities in a bar audit.
- **Fix:**
  - STANDARD.md line 16: change `Draft for Cory's yes` to `Approved by Cory 2026-11-21 (Desk q-prework-open-2)`.
  - STANDARD.md line 51: change to `data/courses.csv holds four ELD band rows (eld-k-2, eld-3-5, eld-6-8, eld-9-12), matching docs/COURSES-STATUS.md.` Drop the redundant future-tense sentence at lines 68 to 69.
  - STANDARD.md line 97: change to `Newcomers, long-term English learners and English learners with disabilities get named notes in every unit (bar item 5; California 1.23).`
  - STANDARD.md line 108: change `adopt "all four modes in every unit"` to `adopt "all four domains (listening, speaking, reading, writing) across both modes (interpretive and expressive) in every unit"`.
  - APPROACH.md line 87: change `talk and writing both in every unit` to `both modes (interpretive: listening, reading or viewing; expressive: talk and writing) in every unit`.
  - ADOPTION-BAR-SUBJECTS.md line 487: change `notes for newcomers and long-term English learners` to `notes for newcomers, long-term English learners and English learners with disabilities`. Update line 570 to note the 2026-11-20 read, the 2026-11-21 approach approval, and the owed `scripts/progression.py` ELD support.
  - RUBRIC-ELD.md line 26: note that Appendix C (all 104 ids) was read in full on 2026-11-20.
- **Confidence:** Firm on items 1 to 5 and 7; Judgment call on item 6.

## What is right and should not be touched

- **data/standards/wida-2020.txt:** all 104 ids are unique, follow the WIDA 2020 code grammar, keep SI mode-free and non-SI paired across Interpretive and Expressive, and hold ids only with a clear reuse header.
- **Language through grade-level content:** the core stance in STANDARD.md, APPROACH.md, the lens and bar part 10 (same task and thinking demand at all three entry points; scaffolds change, never the grade-level content; ELD is not remedial reading or repeated ELA).
- **The C11 gate and its test** (STANDARD.md section 6): building waits until C11 passes with no fail in the probe and guard units of at least two core subjects, one of them ELA.
- **The kinds-of-day table and daily evidence:** spoken or written sample of the day's form on the day's content against look-fors, paper "seen / not yet" sheet, student self-check kept by the student, no scores stored.
- **What a tool may and may not do** (APPROACH.md lines 113 to 118): clear guardrails against recording voice/writing, scoring accent/pronunciation, placement, family translation, or replacing partner talk.
- **Home-language reader gate** (APPROACH.md lines 91 to 96): Spanish first with a `spanish` read; other languages wait until a reader exists.
- **Base-text scout** (docs/reviews/eld-open-material-2026-11-16.md): honest "no whole-course open base" finding, EL Education Language Dive pairing for K to 5, and item-by-item licence/agency check for VOA Learning English.

## Not checked

- **WIDA 2020 Framework PDF (local copy):** not opened directly; code grammar and representative codes were verified via web search against `wida.wisc.edu`, and exact 104-code completeness against Appendix C rests on the file header and the 2026-11-20 read recorded in APPROACH.md.
- **Progression row coverage of each standard's parts:** `data/progressions/eld.csv` does not exist yet (waits on the C11 gate), so checking that every owner row teaches every part of each id it owns must wait for stage 2. Note also that `wida-2020.txt` holds ids only, with no own-words companion file yet (see Question for Cory 2).
- **California criteria map (91 pages), WIDA PRIME 2020 workbook (54 pages), National Academies 2017 report, ELSF guidelines, EL Education K to 5:** not re-opened.
- **Remaining ELA progression families** (reading-literature, reading-informational, presenting and language rows): named by strand/family rather than individual id in STANDARD.md section 5, so not checked id by id.
- **scripts/plan.py and scripts/unitplan.py:** not read.

## Against the first read

Opened docs/reviews/prework-eld-read-2026-11-20.md only after writing findings 1 to 8 above. Most of the first read's
ten findings (missing ownership rule, missing grain, missing APPROACH fields and wrong "two rooms" meaning, missing
"Sensitive ground" section, missing tool rule, stale validator note, missing sources section, bar items 13 and 14,
unbounded newcomer strand) were already fixed in STANDARD.md and APPROACH.md before this second-model read.

- **Already in the first read (still owed in code):** `scripts/progression.py` still lacks `eld` in `STD_FILES`,
  `ANCHOR` and `code_grades` (part of my finding 1; first read finding 1). Also, the first read flagged Arizona, Rhode
  Island and Montana as "per search summary, check before publishing" (first read finding 5).
- **New in this second-model read:**
  - **Finding 1 (row-count contradiction and SI K-3 label):** new; the first read's own fix text introduced the
    contradiction between "104 owned rows" and pairing Interpretive and Expressive on one row (56 owned rows), and
    mislabeled SI K-3 as an exception.
  - **Finding 2 (handoff rule "one cluster earlier"):** new; introduced by the first read's fix for Unit field 3, which
    skips intermediate grades in multi-grade clusters and fails for six first-appearance content KLUs plus Kindergarten.
  - **Finding 3 (Section field 2 placement fault, three dropped C10 slots in Section field 9, interpretive check missing
    from Unit field 5, and minor omissions in Unit 2 and Section 1/3/5):** new; the first read caught the missing fields
    and Section field 10, but missed the Section field 2 placement fault and called Section field 9 "Filled; the
    strongest part".
  - **Finding 4 (Montana verified as local-flexibility with no 45 to 135 minute mandate, plus "about 30"):** new
    verification resolving the first read's open check on the three states.
  - **Finding 5 (propagating sensitive-ground rules into Section field 1, Unit field 5, Section field 7, Unit field 9,
    plus leave-out/swap rule and at-home hotline):** new.
  - **Finding 6 (ELD-LA Argue 4-5 paired with K to 3 opinion rows and non-exact ELA id punctuation):** new.
  - **Finding 7 (newcomer strand's "cluster's Inform only" exists only in ELD-LA from 2-3 up, plus 20-day calendar
    placement):** new; introduced by the first read's finding 10 fix.
  - **Finding 8 (stale catalogue/approval notes, bar item 5 missing English learners with disabilities, "all four modes"
    vs two modes, RUBRIC-ELD staleness, "WIDA ids" in teacher-facing Unit field 2):** new.

## Sources

- WIDA English Language Development Standards Framework, 2020 Edition (via web search on `wida.wisc.edu`),
  https://wida.wisc.edu/sites/default/files/resource/WIDA-ELD-Standards-Framework-2020.pdf : checked code grammar,
  five standards, grade-level clusters and representative Language Expectation codes.
- WIDA Policies (via web search on `wida.wisc.edu`), https://wida.wisc.edu/policies : verified copyright and
  non-reproduction terms supporting Curio Class's ids-and-own-words rule.
- California Department of Education, Instructional Services FAQ (via web search on `cde.ca.gov`),
  https://www.cde.ca.gov/sp/ml/isfaqs.asp : verified California sets no statewide minimum daily minute count for
  designated ELD.
- Arizona Department of Education, SEI Models (via web search on `azed.gov`),
  https://www.azed.gov/oelas/sei-models : verified 120 minutes/day (K to 5) and 100 minutes/day (6 to 12) under A.R.S.
  section 15-756.01.
- Rhode Island Department of Education, Multilingual Learners (via web search on `ride.ri.gov`),
  https://ride.ri.gov/instruction-assessment/multilingual-learners : verified 45 minute period floor scaling 1 to 3
  periods (45 to 135 minutes) by proficiency level.
- Montana Office of Public Instruction, English Learners (via web search on `opi.mt.gov`),
  https://opi.mt.gov/Educators/Teaching-Learning/English-Learners : verified Montana uses local district flexibility
  with no rigid statewide 45 to 135 minute mandate.

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| ELD progression uses 56 owned rows (8 SI + 48 paired Interpretive/Expressive content rows), covering all 104 ids; only SI 4-12 breaks the last-grade owner rule | Resolves the 104-vs-56 row contradiction while keeping both modes together per unit and satisfying the gate | docs/courses/eld/STANDARD.md section 2 |
| Unit field 3 builds on the prior grade's row (with explicit SI + Inform/Explain bridge for the six first-appearance content KLUs and "assumes nothing" for K unit 1) | Stops grade skips inside multi-grade clusters and prevents broken predecessor references | docs/courses/eld/APPROACH.md Unit field 3 |
| Move student language goals out of Section field 2 into Section field 1 (section goal) and Section field 6 (daily goal in student words); restore reading load, check accommodations and same-standard extension in Section field 9; add interpretive prompt to Unit field 5 | Matches docs/courses/UNIT-PLAN.md field placement and C8/C10/bar item 11 | docs/courses/eld/APPROACH.md; docs/courses/eld/STANDARD.md section 4 |
| Drop the inaccurate Montana 45 to 135 minute figure; cite verified Arizona, Rhode Island, California and Montana rules; state fixed defaults (30 and 45 minutes) | Meets C2 (fixed period length) and C3 (accurate sourced figures) | docs/courses/eld/APPROACH.md "Pacing"; docs/courses/eld/STANDARD.md section 2 |
| Restrict `ELD-LA Argue (from 4-5)` ELA lean to `e4-opinion` and `e5-opinion` (not K to 3) and use exact hyphenated ELA ids | Matches `wida-2020.txt` and `data/progressions/ela.csv` | docs/courses/eld/STANDARD.md section 5 |
| Propagate sensitive-ground rules (reporting route, family-note preview/opt-out, invented-character option, neutral alternative host text, at-home hotline) into plan fields | Ensures writers carry sensitive-ground rules into every unit, section and family note | docs/courses/eld/APPROACH.md |
| Use "the ELD standard ids" in teacher-facing Unit field 2 | Keeps organization names out of teacher-facing copy (AGENTS.md; matches SEL precedent) | docs/courses/eld/APPROACH.md Unit field 2 |

## Questions for Cory

1. **Newcomer strand calendar placement (finding 7).** Should the 20-day newcomer strand sit as a standalone 20-day
   on-ramp beside each 160-day grade frame (so a newcomer arriving at any point in the year can take it before joining
   the class's current unit, and the grade frame keeps all 160 days), or replace the first 20 days of unit 1 inside the
   160-day frame? **Recommended:** standalone 20-day on-ramp beside the 160-day frame.
2. **Own-words companion file for the 104 WIDA codes (Not checked).** Unlike CASEL (`casel-5.txt`) and NCAS
   (`ncas-performance-standards-words.txt`), `data/standards/wida-2020.txt` holds ids only. Before stage 2
   (`data/progressions/eld.csv`) starts after the C11 gate, should Curio Class write a planning-only own-words companion
   file (`data/standards/wida-2020-words.txt`) so progression and frame writers have a single checked own-words summary
   of every id, or keep ids only and have each writer work from the local WIDA PDF? **Recommended:** write
   `data/standards/wida-2020-words.txt` in our own words once, before stage 2, and check it cold against the framework.
3. **Syncing ADOPTION-BAR-SUBJECTS.md part 10 item 5 (finding 8).** STANDARD.md section 4, APPROACH.md and the ELD lens
   all include "English learners with disabilities" in every unit's learner notes, while ADOPTION-BAR-SUBJECTS.md part
   10 item 5 still names only newcomers and long-term English learners. **Recommended:** update bar part 10 item 5 to
   include English learners with disabilities so the bar matches the approved approach.

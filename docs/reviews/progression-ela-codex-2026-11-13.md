# ELA progression: independent expert cold read

**Date:** 2026-11-13  
**Reviewer:** Codex, second independent reader  
**Requested report path:** `docs/reviews/progression-ela-codex-2026-11-13.md`  
**Delivery:** Complete report below. No report file was written.

## Verdict

The progression has complete standard-code coverage and a broadly sound rise in reading, writing and language demand, but it needs corrections before course frames are fixed. Its greatest risk is contradictory guidance: several notes misstate when skills begin, some cross-subject links promise knowledge their targets do not teach, and paper alternatives leave digital requirements unfinished. Correct those statements and dependencies first, while preserving the foundational sequence through grade 5.

**Finding count: 9 consolidated findings.**

## What I read and checked

I read all **374 rows and every column** of [ela.csv](/S:/CurioClass/data/progressions/ela.csv), including the embedded notes.

I also read:

- `ela-excluded.csv`: header only, **zero exclusions**.
- All five ELA band-edge notes under `data/progressions/parts/`: K to 2, 3 to 5, 6 to 8, 9 to 10, and 11 to 12.
- `docs/agents/EXPERT.md`, the ELA lens, and `docs/RUBRIC-ELA.md`.
- The foundation, glossary, relevant baseline rules, approach guidance, source-access notes, and roadmap planning requirements.
- `docs/sources/BASE-TEXTS.md` and the relevant source manifest entries.
- Both ELA standards files: **455 parent standards**, with **413 lettered parts** in the full-text inventory.
- The progression checker and its coverage, ownership, handoff, model and cross-subject rules.
- All **99 cross-subject entries**, resolving their targets against the science and social studies progressions and checking the mathematics codes.
- The **20 distinct science target rows** and **49 distinct social studies target rows** needed for those references.

I checked the elementary order against the publisher’s K, grade 1 and grade 2 Skills Block year-at-a-glance documents, its grade 2 standards sequence, and the stored 2017 grades 3 to 5 curriculum plan. I read that local plan directly to standard output without creating an extracted file.

I did not open earlier ELA course pages or earlier ELA course/progression reviews. After forming the independent findings, I read `docs/reviews/progression-ela-reconcile-2026-11-13.md`. For repeat classification, I also consulted the permitted science and social studies progression reports.

**Memory:** No substantive finding rests on personal or saved memory. Recommendations identified as judgment calls are reviewer decisions rather than research findings.

### Gate result

The requested command could not finish:

```text
python -X utf8 scripts/plan.py check
ModuleNotFoundError: No module named 'markdown'
```

The authorized fallback completed:

```text
progression ela: 374 rows, 0 failure(s)
note e8-dramatic-irony (grade 8) hands on to e11-lit-irony (grade 11):
skips 2 grade(s)
```

The fallback settles its structural checks. It does not establish that a valid cross-subject code is taught early enough, that the target teaches the promised content, or that a row’s prose preserves every requirement.

## Coverage, ownership and pace

| Grade | Skill rows | Foundational | Reading | Writing | Speaking and listening | Language |
|---|---:|---:|---:|---:|---:|---:|
| K | 29 | 8 | 11 | 5 | 2 | 3 |
| 1 | 31 | 9 | 12 | 5 | 2 | 3 |
| 2 | 30 | 6 | 14 | 5 | 2 | 3 |
| 3 | 28 | 2 | 14 | 6 | 2 | 4 |
| 4 | 30 | 2 | 16 | 6 | 3 | 3 |
| 5 | 30 | 2 | 17 | 6 | 2 | 3 |
| 6 | 29 | 0 | 17 | 7 | 2 | 3 |
| 7 | 28 | 0 | 16 | 7 | 2 | 3 |
| 8 | 29 | 0 | 17 | 7 | 2 | 3 |
| 9 | 24 | 0 | 13 | 6 | 2 | 3 |
| 10 | 26 | 0 | 15 | 6 | 2 | 3 |
| 11 | 30 | 0 | 17 | 6 | 2 | 5 |
| 12 | 30 | 0 | 17 | 6 | 2 | 5 |
| **Total** | **374** | **29** | **196** | **78** | **27** | **44** |

- **Standards named by no skill:** none of the 455 ELA parent standards.
- **Skills naming no standard:** none.
- **Duplicate owning grades:** none under the checker’s ownership rules.
- **High school bands:** the `~CODE` contribution in the first year and ownership in the second year are coherent. Requirements carried across the band, including American drama and the historical span of American literature, are explicitly acknowledged.
- **Handoffs:** all **405 recorded prerequisite edges** are reciprocal. One skips intervening grades, addressed in F6.
- **Models:** **20 model names**, with no missing intervening grade between a model’s first and last recorded use. The remaining problem is contradictory prose, addressed in F8.
- **Cross-subject entries:** 31 science, 60 social studies and 8 mathematics references.

No grade has a convincing overload merely from these counts. Grade 1 has 31 rows against 29 and 30 in its neighbours. Grade 9’s 24 rows partly reflect bundled standards, while grade 11 separates more language work. These are differences in row granularity, not evidence of instructional minutes.

The foundational strand ends after grade 5 as expected. Grade 6 explicitly retains fluency practice. I found no unexplained disappearance and later restart of a whole literacy strand.

## Findings

`REPEAT` identifies a finding type already present in the permitted earlier reports or the reconcile report. “New” means new within that comparison set, not an exhaustive claim about unopened ELA reviews.

### F1. Early phonics notes conflict with the base text and with one another

**Severity:** High  
**LAYER:** base text  
**REPEAT:** yes, source-order discrepancies recur in the science progression read, F2  
**Confidence:** firm

**Skills:** `ek-phonemes`, `ek-letter-sounds`, `ek-cvc-decoding`, `e1-short-vowels`, `e1-inflections`, `e2-prefixes-suffixes`.

Three statements need correction:

1. `ek-phonemes` excludes digraph segmentation, although kindergarten teaches and decodes `sh`, `ch` and `th`. A digraph can represent one phoneme; excluding it is not the same as limiting words to three phonemes.
2. `ek-cvc-decoding` places reading `-ank` and `-ink` in kindergarten. The base text introduces these in **spoken words** in kindergarten cycle 21.
3. `e1-inflections` places dropping silent `e` before a vowel suffix in grade 1 while claiming the base text’s order. The published grade 2 sequence explicitly introduces that generalization in cycle 13.

The publisher’s [kindergarten sequence](https://files.eleducation.org/web/resources/Section-5_CurriculumTools_SkillsBlock-Year-at-a-Glance_GradeK.pdf), PDF page 2, and [grade 2 sequence](https://files.eleducation.org/web/resources/Section-5_SkillsBlock-Year-at-a-Glance_Grade2_071417.pdf), PDF page 2, establish those placements. The [kindergarten standard](https://www.thecorestandards.org/ELA-Literacy/RF/K/) also distinguishes phoneme count from letter count.

**Why it matters:** A writer could produce decodable text with an untaught spelling, omit sound work needed for already taught digraphs, or unknowingly accelerate a spelling rule.

**Exact fix:**

- In `ek-phonemes.notes`, replace the digraph ban with: “Use three-phoneme words, including words containing taught consonant digraphs. Consonant clusters extend in grade 1.” Attach the `/l/`, `/r/`, `/x/` exclusion specifically to RF.K.2d.
- In `ek-cvc-decoding.notes`, describe `-ank` and `-ink` as oral work at this point; leave their printed decoding to grade 1.
- Align the silent-`e` dropping rule with grade 2 by removing it from `e1-inflections.notes` and explicitly adding it to `e2-prefixes-suffixes.notes`, or record a deliberate, justified departure from the base order.

The last two placement choices change the written grade expectations and go to Cory.

### F2. Several notes give the wrong teaching onset

**Severity:** High  
**LAYER:** standard  
**REPEAT:** yes, incorrect grade assignments are the same kind of problem corrected in reconcile differences 15 and 16  
**Confidence:** firm

**Skills and exact note corrections:**

| Skill | Incorrect statement or implication | Replacement |
|---|---|---|
| `e2-grammar` | Tenses beyond simple begin in grade 3 | Simple tenses continue in grade 3; progressive begins in grade 4 and perfect in grade 5 |
| `e2-prefixes-suffixes` | Greek and Latin roots begin in grade 3 | Grade 3 includes Latin suffix decoding; Greek and Latin root strategies are explicit in grade 4 |
| `e2-reasons-support` | Evidence sufficiency begins in grade 4 | Grade 4 explains reasons and evidence; sufficiency is explicit in grade 7 |
| `e5-quote-accurately` | Several pieces of evidence are the grade 6 step | Several pieces are explicit in grade 7 |
| `e5-opinion` | Answering an opposing claim defines grade 6 argument | Grade 6 develops claims with reasons and evidence; acknowledging opposing claims is explicit in grade 7 |
| `e5-research` | Standard citation format begins in grade 6 | Grade 6 requires basic bibliographic information; standard format is explicit in grade 7 |
| `e6-narrative-writing` | Grade 6 adds pacing | Grade 5 already includes pacing; grade 6 develops control and time/setting transitions |
| `e6-revise-edit` | Grade 6 adds trying a new approach | Grade 5 already includes it; describe the increased control of style and tone |
| `e11-word-strategies` | Verification is a new step here | Verification is already explicit in grade 6 |
| `e12-narrative` | Reflection becomes a technique here | Reflection is already explicit inside narrative in grade 8; grade 12 deepens significance and control |

These corrections follow the [standards’ grade tables](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf). Several are also contradicted by the correctly written later rows in this CSV.

**Why it matters:** Handoff notes are planning instructions. These statements can cause premature expectations or repeated introductory teaching.

**Exact fix:** Replace the identified boundary or “adds” sentences. Keep the correctly assigned standard owners and later-grade rows.

### F3. Paper and unrecorded alternatives leave parts of claimed standards unfinished

**Severity:** High  
**LAYER:** progression  
**REPEAT:** yes, reconcile difference 6 corrected this explicitly for grade 6  
**Confidence:** firm

**Skills:** `ek-revise-publish`, `e1-revise-publish`, `e2-revise-edit`, `e2-tell-and-record`, `e3-writing-process`, `e4-writing-process`, `e5-writing-process`, `e7-produce-publish`, `e8-produce-publish`, `e9-w-process`.

Grade 6 correctly states that its paper path does not complete W.6.6. Comparable alternatives elsewhere lack that distinction:

- Paper publishing replaces digital production.
- Grades 3 to 5 move keyboarding to an assumed home or library session.
- Grade 7 substitutes a printed source list for live links.
- Grade 8 substitutes a paper diagram for technology use.
- Grade 2 allows an unrecorded presentation without explaining the resulting SL.2.5 gap.

Digital production, keyboarding and creating recordings remain distinct performances in the [standards](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf).

**Why it matters:** A teacher can finish the offered alternative while a claimed requirement remains untaught or undemonstrated.

**Exact fix:** Add a completion boundary to each affected row:

> “The paper or unrecorded alternative supports the other goals but does not demonstrate the digital, keyboarding or recording requirement. Record that requirement separately until its stated performance is completed.”

For grades 3 to 5, replace assumed home/library completion with a specified access route before the year ends, or explicitly mark the requirement unfinished. Preserve student privacy and the option not to make a recording; do not count an unrecorded talk as a recording.

K to 2 device assumptions remain Cory’s decision.

### F4. Five cross-subject references point forward or promise the wrong content

**Severity:** High  
**LAYER:** progression  
**REPEAT:** yes, wrong-content references recur in the science read, F7  
**Confidence:** firm

| ELA skill | Problem | Exact replacement |
|---|---|---|
| `e6-argument-writing` | `D4.1.6-8` is owned by `ss8-court-research`, grade 8 | Use `social-studies:ss6-research-contribution`, whose notes already require a sourced argument about historical significance |
| `e3-informative` | `3-LS4-2` concerns differences among individuals of one kind; the ELA task concerns frog traits and survival | Use `science:s3-habitat-survival`, describing needs, traits and habitat conditions |
| `e3-short-research` | The same variation-versus-adaptation mismatch | Use `science:s3-habitat-survival` for the stated research task |
| `e9-rl-myth-retold` | `wh1-classical-learning` teaches transmission of classical learning, not Greek myth and epic | Use `social-studies:ss7-greek-myth`; ELA supplies the epic text |
| `e10-rl-source-transformation` | `wh1-classical-learning` does not teach Caesar’s history or Plutarch | Use `social-studies:ss7-republic-to-empire` for historical context; state that ELA supplies and teaches the Plutarch comparison |

Evidence is in the current [social studies progression](/S:/CurioClass/data/progressions/social-studies.csv) and [science progression](/S:/CurioClass/data/progressions/science.csv).

**Why it matters:** These links hide missing preparation behind valid identifiers.

**Reconcile disagreement:** Difference 10 restored the grade 6 C3 link because the gate accepts its code. I disagree with that decision as a readiness claim: its current completion owner is grade 8.

No other science or social studies reference had a later owning grade. Mathematics timing remains qualified in F9.

### F5. Grades 6 to 8 do not establish a connected knowledge progression

**Severity:** Medium  
**LAYER:** progression  
**REPEAT:** new  
**Confidence:** firm on the missing record; judgment call on the eventual topics

**Skills:** `e6-reading-range`, `e7-reading-range`, `e8-reading-range`, their academic-word rows, and the informational reading/writing rows built around unit topics.

Elementary rows name recurring topic sets. The middle school rows mostly offer examples such as a flood town, an epidemic, a scientist or a policy issue. They do not identify which topic knowledge the next grade inherits or how it deepens.

The [6 to 12 review criteria](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Review_Criteria_2_0_a3fc2b49ab.pdf), indicators 2d and 2k, require coherent knowledge building and vocabulary development. The Curio Class progression lens specifically asks for connections across grades.

**Why it matters:** Skill demand can rise while students repeatedly start unrelated topics with little accumulated knowledge.

**Exact fix:** Before course frames are fixed, add a compact topic-handoff record to the grade 6, 7 and 8 reading-range notes:

```text
Named topic sets:
Knowledge inherited from earlier grades:
New knowledge this grade adds:
Words and concepts deliberately reused:
Next-grade row that uses them:
```

Populate it with the actual chosen topics and receiving skill IDs. A broad theme or “science and history” is insufficient.

Topic selection changes what grades teach and goes to Cory.

### F6. The irony handoff explains the gap without securing readiness

**Severity:** Medium  
**LAYER:** progression  
**REPEAT:** yes, long-range ancestry recorded as retained prerequisites recurs in the social studies read, F5  
**Confidence:** firm

**Skills:** `e8-dramatic-irony`, `e9-rl-world-stories`, `e10-rl-world-literature`, `e11-lit-irony`.

The direct grade 8 to grade 11 edge skips grades 9 and 10. Its explanation is accurate: the intervening point-of-view standards focus on cultural experience. That explains the standards’ change of emphasis, but it does not establish retention of dramatic irony.

**Why it matters:** Grade 11 may treat a skill last explicitly taught three school years earlier as ready for immediate use.

**Exact fix:**

- Remove `e11-lit-irony` from `e8-dramatic-irony.hands_on`.
- Remove `e8-dramatic-irony` from `e11-lit-irony.assumes`.
- Preserve the adjacent point-of-view chain through grades 9 and 10.
- Add to `e11-lit-irony.notes`: “Grade 8 dramatic irony is a historical connection. Begin with a short retrieval example and reteach the character/reader knowledge gap before using it in the stated-versus-meant analysis.”

This reactivates content already inside the grade 11 row. It does not require adding a new grade 9 or 10 topic.

### F7. High school mathematics references have no verified course owner

**Severity:** Medium  
**LAYER:** process  
**REPEAT:** yes, unresolved mathematics readiness recurs in the science read, F8  
**Confidence:** firm

**Skills:** `e9-ri-argument-evaluate`, `e10-ri-argument-evaluate`, `e11-info-multiple-sources`, `e12-info-multiple-sources`.

Four of the eight mathematics references use high school codes without an established owning grade in a mathematics progression:

- `S-ID.C.9`
- `S-IC.B.6`, used twice
- `S-ID.B.5`

The codes are valid. Their grade availability is unverified. A high school code alone cannot establish preparation by grade 9, 10 or 11.

The other four mathematics references have explicit K to 8 grades at or before their ELA use.

**Why it matters:** An ELA task can depend on statistical reasoning students have not yet encountered.

**Exact fix:** Add to each affected row:

> “Mathematics ownership and timing are pending. Provide the display, a worked interpretation and the statistical distinction needed for this task; do not assume prior completion of this high school mathematics code.”

Replace the provisional code reference with the actual skill ID and owning grade when the mathematics progression exists.

### F8. Model columns are continuous, but prose gives conflicting introductions

**Severity:** Medium  
**LAYER:** process  
**REPEAT:** yes, model-record inconsistencies recur in the science read, F5  
**Confidence:** firm

**Skills:** `e3-literal-nonliteral`, `e3-story-parts`, `e3-text-connections`, `e4-reasons-evidence`, `e6-author-purpose`, `e6-trace-argument`, `e9-ri-purpose-rhetoric`; corresponding band-edge notes.

The stitched columns correctly carry models already introduced earlier. Their prose still says they are introduced again:

| Model | First recorded grade | Later prose calling it introduced |
|---|---|---|
| `figurative-language` | 1 | Grade 3 |
| `narrative-arc` | K | Grade 3 |
| `text-structure` | K | Grade 3 |
| `claim-evidence-reasoning` | K | Grade 4 |
| `rhetorical-situation` | 4 | Grades 6 and 9 |
| `argument-map` | 5 | Grade 6 |

**Why it matters:** A writer cannot tell whether to retrieve an existing representation, extend it or teach a replacement.

**Exact fix:** Replace those introduction claims with “extends” or “formalizes,” naming the added feature. For example, grade 4 adds explicit evidence to the earlier point-and-reasons representation; grade 6 adds a mark for unsupported claims.

Synchronize the edge notes with the stitched CSV, or label their obsolete drafting instructions as historical. Keep the current model columns and names.

### F9. Independence wording can be read as withdrawing teaching support from everyone

**Severity:** Medium  
**LAYER:** progression  
**REPEAT:** new  
**Confidence:** likely, a wording risk rather than evidence of classroom practice

**Skills:** `e8-reading-range`, `e10-rl-range-independent`, `e11-reading-band`, `e12-reading-band`.

These rows correctly target independence. Some phrases turn that destination into a general instructional rule: later anchors have no before-reading help, the final anchor loses the long-sentence routine, or routine supports are removed.

[Appendix A](https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-a.pdf), PDF pages 10 to 11, supports increasing independence while retaining help needed to access grade-level complexity. The [review criteria](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Review_Criteria_2_0_a3fc2b49ab.pdf), 2c and 3j, likewise retain instructional supports.

**Why it matters:** A busy writer could withhold useful instruction from a struggling reader merely because the class has reached the final unit.

**Exact fix:** Replace blanket removal language with:

> “Fade routine scaffolds as students demonstrate readiness. Include independent reading checkpoints at the required band demand. Continue targeted instruction and access supports, and distinguish supported learning from evidence of independent proficiency.”

Keep the independent end-of-band target and appropriate cold-read assessments.

## Lens checklist: progression layer

| Checklist line | Status | Evidence |
|---|---|---|
| Reading and writing climb in task or text demand | **Met, with corrections** | Increasing analysis, text bands and independence are explicit; F2 corrects false onset statements |
| K to 2 phonics elements precede their decodable use | **Missed** | Kindergarten `-ank`/`-ink` placement and contradictory digraph guidance, F1 |
| Grade 3 builds on grade 2 with its own phonics and fluency plan | **Met** | `e3-long-words` inherits four grade 2 foundational skills; `e3-fluency` retains instruction and checks |
| Topic sets connect across grades without repeating the same depth | **Missed** | The middle school knowledge handoffs are not established, F5 |
| Argument/opinion, informative and narrative writing remain balanced across grades | **Met at progression level** | All three appear every year with increasing demands; actual shares require the later writing calendars |

The lens’s course-frame, scope-and-sequence, unit and day checklists are **not applicable to scoring this progression**. They remain later checks, including anchor-text records, question counts, full-process writing frequency and lesson-level decodable alignment.

### Words

The word lists generally fit their grades when specialist labels are explicitly taught. I found no additional clear grade inversion requiring a separate finding.

Within-year teach-before-use cannot be established from these annual rows alone. The course word records and phonics cycles must supply that timing. New terminology should be taught at first use rather than treated as already known because it appears in `words`.

## Settled by the expert

These are item-level corrections or interpretations. No edits were applied.

| Choice | Reason | File affected |
|---|---|---|
| Count phonemes, not letters, when selecting kindergarten sound examples | A taught consonant digraph can represent one phoneme | `data/progressions/ela.csv`, `ek-phonemes` |
| Keep kindergarten long-vowel association distinct from grade 1 CVCe decoding | RF.K.3b does not require moving the whole grade 1 spelling sequence into kindergarten; make the printed-vowel association explicit | `ela.csv`, `ek-cvc-decoding` |
| Use the corrected onset sentences in F2 | They repair descriptions while retaining the correctly placed owners | `ela.csv`, listed rows |
| Use the five replacement cross-subject targets in F4 | They identify existing, appropriately placed content | `ela.csv`, five `cross_subject` cells |
| Reactivate grade 8 irony inside the existing grade 11 work | Removes an unsupported retained-prerequisite claim without inventing intervening content | `ela.csv`, `e8-dramatic-irony`, `e11-lit-irony` |
| Change repeated model “introductions” to explicit extensions | The columns already preserve continuity | `ela.csv` and ELA edge notes |
| Retain writing-share targets as planning guidance, with correct attribution | The standards’ introduction describes writing across subjects; the review guide separately reports ELA process-writing distributions | `ela.csv`, `e10-w-argument`, `e11-argument` |
| Separate supported learning from independent checkpoints | Preserves both instruction and the required proficiency target | `ela.csv`, reading-range rows |

For the writing-share attribution, see the [standards’ introduction](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf), PDF page 5, and the [6 to 12 evidence guide](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Evidence_Guide_2_0_2068cea08f.pdf), PDF page 62. No imbalance is established from skill-row counts.

## What is right and should remain

- Explicit, systematic foundational instruction, with decoding separated from meaning-making through context.
- Decodable text constrained by taught patterns and taught irregular words.
- Rich read-alouds while independent decoding develops.
- Grade 3 to 5 long-word instruction, spelling, connected-text practice and fluency checks.
- Increasing evidence demands from accurate quotation to multiple, strongest and thorough evidence.
- Continued narrative writing alongside argument and explanation.
- Research, discussion, sentence work and vocabulary represented throughout the grades.
- High school band contributions distinguished from completion ownership.
- The explicit grade 6 statement that its paper path does not complete W.6.6.

These strengths are consistent with the [WWC foundational-skills recommendations](https://ies.ed.gov/ncee/wwc/PracticeGuide/21), particularly linking sounds to letters, decoding and word analysis, and daily connected-text reading.

## What I could not judge

- Actual anchor-text quality, rights, complexity and representation. Proposed titles or plot descriptions do not establish those qualities.
- Every phonics pattern’s lesson-level timing or every decodable word’s eligibility.
- Annual minutes, workload and writing-type shares. Rows combine unequal amounts of work.
- Actual proficiency checks, scoring guidance and instructional responses.
- High school mathematics availability before its course ownership is assigned.
- Complete K to 2 topic-map detail from the older public curriculum-plan PDF, which returned 404. The phonics sequence PDFs were accessible, and the stored grades 3 to 5 plan was readable.

## Sources and access notes

All findings above use current repository evidence or sources opened during this read.

| Source | Use |
|---|---|
| [Common Core ELA standards, official CCSSO PDF](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf) | Grade requirements, lettered parts, high school bands and writing-share attribution |
| [Appendix A, state-hosted copy](https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-a.pdf) | Complexity, scaffolding and independence |
| [Kindergarten Skills Block sequence](https://files.eleducation.org/web/resources/Section-5_CurriculumTools_SkillsBlock-Year-at-a-Glance_GradeK.pdf) | Digraphs, oral versus printed patterns and kindergarten order |
| [Grade 1 Skills Block sequence](https://files.eleducation.org/web/resources/Section-5_CurriculumTools_SkillsBlock-Year-at-a-Glance_Grade1.pdf) | Grade 1 phonics and syllable progression |
| [Grade 2 Skills Block sequence](https://files.eleducation.org/web/resources/Section-5_SkillsBlock-Year-at-a-Glance_Grade2_071417.pdf) | Suffix rules, syllables, vowel teams and schwa |
| [Grade 2 standards sequence](https://curriculum.eleducation.org/sites/default/files/curriculumtools_skillsblock-standards-scope-and-sequence_grade2_052217_0.pdf) | Foundational end points and continuing practice |
| [2017 grades 3 to 5 curriculum plan](https://web.archive.org/web/20240705100431id_/http://curriculum.eleducation.org/sites/default/files/curriculumtools_curriculumplan-3-5_072017.pdf) | Topic and task order; read from the existing local copy |
| [K to 2 review criteria](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_20_K_2_20_Review_20_Criteria_2_1_44660ca52d.pdf) | Phonemic awareness, intentional phonics order and aligned decodables |
| [Grades 3 to 5 review criteria](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_3_5_Review_Criteria_2_1_bb1cc2d7c6.pdf) | Morphology, long words, connected text and fluency |
| [Grades 6 to 12 review criteria](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Review_Criteria_2_0_a3fc2b49ab.pdf) | Knowledge building, scaffolds and access |
| [Grades 6 to 12 evidence guide](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Evidence_Guide_2_0_2068cea08f.pdf) | Indicator 2o’s writing distribution and its reporting status |
| [WWC foundational-skills guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/21) | Research-supported foundational practices |

### For the source list

- The [review-tools index](https://edreports.org/process/review-tools/ela) successfully opened the linked criteria and evidence guide after direct PDF requests initially failed.
- `pdftotext -layout INPUT.pdf -` reads the stored base-text PDF to standard output without creating an extracted file.
- The older K to 2 and grades 3 to 5 curriculum-plan addresses returned 404. Preserve their manifest/archive routes rather than assuming the old addresses work.

## For Cory

- Decide whether to restore the base-text placements for printed `-ank`/`-ink` and silent-`e` dropping, or retain explicitly justified accelerations.
- Select the grades 6 to 8 topic sets and knowledge handoffs before their course frames are fixed.
- Resolve the K to 2 device-access assumption. Until a digital performance is provided, keep its completion status explicit.

**Verdict:** Revise before fixing course frames. **Findings:** 9. **Intended report path:** `docs/reviews/progression-ela-codex-2026-11-13.md`, delivered here, not written.
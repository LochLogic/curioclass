# Independent expert cold read: social studies grade 3

**Date:** 2026-11-13  
**Intended report path:** `docs/reviews/frame-social-studies-grade-3-2026-11-13.md`  
**Delivery:** Report supplied here only. No files were changed.

## Verdict

The seven-unit structure is coherent, and every grade 3 progression skill has one clear unit placement. The frame needs revision before it guides writing because its apparent standards completeness hides several missing demands and one inaccurate historical generalization. Correct the coverage descriptions and founding-era citizenship statement while preserving the unit structure and year total.

## What I read and checked

I read:

- `docs/agents/EXPERT.md` and `docs/agents/lenses/social-studies.md`.
- `docs/FOUNDATION.md`, the relevant path and gaps in `docs/ROADMAP.md`, BASELINE rules 20 to 24, and `docs/GLOSSARY.md`.
- `docs/APPROACH.md` and relevant source-access material in `docs/APPROACH-SOURCES.md`. No social studies approach page exists.
- Section 1 and the relevant shared criteria of `docs/ADOPTION-BAR-SUBJECTS.md`.
- `docs/courses/social-studies/STANDARD.md` and `grade-3-outline.md`.
- The complete grade 3 frame and the neighboring grade 2 and grade 4 frames.
- Grade 3 progression rows, neighboring-grade handoffs, relevant cross-subject progression rows, and `social-studies-excluded.csv`.
- `data/plans/frames.csv`, `data/plans/later.csv`, and `docs/sources/BASE-TEXTS.md`.
- Earlier social studies standard, progression, fix and source reviews, plus the cross-subject fix report.
- The relevant frame-checker and stale-checker behavior.

Outside checking used the official standards, historical records and curriculum references linked below. No finding rests solely on memory.

### Gate results

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check`, run first | Could not finish: `ModuleNotFoundError: No module named 'markdown'` |
| `python -B -X utf8 scripts/frame.py check social-studies-grade-3` | 0 failures |
| `python -B -X utf8 scripts/progression.py check social-studies` | 384 rows, 0 failures |
| `python -B -X utf8 scripts/stale.py check` | 16 files, 0 failures |

The first result is an environment limitation, not an established plan failure. I continued with the requested substantive review and the available read-only checks. Nothing was installed.

## Findings, most serious first

### 1. Unit 6 conflates citizenship, voting and equal rights

**LAYER:** standard  
**REPEAT:** new  
**Severity:** serious  
**Confidence:** firm

The frame says that full citizenship was limited to white men who owned property. The same generalization appears in `ss3-founding-ideas` and the loaded paraphrase of `MA.3.T6.4`.

Citizenship and eligibility to vote were different questions. The original Constitution tied House voting qualifications to state rules. New Jersey permitted some women and free Black property owners to vote before removing those rights in 1807. The nationwide formulation therefore teaches a false uniform rule. See the [original Constitution, Article I, Section 2](https://www.archives.gov/founding-docs/constitution-transcript) and [New Jersey’s historical account and constitutional provision](https://www.nj.gov/state/historical/assets/pdf/it-happened-here/ihhnj-er-petticoat-politicians.pdf).

**Why it matters:** students would carry an inaccurate account of both citizenship and exclusion into later civics.

**Exact fix:** replace the generalization in the frame, progression note and standards paraphrase with:

> The founding documents promised rights, but laws and practices denied many people equal rights and political power. Voting rules differed by state and usually favored adult white men; many states also required property or tax payments. Some women and free Black people voted in New Jersey before that right was taken away in 1807. Citizenship, voting and equal rights were different questions.

Keep the plain account of slavery and unequal treatment. Mark the standards paraphrase as a clarification of the anchor’s oversimplified statement.

### 2. Generalizing the anchor has removed some of its required work

**LAYER:** frame  
**REPEAT:** yes, bundled-standard omissions in `progression-social-studies-codex-2026-11-13.md`, finding 2  
**Severity:** serious  
**Confidence:** firm

The own-state substitution is authorized. It should replace locations while preserving the intellectual work. Several unit descriptions currently lose that work.

| Placement | Missing or unsecured requirement | Exact addition |
|---|---|---|
| Unit 1, `MA.3.T1.1` | Historic landmarks’ significance | Explain what one mapped historic landmark reveals about the community. |
| Unit 1, `MA.3.T2.2` | Locating the states within the region | Locate and name the states in the student’s home region on a US political map. |
| Unit 2, `MA.3.T1.3` | School governance and property taxes | Identify who governs public schools; explain how property taxes support local services. |
| Unit 4, `MA.3.T2.3a` | At least three distinct Native groups | Require three named nations across the local and supplied regional cases. |
| Unit 5, `MA.3.T5.2` | Religious conversion among colonization’s consequences | Include a brief, sourced explanation alongside land loss, disease and conflict. |
| Unit 7, `MA.3.T6.1` | Historical territorial extent and reasons for eighteenth-century town growth | Interpret a worked state’s historical boundaries and explain its town growth, then make a suitable local comparison. |

These checks come from the [Massachusetts framework, PDF pages 53 to 56](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf).

**Why it matters:** a writer could faithfully follow the frame and produce incomplete teaching.

The corresponding progression notes also need these commitments. Adding lettered codes alone would not repair them.

### 3. Several C3 ownership claims still exceed the specified teaching

**LAYER:** progression  
**REPEAT:** yes, semantic coverage in both earlier social studies progression reads  
**Severity:** serious  
**Confidence:** firm

| Placement and indicator | Gap | Exact fix |
|---|---|---|
| Unit 1, `D1.3.3-5` | Supporting-question interpretations remain unspecified | Identify one idea with two defensible interpretations for each supporting question. |
| Unit 2, `D2.Civ.5.3-5` | Frame comparison omits origins and functions | Carry those explicit progression-note requirements into the frame. |
| Unit 2, `D2.Civ.6.3-5` | Participation omits cooperation’s difficulties | Compare benefits and challenges in family, workplace, voluntary-group and government examples. |
| Unit 3, `D2.Eco.10.3-5` | Interest is named, but a rate is not explained | Compare returns for the same principal and year, expressed as dollars per $100, without percent calculations. |
| Units 1 and 4, `D2.Geo.4–6.3-5` | Physical changes dominate; cultural influences remain implicit | Add sourced explanations connecting cultural practices to land use, change and settlement patterns. |
| Unit 7, `D4.7.3-5` | Only local collective action is specified | Compare individual and group approaches to regional and global problems and predict results; retain one local action. |

The [official C3 indicator tables](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf) support these distinctions.

**Why it matters:** code coverage would overstate taught coverage.

The interest finding remains despite the earlier fix record. Removing the vocabulary burden of “interest rate” did not remove the indicator’s demand.

### 4. The frame leaves its five worked Native-nation examples unselected

**LAYER:** frame  
**REPEAT:** new  
**Severity:** moderate  
**Confidence:** likely

`ss3-first-nations-region` says the course frame settles five regional examples. The frame instead defers selection through L5, whose due point is the writing of this frame.

**Why it matters:** the unit’s 18-day allocation and promised regional range cannot be assessed against an actual case set. Writers must make a course-level selection that this layer was supposed to settle.

**Exact fix:** name the following worked cases, using the linked nations’ own public materials as starting sources:

| Region | Worked case and source |
|---|---|
| Northeast | [Mashpee Wampanoag Tribe](https://mashpeewampanoagtribe-nsn.gov/timeline) |
| Southeast homelands | [Cherokee Nation](https://www.cherokee.gov/about-the-nation/history/) |
| Midwest | [Menominee Indian Tribe of Wisconsin](https://www.menominee-nsn.gov/culturepages/briefhistory) |
| Southwest | [Navajo Nation](https://www.navajo-nsn.gov/History) |
| West | [Makah Tribe](https://makah.com/makah-tribal-info/) |

Distinguish homelands from present locations, especially in the Cherokee case. These are five particular nations, not representatives of every nation in their regions. Keep the local thread and the required sensitivity and qualified-person reads.

Update L5 only after the selection is recorded.

### 5. Unit 2 compares constitutions before securing their basic purpose

**LAYER:** frame  
**REPEAT:** yes, prerequisite mismatches in the earlier social studies progression review, finding 2  
**Severity:** moderate  
**Confidence:** likely

The frame explicitly reserves what a constitution is for until unit 6, while unit 2 compares state, national and another governmental system. Its own final notes recognize this tension but leave two alternatives.

**Why it matters:** students could compare institutional names without understanding the governing document that establishes them.

**Exact fix:** retain `ss3-state-constitution` in unit 2. Before the comparison, teach:

> A constitution is a basic plan that establishes a government, describes its powers and limits, and may state protected rights.

Treat national branch names as a preview used for comparison. Unit 6 then revisits constitutional purpose in its founding context. No standard needs to move.

### 6 to 12. Unmarked stale notes remain after the checker passes

Each row below is a separate finding.

**LAYER:** process  
**REPEAT:** yes for each, stale-note findings in the earlier progression reviews  
**Severity:** minor individually  
**Confidence:** firm

These notes can cause duplicate work or false blockers. The marked-note checker does not establish that unmarked prose is current.

| # | Stale note | Evidence of completion | Exact replacement |
|---|---|---|---|
| **6** | Grade 3 frame, lines 175–176, requests frame synchronization | `frames.csv` already records 7 units and 160 days; the frame check passes | “The frame and `frames.csv` agree: 7 units, 160 days.” |
| **7** | Grade 2 frame, lines 186–187, says the CSV disagrees until synchronization | Its CSV row already matches the frame’s 7 units and 96 days | “The frame and `frames.csv` agree: 7 units, 96 days.” |
| **8** | Progression fix report, line 43, says cross-subject ownership checking waits on other progressions | All four progressions exist; the cross-subject fix report records the ownership and grade-order gate | “Cross-subject ownership and grade-order checking were completed in the cross-subject pass. Within-year availability remains a frame-level check.” |
| **9** | `ROADMAP.md`, lines 95–96, says the social studies content standard remains open | `STANDARD.md` records the chosen standard and implemented course list | “The social studies standard is chosen and recorded in `STANDARD.md`; work follows `PRODUCTION-PATH.md`.” |
| **10** | Open-material review, line 225, says the tribal-sovereignty files await loading approval | L9 and `BASE-TEXTS.md` record loading | “Loaded: 17 unit pages and 117 files. Earlier totals counted shared files more than once.” |
| **11** | Same review, line 226, says financial-education activities await loading approval | L9 and `BASE-TEXTS.md` record loading | “Loaded: 134 of 135 activities, 262 PDFs. One activity page is unavailable.” |
| **12** | Same review, line 175, still asks Cory to decide the OGL licence and retired-text AI clause | `BASE-TEXTS.md` records both decisions dated 2026-11-13 | “Decided 2026-11-13: OGL v3.0 is accepted; the recorded retired-text use is authorized under Cory’s interpretation. Item-level exclusions still apply.” |

Preserve the original dated research as history, but mark superseded requests clearly.

## Ownership, order, days and seams

### Placement and time

All **27 owned skills** appear exactly once in the unit ownership column. Their rows collectively name **19 Massachusetts codes and 41 C3 indicators**. No foreign-grade skill ID appears as an owned grade 3 skill.

| Unit | Owned skills | Days | Course days, including intervening checks | Judgment |
|---|---:|---:|---|---|
| 1. Where we live | 6 | 24 | 1–24 | Appropriate foundation for maps and inquiry |
| 2. Who decides here | 5 | 24 | 25–48 | Reasonable, with dormant-grade readiness work |
| 3. Making a living here | 4 | 20 | 49–68 | Reasonable for economic reasoning and repeated savings records |
| 4. First peoples | 2 | 18 | 72–89 | Defensible for substantive cases and source work |
| 5. First meetings and colonies | 6 | 32 | 90–121 | The largest allocation fits its content breadth |
| 6. Founding ideas | 1 | 12 | 125–136 | Defensible because the row bundles several concepts |
| 7. Community change | 3 | 20 | 137–156 | Reasonable for research, biography, sharing and action |
| Course checks and responses | — | 10 | 69–71, 122–124, 157–160 | Explicitly reserved |
| **Total** | **27** | **160** | | Matches `frames.csv` |

No unit is demonstrably far over or under its share. Skill-row counts alone cannot establish instructional load: unit 6’s single row is broad, while unit 4 needs sustained work with particular nations and evidence.

A 160-day course leaves 20 days against a 180-day school-year reference. The daily 40-minute block remains an audience assumption for Cory. Unit assessments and responses must fit inside the existing unit allocations when the scope and sequence is written.

### Order and handoffs

The sequence has sound reasons: place supports civics and trade; Native nations precede European arrival; colonies precede founding; community research gathers the year’s methods.

Grade 2’s map, source, migration, interview and claim handoffs are picked up. Grade 1’s dormant civics and saving knowledge has named readiness checks. Grade 4’s incoming requirements align with the grade 3 frame, including the deliberate return to earlier voyages.

Keep the staged distinctions:

- Whole-bar map distances here, ruler measurement and partial bars in grade 4.
- Latitude and longitude named here, numerical location in grade 4.
- Given sources and class-supported inquiry here, greater source choice later.

The explicitly deferred Revolution-events standard has a named grade 5 destination. No base text is adopted, so base-lesson mapping, exclusions and base-order checks are **not applicable**. The absent `source-map.csv` is not a defect.

### Cross-subject availability

The referenced skills resolve to the appropriate progression grades. However, **no math, ELA or science course frames were present**, so their within-year teaching order could not be verified.

The ELA progression places opinion-writing applications in units 3 and 4, rather than establishing that skill in the first writing unit. Retain the social studies frame’s spoken and sentence-frame bridge from unit 1. Research and informative-writing applications appear earlier in the ELA progression; the social studies research project is late in the year.

The math sums-within-100 bridge and local teaching of climate patterns provide workable safeguards. Mark the calendar as provisional until peer frames exist.

## Course-frame lens checklist

| Checklist line | Status | Reason |
|---|---|---|
| Every anchor standard in the course’s range has a unit | **Missed in substance** | Every owned code is placed, but findings 2 and 3 identify incomplete demands. |
| The replaced grade 3 year avoids Massachusetts-only content | **Met** | Own-place tasks and examples from several states replace a compulsory Massachusetts year. |
| Each unit identifies check-set additions and their sources | **Met at frame depth** | Every unit names a candidate or confirmation and a check-state source. Full comparison belongs to unit planning. |

Progression, scope-and-sequence, unit and day checklist lines were used to inspect dependencies, but those layers are not certified by this frame read.

## Settled by the expert

These are recommendations for the caller to apply. No edits were made.

| Choice | Reason | File touched |
|---|---|---|
| Keep seven units and the current allocations | No demonstrated allocation defect warrants reshaping | Grade 3 frame |
| Keep state-constitution work in unit 2, with the introductory explanation in finding 5 | Repairs the prerequisite without moving ownership | Grade 3 frame |
| Apply the item-level coverage clarifications in findings 2 and 3 | Completes existing ownership | Frame and named progression notes |
| Use the five worked Native-nation cases in finding 4 | Resolves the frame’s promised selection | Frame, outline and L5 |
| Retain source classification by relationship to the question | Earlier definition repair is sound | Frame and `ss3-primary-secondary` |
| Retain one completed local action | Broader comparison does not require additional projects | Frame and `ss3-informed-action` |
| Keep the existing map-scale and chronology staging | Neighboring frames pick it up coherently | No change |
| Mark completed handoff work with the replacement notes above | Prevents duplicate tasks and false blockers | Named process documents |

## What is right and should not be touched

- The own-place method preserves national usability.
- Native nations appear as present-day governments and peoples.
- Hard-history notes protect dignity and prohibit harmful simulations.
- Geography and economics support explanations rather than isolated vocabulary.
- Claims recur across the year.
- Course checks use unfamiliar sources and have response time reserved.
- Family financial and immigration information is protected.
- The community project draws together the year’s content and methods.

## What I could not judge

- A complete `plan.py check`, because of the missing dependency.
- Cross-subject order against peer course frames that do not yet exist.
- Actual source difficulty, rights, accessibility and reading load.
- Daily feasibility or assessment completeness before unit plans exist.
- Final Native-content accuracy and sensitivity without the required reads.

The two outside curriculum comparisons were limited to their published inquiry structures. They were not full lesson-by-lesson audits.

## For Cory

- **Audience and scope:** confirm the daily 40-minute, 160-day assumption. If a shorter route is required, require a concrete route that preserves owned standards.
- **People:** arrange the qualified community reader required before Native and hard-history units go live. None was contacted.

No money or outreach is requested for the item-level corrections.

## Sources and source-list additions

- [Massachusetts History and Social Science Framework](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf): anchor content and grade transitions.
- [C3 Framework](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf): indicator meanings.
- [EdReports and AIR social studies criteria](https://air.org/sites/default/files/2024-01/23-23505_HQIM_for_SS_Final.pdf): coherent sequencing, feasibility and disciplinary work.
- [Original US Constitution](https://www.archives.gov/founding-docs/constitution-transcript): state-linked voting qualifications.
- [New Jersey historical source](https://www.nj.gov/state/historical/assets/pdf/it-happened-here/ihhnj-er-petticoat-politicians.pdf): founding-era voting exception.
- [Investigating History, grade 3 unit 2](https://www.doe.mass.edu/investigatinghistory/curriculum/units.aspx?grade=3&unit=2): reference comparison of historical sequence and perspectives.
- [Leadership and Government inquiry](https://c3teachers.org/inquiries/leadership-and-government/): reference comparison of question, evidence and argument structure.
- The five nations’ own sources linked in finding 4: starting sources for worked-case selection.

**For the source list:** add the constitutional and New Jersey sources, the accessible curriculum routes, and the five nation-specific routes with their limited uses. The attempted Acoma website was inaccessible. No paywalled material was used.

**Verdict:** revise before course writing. **Finding count:** 12. **Intended report path:** `docs/reviews/frame-social-studies-grade-3-2026-11-13.md`, delivered here only.
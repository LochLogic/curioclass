# Independent cold read: social studies progression

**Reviewer:** Codex  
**Date:** 2026-11-13  
**Intended report path:** `docs/reviews/progression-social-studies-codex-2026-11-13.md`  
**Delivery:** Complete report below. No report file was created.

## Verdict

The progression has a defensible content sequence and substantial strengths, but it is not ready to guide course writing unchanged. Its biggest risk is apparent completeness: every loaded standard has a recorded disposition, while several C3 mappings and bundled content rows leave required work unspecified. Correct the semantic coverage and prerequisite records before treating the structural pass as evidence that the progression is complete.

## What I read and checked

I read all **384 progression rows**, including their notes, and all **10 exclusion rows**. I did not read the band drafts or anything under `data/progressions/parts/`.

The governing material read included:

- `docs/agents/EXPERT.md`
- `docs/agents/lenses/social-studies.md`
- `docs/FOUNDATION.md`
- The relevant path, layers and gaps in `docs/ROADMAP.md`
- BASELINE rules 20 to 24
- The shared core and social studies section of `docs/ADOPTION-BAR-SUBJECTS.md`
- `docs/courses/social-studies/STANDARD.md`
- `docs/courses/social-studies/grade-3-outline.md`
- `docs/APPROACH.md`, its evidence notes in `docs/APPROACH-SOURCES.md`, and `docs/sources/BASE-TEXTS.md`
- The loaded Massachusetts, C3 and relevant cross-subject standards files
- `scripts/progression.py`, including what its checks actually establish

For earlier findings, I read the social studies content-standard and expert reports, the open-material report, the earlier math progression review, and the relevant adoption-bar reviews.

Outside checking included the official [C3 Framework](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf), its indicator tables on printed pages 23 to 24, 31 to 48, 53 to 54 and 59 to 61, and targeted pages of the official [Massachusetts framework](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf). I also checked the sources linked below.

### Gate result

The requested `python -X utf8 scripts/plan.py check` stopped before printing progression results:

```text
ModuleNotFoundError: No module named 'markdown'
```

The bundled Python produced the same dependency error. I installed nothing.

The separate read-only progression check completed:

```text
progression social-studies: 384 rows, 0 failure(s)
```

That check reported repeated C3 indicators, skipped-grade handoffs and grade counts. It establishes structural consistency, not semantic alignment.

### Coverage inventory

| Check | Result |
|---|---:|
| Progression rows | 384 |
| Unique C3 indicators named | 283 |
| C3 assignments across rows | 324 |
| Rows carrying C3 indicators | 184 |
| Massachusetts standards and lettered parts, excluding headings | 880 |
| Named directly | 704 |
| Covered structurally through a named parent | 166 |
| Explicit exclusions | 10 |
| Unexplained unnamed Massachusetts codes | 0 |
| Skills with no standard named | 0 |
| Reciprocal handoff edges | 356 |
| Adjacent-grade edges | 249 |
| Edges skipping at least one grade | 107 |
| Cross-subject references | 146 |

The ten exclusions are explicit: nine dispose of the shared grade 1 and 2 economics topic, and one moves the grade 3 Revolution-events content to grade 5. Their educational acceptability is addressed under “For Cory.”

There is **no adopted whole-course social studies base text** whose sequence must be preserved. At the time of this read, candidate partial bases had not been loaded; later loading is recorded in docs/sources/BASE-TEXTS.md. Base-text ordering is therefore not applicable to this file; the Massachusetts content order is the relevant sequence check.

## Findings, most serious first

### 1. C3 code presence overstates the work actually specified

**LAYER:** progression and standard  
**REPEAT:** yes, the same kind of standard-to-task mismatch identified in the earlier math progression review  
**Confidence:** firm for direct mismatches; likely where an omitted requirement could otherwise be supplied during course planning

All 283 indicators are named, but naming them does not establish that their distinct requirements are taught. The table below identifies mappings that remain unsecured under a literal cold read. These include incomplete claims as well as outright task mismatches.

I accepted explicitly staged introductions where a later row completes the indicator, such as grade 3 sequencing followed by grade 4 simultaneous developments. I did not count such deliberate staging as duplicate ownership.

**Evidence:** the progression notes compared with the official [C3 indicator tables](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf).

In this table, code suffixes retain their current grade band. “Add” means add explicit student work to `notes`, not merely another vocabulary word.

| Skill id | Unsecured code | Exact repair direction |
|---|---|---|
| `ss1-supporting-questions` | `D1.3.K-2` | Associate facts and concepts with each supporting question. |
| `ss1-community-problems` | `D4.6.K-2; D4.7.K-2` | Extend the exclusively local examples to regional and global problems. |
| `ss2-climate-regions` | `D2.Geo.10.K-2` | Compare a region at two dates. |
| `ss2-country-report` | `D4.3.K-2` | Present an argument, not only collected facts. |
| `ss3-levels-of-government` | `D2.Civ.1.3-5` | Complete branch responsibilities in `ss5-constitution`; record the staged depth. |
| `ss3-state-constitution` | `D2.Civ.5.3-5` | Complete the comparison of governmental systems, origins and functions. |
| `ss3-money-saving` | `D2.Eco.9.3-5; D2.Eco.10.3-5` | Include nonbank institutions and explain interest rates. |
| `ss3-inquiry-questions` | `D1.2.3-5; D1.3.3-5` | Identify competing interpretations, not just question types. |
| `ss4-map-scale` | `D2.Geo.3.3-5` | Compare maps at different scales. |
| `ss4-canada-mexico-research` | `D1.5.3-5; D3.1.3-5` | Make viewpoints and source context selection criteria. |
| `ss4-primary-source` | `D2.His.9.3-5` | Explain how different source kinds support historical accounts. |
| `ss4-disasters-response` | `D2.Civ.13.3-5` | Trace policy development, not just a response. |
| `ss5-independence-war` | `D2.Eco.11.3-5` | Add deflation and unemployment alongside inflation. |
| `ss5-abolition` | `D2.Civ.14.3-5` | Connect historical tactics with contemporary methods. |
| `ss5-civil-rights-research` | `D1.2.3-5; D1.3.3-5; D1.5.3-5` | Specify interpretive alternatives and viewpoint-aware source selection. |
| `ss6-social-science-lenses` | `D1.1.6-8` | Require explanations for the question classifications. |
| `ss6-changing-interpretations` | `D1.2.6-8` | Identify expert agreement as well as disagreement. |
| `ss6-phoenician-trade` | `D2.Eco.3.6-8` | Complete labor and financial markets beyond goods. |
| `ss6-writing-systems` | `D2.Geo.7.6-8` | Compare connections before and after technological change. |
| `ss6-research-contribution` | `D1.3.6-8; D1.4.6-8; D1.5.6-8; D3.1.6-8` | Add expert agreement, reciprocal question revision and fuller source-selection checks. |
| `ss6-africa-geography` | `D2.Geo.3.6-8` | Produce and analyze electronic representations; comparison of existing maps is insufficient. |
| `ss7-indus-valley` | `D2.His.11.6-8` | Infer audience and origin, not merely maker/date/use. |
| `ss7-south-asia-geo` | `D2.Geo.12.6-8` | Connect local land-use change to wider population redistribution. |
| `ss7-silk-road-trade` | `D2.Eco.4.6-8; D2.Eco.6.6-8` | Complete wages, labor, credit and currency applications. |
| `ss7-roman-economy` | `D2.Eco.12.6-8` | Include deflation and unemployment effects. |
| `ss8-state-local-government` | `D2.Civ.11.6-8` | Compare procedures through their civic purposes. |
| `ss8-public-budget` | `D2.Eco.8.6-8; D2.Eco.11.6-8` | Show spillovers changing market outcomes; complete the indicator data set. |
| `ss8-civic-action` | `D2.Civ.9.6-8` | Compare deliberative processes, rather than only using one. |
| `wh1-sources-of-the-past` | `D3.1.9-12` | Explicitly assess authority, structure, context and corroborative value. |
| `wh1-graphic-displays` | `D2.Geo.1.9-12` | Include actual geospatial technology use. |
| `wh1-atlantic-slave-trade` | `D2.His.8.9-12` | Test a current interpretation against the surviving record. |
| `wh2-contested-questions` | `D1.3.9-12` | Apply expert agreement/disagreement to supporting questions too. |
| `wh2-postwar-world` | `D2.Geo.5.9-12` | Evaluate resulting cultural or environmental changes beyond borders. |
| `wh2-decolonization` | `D2.Civ.14.9-12` | Include contemporary and emerging methods of change. |
| `wh2-research-argument` | `D4.5.9-12` | Add a distinct explanation critique. |
| `us1-research-inquiry` | `D3.1.9-12` | Complete the source-selection checks noted for grade 9. |
| `us2-research-paper` | `D4.3.9-12` | Specify an audience outside the classroom. |
| `gov-federalism` | `D2.Civ.1.9-12` | Complete international institutions in `gov-international-orgs`. |
| `gov-ideals-gap` | `D2.Civ.9.9-12` | Record application in multiple settings. |
| `gov-checks-balances` | `D2.Civ.11.9-12` | Evaluate decision procedures across governmental levels. |
| `gov-local-action` | `D4.8.9-12` | Require a completed, student-chosen civic action. |
| `econ-market-structures` | `D2.Eco.4.9-12` | Include competition among buyers. |

**Why it matters:** these rows can produce lessons on the right general topic while leaving the actual indicator untaught. Economics is particularly vulnerable: a historical trade example does not automatically carry every market named by its attached indicator.

**Fix:** retain a code only when its work is explicit in this row or in a clearly named completion row. Add own-word indicator descriptions and page pointers to the standards record so future writers do not reconstruct meanings from codes. Changes that add content or move a completion grade go to Cory.

### 2. Bundled Massachusetts codes conceal partially specified content

**LAYER:** progression  
**REPEAT:** yes, omitted requirements inside a claimed standard recur in the earlier math progression review  
**Confidence:** firm on the requirements; likely on the resulting instructional omission

The structural coverage count is correct. The following content is nevertheless not secure enough to build from. The official [Massachusetts framework](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf), particularly pages 33, 72 to 74 and 86, distinguishes these requirements.

| Skill id | What is missing or blurred | Exact row repair |
|---|---|---|
| `ssk-national-symbols` | Stars and stripes are explained, but the remaining historical “why” questions are largely replaced by identification. | Add explicit investigations of the flag’s colors, the eagle’s selection and the anthem’s selection. Distinguish documented history from later symbolism. |
| `ss5-slavery-colonies` | “Lives,” “skills” and “ways people resisted” do not preserve all of `MA.5.T1.7a-d`. | Explicitly compare free and enslaved people’s legal, living and working conditions; name family separation, educational restrictions, hiring out, routes to freedom and free people’s property and employment rights. |
| `ss5-revolution-causes` | Women’s work is narrowed to boycotts and writing. | Add managing farms and businesses, fundraising and support for the army to the treatment of `MA.5.T2.1d`. |
| `ss5-independence-war` | The named events in `MA.5.T2.5a-c` become generic “later battles.” | Name Trenton, Saratoga, Valley Forge and Yorktown in `notes`, with location and significance. |
| `ss6-timeline-deep-time` | `MA.6.T2.1` becomes the end of the last Ice Age and conditions for farming. That is narrower than the environmental history associated with human life. | Separate the geological/environmental overview from the later warming and farming transition. Retain both standards, with distinct objectives. |
| `us2-economy-government` | The Federal Reserve’s creation and tools appear, but its organization is not specified. | Add the institutional organization required by `MA.USII.T1.7`, alongside its functions and historical creation. |

**Why it matters:** a parent code silently satisfies its children in the checker. Writers need a visible statement of what the bundle includes.

**Fix:** make the additions above to `notes`; do not add more parent codes as a substitute. For large bundles, enumerate required components separately from optional case choices.

### 3. The file narrows Government and Economics to grade 12 without a matching scope decision

**LAYER:** progression and process  
**REPEAT:** new  
**Confidence:** firm about the written discrepancy

`STANDARD.md` places Government and Economics in **grades 11 to 12**. All 44 progression rows for those courses are owned by grade 12, and numerous notes explicitly declare them grade 12 courses.

Their prerequisites also include grade 11 work, for example:

- `gov-founding-documents` assumes `us1-declaration` and `us1-articles-constitution`.
- `gov-civic-associations` assumes `us1-reform-movements`.
- `econ-business-forms` and `econ-market-structures` assume `us1-industrialization`.
- `econ-government-role` assumes `us1-progressivism`.

**Why it matters:** a teacher choosing either half-year course in grade 11 cannot satisfy the progression as written. This is an access and scheduling decision, not a harmless endpoint label.

**Exact fix, after Cory’s choice:**

- If grade 12 is mandatory, revise the course placement in `STANDARD.md` and the course record.
- If either grade remains available, document entry requirements independent of completing US History I, teach or reactivate the necessary historical examples inside the half-year course, and remove grade 11 completion as a mandatory prerequisite.

Do not change grades or prerequisite policy silently.

### 4. Annual informed action is absent from several courses

**LAYER:** progression  
**REPEAT:** yes, `bar-subjects-2026-11-11.md`, finding 4  
**Confidence:** firm

The subject bar requires informed action once per course per year. Explicit annual cycles appear in grades 3, 5 and 8, World History II and Government. Comparable commitments are missing from:

- Grade 2
- Grade 4
- Grade 6
- Grade 7
- World History I
- US History I
- US History II
- Economics

Grade 1 already includes a real election; connect it explicitly to inquiry and the class’s chosen problem. Kindergarten’s real collective decision is a reasonable age-level starting point.

`ss4-disasters-response` studies what other people did. `us2-research-paper` communicates research. Neither automatically establishes the required application to a real problem. Similarly, `gov-local-action` must distinguish identifying possible participation from completing a chosen action.

**Why it matters:** action disappears for whole courses, and `ss8-civic-action` then assumes a cycle last explicitly taught in grade 5. The external [EdReports and AIR criteria](https://air.org/sites/default/files/2024-01/23-23505_HQIM_for_SS_Final.pdf) also distinguish studying sources and conclusions from applying them.

**Fix:** add one small annual cycle to each missing course, using existing content. Examples include a local history interpretation proposal, a source-based public information display, or a consumer information project. Students choose the issue and response. A safe public explanation can provide a participation route without requiring political advocacy.

These additions change course requirements and need Cory’s approval.

### 5. The handoff graph records long returns as though they were maintained prerequisites

**LAYER:** progression  
**REPEAT:** yes, the earlier math progression review identified unsupported prerequisite claims  
**Confidence:** firm on the gaps; judgment call on which content returns need annual maintenance

There are **107 skipped-grade edges**:

| Grades skipped | Edges |
|---|---:|
| 1 | 52 |
| 2 | 25 |
| 3 | 20 |
| 5 | 10 |

The notes usually explain why the topic disappears. That is useful, but “the intervening courses teach something else” does not establish that students retain the prerequisite.

No edge points backward to a skill taught later. The problem is maintenance and the meaning of the relationship.

Some edges also name related content where the actual prerequisite is a different skill:

| Current edge | Problem | Exact repair |
|---|---|---|
| `ss6-ancient-israel` → `ss7-hinduism-caste` | Studying ancient Israel is not the prerequisite for continuity/change reasoning about Hinduism and caste. | Use `ss6-paleolithic-neolithic` for the continuity/change skill; retain the religion comparison in notes. Update both reciprocal cells. |
| `ss5-native-sovereignty-removal` → `ss6-caribbean-peoples` | Removal history is not required for explaining Caribbean peoples’ identities and environments. | Remove the mandatory edge. Name the actual geography and source-use prerequisites, with an explicit current-nations introduction. |
| `ss7-time-zones` → `wh1-empires-1600s` | Calculating time offsets does not prepare students to interpret imperial maps. | Use a map-analysis prerequisite; retain time-zone knowledge only if a task actually needs it. |
| `wh1-english-exception` → `wh2-wwi-causes` | Britain’s constitutional history is an indirect topical connection. | Use `wh1-black-death` for the explicitly taught multicausal explanation skill. Teach Britain’s alliance context in grade 10. |

**Fix for all skipped edges:** distinguish three relationships.

1. **Maintained skill:** provide adjacent-grade application and handoff.
2. **Historical content revisited later:** record the return in `notes`; reactivate it before use.
3. **Necessary but dormant knowledge:** provide a readiness check and a named reteach before dependent work.

Do not repair the graph by teaching US history every year or by inserting empty carry rows. The complete skipped-edge inventory appears in Appendix A.

### 6. Cross-subject codes are valid identifiers, but ownership and several task matches remain unverified

**LAYER:** progression and process  
**REPEAT:** yes, the earlier math progression review found prerequisites attached to standards that did not teach them  
**Confidence:** firm on the examples below; unresolved on actual cross-subject scheduling

All **146 references** pass identifier checking. However, the other subject progression files are absent, so these references cannot yet identify a verified owning skill and its teaching position.

Update, 2026-11-13: the other three progression files now exist. Subsequent cross-subject reviews and their fix report address ownership and readiness; teaching order within a year remains a frame check.

Specific repairs are already possible:

| Social studies skill | Current dependency | Problem and exact fix |
|---|---|---|
| `ss6-mena-settlement` | `math:6.SP.B.4` | Climate graphs and relationships between variables are not the same as displaying one-variable distributions. Use the applicable relationship/graph skill, such as `6.EE.C.9`, and state the graph form taught locally. |
| `wh1-graphic-displays` | `math:6.SP.B.4` | Categorical comparison bars do not become histograms or box plots. Cite `3.MD.B.3` for scaled category bars; retain `6.SP.B.4` only for an actual distribution task. |
| `wh1-sources-and-interpretations` | `ela:RI.9-10.9` | The example concerns Mansa Musa, while this code concerns seminal US documents. Replace it with the relevant source-comparison or viewpoint skill, for example `RI.9-10.6` for the stated viewpoint work. |
| `us2-civil-rights-laws` | `math:S-ID.A.2` | Trends, percentages and maps do not necessarily compare distribution centers and spreads. Use `8.F.B.5` and `7.RP.A.3` for the described work, or add an actual center-and-spread comparison. |

The middle-school and high-school science references need special attention. A band-level code does not establish teaching by grade 6, 7 or 9. Examples include `ss6-changing-interpretations`, `ss6-timeline-deep-time`, `ss7-south-asia-geo` and `wh1-scientific-revolution`.

**Why it matters:** a valid code can hide an unavailable prerequisite. The plan checker checks existence, not the match between the code’s task and the lesson’s demand.

**Fix:** make the four corrections above now. When the other progressions exist, replace or supplement standard references with owning skill ids, verify grade and within-year order, and teach missing prerequisites locally until that verification is complete.

### 7. Model continuity is not established, and different models share names

**LAYER:** progression  
**REPEAT:** new  
**Confidence:** firm

The checker permits a model to reappear after any number of missing grades. The brief requires a continuous account.

| Model | Recorded gaps before reuse |
|---|---|
| `budget` | Grade 2; grades 4 to 6; grades 9 to 11 |
| `opportunity-cost` | Grades 9 to 11 |
| `supply-demand` | Grades 8 and 11 |
| `corroboration` | Grade 4 |
| `map-scale` | Grade 8 |
| `latitude-longitude` | Grade 8 |
| `region` | Grade 8 |
| `branches-of-government` | Grades 6 and 10 |
| `map-key` | Grade 5, then grades 7 and 8 before grade 9 |
| `compass-directions` | Grade 5 before grade 6 |

Some gaps are missing metadata rather than missing teaching. For example, `ss4-canada-mexico-research` already has multiple-source work that could carry corroboration, and grade 5 clearly uses maps.

There are also three definition problems:

- `econ-macro-measures` outputs `circular-flow`, but its notes do not actually teach that diagram.
- `econ-business-cycles` carries `supply-demand` into aggregate supply and demand. The aggregate model needs its own identity, axes and limits.
- `ss6-paleolithic-neolithic` says it introduces continuity/change, although that model begins in kindergarten. Similar “introduced here” language recurs for models already introduced earlier.

**Why it matters:** writers can either assume an absent model or mistake a new diagram for a familiar one.

**Exact fixes:**

- Add actual annual applications to the relevant `model_in` and `model_out` cells where the work already exists.
- Where it does not exist, specify reactivation or propose a real carry task.
- Give aggregate supply and demand a distinct model token.
- Either explicitly teach circular flow or remove the unsupported output.
- Replace false first-introduction claims with “reintroduced for this course.”
- Add a grade-by-grade model audit to the checker’s notes.

### 8. The grade 3 primary-source definition contradicts earlier interviews

**LAYER:** progression  
**REPEAT:** new  
**Confidence:** firm

`ss3-primary-secondary` defines a primary source as made at the time by somebody who was there, and a secondary source as made later by somebody studying it.

That makes the grade 2 retrospective interviews difficult to classify correctly. Later memoirs and oral histories can be primary sources. Date alone does not determine source type. The [Library of Congress explanation](https://ask.loc.gov/faq/303148) explicitly includes later-recorded firsthand accounts.

**Why it matters:** this distinction feeds every later history course. Students could wrongly reject testimony because it was recorded years afterward.

**Exact replacement for the definition in `notes`:**

> A primary source provides original evidence for the question being studied, such as an object, record or firsthand account. An eyewitness interview or memoir can be recorded later. A secondary source interprets or explains evidence from other sources. Ask how the source relates to this question, then consider its date, purpose and limitations.

Include the earlier interview as one classification example. Keep the vocabulary age appropriate through concrete examples.

Also qualify `ss2-two-accounts`: agreement increases confidence only after checking whether the accounts are independent and whether their evidence supports that agreement.

### 9. The grade 6 timeline analogy introduces a nonexistent historical year zero

**LAYER:** progression  
**REPEAT:** new  
**Confidence:** firm

`ss6-timeline-deep-time` explains BCE ordering as counting back from a zero point, like negative numbers. Used literally, that teaches the wrong boundary convention.

Historical BCE/CE numbering passes from 1 BCE to 1 CE without a year zero. The [US Naval Observatory](https://aa.usno.navy.mil/faq/millennium) distinguishes this convention from astronomical numbering.

**Why it matters:** students can order dates correctly but calculate cross-boundary intervals incorrectly.

**Exact replacement:**

> BCE years count down toward 1 BCE; the next year is 1 CE. There is no historical year zero. Signed number lines help explain ordering, but their labels do not transfer directly to BCE/CE dates.

Show `3 BCE, 2 BCE, 1 BCE, 1 CE, 2 CE`. Preserve the long-strip and zoomed-strip representation.

## Pace and strand continuity

| Grade | Civics | Economics | Geography | History | Inquiry | Total |
|---|---:|---:|---:|---:|---:|---:|
| K | 6 | 3 | 4 | 4 | 2 | 19 |
| 1 | 7 | 4 | 4 | 3 | 3 | 21 |
| 2 | 1 | 3 | 7 | 4 | 3 | 18 |
| 3 | 7 | 5 | 4 | 8 | 3 | 27 |
| 4 | 1 | 1 | 7 | 6 | 2 | 17 |
| 5 | 5 | 1 | 1 | 12 | 2 | 21 |
| 6 | 0 | 2 | 6 | 17 | 4 | 29 |
| 7 | 1 | 2 | 5 | 20 | 1 | 29 |
| 8 | 19 | 1 | 0 | 3 | 4 | 27 |
| 9 | 3 | 2 | 3 | 24 | 5 | 37 |
| 10 | 2 | 4 | 1 | 33 | 3 | 43 |
| 11 | 0 | 1 | 0 | 22 | 4 | 27 |
| 12, combined | 19 | 27 | 0 | 22 | 1 | 69 |

Three comparisons need attention during course framing:

- Grade 3 has **27 rows**, against **18** in grade 2 and **17** in grade 4. Its seven units and recurring threads require deliberate time allocation.
- Grade 10 has **43 rows**, against **37** in grade 9 and **27** in grade 11. Several grade 10 rows already contain substantial surveys and an in-depth case.
- Grade 12’s **69** is three courses: **25 US History II, 19 Government and 25 Economics**. It is not a valid single-course overload comparison. Economics nevertheless packs 25 substantial rows into a half year.

Economics appears every grade. Civics has no strand-owned row in grades 6 or 11, although governmental content appears inside history. Geography has no strand-owned row in grades 8, 11 or 12, although map work continues.

These labels alone do not prove instructional gaps. The model and handoff gaps above identify where continuity is actually unsecured. Row counts cannot establish feasibility without days and minutes.

## Words and reading level

The planned vocabulary generally grows sensibly: oral explanations and familiar examples in K to 2, named disciplinary language in grades 3 to 5, then technical analysis.

Two implementation choices should be explicit:

- `ss7-rome-fall` lists **counterclaim** before grade 8 formally develops the skill. Introduce the word and a simple response frame in that grade 7 row; do not assume students already know it.
- `econ-price-controls` requires marginal reasoning. Define **marginal benefit** alongside **marginal cost** before the argument task.

The word lists are not student texts. Actual reading-level fit, vocabulary support and source accessibility remain unjudged until excerpts and tasks exist. That is a limit of this layer, not evidence that the texts will fail.

## Progression lens checklist

| Checklist line | Status | Reason |
|---|---|---|
| C3 skills have identifiable ownership and distinct depth | **Missed** | All codes appear, but finding 1 identifies incomplete mappings. Several staged repetitions are sound. |
| Every assumed skill is taught and handed forward | **Missed** | No backward-time references; 107 skips and several weak prerequisite choices remain. |
| Chronology continues across grades, with reasons for departures | **Met** | Grade 7 to grade 9 resumes around 500. The grade 8 civics interruption and regional departures are explained. |
| Geography and economics develop as reasoning | **Missed** | Strong overall intent, but missing market applications and model continuity prevent a clean pass. |
| Base-text order is preserved | **Not applicable** | No whole-course base text is adopted. |
| Course-frame, unit and day checklist lines | **Not applicable** | Those artifacts are outside this progression read. |

## Settled by the expert

These are item-level corrections within the stated scope. They are recommendations for the caller to apply, not edits made during this read.

| Choice | Reason | File touched |
|---|---|---|
| Use original evidence and relation to the question to distinguish primary from secondary sources | Preserves oral histories and avoids a false date rule | `data/progressions/social-studies.csv`, `ss3-primary-secondary` |
| Explicitly teach the absence of year zero | Prevents an inaccurate number-line transfer | Same file, `ss6-timeline-deep-time` |
| Distinguish aggregate supply/demand from product-market supply/demand | Different models need different axes and limits | Same file, Economics model cells |
| Correct the four cross-subject task mappings in finding 6 | Existing codes do not match the described work | Same file, named rows |
| Teach “counterclaim” when first listed in grade 7 | A word list should not become an assumed prerequisite | Same file, `ss7-rome-fall` |
| Define marginal benefit before the price-control argument | Completes the language already required by the task | Same file, `econ-price-controls` |
| Describe grade 2 map scale with repeated whole units; distinguish this from later measurement sophistication | Keeps the early representation concrete and removes the apparent grade 3 retreat | Same file, `ss2-make-map`, `ss3-map-skills`, `ss4-map-scale` |
| Qualify agreement between sources with an independence check | Agreement alone can repeat one mistaken account | Same file, `ss2-two-accounts` |

## For Cory

The eight questions raised by the writers:

| Question | My recommendation |
|---|---|
| Split the shared K to 2 economics topic once between grades 1 and 2 | **Agree.** The anchor permits sharing. Keep the exclusions, but maintain choice and saving through application in grade 2. |
| Teach “your own state” in K to 2, grade 8 and Government | **Agree.** Supply worked examples and usable official-source routes. A national course must not leave the teacher to invent the state component. |
| Teach grade 9 and 10 “one example” standards through a survey plus one in depth | **Agree conditionally.** A brief orientation is useful; the options must not become compulsory equal-depth mini-units. Provide a one-child route that does not depend on classmates studying the other options. |
| Grade 10 genocide anchor case | **No fixed anchor is actually selected in the row.** Recommend the 1994 genocide against the Tutsi in Rwanda as the default, with a supported alternative. The [Holocaust Museum account](https://encyclopedia.ushmm.org/content/en/article/the-rwanda-genocide) provides a clear starting source. Do not treat every conflict in the option list as automatically interchangeable with genocide. |
| Place C3 economics in grades 3 to 8 inside history units | **Agree.** Historical contexts can carry the reasoning, but finding 1 shows where they currently omit parts of the indicators. Include present-day applications where required. |
| Add hard history in grades 4 and 5 | **Agree.** Much is already required by the anchor. Keep plain facts, human lives, resistance and age-suited sources. The required community and sensitivity reads remain necessary. |
| Teach Native nations as governments in grade 8 | **Agree.** Present-day governmental powers and sovereignty should accompany the historical influence inquiry. Preserve the distinction between examining influence evidence and teaching current governments. |
| Teach economics in both US History II and Economics | **Agree.** US History II needs a self-contained toolkit. Economics should deepen it rather than depend on taking the history course first. |

Additional decisions:

- Resolve Government and Economics placement: grade 12 only, or available in either grade 11 or 12.
- Approve the additional C3 work and annual action commitments before they change course scope.
- Set the time budget for grade 3, grade 10 and half-year Economics before approving their course frames.
- Arrange the required qualified community readers. No outreach or spending was undertaken.

## What is right and should not be undone

- The broad content order follows the selected anchor.
- Grade 7 to grade 9 chronology is connected explicitly.
- The grade 3 replacement preserves preparation for later colonial history.
- Native nations appear as living peoples and governments.
- Hard-history notes repeatedly prohibit harmful simulations and protect students’ private family information.
- Many C3 repetitions explain how independence or depth increases.
- News and media literacy has explicit high-school placement.
- The exclusions expose deliberate substitutions instead of hiding missing codes.

The treatment of testimony, human lives and simulations is consistent with the [Holocaust Museum’s teaching guidance](https://www.ushmm.org/teach/fundamentals/guidelines-for-teaching-the-holocaust). This is support for those design choices, not a substitute for the required course reads.

## What I could not judge

- A complete `plan.py check` result, because of the missing dependency.
- Actual cross-subject ownership and within-year availability until the other progressions exist. (Resolved in progression-cross-fixes-2026-11-13.md: the other progressions exist and cross-subject ownership checks were applied. Within-year availability still needs the course frames.)
- Daily reading load, source accessibility, assessment depth or teaching time.
- Final historical accuracy and sensitivity of excerpts not yet selected.
- A whole-course comparison with candidate partial bases that have not been adopted.
- Full external curriculum benchmarking. I inspected the [New York grade 3 inquiry’s opening plan](https://c3teachers.org/wp-content/uploads/2024/04/NewYork_3_Leadership_Government.pdf) and the [Reading Like a Historian curriculum description](https://www.inquirygroup.org/history-lessons). These support comparison of inquiry structures, not a claim that their complete sequences were audited. The Massachusetts Investigating History web routes attempted were inaccessible.

No material finding rests solely on remembered factual claims. Age suitability, workload concerns and proposed repairs include professional judgment and are identified accordingly.

## Sources and source-list additions

- [C3 Framework](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf): indicator meanings and band endpoints.
- [Massachusetts 2018 framework](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf): course order, shared economics and required content components.
- [EdReports and AIR social studies criteria](https://air.org/sites/default/files/2024-01/23-23505_HQIM_for_SS_Final.pdf): coherent sequencing, disciplinary work, action and feasibility.
- [Library of Congress primary-source explanation](https://ask.loc.gov/faq/303148): later-recorded firsthand evidence.
- [US Naval Observatory calendar explanation](https://aa.usno.navy.mil/faq/millennium): historical year numbering.
- [Holocaust Museum teaching guidance](https://www.ushmm.org/teach/fundamentals/guidelines-for-teaching-the-holocaust): source care, human context and responsible methods.
- [Holocaust Museum Rwanda account](https://encyclopedia.ushmm.org/content/en/article/the-rwanda-genocide): proposed default case.
- [New York grade 3 inquiry](https://c3teachers.org/wp-content/uploads/2024/04/NewYork_3_Leadership_Government.pdf): limited inquiry-plan comparison.
- [Reading Like a Historian description](https://www.inquirygroup.org/history-lessons): limited disciplinary-routine comparison.

**For the source list:** add the Library of Congress, US Naval Observatory and Rwanda sources, with the uses above. Preserve the access limitation on Investigating History.

## Appendix A: complete skipped-grade handoff inventory

Each arrow below is a finding under finding 5. Every listed relationship needs classification as maintained skill, content return or dormant prerequisite.

| Source grade and skill | Later targets |
|---|---|
| 1: `ss1-leaders` | `ss3-biography` |
| 1: `ss1-voting` | `ss3-taking-part` |
| 1: `ss1-elected-leaders` | `ss3-levels-of-government` |
| 1: `ss1-citizens` | `ss3-rules-rights` |
| 1: `ss1-national-symbols` | `ss3-founding-ideas` |
| 1: `ss1-choices` | `ss3-scarcity-choice` |
| 1: `ss1-saving` | `ss3-money-saving` |
| 1: `ss1-community-problems` | `ss3-deliberation`; `ss3-informed-action` |
| 3: `ss3-levels-of-government` | `ss5-constitution` |
| 3: `ss3-founding-ideas` | `ss5-independence-war`; `ss5-constitution` |
| 4: `ss4-first-peoples-evidence` | `ss6-paleolithic-neolithic` |
| 5: `ss5-slavery-colonies` | `wh1-atlantic-slave-trade` |
| 5: `ss5-revolution-causes` | `ss8-declaration`; `us1-revolution-causes` |
| 5: `ss5-independence-war` | `ss8-declaration` |
| 5: `ss5-constitution` | `ss7-roman-republic`; `ss8-constitution-text`; `ss8-articles-convention`; `ss8-federal-state-powers`; `ss8-state-local-government` |
| 5: `ss5-first-presidents` | `us1-early-republic` |
| 5: `ss5-republic-growth` | `us1-westward-expansion` |
| 5: `ss5-native-sovereignty-removal` | `us1-jackson-removal`; `us1-native-west` |
| 5: `ss5-abolition` | `us1-reform-movements` |
| 5: `ss5-civil-war` | `us1-civil-war` |
| 5: `ss5-reconstruction-amendments` | `ss8-amendments-civil-war` |
| 5: `ss5-womens-suffrage` | `us1-women-work-suffrage` |
| 5: `ss5-jim-crow` | `us1-jim-crow`; `us1-civil-rights-1900s` |
| 5: `ss5-civil-rights-movements` | `ss8-civil-rights-laws` |
| 5: `ss5-informed-action` | `ss8-civic-action` |
| 6: `ss6-ancient-israel` | `wh1-belief-systems` |
| 6: `ss6-christianity-origins` | `wh1-belief-systems`; `wh1-reformations` |
| 6: `ss6-islam-origins` | `wh1-religions-spread` |
| 6: `ss6-axum-swahili` | `wh1-african-kingdoms` |
| 6: `ss6-west-africa-trade` | `wh1-african-kingdoms` |
| 6: `ss6-caribbean-peoples` | `wh1-colonial-americas` |
| 6: `ss6-maya-andes-research` | `wh1-american-empires` |
| 7: `ss7-hinduism-caste` | `wh1-belief-systems` |
| 7: `ss7-silk-road-trade` | `wh1-farming-and-cotton`; `wh1-silk-roads-mongols`; `wh1-dutch-trade` |
| 7: `ss7-comparing-societies` | `wh1-graphic-displays` |
| 7: `ss7-shang-zhou-confucius` | `wh1-belief-systems` |
| 7: `ss7-buddhism-east-asia` | `wh1-religions-spread`; `wh1-song-kamakura` |
| 7: `ss7-europe-geo` | `wh1-geography-shapes-contact` |
| 7: `ss7-time-zones` | `wh1-empires-1600s` |
| 7: `ss7-roman-slavery-class` | `wh1-slavery-across-world` |
| 7: `ss7-rome-fall` | `wh1-ways-societies-interact`; `wh1-european-kingdoms`; `wh1-empire-power-culture` |
| 7: `ss7-ideas-spread` | `wh1-classical-learning` |
| 8: `ss8-greek-roman-roots` | `gov-foundations` |
| 8: `ss8-declaration` | `us1-declaration` |
| 8: `ss8-articles-convention` | `us1-articles-constitution` |
| 8: `ss8-ratification-debate` | `us1-articles-constitution` |
| 8: `ss8-three-branches` | `gov-executive`; `gov-checks-balances` |
| 8: `ss8-courts-review` | `gov-courts`; `us1-early-republic` |
| 8: `ss8-elections-parties` | `gov-parties-elections` |
| 8: `ss8-election-info` | `gov-policy-news` |
| 8: `ss8-citizenship` | `gov-foundations` |
| 8: `ss8-protest-change` | `us2-social-movements` |
| 8: `ss8-interest-groups-policy` | `gov-interest-groups` |
| 8: `ss8-amendments-civil-war` | `us1-reconstruction` |
| 8: `ss8-civil-rights-laws` | `us2-civil-rights-laws` |
| 8: `ss8-federal-state-powers` | `gov-federalism` |
| 8: `ss8-state-rights-documents` | `gov-rights-cases` |
| 8: `ss8-state-local-government` | `gov-federalism` |
| 8: `ss8-public-budget` | `econ-taxes-budgets`; `econ-scarcity-choice`; `econ-earning-income`; `us2-econ-toolkit` |
| 8: `ss8-press-freedom` | `us1-press-history` |
| 8: `ss8-news-literacy` | `us1-news-reading` |
| 8: `ss8-editorial-analysis` | `gov-media-democracy` |
| 8: `ss8-civic-action` | `wh2-global-problems`; `gov-local-action` |
| 9: `wh1-renaissance` | `us1-revolution-war` |
| 9: `wh1-atlantic-slave-trade` | `us1-slavery-economy` |
| 9: `wh1-empires-1600s` | `us1-westward-expansion` |
| 9: `wh1-enlightenment` | `us1-declaration` |
| 9: `wh1-philosophies-of-government` | `gov-foundations` |
| 9: `wh1-constitutional-democracy` | `us1-articles-constitution` |
| 10: `wh2-great-depression` | `us2-depression` |
| 10: `wh2-totalitarian-regimes` | `us2-isolation-fascism` |
| 10: `wh2-road-to-war` | `us2-isolation-fascism` |
| 10: `wh2-wwii-war-and-diplomacy` | `us2-wwii-war` |
| 10: `wh2-holocaust` | `us2-holocaust-response` |
| 10: `wh2-atomic-bombs` | `us2-atomic-bomb` |
| 10: `wh2-wwii-consequences` | `gov-rights-cases`; `gov-international-orgs` |
| 10: `wh2-cold-war-blocs` | `us2-cold-war-origins` |
| 10: `wh2-cold-war-world` | `us2-vietnam` |
| 10: `wh2-decolonization` | `us2-social-movements` |
| 10: `wh2-soviet-collapse` | `us2-cold-war-end` |
| 10: `wh2-globalization` | `econ-global-economy`; `econ-trade` |
| 10: `wh2-middle-east-since-1980` | `gov-world-affairs` |
| 10: `wh2-global-problems` | `gov-local-action` |
| 10: `wh2-terrorism` | `us2-terrorism-response` |

**Verdict:** revise before course writing. **Finding count:** 9. **Intended report path:** `docs/reviews/progression-social-studies-codex-2026-11-13.md`, delivered here only.
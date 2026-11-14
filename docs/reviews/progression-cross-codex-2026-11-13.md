# Cross-subject progression review, 2026-11-13

The four progressions are broadly coherent, but their cross-subject leans are not yet a dependable statement of student readiness. The largest risk is that a writer treats a valid reference, a partial contribution or a generic scaffold as evidence that the required mathematics or science has already been taught. The most useful change is to replace the remaining future dependencies with precise earlier skills and explicit teaching inside the receiving row.

**Findings: 7.** Intended report path: `docs/reviews/progression-cross-2026-11-13.md`. This report is supplied here only; no repository file was created or changed.

## What I read and checked

| Progression file | Rows |
|---|---:|
| `data/progressions/social-studies.csv` | 384 |
| `data/progressions/science.csv` | 198 |
| `data/progressions/ela.csv` | 374 |
| `data/progressions/math.csv` | 305 |
| **Total** | **1,261** |

I compared the grades, standards, contributing rows, prerequisites, models, vocabulary, cross-subject references and instructional notes, concentrating detailed note checks on quantitative demands, literacy handoffs, knowledge topics and sensitive content.

Guidance consulted:

- `docs/agents/EXPERT.md` and all four subject lenses.
- `docs/FOUNDATION.md`, the relevant ROADMAP sections, `docs/GLOSSARY.md`, BASELINE rules 20 to 24, the shared approach and the math and ELA approaches.
- `docs/RUBRIC-MATH-K8.md`, `docs/ADOPTION-BAR-SUBJECTS.md` and `docs/APPROACH-SOURCES.md`.
- Relevant local standards text.
- The four subjects’ earlier expert and Codex reviews and their fix reports, with particular attention to deferred cross-subject checks. Settled single-subject findings are not reissued below.

**Gate result:** I ran the requested `python -X utf8 scripts/plan.py check`, with bytecode writing disabled. It stopped during import because the installed Python lacks `markdown`. The alternate Python launcher also failed to start. Consequently, this read does **not** establish a successful full plan check.

The progression check itself ran successfully twice: **1,261 rows, zero failures**. Its structural checks are therefore available for this review.

There are **487 cross-subject entries**: social studies 152, science 177, ELA 106 and math 52. Of these, 39 point to a standard whose formal owner is later than the receiving grade. Thirty-two have an earlier contributing row, which must be checked for the actual feature needed. Seven have no contribution at or before the receiving grade: six social studies science leans and the Chemistry pH lean.

All proposed replacement skill identifiers were checked for existence and placement at the receiving grade or earlier. No finding rests solely on memory. Suggested scaffolds and scheduling prescriptions are expert judgments, distinguished from source requirements below.

## Findings, most serious first

### 1. High school science still carries provisional mathematics contracts after the mathematics progression has been written

**Severity:** substantial planning risk  
**LAYER:** progression  
**REPEAT:** yes, follow-through on science Codex F8 and expert finding 12  
**Confidence:** firm on placements and stale wording; likely on the resulting instructional risk

**Rows and grades:** science `bio-population-carrying-capacity` and `bio-biodiversity-simulation`, grade 9; `chem-carbon-cycle-quantitative` and `chem-human-earth-systems`, grade 10. Relevant math includes `alg1-scatter-linear-models` and `alg1-quadratic-patterns`, grade 9; `geo-modeling-objects-density`, grade 10; `alg2-combining-functions-models` and `alg2-logarithms`, grade 11.

Twenty-nine science rows still say that their high school mathematics “is not yet placed in a Curio Class math course.” That is now false.

More consequentially, the earlier contributions do not automatically supply the needed depth:

- Grade 9 linear fitting does not establish independent fitting of a population curve that levels off or crashes.
- The grade 9 contribution to F-BF.A.1 concerns quadratic patterns. It does not establish a general method for constructing a multi-parameter ecological simulation.
- The Chemistry carbon-stock update needs explicitly taught quantities, units and an update rule, rather than an unexplained appeal to the whole F-BF.A.1 standard.
- `chem-human-earth-systems` points to logarithms in grade 11. Its generic scaffold does not specify how grade 10 students read pH.

Students should perform the science without having to infer an untaught mathematical method. NGSS specifically requires mathematics to remain consistent with its grade progression, and HS-ESS3-6 limits assessment to using published model results. [NGSS mathematics connections](https://www.nationalacademies.org/read/18290/chapter/18), [HS-ESS3-6](https://www.nextgenscience.org/pe/hs-ess3-6-earth-and-human-activity).

**Exact fixes in `data/progressions/science.csv`:**

First, in the **29 rows whose `notes` contain** `not yet placed in a Curio Class math course`, replace the entire provisional `Math readiness:` sentence with:

> Math readiness: Use the grade and explicitly taught features of the linked rows in math.csv. Check same-year mathematics before use, and supply a worked example and representation when that feature has not yet been taught. Later-grade mathematics is not an assumed prerequisite.

Then make these specific repairs:

| Row | `cross_subject`: new value | Append to `notes` |
|---|---|---|
| `bio-population-carrying-capacity` | `math:m8-scatter-plots (plot population data and compare it with a supplied model); math:alg1-writing-equations-constraints (name model quantities and units, taught locally if needed)` | `The population update rule is supplied and explained. Students change inputs and compare output with observations; independent fitting of a nonlinear population function is not required.` |
| `bio-biodiversity-simulation` | `math:m6-expressions-variables (evaluate supplied update rules); math:m7-percent-problems (interpret population and resource-use changes); math:m8-scatter-plots (compare simulation output with observations)` | `Teach the spreadsheet or program update explicitly. Students construct or revise the simulation using supplied scientific rules and then test its consequences. They do not independently derive a family of nonlinear functions.` |
| `chem-carbon-cycle-quantitative` | `math:geo-modeling-objects-density (choose and track units in stock and flow data); math:alg1-writing-equations-constraints (represent a stock update with named quantities)` | `Teach each update as new stock equals old stock plus inflow minus outflow over one stated interval. Distinguish the units of stocks from the units of flows. Supply the unit interpretation if the same-year Geometry work has not occurred.` |
| `chem-human-earth-systems` | `math:m8-integer-exponents (read supplied factor-of-ten comparisons on a pH table)` | `Teach the supplied pH scale here: lower pH means greater hydrogen-ion concentration, and a decrease of one whole pH unit corresponds to a factor of ten. Fractional-pH comparisons are supplied. Calculating logarithms is not required; alg2-logarithms develops that mathematics in grade 11.` |

The pH replacement preserves the scientific meaning without moving logarithm instruction into grade 10. [EPA explanation of pH](https://www.epa.gov/ocean-acidification/understanding-science-ocean-and-coastal-acidification).

### 2. Early middle school science uses mathematics that the math base text develops substantially later in the same year

**Severity:** substantial planning risk  
**LAYER:** base text  
**REPEAT:** yes, the readiness-scaffolding kind identified in science Codex F8; these are additional receiving rows  
**Confidence:** firm on source order; likely on the required amount of local teaching

**Rows and grades:**

- Science grade 6: `s6-insulator-design`, `s6-hazard-forecast`.
- Math grade 6: `m6-center-variability`, `m6-data-displays`, `m6-summarize-data`.
- Science grade 8: `s8-kinetic-energy-graphs`, `s8-wave-amplitude-energy`.
- Math grade 8: `m8-function-qualitative`.

Science’s thermal-design work is in its second grade 6 unit, while the mathematics course places statistical summaries in unit 8. Grade 8 science uses qualitative nonlinear graphs in units 8.1 and 8.2, while mathematics develops the relevant functions work in unit 5. Same-grade placement does not secure readiness at those points. [Science sequence](https://openscied.org/curriculum/middle-school/explore-the-curriculum/), [grade 6 mathematics narrative](https://im.kendallhunt.com/MS/teachers/1/narrative.html), [grade 8 mathematics narrative](https://im.kendallhunt.com/MS/teachers/3/narrative.html).

The existing guided-statistics note on `s6-light-paths` is a useful model. It should not be undone.

**Exact fixes:** append the following to `notes` in `data/progressions/science.csv`.

| Row | New text |
|---|---|
| `s6-insulator-design` | `Math timing: center is developed later in the grade 6 math sequence. Before summarizing trials, science teaches the selected summary with one worked example and guided practice using a small data set. Retain individual trial values. Independent choice among statistical summaries is not assumed.` |
| `s6-hazard-forecast` | `Math timing: if histograms precede m6-data-displays, science explicitly teaches frequency, equal-width intervals and how a histogram differs from a category bar graph, using supplied counts. Students are not expected to infer the display conventions unaided.` |
| `s8-kinetic-energy-graphs` | `Math timing: this unit precedes the usual grade 8 functions unit. Science models reading the axes and comparing equal input increases on straight and curved graphs, then gives guided practice before independent interpretation. Function notation and deriving an energy formula are not required.` |
| `s8-wave-amplitude-energy` | `Math timing: reuse the graph-reading instruction from s8-kinetic-energy-graphs before relating amplitude and energy. If this unit is taught first, supply that instruction here. Do not assume m8-function-qualitative has already occurred.` |

The course frames must allocate time for these bridges. This finding does not prescribe moving either base text’s units.

### 3. Three grade 6 social studies leans depend on science taught in grades 7 or 8

**Severity:** moderate  
**LAYER:** progression  
**REPEAT:** yes, completing the deferred timing check in social studies Codex finding 6  
**Confidence:** firm

| Social studies row, grade 6 | Current science target | Target grade |
|---|---|---:|
| `ss6-changing-interpretations` | `s8-fossil-record`, MS-LS4-1 | 8 |
| `ss6-mena-settlement` | `s7-resource-distribution`, MS-ESS3-1 | 7 |
| `ss6-africa-geography` | `s7-human-impact-design`, MS-ESS3-3 | 7 |

The topics belong in grade 6 social studies. The problem is presenting later science as their preparation. Grade 3 fossil work supplies a useful foundation, but its relative-age and past-environment work does not itself teach human-origin research or genetic evidence. [Grade 3 fossil expectation](https://www.nextgenscience.org/pe/3-ls4-1-biological-evolution-unity-and-diversity), [middle school fossil expectation](https://www.nextgenscience.org/pe/ms-ls4-1-biological-evolution-unity-and-diversity).

**Exact fixes in `data/progressions/social-studies.csv`:**

| Row | `cross_subject`: new value | Append to `notes` |
|---|---|---|
| `ss6-changing-interpretations` | `science:s3-fossils (fossils provide evidence of earlier life); ela:e6-compare-accounts (compare accounts using a supplied source set)` | `Teach the human-origin case from a short source pack that explains what the fossil, tool, dating and genetic evidence can show. Earlier science supplies fossil evidence at elementary depth; students do not independently interpret genetic studies or calculate dates. Grade 8 later develops the fossil-record progression.` |
| `ss6-mena-settlement` | `math:6.EE.C.9 (read supplied monthly climate graphs with local teaching if needed); science:s5-sphere-interactions (land, air and water shape conditions); science:s5-water-distribution (available fresh water is limited)` | `Teach the regional resource distribution from supplied maps and explanations. For climate graphs, explain each axis and unit, and read temperature and rainfall separately before comparing their patterns. Grade 7 science later explains the geologic distribution of resources.` |
| `ss6-africa-geography` | `science:s5-protect-resources (compare ways communities protect land and water)` | `Teach the drought, desertification and restoration case here from dated maps and a short explanation of the mechanisms needed. The task compares evidence about responses; it does not assume the grade 7 human-impact design performance has been taught.` |

These are local teaching bridges, not proposals to move science standards.

### 4. Three grade 9 world-history leans similarly point to later science courses

**Severity:** moderate  
**LAYER:** progression  
**REPEAT:** yes, the deferred cross-subject availability check in the social studies reviews  
**Confidence:** firm on placement; likely on the sufficient earlier preparation

**Rows:** `wh1-geography-shapes-contact` and `wh1-farming-and-cotton` lean on `chem-resources-hazards-climate-human`, grade 10. `wh1-scientific-revolution` leans on `phys-orbits`, grade 11.

The first two history tasks need environmental mechanisms and evidence about human choices. The Scientific Revolution task needs a taught comparison of historical explanations and observations. None needs to assume completion of the later science performance.

**Exact fixes in `data/progressions/social-studies.csv`:**

| Row | `cross_subject`: new value | Append to `notes` |
|---|---|---|
| `wh1-geography-shapes-contact` | `science:s6-climate-circulation (winds and regional climate); science:s7-resource-distribution (resources are unevenly distributed)` | `Retrieve the relevant climate or resource mechanism, then teach its historical application from the unit's maps and sources. The grade 10 human-activity explanation is later reinforcement, not a prerequisite.` |
| `wh1-farming-and-cotton` | `science:s6-climate-circulation (climate conditions affecting farming); science:s7-resource-distribution (water and other resources differ by place)` | `Supply the crop, water and land-use facts needed for the historical explanation. Students connect these facts to production and trade without assuming the grade 10 Earth-and-human-systems performance.` |
| `wh1-scientific-revolution` | `science:s8-earth-sun-moon (observations explained by a sky model); science:s8-gravity-solar-system (qualitative orbital models)` | `Teach the historical comparison of Earth-centered and Sun-centered explanations with diagrams and the observations available to the people studied. Orbital calculations and Kepler-law algebra are not required; phys-orbits develops the quantitative science in grade 11.` |

This retains the existing historical scope and uses the distinction between earlier preparation and later application required by the [NGSS mathematics connections](https://www.nationalacademies.org/read/18290/chapter/18).

### 5. “Graph the results” leaves the grade 2 plant investigation open to a later-grade representation

**Severity:** moderate wording risk  
**LAYER:** progression  
**REPEAT:** yes, the graph-form mismatch kind found in the earlier social studies reads  
**Confidence:** likely

**Rows:** science `s2-plant-needs-test`, grade 2; math `m2-picture-bar-graphs` and `m2-line-plots`, grade 2; `m5-graph-points`, grade 5.

The science note calls for measurements over several weeks and graphing the results, without naming the graph. A busy writer could reasonably produce a connected time-height graph. The available grade 2 mathematics instead establishes single-unit category bars and measurement line plots. A line plot here is a frequency display, not a connected growth graph. [Grade 2 measurement and data standards](https://tasks.illustrativemathematics.org/2.MD-4).

**Exact fix in `data/progressions/science.csv`, row `s2-plant-needs-test`:**

- Append to `cross_subject`:

  `math:m2-picture-bar-graphs (compare whole-unit plant heights on one selected observation day)`

- Replace the sentence beginning `Students measure height` with:

  > Students measure height to the nearest whole centimetre and draw how the plants look over two to three weeks, recording change in a dated table. On one selected day, they make a single-unit bar graph comparing the three conditions. An optional line plot shows the heights of several plants measured on that same day; it is a frequency display, not a connected time-height graph.

The investigation still studies change over time. The representation now has a defined, available mathematical demand.

### 6. The repaired primary-source definition has not fully reached the ELA handoff wording

**Severity:** minor  
**LAYER:** progression  
**REPEAT:** yes, the primary-source wording issue settled in social studies Codex finding 8  
**Confidence:** likely

**Rows:** social studies `ss3-primary-secondary`, grade 3, and `ss4-primary-source`, grade 4; ELA `e4-firsthand-secondhand`, grade 4.

The social studies definition correctly makes the source’s relationship to the question decisive and includes later-recorded memories. The ELA lean still describes its connection as “what a source made at the time can tell us.” That is a valid example, but an unnecessarily narrow handoff description immediately after the definition was repaired.

Later-recorded firsthand accounts can be primary sources. [Library of Congress explanation](https://ask.loc.gov/faq/303148).

**Exact fix in `data/progressions/ela.csv`, row `e4-firsthand-secondhand`:**

Replace `cross_subject` with:

`social-studies:ss4-primary-source (compare firsthand evidence with an interpretation, considering the question, maker, date and purpose)`

Append to `notes`:

> A firsthand account may be recorded later, as a memoir or interview. Date helps assess the account but does not by itself decide whether it is firsthand or a primary source.

Keep the distinction between **firsthand versus secondhand account** and **primary versus secondary source**. They overlap, but they are not universal interchangeable labels.

### 7. Three worthwhile reinforcement connections remain unwired

**Severity:** minor, reinforcement opportunity  
**LAYER:** progression  
**REPEAT:** yes, missing cross-subject links are an earlier finding kind; these pairs are additional  
**Confidence:** judgment call

These connections provide a meaningful return to earlier knowledge or a shared source task. They do not require another subject’s entire unit to be repeated.

| Pair | Why wire it | Exact edit |
|---|---|---|
| ELA `e2-research`, grade 2, and science `s3-fossils`, grade 3 | ELA already includes fossil reading and notes. Science can retrieve that familiarity before introducing evidence interpretation. | In `science.csv`, append to `s3-fossils.cross_subject`: `ela:e2-research (retrieve earlier fossil reading before interpreting new evidence)`. Append to `notes`: `Earlier ELA reading supplies topic familiarity, not proof that students can interpret fossil evidence.` |
| Science `s7-climate-change-evidence`, grade 7, and math `alg1-correlation-causation`, grade 9 | Science already distinguishes correlation from cause qualitatively. Algebra I should build on that reasoning while adding the correlation coefficient and statistical precision. | In `math.csv`, append to `alg1-correlation-causation.cross_subject`: `science:s7-climate-change-evidence (revisit earlier qualitative reasoning about correlation and cause)`. Append to `notes`: `Retrieve the earlier distinction, then teach the correlation coefficient and the limits of statistical association as new mathematics.` |
| Science `s7-climate-change-evidence` and ELA `e7-evaluate-argument`, both grade 7 | The ELA knowledge thread already includes climate and human impact. Its argument evaluation can reinforce the actual evidence reasoning used in science. | In `science.csv`, append to `s7-climate-change-evidence.cross_subject`: `ela:e7-evaluate-argument (evaluate evidence and causal reasoning in the climate source set, with local modelling if this comes first)`. In `ela.csv`, set `e7-evaluate-argument.cross_subject` to `science:s7-climate-change-evidence (apply argument evaluation to the climate knowledge thread)`. |

The first pair preserves the distinction between reading about fossils and demonstrating the science performance. The third retains explicit teaching rather than assuming transfer between subjects. [Grade 3 fossil expectation](https://www.nextgenscience.org/pe/3-ls4-1-biological-evolution-unity-and-diversity), [WWC secondary writing guidance](https://ies.ed.gov/ncee/wwc/practiceguide/22).

## Settled by the expert

| Choice | Decision and reason | File or next artifact |
|---|---|---|
| Future science references in social studies | Keep the existing social studies content and grades. Use earlier preparation plus explicit local teaching, as specified above. | `social-studies.csv` |
| Chemistry pH | Require interpretation of a supplied scale; logarithm calculation remains grade 11 mathematics. | `science.csv` |
| Grade 2 plant graph | Use a dated table and a single-unit comparison bar graph. A measurement line plot remains an optional frequency display. | `science.csv` |
| Claim, evidence and reasoning | Use **claim-evidence-reasoning** as the common teacher-facing family name. Social studies’ `claim-evidence` is its early data label. Keep the grade-specific demand: kindergarten ELA opinion writing does not suddenly require a three-part scientific explanation. | Course-frame terminology |
| Line plot and dot plot | These name the same measurement-frequency representation in the relevant elementary rows. Use “line plot” when teaching the elementary standard and explain its later “dot plot” name. Neither means a connected time-series graph. | Math and science course frames |
| `data-graph` | Keep it as an umbrella data label. Student tasks must name the actual representation: picture graph, bar graph, line plot, histogram, scatter plot or time-series graph. | Science course frames |
| Timeline and number line | Keep both names. A scaled timeline uses number-line reasoning, but historical BCE/CE labels have no year zero. | Existing timeline rows and course frames |
| Map coordinates and Cartesian coordinates | Keep both names. Latitude/longitude are angular geographic coordinates, not interchangeable Cartesian distances. | Geography and math course frames |
| Physics trigonometry and vectors | No new core prerequisite is warranted by the present one-dimensional mechanics boundaries and algebraic wave relation. A frame that adds component-vector or trigonometric calculations must teach their specific mathematics explicitly. | Physics course frame |
| Source attribution | Use the existing climb: source list in grade 4, basic bibliographic information in grade 6, standard citation format in grade 7. Content subjects retain responsibility for source use in their own discipline. | ELA, science and social studies frames |

## Rows per grade per subject

Rows are not days, equivalent amounts of work or a student timetable.

| Grade | Math | ELA | Science | Social studies | Total |
|---|---:|---:|---:|---:|---:|
| K | 20 | 29 | 11 | 19 | 79 |
| 1 | 26 | 31 | 10 | 21 | 88 |
| 2 | 28 | 30 | 12 | 18 | 88 |
| 3 | 24 | 28 | 15 | 27 | 94 |
| 4 | 27 | 30 | 14 | 17 | 88 |
| 5 | 25 | 30 | 14 | 21 | 90 |
| 6 | 26 | 29 | 14 | 29 | 98 |
| 7 | 23 | 28 | 18 | 29 | 98 |
| 8 | 24 | 29 | 26 | 27 | 106 |
| 9 | 28 | 24 | 24 | 37 | 113 |
| 10 | 28 | 26 | 20 | 43 | **117** |
| 11 | 26 | 30 | 20 | 27 | 103 |
| 12 | 0 | 30 | 0 | 69 | 99 |
| **Total** | **305** | **374** | **198** | **384** | **1,261** |

The important concentrations are:

- **Grade 6:** signed numbers, ratios, statistical summaries and a new reading-complexity band arrive while science and geography already need quantitative displays.
- **Grade 8:** science has its largest row count while math develops functions, scientific notation and bivariate data. ELA also reaches independent reading at the top of its band.
- **Grade 9:** Algebra I functions, Biology computational modelling, renewed world-history chronology and the next ELA complexity band coincide.
- **Grade 10:** the largest aggregate count combines Geometry, Chemistry, World History II and demanding literary work. Several subjects are near their own row-count peaks.
- **Grade 12:** the 69 social studies rows comprise **25 US History II, 19 Government and 25 Economics rows**. They cannot be interpreted as one ordinary course. The zero math and science counts describe these core progression files, not an expectation that students take neither subject.

## Topic threads

| Grade or band | Connection or concern |
|---|---|
| K to 1 | Weather, trees, living needs, sky patterns and bird structures connect well with the corresponding science rows. Preserve rich read-aloud knowledge while decoding develops separately. |
| 2 to 3 | Pollinator reading aligns directly with grade 2 science. Fossil reading is a legitimate preview before grade 3 evidence interpretation, addressed in finding 7. |
| 3 | Frog adaptations align with `s3-habitat-survival`. Water reading can build knowledge without claiming that later water-system science has already been taught. |
| 4 | Animal-defense reading aligns strongly with `s4-structures-function`. The unnamed “unit 3 history set” is not specific enough to establish a dependable content match; its course frame must identify the actual events and supply their context. |
| 5 | Rainforest, resource protection, disaster preparation and people who led change have useful connections to science and social studies. Reuse knowledge while increasing research and source-comparison demand. |
| 6 | Early law codes and Earth hazards are now explicit, connected knowledge threads. Preserve the earlier fix. |
| 7 | Citizenship in Greece and Rome, ecosystems, resources and climate align well. Finding 7 makes one substantive argument-evaluation connection explicit. |
| 8 | Founding documents, rights, news literacy and heredity technology form a coherent continuation of the grade 6 and 7 threads. |
| 9 to 10 | Myth transformation deliberately revisits earlier knowledge at a new literary demand. Biology evidence, climate forecasts, imperialism and colonial literature offer useful same-grade pairings. |
| 11 | American literary periods align with US History I. The Douglass connection is promising, but the social studies source task offers several alternatives; a shared reading is not yet guaranteed merely because the ELA lean calls it “the same narrative.” |
| 12 | Modern American literature, court reasoning, policy sources and economics can reinforce each other. The frames need distinct disciplinary questions and a coordinated research calendar. |

No necessary cross-subject topic clash warrants moving a standard or replacing a knowledge thread.

## Sensitive and hard topics

| Topic | Cross-subject judgment |
|---|---|
| Evolution and human origins | The stance is consistent: evidence decides scientific claims, and students are not asked to declare beliefs. Grade 6 human origins can precede grade 8 fossil-record work when its needed scientific content is taught locally, as in finding 3. |
| Climate | Grade 7 science and ELA align, followed by grade 10 science and social studies. Argument tasks should examine evidence, explanations and responses without converting established findings into an unsupported “two sides” exercise. |
| Slavery and racism | Social studies provides early plain naming, resistance and human lives; later ELA develops source and rhetorical analysis. Preserve that stance when texts are shared. A teacher preview does not override BASELINE’s prohibition on printed slurs. |
| Genocide | The explicit grade 10 social studies work and grade 12 response studies have different, age-appropriate purposes. No contradictory ELA stance was found in the progression notes. Actual text selection still requires review. |
| Puberty and health | These files contain body systems, inheritance, reproduction and health cases, but no identified puberty sequence. Science’s stated boundaries do not establish coverage of the separate health curriculum. |

Keep the existing prohibition on victim/perpetrator role play. Survivor testimony, contextual evidence and careful source selection are consistent with the [Holocaust teaching guidance](https://www.ushmm.org/de/teach/fundamentals/guidelines-for-teaching-the-holocaust). The progression read does not replace the required sensitivity and qualified-person reads.

## What is right and should not be undone

- The repaired ownership and contributing-row structure, including the science completion moves.
- Earlier ELA contributions in grades 9 and 11. A later formal owner is not automatically a timing defect.
- Supplied averages in grade 3 science and parts-out-of-100 treatment in grade 5.
- Elementary map-scale work that counts whole scale-bar units before demanding formal proportional reasoning.
- The explicit grade 6 to 8 ELA knowledge threads.
- The science boundaries that keep qualitative explanation separate from later calculation.
- Plain, evidence-based treatment of evolution, climate and hard history.

## For the course frames

Step 2 must handle the following. These are not additional progression findings.

1. **Make a shared availability calendar.** For every same-year lean, record the first use, the needed feature, its teaching point in the other course and the local bridge when that teaching comes later.
2. **Budget the bridges in finding 2.** “Guided” must become an actual worked example, student practice and readiness evidence.
3. **Protect mathematical boundaries.** Grade 6 negative-temperature reading must not silently become assumed grade 7 signed arithmetic. Physics spreadsheet orbits must not silently become an untaught vector course.
4. **Coordinate research and writing load.** Give shared topics distinct disciplinary questions and feedback. Stagger substantial ELA, history and science products, especially in grades 9 to 12.
5. **Resolve same-grade reciprocal leans.** For example, `e6-short-research` and `ss6-research-contribution` must identify who first models the research routine. Mutual references do not establish an order.
6. **Name actual topic sets and shared texts.** Identify grade 4’s history set. Decide whether the grade 11 Douglass reading is genuinely shared or supplies context for a different history source task.
7. **Use the load notes, not equal row allocations.** Grade 8 completion rows and Biology’s combined performances need different amounts of time.
8. **Show the grade 12 timetable.** Account separately for US History II, Government and Economics under the eventual placement decision.
9. **Carry disciplinary literacy explicitly.** The already documented RH/RST/WHST inventory issue remains open. Do not claim that ELA reading and writing codes alone complete historical or scientific literacy. The standards distinguish those disciplinary demands. [Organization of the literacy standards](https://www.thecorestandards.org/ELA-Literacy/introduction/how-to-read-the-standards/).
10. **Coordinate sensitive source handling.** Shared texts need consistent content notes, marked omissions where required, safe alternatives and the existing restrictions on simulations and personal disclosure.

## For Cory

None newly required by these proposed repairs. They clarify prerequisites, representations and reinforcement within existing grades.

The previously recorded Government and Economics placement question remains a scope decision for Cory; this report does not settle it. (Resolved since by Desk card q-ss-progression-1, 2026-11-13: Government and Economics may be taken in grade 11 or 12; rows stay stored at grade 12.)

## What I could not judge

- A successful full `plan.py check`, because of the missing dependency.
- Actual within-year availability before course frames and calendars exist.
- Whether the proposed bridges fit the eventual time budgets.
- The accuracy, accessibility and sensitive-content handling of all eventual anchor texts and lesson pages.
- The remaining disciplinary-literacy inventory work, already identified by the earlier science read.

The live grade 2 ELA base-text page redirected to a page without usable curriculum content. The fossil-topic comparison therefore rests on the current repository rows, not a claimed fresh verification of that base-text module.

## Sources and source-list notes

The linked sources above were used for the following limited purposes:

- [NGSS mathematics connections](https://www.nationalacademies.org/read/18290/chapter/18): grade consistency and the relationship between science and mathematics instruction.
- [Grade 6 mathematics narrative](https://im.kendallhunt.com/MS/teachers/1/narrative.html) and [grade 8 mathematics narrative](https://im.kendallhunt.com/MS/teachers/3/narrative.html): within-year placement of statistics and functions.
- [Middle school science sequence](https://openscied.org/curriculum/middle-school/explore-the-curriculum/): early placement of the receiving science units.
- [HS-ESS3-6](https://www.nextgenscience.org/pe/hs-ess3-6-earth-and-human-activity): published computational-model results and assessment limits.
- [EPA pH explanation](https://www.epa.gov/ocean-acidification/understanding-science-ocean-and-coastal-acidification): direction and factor-of-ten interpretation of pH.
- [Grade 3 fossil expectation](https://www.nextgenscience.org/pe/3-ls4-1-biological-evolution-unity-and-diversity) and [middle school fossil expectation](https://www.nextgenscience.org/pe/ms-ls4-1-biological-evolution-unity-and-diversity): the difference between earlier preparation and later depth.
- [Grade 2 measurement and data standards](https://tasks.illustrativemathematics.org/2.MD-4): available elementary graph forms.
- [Library of Congress primary-source explanation](https://ask.loc.gov/faq/303148): later-recorded firsthand accounts.
- [WWC secondary writing guide](https://ies.ed.gov/ncee/wwc/practiceguide/22): explicit writing instruction across disciplines.
- [Holocaust teaching guidance](https://www.ushmm.org/de/teach/fundamentals/guidelines-for-teaching-the-holocaust): source-based teaching and avoiding simulations.

For `APPROACH-SOURCES.md`, retain the usable full-grade mathematics narrative URLs, the EPA pH page and the failed ELA redirect access note if they are not already recorded. No source-list file was edited.

**Verdict:** broadly coherent; local cross-subject readiness repairs are needed. **Finding count:** 7. **Report path:** `docs/reviews/progression-cross-2026-11-13.md`, supplied above and not written.
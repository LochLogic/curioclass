# Scope and sequence read: math-grade-7
**2026-11-15 | Independent first reader, before the expert**

Report destination: `docs/reviews/sequence-math-grade-7-2026-11-15.md`. Supplied here in full; no file was written.

## Verdict

Revise before unit planning. The eight-unit order is coherent, all 43 owned codes have assessment placements, and the source map accounts for all 145 base lessons. The biggest risk is that several assessment reservations promise evidence that the preceding instruction or allotted minutes do not yet support; establish the sample-comparison teaching and repair those evidence reservations first.

## What I read

- `docs/agents/EXPERT.md`, the mathematics lens, `docs/RUBRIC-MATH-K8.md`, the foundation, relevant roadmap sections, BASELINE rules 20 to 24, the shared and mathematics approaches, and the mathematics source-list entries and evidence notes.
- The complete grade 7 scope and sequence, frame, 160 day rows and 182 source-map rows.
- Grade 7 progression rows, their grade 6 prerequisites and grade 8 destinations, plus the older angle, fraction, hierarchy and volume prerequisites.
- Relevant grade 5 and grade 6 day rows to verify prerequisite last use.
- Grade 7 calendar rows, `docs/courses/CALENDAR.md`, sequence-writing rule 2 and the glossary.
- Earlier grade 7 frame findings and relevant grade 5 and grade 6 sequence findings, after reading the target sequence.
- Outside sources linked below, including two curricula, official standards, accessible progression drafts and federal guidance.

The prohibited files and the grade 7 writer’s report were not opened. Memory supplied only general review-workflow guidance; no curriculum finding rests on memory.

## Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Stopped before grade 7 because importing `lesson.py` requires the unavailable `markdown` package. |
| `python -X utf8 scripts/frame.py calendar` | Passed; grade 7 mathematics checks occupy weeks 9, 24 and 32. |
| `python -X utf8 scripts/frame.py check math-grade-7` | Passed, zero failures. |
| `python -X utf8 scripts/plan.py check math-grade-7` | Passed, zero failures. |
| `python -X utf8 scripts/stale.py check` | Passed, 56 files checked, zero failures. |

## Findings, most serious first

### 1. The culminating sample-comparison instruction becomes an assessment

**Severity:** Serious  
**LAYER:** sequence, base text  
**REPEAT:** new  
**Confidence:** Firm

**Location:** Unit 8 narrative; `days.csv`, days 149 and 153 to 155; source-map row for 7.8.18.

Day 149 teaches comparison of distributions before sampling. Day 153 estimates a population center and examines variation among samples; day 154 estimates population proportions. The first explicit instruction connecting two random samples to a comparative inference about their populations, including the median/IQR version, is then scheduled as day 155’s end-of-unit assessment.

The base lesson supplies instruction and discussion for this transition. Its median/IQR activity explicitly extends reasoning developed earlier in that lesson. Turning the lesson into independent assessment removes that teaching step. A student who can estimate one population’s center has not necessarily learned to justify a comparison between two populations. [Base lesson preparation](https://im.kendallhunt.com/MS/teachers/2/8/18/preparation.html), [lesson activities](https://im.kendallhunt.com/MS/teachers/2/8/18/index.html).

**Exact fix:** Preserve day 155 as assessment, but explicitly teach the transition beforehand:

- Day 153: use samples from two supplied object populations; teach comparison through sample means and MAD after generating and examining repeated samples.
- Day 154: reserve ten minutes to connect that reasoning to sample medians and IQR, then retain the categorical sampling and independent population-estimate product.
- Update the goals, notes and source map to identify these instructional portions of 7.8.18 before the independent assessment.

Keep both comparison methods and the repeated-sample work. Add no day.

### 2. Five minutes cannot credibly supply the complete proportional-representation record promised for check 2

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, assessment-load findings in the grade 5 sequence read  
**Confidence:** Likely

**Location:** `days.csv`, day 112; day 119; scope and sequence, course-level checks table.

Day 112’s five-minute opening must produce an individual record covering proportional and nonproportional tables and graphs, constants in every representation and words/diagrams, an equation, and interpretations of three kinds of graph point. Day 119 then relies on this record as complete earlier-unit evidence.

This is several distinct student responses inside one ordinary opening, alongside a new distribution-and-factoring lesson. The likely result is incomplete annotations or supplied answers being treated as demonstrated understanding.

**Exact fix:** Build the record across three existing openings:

| Day | Evidence collected |
|---|---|
| 107 | Table test and constant from a diagram or verbal description |
| 108 | Graph test, graph constant and contextual point meanings |
| 112 | Equation representation and remaining constant interpretations |

State that these replace the ordinary openings. Day 119 should name the three dated records rather than describe day 112 alone as covering every part. Preserve the algebra cores and remaining mixed practice.

### 3. The year-end audit does not explicitly require independent equation fluency

**Severity:** Moderate  
**LAYER:** sequence, standard  
**REPEAT:** yes, grade 5 sequence finding 3  
**Confidence:** Likely

**Location:** `days.csv`, day 159; scope and sequence, check 3.

The final equation evidence is described as an annotated claim-chain audit. It includes equation “parts,” but does not explicitly reserve independent solving. Correcting or judging supplied steps can conceal difficulty producing a solution unaided.

The standard requires fluent solving of both equation forms, and sequence-writing rule 2 requires direct sampling of each fluency standard at year-end. [Official standards, page 49](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf#page=49).

**Exact fix:** Reserve eight minutes within day 159’s existing check time for four short, independent equations, two of each form, including signed rational coefficients. Supply no solution steps and show no student countdown. Shorten repetitive audit annotations to make room. Retain contextual modeling and arithmetic/algebra comparison elsewhere in the evidence record.

### 4. Several prerequisite retrieval tasks arrive after their first use

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, grade 6 sequence finding 3  
**Confidence:** Firm

**Location:** Prerequisite table; `days.csv`, days 7, 10, 77, 85, 92, 99 and 111.

The last-use grades are generally classified correctly, but some first retrieval placements are late:

| Prerequisite | Named retrieval | Earlier use |
|---|---:|---|
| `m6-unit-conversion` | 49 | Different-unit scales on day 10, with map-unit interpretation already on day 7 |
| `m6-one-step-equations` | 92 | Signed one-step equations begin on day 85 |
| `m6-equivalent-expressions` | 111 | Distribution justifies negative products on day 77 and is used in equation-method comparison on day 99 |

Generic mixed practice does not identify these prerequisite tasks. Writers following the ledger could therefore miss the intended connection when students first need it. The expression progression explicitly builds grade 7 transformations on grade 6 property work. [Expression progression, PDF page 8](https://commoncoretools.files.wordpress.com/2011/04/ccss_progression_ee_2011_04_25.pdf#page=8).

**Exact fix:** Use existing openings to retrieve unit conversion before day 10’s work, one-step equation meaning on day 85, and numerical distribution on day 77. Retrieve the expression version again before day 99’s method comparison. Update the prerequisite table and relevant skills fields; retain days 49, 92 and 111 as later retrieval.

### 5. Some mid-unit code lists promise more than their tasks assess

**Severity:** Moderate  
**LAYER:** sequence, standard  
**REPEAT:** new  
**Confidence:** Firm

**Location:** `days.csv`, days 21, 57, 78 and 104.

The brief requires each check to address every part of each code it lists. Several mid-unit lists exceed the stated task:

- Day 21 lists all of `7.RP.A.2` and `7.RP.A.2b`, but assesses tables, diagrams, words and equations before graph work begins on day 26.
- Day 57 lists `7.RP.A.3`, while its task covers percent change before the later interest, tax, commission, fee and error work.
- Day 78 lists `7.NS.A.2a`, but names negative-product justification without the contextual interpretation of products.
- Day 104 lists parent `7.EE.B.4`, while inequality instruction begins on day 106.

This need not change the sensible mid-unit positions. It needs narrower claims and an explicit distinction between partial diagnostic evidence and complete coverage. [Official grade 7 standards](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf#page=48).

**Exact fix:** Keep the assessment dates. For day 21, retain complete equation coverage and describe the remaining taught subskills as partial diagnostics, without crediting complete parent or representation-wide coverage. Apply the same treatment to day 57’s percent diagnostic. Remove parent `7.EE.B.4` from day 104’s complete-coverage claim while retaining `7.EE.B.4a`. Add a short contextual product interpretation on day 78.

Where the CSV cannot distinguish partial evidence, put the limited claim in its note and reserve complete-code attribution for the later assessment.

### 6. Unit 1 follows the repository exception but violates this run’s readiness instruction

**Severity:** Moderate  
**LAYER:** process, sequence  
**REPEAT:** yes, prerequisite-placement issues in earlier grade 7 frame reads  
**Confidence:** Firm

**Location:** Scope and sequence, lines 41 to 57; `days.csv`, day 1; sequence-writing rule 2 and glossary.

The run explicitly requires unit 1 readiness in the start-of-year check and prohibits readiness on a unit’s first day. The plan instead puts angle and protractor readiness in day 1’s last ten minutes.

The repository’s current rule 2 and glossary explicitly allow this unit 1 exception. Thus the writer followed a documented repository rule, but the supplied run instruction takes precedence here. The passing structural checks do not settle that conflict.

**Exact fix:** Place the diagnostic before the first unit hook. One concrete 160-day arrangement is:

1. Make day 1 a course-level launch with unmarked grade 6 retrieval and the final ten-minute older-angle readiness check.
2. Shift the existing twelve unit 1 days to days 2 to 13.
3. Move unit 2’s hook to day 14 and fold its current day 14 practice into day 15, as the shorter-path table already permits.
4. Keep subsequent dates unchanged; record 152 unit days and eight course-level days in the frame, sequence and source map.

The lead should also align the repository wording with the run’s chosen rule so subsequent readers do not inherit both instructions.

### 7. Day 120 retains a five-minute opening outside its complete response/readiness budget

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, grade 6 sequence finding 2  
**Confidence:** Firm

**Location:** `days.csv`, day 120.

The row reserves 40 minutes for course-level response and ten minutes for readiness, then separately retains a five-minute mixed-retrieval opening. Unlike day 109’s replacement opening, it never says this opening is displaced or included. The literal schedule takes 55 minutes.

**Exact fix:** State: “40 minutes targeted response, including any retrieval, revised reasoning and reflection; final ten minutes readiness; total 50. No separate opening.” For the shorter period, specify 35 minutes response plus ten minutes readiness.

### 8. Day 132’s major-work allocation is not established by its named task

**Severity:** Minor  
**LAYER:** sequence, standard  
**REPEAT:** yes, major-work accounting in earlier grade 7 frame reads  
**Confidence:** Likely

**Location:** `days.csv`, day 132; focus paragraph.

The row credits 35 minutes to `7.EE.B.4a`, but its goal is layer-based volume and finding a missing prism height. With known base area, `V = Bh` gives the one-step equation already taught in grade 6. The row does not name the two-step situation that would substantiate this allocation.

This does not overturn the year’s focus judgment, but it overstates the evidence behind the precise percentage. Connected work may count when its grade-level connection is demonstrated. [Evidence guide, indicator 1e](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf#page=13).

**Exact fix:** Remove these 35 minutes from the qualifying total unless a genuine two-step contextual task and its time are named. This isolated correction changes 5,355 minutes to 5,320, or 66.5 percent. Recalculate again after implementing the other scheduling changes.

### 9. The frame retains superseded readiness directions

**Severity:** Minor  
**LAYER:** frame, process  
**REPEAT:** yes, grade 6 sequence finding 4  
**Confidence:** Firm

**Location:** Frame readiness bullet, unit descriptions and source map.

The sequence correctly substitutes retrieval for grade 6 prerequisites, but the frame still directs readiness on ratio tables in unit 1 and negative numbers in unit 5. It also retains readiness-day descriptions for units 2 and 4, and a unit 7 “recheck” of angle/protractor work explicitly taught earlier this year.

The next writer receives conflicting directions despite the automated stale check passing.

**Exact fix:** Replace these frame directions with the sequence’s verified classifications. Preserve older-row readiness for fractions, additive angles, hierarchy and additive volume. Update the frame’s major-unit arithmetic from 94 to 93 days and replace its remaining six-course-day reference with the current allocation, then incorporate finding 6’s redistribution if adopted.

## Coverage, order and load

| Unit | Days | Judgment |
|---|---:|---|
| 1. Scale drawings | 12 | Recognition, factors, area, construction and rescaling form a sound arc. Readiness placement needs finding 6. |
| 2. Proportional relationships | 21 | Tables precede equations and graphs. Representation evidence needs findings 2 and 5. |
| 3. Circles | 11 | Circumference precedes area derivation and measurement choice. No excessive allocation found. |
| 4. Rates and percentages | 22 | Fractional rates, percent bases, applications and error receive distinct teaching time. |
| 5. Rational arithmetic | 23 | Seven initial addition/subtraction days, multiplication/division development and an explicit decimal-expansion day are justified. |
| 6. Expressions, equations and inequalities | 27 | Twelve equation teaching days, five inequality days and six expression days match the load. Required mid-unit assessment is present. |
| 7. Geometry | 18 | Five angle days, five construction days, slicing and five measurement/application days are proportionate. |
| 8. Probability and sampling | 19 | Ten probability days and six preparation days precede the two-part assessment. Comparative inference needs finding 1. |

All 43 owned codes appear on end-of-unit assessment rows. This establishes placement, not item-level sufficiency. The explicit decimal-expansion completion, student-controlled digital construction, both sliced solids, repeated samples and saved simulation records resolve substantial risks identified at the frame layer.

The older prerequisites have appropriate last-use classifications: angle concepts and protractor use remain grade 4; the two fraction rows, hierarchy and additive volume remain grade 5. Grade 6’s passing fraction and hierarchy retrieval does not reset those grades. Days 68 and 120 immediately precede their receiving units; no readiness check is weeks ahead of its unit.

The source map has 121 keep rows, four merge rows, 20 cuts and 37 original allocations. All 145 base lessons occur exactly once, retained lessons preserve their order, and every day has a mapped allocation. No additional source-map omission was found.

## Other required checks

| Requirement | Result |
|---|---|
| Checks do not repeat the preceding unit assessment | Met in the specified contexts and forms; preserve direct performance evidence under finding 3. |
| Calendar targets | Met at weeks 9, 24 and 32. |
| Same-year leans | Engineering overlaps days 24 to 41 and has a supplied-data bridge. Percent precedes the later science and Roman-economy work. Clock-offset context is explained before history’s days 78 to 86. |
| Candidate cells | Settled, with retained extensions’ minutes or reasons for dropping them. |
| Shorter period | A 45-minute structure is present; day 120 needs finding 7. Actual assessment and device-transition timing remains unverified. |
| Shorter year | Ten named fold-ins produce 150 meetings without removing an assessment, readiness or respond day. Required work is assigned destinations. |
| Response counted once | Assessment windows name single response allocations. Day 120’s minutes need correction. |
| Stale notes | Automated check passed; manual frame conflicts remain in finding 9. |

## Mathematics lens checklist, scope and sequence layer

| Checklist line | Result |
|---|---|
| Every owned standard is completed | **Missed as a fully usable instructional specification:** sample-comparison teaching and assessment claims need findings 1 and 5. Other owned parts have named destinations. |
| Problems intentionally join units | **Met:** scale/rate choices, percent equations, signed financial changes, angle equations and population scaling. |
| Fluency receives spaced mixed practice | **Met:** repeated arithmetic and equation openings. Direct year-end equation evidence needs finding 3. |

All eight mathematical practices have named content tasks. These are useful planning commitments; their assessment evidence still belongs in the unit plans.

## What is right and should be preserved

- The eight-unit sequence and its main dependencies.
- Number-line and property reasoning before signed-operation fluency.
- Decimal expansion beginning in unit 4 and explicitly finishing in unit 5.
- Independent digital construction records rather than teacher demonstration.
- Neutral supplied contexts, printable stand-ins and no student countdown timers.
- Saved products and single response allocations rather than repeated full performances.

## Settled by the expert

These are concrete recommendations for the lead to apply; this reader edited nothing.

| Choice | Reason | Files affected |
|---|---|---|
| Teach both sample-comparison methods before day 155 | Assessment should follow the culminating instruction | Sequence, days and source map |
| Assemble proportional evidence over days 107, 108 and 112 | Preserves the five-minute openings without claiming one oversized record | Sequence and days |
| Add four independent year-end equations | Directly samples both fluency forms | Day 159 and check 3 description |
| Move named retrieval before first use | Supports the actual teaching sequence | Prerequisite table and days |
| Keep mid-unit dates and narrow coverage claims | Avoids assessing untaught material | Mid-unit rows |
| Use a pre-unit start-of-year diagnostic for this run | Follows the explicit run instruction | Frame, sequence, calendar and maps |
| Replace day 120’s separate opening | Restores its 50-minute budget | Day 120 and shorter-period note |
| Withdraw unsupported volume-equation minutes | Keeps focus accounting tied to named grade-level work | Day 132 and focus total |

## For Cory

None arising from these instructional fixes. Any purchase or change to the intended audience remains outside this review.

## Limits and sources

Original items, keys, scoring guidance, accommodations and classroom timing do not yet exist, so they were not certified. The digital rotation is arithmetically possible, but tool usability and transitions remain untested.

The compiled 2023 Progressions PDF exceeded the web tool’s size limit; attempted Geometry and Number System draft links were inaccessible. Those portions were checked against local progression records and official standards, without substituting remembered source claims.

Sources opened and used:

- [Official mathematics standards](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf): grade 7 requirements and grade boundaries.
- [Ratio progression](https://commoncoretools.files.wordpress.com/2012/02/ccss_progression_rp_67_2011_11_12_corrected.pdf): proportional representations and percent development.
- [Expression progression](https://commoncoretools.files.wordpress.com/2011/04/ccss_progression_ee_2011_04_25.pdf): earlier property work and rational expressions.
- [Statistics and probability progression](https://commoncoretools.files.wordpress.com/2011/12/ccss_progression_sp_68_2011_12_26_bis.pdf): probability before sampling and comparative inference.
- [Publishers’ criteria](https://achievethecore.org/content/upload/Math_Publishers_Criteria_K-8_Spring_2013_FINAL.pdf): focus, coherence and connected supporting work.
- [Mathematics evidence guide](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf): qualifying focus calculations.
- [Base-text sequence](https://im.kendallhunt.com/MS/teachers/2/narrative.html), [dependency guidance](https://im.kendallhunt.com/MS/teachers/2/scope_and_sequence.html), and the lesson pages linked in the findings: order and instructional purpose.
- [Second curriculum’s grade 7 sequence](https://www.fishtanklearning.org/curriculum/math/7th-grade/): comparison of mathematical dependencies, without treating its pacing as mandatory.
- [Federal problem-solving guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/16): representations, reflection and comparison of strategies.

**For the source list:** Retain the accessible progression-draft links as fallbacks for the oversized compiled document.

**Verdict:** Revise before unit planning. **Finding count:** 9. **Report path:** `docs/reviews/sequence-math-grade-7-2026-11-15.md`, supplied here without writing a file.


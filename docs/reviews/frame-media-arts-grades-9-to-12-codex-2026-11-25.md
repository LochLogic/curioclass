# Frame read: Media Arts, grades 9 to 12

2026-11-25. Independent second read. No files were changed.

## Verdict

**Sound structure, with revisions needed before the scope and sequence is written.** All 28 selected progression rows are placed once, standards ownership follows the three proficiency levels, and each level fits its calendar. The main risk is awarding full-standard achievement from partial or impractical assessment evidence; correct those evidence contracts first.

**Seven findings follow, most serious first.**

## What I read and checked

- The frame-read brief, after-core frame-writing provisions, expert instructions, arts lens, arts adoption bar, and arts STANDARD and APPROACH pages.
- The target frame in full; its course-list selector, frames.csv entry and calendar rows; all 28 selected progression rows and their standards action lines.
- The preceding media arts frame’s relevant units, models and reciprocal seams. There is no following media arts course.
- Relevant foundation, approach, baseline and arts decisions; arts progression reviews and earlier media arts and visual arts frame reviews.
- Outside primary sources linked below.

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check media-arts-grades-9-to-12` | One failure: the plan stage expects lesson-plan data that this frame does not have. The check was course-filtered because repository instructions prohibit an unfiltered run. |
| `python -X utf8 scripts/frame.py check media-arts-grades-9-to-12` | **0 failures.** |
| `python -X utf8 scripts/stale.py check` | **0 failures across 121 files.** Unmarked stale prose remains below. |

## Findings

### 1. Several full-standard claims permit partial evidence

**Severity:** Major  
**LAYER:** frame, with related progression and standard action-line corrections  
**REPEAT:** yes, incomplete standards coverage recurs in the earlier arts reads  
**Confidence:** firm

**Location:** Units 2, 3, 4, 8, 13, 14 and 15, frame lines 304 to 317.

Every owned ID is present, but some teaching or scoring descriptions narrow its actions. A writer following these descriptions could mark incomplete performance “met.”

| Location | Problem | Exact fix |
|---|---|---|
| **Unit 13, `MA:Cr2.1.III`** | The named evidence is a one-page proposal. It does not require a tested prototype or evidence of testing the proposed framework. | Require a prototype, a recorded test against goals, time, resources and personal limitations, and a revised framework justified by the results. Keep the proposal as one part of that evidence. Restore testing and prototypes in `ma-g11-ideas` and its words-file line. [Advanced creating standard](https://www2.cde.ca.gov/cacs/id/web/30381). |
| **Unit 8, `MA:Cr2.1.II`** | The final look-for checks the student’s aesthetic and resource limits, but omits presentation context and evaluation of production strategy. | Add the intended presentation context, a tested production strategy and a reason for its revision to the portfolio and final look-for. Restore those requirements in `ma-g10-ideas` and its action line. [Accomplished creating standard](https://www2.cde.ca.gov/cacs/id/web/30380). |
| **Unit 3, `MA:Pr5.1.Ia`** | A chosen role and growth in **one** art, design, technical **or** interpersonal skill can earn “met.” | Require individually attributed growth across all four skill areas, through selected roles and more than one production. Collect the baseline and later evidence within unit 3, using its prototype trials and finished work. Update `ma-g9-craft` accordingly. [Proficient producing standard](https://www2.cde.ca.gov/cacs/id/web/30418). |
| **Unit 8, `MA:Pr5.1.IIa`** | Leading one producer day and carrying out its plan does not establish command of all four skill areas. | Retain the rotating producer role, but score artistic, design, technical and interpersonal performance separately from observed production and attributed work. The log supports those judgments rather than replacing them. [Accomplished producing standard](https://www2.cde.ca.gov/cacs/id/web/30419). |
| **Units 4 and 14, `MA:Re9.1.I` and `MA:Re9.1.III`** | Critiquing the piece at production stages does not explicitly require evaluating the production process itself. | Require evaluation of both the work and its production process. In unit 4, apply criteria at rough-cut and final stages. In unit 14, require independently selected criteria, complex goals or competing factors, and strategically sought feedback. Restore production-process evaluation in the corresponding progression notes and words lines. [National standards, PDF page 7](https://nationalartsstandards.org/sites/default/files/Media%20Arts%20at%20a%20Glance%20Updated.pdf), [Advanced evaluation standard](https://www2.cde.ca.gov/cacs/id/web/30472). |
| **Unit 15, `MA:Cn10.1.IIIb`** | Both teaching and evidence substitute “new meaning, new knowledge **or** a cultural experience” for the complete demand. | Require the work and account together to demonstrate new meaning, knowledge **and** an impactful cultural experience. Add one evidence field for each. Align `ma-g11-sources` with that requirement. [Advanced connecting standard](https://www2.cde.ca.gov/cacs/id/web/30485). |
| **Unit 15, `MA:Pr6.1.IIIa`** | The promotion plan checks a stated effect and audience, but does not explicitly assess curation, distribution or adaptation across contexts. | Require a curated selection and presentation/distribution plan for two distinct school-approved contexts, with the intended effect and promotion adapted to each. Existing printed and live forms can supply those contexts. [National standards, PDF page 5](https://nationalartsstandards.org/sites/default/files/Media%20Arts%20at%20a%20Glance%20Updated.pdf). |
| **Unit 2, `MA:Re7.1.Ib`** | The evidence asks how sight and sound steer experience, omitting how they establish intention. | Add an explanation of the intention communicated through the interacting modes, supported by specific choices in the work. [National standards, PDF page 6](https://nationalartsstandards.org/sites/default/files/Media%20Arts%20at%20a%20Glance%20Updated.pdf). |

These corrections complete existing ownership. They require no standards to move between units.

### 2. Individual assessments lack workable time allocations, and the Level 4 checkpoint repeats scored work

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, assessment-time and individual-evidence problems recur in earlier arts frame reads  
**Confidence:** firm for the missing allocations and repeated evidence; likely for classroom feasibility

**Location:** “Scored evidence,” lines 108 to 124; units 3, 8, 13 and 17; Level 4 course-level checks, lines 333 to 334.

The screening procedure uses 39 minutes. Units 3, 8 and 13 additionally require every student to demonstrate tool use at the teacher’s table, without allocating a separate observation window. A team screening cannot establish each student’s individual adaptation.

Unit 17 assigns a defended talk to “the check day,” and the Level 4 mid-year checkpoint assigns individual presentations to a panel. Neither supplies a schedule for 30 students. The mid-year checkpoint also scores the proposal and first pieces already scored in unit 16, contradicting the statement that no artifact is scored twice.

**Exact fix:**

- Collect tool-use observations during the final three production sessions already allocated in units 3, 8 and 13: ten students per session, approximately 90 seconds each, with individual record fields. Keep screenings separate.
- Allocate four existing unit 17 sessions to defended talks, with groups of 8, 8, 8 and 6 students. Allow four minutes per student, including questions; give other students a named independent task.
- Replace the Level 4 mid-year panel with a fresh individual framework-and-prototype task under a new constraint. Carry unit 16’s scored records unscored.
- On the Level 4 year-end second check day, collect individual written answers to two fresh questions about production decisions and evaluation. Carry earlier defended-talk records unscored.
- State that all marks are available before the corresponding respond session.

This preserves the annual day totals.

### 3. *Kicking the Clouds* is assigned the wrong language and an incomplete cultural context

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, incorrect work identification occurs in the preceding independent media arts read; this correction is new  
**Confidence:** firm

**Location:** Leave-out bullet, line 160; sensitivity summary, line 219; unit 11, line 313.

The frame calls the family recording Hocak. Hopinka identifies it as his grandmother learning the **Pechanga language** from her mother. His affiliations include both the Ho-Chunk Nation and the Pechanga Band of Luiseño Indians. [Filmmaker’s account](https://www.skyhopinka.com/kicking-the-clouds), [National Gallery of Art](https://www.nga.gov/exhibitions/sky-hopinka).

**Why it matters:** The error would enter work cards and direct the sensitivity reader toward an incomplete set of community sources.

**Exact fix:** Replace the work description with:

> Sky Hopinka, affiliated with the Ho-Chunk Nation and Pechanga Band of Luiseño Indians, *Kicking the Clouds* (2021), a reflection on family and place guided by a recording of his grandmother learning Pechanga from her mother.

Use that description consistently in the leave-out and sensitivity notes. Require the sensitivity read to consult the filmmaker’s account and Pechanga community sources. Retain the prohibition on imitating the language or family recording.

### 4. Firm work selections have no direct source links

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, missing work and safety-source links were identified in the independent earlier-band reads  
**Confidence:** firm

**Location:** Base-text bullet, lines 69 to 85; works throughout the Units table; safety sources, lines 198 to 202; For the lead item 6.

The frame repeatedly says works are “described and linked,” but supplies institution names rather than direct work links. Item 6 acknowledges that no work facts were fetched. Finding 3 demonstrates the cost of postponing every factual check.

A completed reproduction-rights review belongs later, but the identity and teaching purpose of a firm frame selection need an identifiable source now.

**Exact fix:**

1. Add a direct maker, holding-institution or distributor link beside each named work.
2. Give a short checked description supporting the date, setting and feature being studied.
3. Keep eventual reproduction and excerpt checks separately identified.
4. Replace the blanket memory note with item-specific verified or unresolved statuses.
5. Replace safety-guide domains with direct links to the named documents and criterion.

For example, Hopinka’s linked account above supplies the corrected context. The [film agency’s *Begone Dull Care* page](https://www.nfb.ca/film/begone_dull_care/) identifies its makers and direct-on-film technique; its viewing and licensing conditions still need their own use-specific check.

### 5. Adult consent and leave-out provisions are inconsistent across the frame and selected rows

**Severity:** Moderate  
**LAYER:** frame and progression  
**REPEAT:** yes, adult consent was identified in the arts progression reads  
**Confidence:** firm

**Location:** Leave-out bullet, lines 156 to 162; recording and showing instructions, lines 147 to 155; selected progression notes at arts.csv lines 472 to 499.

The opening frame correctly gives students aged 18 or over their own consent choice. Other instructions still require each family’s permission without that exception, and the leave-out bullet names only schools and families. Several selected progression notes independently repeat the unqualified family requirement.

**Why it matters:** Unit writers receive these rows as instructions. The inconsistent versions can restore a family permission requirement that Cory explicitly removed for adults.

**Exact fix:** Use this rule wherever consent or leave-out authority is specified:

> A student under 18 gives their own agreement, with family consent where required. A student aged 18 or over receives the family note and makes their own consent and leave-out choices. The school’s own rules still apply.

Apply it to the frame’s leave-out, recording and showing instructions and all selected progression notes containing an unqualified family-consent requirement. Retain each student’s agreement for recording.

### 6. Level 4 does not secure the annual range of works it promises

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, insufficiently secured cultural and historical range recurs in earlier arts reads  
**Confidence:** firm

**Location:** Base-text bullet, lines 75 to 80; units 16 to 19, lines 318 to 321.

The frame promises living makers and more than one region and period in every level, plus a Native maker in each level. Level 4 requires a living maker and someone outside the student’s region, but its student-choice conditions do not require different periods or a Native maker. A valid proposal could therefore miss the frame’s own annual range.

**Exact fix:** Add one annual source-selection checklist to unit 16’s proposal:

> Across the year’s studied works, include at least one living maker, makers from at least two regions, works from at least two historical periods, and at least one Native maker. Record each work’s maker, place, date, purpose and source.

Unit 17 checks that list and fills any gap through its existing criticism selections. Keep student choice within those conditions.

### 7. Stale prose and one incorrect seam range remain despite the stale check passing

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, the combined media arts read identified the stale seam statement  
**Confidence:** firm

**Locations and exact fixes:**

| Location | Problem | Required replacement |
|---|---|---|
| Target frame, Seams, lines 241 to 243 | Says the preceding frame does not exist. | “The Media Arts, grades 6 to 8 frame hands on reading and society from unit 9, ideas and craft from unit 10, making and judging from unit 11, and presenting and sources from unit 12. Unit 1 reteaches the needed techniques and models as readiness.” |
| Target frame, line 273 | Unit 9 starts at band day **239**, but its range is written “239 to 276” only after a preceding “unit 9 239” construction that should remain explicit and consistent with the table. | State the complete sequence plainly: “Unit 6: 161 to 166; unit 7: 167 to 198; unit 8: 199 to 236; mid-year check/respond: 237 to 238; unit 9: 239 to 276; unit 10: 277 to 316.” |
| ADOPTION-BAR-SUBJECTS.md, arts status row | Still lists NCAS membership checking and loading the 63 music strand IDs as owed. | “Completed 2026-11-21: NCAS membership checking, 63 composition and theory strand IDs, their words lines and progression rows.” L83 and STANDARD.md confirm completion. |
| ADOPTION-BAR-SUBJECTS.md, introductory approach note | Says no subject approach exists. | “Current subject approach pages are linked from docs/APPROACH.md; the table below records remaining work.” |

Apply status corrections to living documents. Leave dated review records intact.

## Coverage, days, seams and calendar

| Level | Units | Selected rows | Owned IDs | Unit days | Course checks/respond | Total |
|---|---|---:|---:|---:|---:|---:|
| 1 | 1 to 5 | 8 | 18 Proficient | 154 | 6 | 160 |
| 2 | 6 to 10 | 8 | 18 Accomplished | 154 | 6 | 160 |
| 3 | 11 to 15 | 8 | 18 Advanced | 154 | 6 | 160 |
| 4, optional | 16 to 19 | 4 | None newly owned; 11 revisited | 154 | 6 | 160 |

Every selected skill is placed exactly once. All 54 expected owned IDs are present at their correct levels, without extra ownership.

The annual allocations are defensible: production units receive more time than reading units, and Level 4’s opening studio receives 48 days for its proposal and first pieces. The 80-day paths also add correctly: 76 unit days plus four course-check/respond days.

Calendar rows agree with the full path. Each level’s mid-year check/respond occupies days 77 and 78; year-end checks/respond occupy days 157 to 160. High school calendar rules permit these placements.

The eight grade 8 handoffs match the incoming Level 1 rows. There is no later media arts course. Cross-subject contacts have local teaching supports, so this frame does not depend on a particular high school ELA or social studies sequence.

There is no base text, so source-map coverage is not applicable.

## Arts lens checklist

| Frame-level check | Result |
|---|---|
| High school levels remain independent of student grade | Met |
| Four artistic processes in every level | Met |
| Technique taught explicitly and increases in difficulty | Met in the design |
| Discipline words support making and analysis | Met |
| Choice, making and showing in every unit | Present |
| Critique followed by revision | Present |
| Annual cultural and historical range, including living makers | Levels 1 to 3 present; Level 4 needs finding 6 |
| Work settings accurately sourced | Needs findings 3 and 4 |
| Practical assessment, self-assessment and portfolios | Present; evidence needs findings 1 and 2 |
| Ordinary-room time, supplies, setup and cleanup | Addressed; individual assessment schedules need finding 2 |
| Making remains with students; software does not judge finished work | Met |
| Media arts retains its own techniques and purposes | Met |
| No copied cornerstone task identified | Met in this frame read |
| Final excerpts, accessibility provisions and safety execution | Not yet judgeable |

## What should be preserved

Preserve the complete annual levels, entry by proficiency, explicit bridge and placement provisions, increasing independence, eight carried models, portfolios, critique routine, invented alternatives to personal disclosure and local storage.

Keep the paper path. The national introduction deliberately leaves particular technologies unspecified. [NCAS media arts introduction](https://www.nationalartsstandards.org/node/763).

Repeated works can support stronger later analysis. I do not adopt the earlier combined review’s proposed numerical cap on revisits: retain a returning work when the later unit names the harder question it answers.

## Settled by the expert

| Choice | Reason | Files affected |
|---|---|---|
| Restore omitted actions within existing ownership | Completes current standards without moving IDs | Target frame, affected progression notes and words lines |
| Observe individual production during allocated making sessions | Secures practical evidence without crowding screenings | Target frame |
| Use scheduled unit talks and fresh course-check tasks | Fits the class and avoids scoring the same artifact twice | Target frame and later scope |
| Correct the language and community context of *Kicking the Clouds* | Supported by the filmmaker and holding museum | Target frame |
| Add an annual Level 4 selection checklist | Makes the frame’s existing range promise enforceable | Target frame |
| Retain purposeful revisits and the paper path | Both can support the required learning | Target frame |

## For Cory

- **Money:** The proposed ceiling of $100 per class per level remains a proposal. Current optional estimates are $90, $80, $80 and $60, with free alternatives retained.
- No new audience, outside-person or standards-ownership decision is required for these corrections.

## Sources and limits

The findings use current repository evidence and the linked primary sources. No finding rests on model memory.

The national handout’s connecting-code labels conflict with its anchor headings. I cross-checked those meanings against the California standards pages rather than reversing the repository’s corrected Cn10/Cn11 placement. California wording also differs in places, so the national statements remained the primary comparison.

The Washington education department’s media arts PDF returned **403** and was not fetched another way; its browser check remains outstanding. Accessible national and California sources supplied the needed standards evidence.

Detailed safety instructions remain marked **“from memory”** pending the specified safety read. This review did not verify every work’s reproduction rights, preview eventual excerpts or judge assessment items that have not yet been written.

**For the source list:** Add Hopinka’s own *Kicking the Clouds* page and the specific standards pages used above if absent.
# Frame read: Media Arts, grades 6 to 8

2026-11-25. Independent second read. No files were changed.

## Verdict

**Sound structure, with revisions needed before the scope and sequence is written.** All selected progression rows and standards are placed correctly, each year totals 64 sessions, and the unit order supports increasingly demanding work. The main risk is assessment: several evidence descriptions permit incomplete performance, while the short path collects assessment during response time; correct those contracts first.

**Seven findings follow, most serious first.**

## What I read and checked

- The frame-read brief, after-core frame-writing provisions, expert instructions, arts lens, arts adoption bar, and arts STANDARD and APPROACH pages.
- The target frame in full, its course-list selector, all 24 selected progression rows, their 54 standards action lines, frames.csv entry, and calendar rows.
- Neighboring media arts frames’ relevant units, models and reciprocal seams; the cited grade 6 and grade 7 ELA units.
- Relevant arts decisions, pre-work and progression reviews, and earlier media arts frame reviews.
- Outside primary sources linked below.

| Check | Result |
|---|---|
| `python -X utf8 scripts/frame.py check media-arts-grades-6-to-8` | 0 failures |
| `python -X utf8 scripts/stale.py check` | 121 files, 0 failures |
| `python -X utf8 scripts/plan.py check media-arts-grades-6-to-8` | 1 failure: expects later-stage plan files |

The plan check was course-filtered because repository instructions prohibit an unfiltered run; its missing-plan-files result does not prevent this frame review.

## Findings

### 1. Producing skills are assessed through descriptions instead of demonstrated production

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, combined media arts read M3  
**Confidence:** firm

**Location:** Units 2, 6 and 10, frame lines 284, 288 and 292.

The frame teaches practical actions, but several final items accept hypothetical solutions or descriptions. Writing alone cannot establish the adaptability demonstrated during production that these standards require. This affects more IDs than the three identified in the earlier combined read. [NCAS media arts standards, PDF page 4](https://www.nationalartsstandards.org/sites/default/files/2021-11/Media%20Arts%20at%20a%20Glance%20-%20new%20copyright%20info.pdf).

**Exact fix:**

| Unit | IDs | Replace the evidence with |
|---|---|---|
| 2 | `MA:Pr5.1.6b`, `MA:Pr5.1.6c` | Individually attributed production evidence showing constraints actually tested and ordinary and experimental tool use actually performed, accompanied by a brief explanation. |
| 6 | `MA:Pr5.1.7b`, `MA:Pr5.1.7c` | A production observation and kept trials showing exploration and adaptation to the assigned purpose. Retain the purpose-card writing as transfer practice. |
| 10 | `MA:Pr5.1.8b`, `MA:Pr5.1.8c` | Individually attributed trials and the resulting work showing the convention changed and tools, methods and content adapted to intent. Retain the written explanation alongside that evidence. |

Collect these observations during the final production sessions already allocated. Name the observation days and individual record fields so a team product cannot substitute for evidence about each student.

### 2. Several standards lose required breadth between teaching and final evidence

**Severity:** Major  
**LAYER:** frame, with related progression and standard action-line corrections  
**REPEAT:** yes, incomplete standards coverage in earlier arts reads  
**Confidence:** firm

**Location:** Units 2, 3, 4, 7, 8, 11 and 12.

Naming every ID does not establish every required action. The following omissions could lead a writer to award “met” for partial evidence.

| Location | Problem | Exact fix |
|---|---|---|
| **Unit 2, `MA:Pr5.1.6a`** | Teaching and evidence permit one assigned role and one skill. The standard requires varied skills developed through multiple assigned roles. | Rotate each student through at least two assigned roles. Record evidence across art, design, technical and interpersonal skills. Correct the singular-role wording in `ma-g6-craft` and the affected seam descriptions. |
| **Units 3 and 7, `MA:Re9.1.6`, `MA:Re9.1.7`** | Context disappears from the teaching and evidence descriptions. Unit 7’s final item also omits explicit evaluation of production processes. | Give the critique a context card. Require criteria applied to both the work and its production process, with an explanation of how context affects the judgment and one constructive suggestion. Restore context in the corresponding progression notes and words-file lines. |
| **Unit 11, `MA:Re9.1.8`** | Teaching names production processes, but the final item names only the classmate’s work, goals and setting. | Add the classmate’s production record to the stimulus and require evaluation of one production decision against the developed criteria, goals and context. |

These corrections follow the national producing and evaluation statements. [NCAS media arts standards, PDF pages 4 and 7](https://www.nationalartsstandards.org/sites/default/files/2021-11/Media%20Arts%20at%20a%20Glance%20-%20new%20copyright%20info.pdf).

Two further gaps concern connecting and presentation:

- **Units 4, 8 and 12, `MA:Cn10.1.6b`, `7b`, `8b`:** The final questions narrow the standards to reinterpretation, new knowledge or wider circulation. Add evidence explaining and demonstrating the cultural experience media creates, alongside the applicable meaning, knowledge or situation. Retain history, learning and worldwide events as contexts. Correct the progression notes and short action lines where they preserve the same narrowing. [NCAS grade 6 connecting statement](https://www2.cde.ca.gov/cacs/id/web/30480), [national connecting statements](https://www.nationalartsstandards.org/index.php/customize-handbook?discipline=Media+Arts).
- **Unit 12, `MA:Pr6.1.8b`:** The final item asks for an improvement “actually made,” but the schedule does not locate implementation after evaluating a presentation; the item also omits personal growth. Place a trial showing and audience feedback during the final application work, then a counted session implementing a presentation improvement before the scored screening. Require the review to explain the change, personal growth and audience effect. [National presentation statements](https://www.nationalartsstandards.org/index.php/customize-handbook?discipline=Media+Arts).

These are corrections within existing ownership. No standard needs moving between units.

### 3. The short path collects assessment during the respond session

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, arts pre-work scoring fix and the independent K to 2 and 3 to 5 reads  
**Confidence:** firm

**Location:** “The once-a-week path,” lines 34 to 45; units 4, 8 and 12.

The short path moves written assessment into the respond session’s first 20 minutes. Students therefore begin response before all relevant evidence has been collected and marked. It also compresses the full path’s 25-minute written allocation without explaining the reduction.

This reverses the arts approach’s explicit fix: marks must be available before the respond session.

**Exact fix:** Keep the existing `7, 9, 6, 6` unit allocations and separate course-check sessions. Give each six-session screening unit this explicit sequence:

| Session | Required work |
|---|---|
| 1 | Study the works, demonstrate the technique and begin a draft |
| 2 | Making, critique and trial showing |
| 3 | Revision, completed records and presentation improvements |
| 4 | Scored screening |
| 5 | Written assessment and self-assessment |
| 6 | Respond from completed marks |

State that sessions 1 to 3 include the necessary source work and connecting evidence. Delete the instruction to collect assessment during respond. This preserves 32 annual sessions and the stated short-path check weeks.

### 4. All six course-level checks exceed the frame’s own two-item limit

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, assessment-load problems in earlier media arts reads  
**Confidence:** firm for the contradiction; likely for classroom feasibility

**Location:** “Scored evidence,” lines 96 to 105; Course-level checks table, lines 300 to 305.

The frame limits each student to two written items on a check day and allocates 25 minutes. Every course-level check specifies three substantial tasks.

At mid-year these are two analyses plus an ethics task. At year-end they include a fresh plan, prototype or workflow plus two further responses. The stated 38-minute procedure supplies no additional production time.

**Exact fix:**

- **Mid-year:** Combine the two related analysis prompts into one structured analysis task with separate scoring fields. Keep the ethics case as the second task.
- **Year-end:** Keep the fresh planning task and the unseen-work interpretation task. Remove the third fresh sample: the angle-change item in year 6, shot-list item in year 7 and technical-polish item in year 8. Those skills retain their unit assessments.
- Budget the 25-minute working window explicitly: approximately 12 minutes for the first task and 13 for the second, including viewing or reading the stimuli.
- Keep recent unit records unscored, as already specified.

### 5. Named works and safety guides lack direct sources, and one work’s country is wrong

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, missing source links in the independent earlier-band reads; country correction new  
**Confidence:** firm

**Location:** Works throughout the Units table; “Safety read,” lines 174 to 189; For the lead item 6.

The frame repeatedly promises that works are “described and linked,” but supplies no direct work links. Generic institution names and domains leave the next writer to reconstruct the evidence behind dates, settings and descriptions.

Unit 1 also labels *The Electric Hotel* “Spain, 1908.” The French national library identifies the film as French; the filmmaker’s nationality should be distinguished from the production’s country. [National library record](https://data.bnf.fr/fr/ark%3A/12148/cb164656103.pdf).

**Exact fix:**

1. Add a freely readable item or contextual source link beside every named work, supporting its identity and setting.
2. Distinguish contextual evidence from the item page used for the eventual rights check.
3. Change the unit 1 description to **“France, 1908, by Spanish filmmaker Segundo de Chomón.”** Correct the same inherited error in the grade 3 to 5 frame through the lead.
4. Replace the safety-guide domains with direct links to the named guides and the specific flashing criterion.
5. Replace For the lead item 6’s blanket memory list with item-specific verified or unresolved statuses.

Useful verified starting points include the [museum record for *Jáaji Approx.*](https://www.moma.org/collection/works/315397) and the [Library of Congress holding list for *Falling Leaves*](https://wwws.loc.gov/rr/mopic/findaid/Alice%20Guy-Blache.pdf). These establish identification or holdings, not unrestricted reuse.

### 6. The claim that no earlier media arts work or maker repeats is false

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, combined media arts read M1  
**Confidence:** firm

**Location:** “Base text,” lines 62 to 79; units 1, 2 and 8.

Repository comparison confirms these repeats:

| Current selection | Earlier placement |
|---|---|
| *The Electric Hotel*, unit 1 | Grade 3 to 5 frame, unit 5 |
| Lumière makers, unit 1 | K to 2 frame, unit 5 |
| *Begone Dull Care*, unit 2 | K to 2 frame, units 2 and 4 |
| *Gertie the Dinosaur*, unit 2 | K to 2 frame, unit 12 |
| *The Horse in Motion*, unit 8 | K to 2 frame, units 1 and 7 |

Revisiting a work can support stronger analysis. The defect is the false assurance and the absence of a stated progression for those revisits.

**Exact fix:** Replace the no-repeat sentence with:

> Several earlier works return deliberately. Each returning work has a harder question here, stated in its unit; other selections maintain the year’s range of makers, regions and periods.

Then label the returning works and their new purposes: audience construction in unit 1, production methods in unit 2, and media’s contribution to knowledge in unit 8.

I do not carry forward the earlier review’s suggestion that repetition itself requires replacement. The instructional purpose should decide that.

### 7. Source-status and shared process notes need correction

**Severity:** Minor  
**LAYER:** process, with a related standard-page correction  
**REPEAT:** yes, stale notes and weekly-time sourcing in earlier arts reads  
**Confidence:** firm

**Locations and exact fixes:**

| Location | Required replacement |
|---|---|
| **Target frame, Days bullet and For the lead item 2** | “The association’s middle school visual arts checklist and general visual and media arts program standards were checked on 2026-11-25. No numerical weekly minimum for media arts was identified in those documents. This course provides 80 minutes weekly, or 40 on the short path; no numerical gap is claimed.” |
| **Arts STANDARD.md, section 3.4** | Record that bounded source-check result for media arts. Do not promise a figure from the middle school checklist or transfer a visual arts figure to media arts. |
| **ADOPTION-BAR-SUBJECTS.md, arts owed row, line 568** | Replace the obsolete gate and strand-loading obligations with: “Completed 2026-11-21: NCAS membership checking, 63 composition and theory strand IDs, their words lines and progression rows.” |
| **ADOPTION-BAR-SUBJECTS.md, introductory claim that no subject approach exists** | Replace with: “Current subject approach pages are linked from docs/APPROACH.md; the table below records remaining work.” |
| **Media Arts, grades 9 to 12, opening Seams note** | Replace “has no frame yet” with the existing grade 8 handoff: reading and society in unit 9, ideas and craft in unit 10, making and judging in unit 11, presenting and sources in unit 12. |

The middle school checklist gives scheduling options without a numerical weekly minimum; the general document’s scheduling section gives qualitative requirements. [Middle school checklist](https://www.arteducators.org/wp-content/uploads/2025/09/OTL-Middle_School_Visual_Media_Arts_Program.pdf), [general program standards](https://www.arteducators.org/wp-content/uploads/2025/09/OTL-PreK-12_Visual_Media_Arts_Programs.pdf).

The obsolete gate obligation is contradicted by `later.csv` L83’s completed entry and the arts standard page. The automated stale check does not catch these prose statements. Apply corrections to living documents, leaving dated review records intact.

## Coverage, days, seams and calendar

| Year | Units | Selected rows | Owned IDs | Unit sessions | Course checks and respond | Total |
|---|---|---:|---:|---:|---:|---:|
| 6 | 1 to 4 | 8 | 18 | 60 | 4 | 64 |
| 7 | 5 to 8 | 8 | 18 | 60 | 4 | 64 |
| 8 | 9 to 12 | 8 | 18 | 60 | 4 | 64 |

Independent counting found every selected skill placed exactly once, all 54 expected IDs present once, and no extra IDs or wrong-year ownership.

The full-path allocation of `14, 18, 14, 14` sessions has a defensible rationale. Planning and production receive the longest units; later work reuses established techniques. No unit is clearly disproportionate to its load.

Progression handoffs match in both directions. The grade 5 unit ranges cited in Seams agree with the calendar. The ELA references also agree: grade 6 unit 1 occupies days 1 to 32, and grade 7 unit 4 occupies days 87 to 108.

Calendar rows match the frame’s full path: mid-year checks on school day 83 and year-end checks on day 158, followed by respond days 85 and 160. No core check occupies day 83; week 32 permits shared finals. Dance, theater and visual arts currently share day 83, so the lead’s after-core calendar reconciliation remains necessary.

There is no base text, so source-map coverage is not applicable.

## Arts lens checklist

| Frame-level check | Result |
|---|---|
| Grade IDs in their own band year | Met |
| Four artistic processes each year | Met |
| Technique taught explicitly and increases in difficulty | Met in the design |
| Discipline words used in making and response | Met |
| Choice and showing in every unit | Met |
| Works from different cultures and periods, including living makers | Present; sourcing needs finding 5 |
| Critique followed by revision | Present; short-path sequence needs finding 3 |
| Practical assessment, self-assessment and portfolio | Present; evidence needs findings 1 and 2 |
| Assessment fits the session | Needs findings 3 and 4 |
| Ordinary room, setup, cleanup and supplies addressed | Met as frame commitments |
| Performing and making remain in the room | Met |
| Five arts retain distinct purposes | Met |
| No copied cornerstone task or essential question identified | Met in the frame read |
| Actual excerpts, final access provisions and safety execution | Not yet judgeable |

## What should be preserved

Preserve the three complete years, reciprocal seams, increasing technical demands, portfolios, explicit critique routine, public or invented alternatives to personal disclosure, local storage and consent protections.

Keep the paper path. The national introduction deliberately leaves technologies unspecified; this read found no basis for requiring electronic devices throughout. [NCAS media arts introduction](https://www.nationalartsstandards.org/node/763).

The corrected Cn10 and Cn11 ownership is consistent with the national statements. Do not reverse that correction.

## Settled by the expert

| Choice | Reason | Files affected |
|---|---|---|
| Observe producing actions during production | Writing alone does not establish performed skills | Target frame |
| Restore omitted actions within current ownership | Completes standards without moving IDs | Target frame, affected arts rows and words lines |
| Keep `7, 9, 6, 6` short-path allocations with separate assessment and respond sessions | Preserves 32 sessions and the stated check weeks | Target frame and later scope |
| Limit course checks to two structured tasks | Matches the frame’s stated working window | Target frame |
| Retain repeated works as named revisits with harder questions | Repetition can serve progression | Target frame |
| Correct the film’s country and publish the bounded weekly-time search result | Replaces unsupported statements with checked evidence | Target frame and identified shared files |

## For Cory

- **Money:** The proposed $75 annual supply ceiling remains a proposal. Current optional estimates are $40, $40 and $45 per class by year, with free alternatives retained.
- No new audience, outside-person or standards-ownership decision is needed for these corrections.

## Sources, confidence and limits

Outside sources were checked through web search and direct opening. No finding rests on model memory.

The frame’s detailed safety rules remain marked **“from memory”** pending its specified safety read. This review does not establish every work’s reproduction rights, the suitability of eventual excerpts, or the quality of assessment items that have not yet been written.

One film-catalog page returned HTTP 429; a different national-library source supplied the country and date. A customized national-standards URL was inaccessible; the national PDF and accessible handbook supplied the standards evidence.

**For the source list:** Record the middle school and general opportunity-to-learn documents linked above, including the limited result that no numerical media arts weekly minimum was identified in those documents.
# Second-model frame read: Health, grades K to 2

**Date:** November 25, 2026  
**Course:** `health-grades-k-to-2`  
**Delivery:** Complete report supplied here. No files changed.

## Verdict

**Revise before scope-and-sequence writing.** The frame has a coherent three-year structure, places every selected progression row, and preserves non-sensitive routes to help when sensitive units are omitted. Its biggest risk is treating a standard’s placement or a pictured response as evidence of full learning; restore the missing indicator content and require observable performance where the indicator calls for action.

**Finding count: 5.**

## What I read and checked

I read the [complete frame](S:/CurioClass/docs/courses/health-grades-k-to-2/frame.md), its `frames.csv` entry, its course-list selector, all 56 selected K, 1 and 2 progression rows, the grade 3 handoff rows, and its stored calendar rows.

The review also used:

- `frame-read.md`, the after-core section of `frame-write.md`, `EXPERT.md`, and the health lens.
- The health adoption bar, `STANDARD.md`, `APPROACH.md`, the local NHES indicator descriptions and HECAT outcome descriptions.
- The foundation, shared approach, relevant production and decision rules, and earlier health pre-work and progression reviews.
- The existing K-to-2 physical education and social and emotional learning frames for the named seams.
- The outside sources linked below.

There is no preceding health course. The health grades 3-to-5 frame was absent, so its receiving end could be checked against progression rows only. A base-text source map is not applicable.

### Checks

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check health-grades-k-to-2` | One failure: the course has no lesson-stage `days.csv` with `parts.csv` or `items.csv`. The check was course-filtered, following AGENTS.md. |
| `python -X utf8 scripts/frame.py check health-grades-k-to-2` | **0 failures.** |
| `python -X utf8 scripts/stale.py check` | **70 files, 0 failures.** Unmarked stale statements remain in finding 5. |
| Independent placement count | **56 selected skills, 56 placements, no duplicates or omissions.** |
| Independent ownership count | **33 indicators, each listed once:** K 10, grade 1 14, grade 2 9. |
| Annual allocation | Each year has **24 unit lessons and four check/respond lessons**. |
| Stored calendar comparison | Unit ranges, check weeks and annual resets match the frame. All six health checks avoid core check weeks. |

These results support structural completeness, not full instructional coverage. The stored calendar also contains collisions with other after-core courses, including kindergarten computer science and grade 2 PE/ELD. Those require shared calendar coordination; the health frame satisfies this brief’s specific requirement to avoid core check weeks.

## Findings, most serious first

### 1. Two owned indicators lose required content

**Location:** Units 4 and 8, frame lines 227 and 231; corresponding progression rows; `NHES.S1.2.6` in `nhes-2024.txt`.  
**Severity:** Serious. **LAYER:** standard. **REPEAT:** yes, incomplete owned-standard coverage was identified in the earlier health second-model review, finding 5. **Confidence:** likely.

**Problem and consequence:** The frame can be implemented faithfully while leaving these parts untaught:

| Indicator | Gap | Exact fix |
|---|---|---|
| `NHES.S3.2.1`, unit 4 | Children identify helpers and choose people for a hand drawing. The frame does not explicitly teach the qualities that make someone trustworthy. | Add: “A trustworthy helper listens, takes a safety concern seriously and helps the child reach appropriate help. Children identify these qualities in two short adult-response scenes, then choose a helper and give one reason.” Include one unfamiliar helper-quality scene in the unit check. |
| `NHES.S1.2.6`, unit 8 | The environment is connected to a child’s health, but its effect on community health is absent. The local indicator description also omits that part. | Add: “Children identify how clean water, clean air or a safe shared play space helps both one character and other people who use the place.” Include a shared-place item in the unit check. Restore the community-health element in the local indicator description and owner-row notes. |

These requirements come from the live [2024 NHES indicators](https://shapeamerica.org/standards/health/new-he-standards/). Keep both owners in their existing units and retain the day counts.

### 2. The assessment design can award action indicators without observing action

**Location:** End-of-unit evidence, lines 52 to 60; units 6 and 15, lines 229 and 238; course-level checks, lines 251 and 254.  
**Severity:** Serious. **LAYER:** frame. **REPEAT:** new for these health indicators. **Confidence:** likely.

**Problem:** Unit 6 owns `NHES.S7.2.2`, but its specified final evidence is choosing a germ-stopping action and explaining why. Its habits chart is voluntary, private, and has no named teacher observation. Unit 15 permits a supplied character’s goal chart and look-back to stand for `NHES.S6.2.5`, even when the child has performed no goal-directed action.

The indicators require doing a health behavior and taking action toward a goal. Interpreting a character’s record can establish understanding, but cannot establish those performances. [2024 NHES indicators](https://shapeamerica.org/standards/health/new-he-standards/). HECAT likewise asks whether assessment measures match the intended skill. [HECAT Appendix 7, PDF page 1, printed APX-26](https://www.cdc.gov/healthy-youth/hecat/pdfs/HECAT_Appendix_07.pdf).

**Cost:** A child can receive “met” while only recognizing what somebody else should do.

**Exact fix:**

- In unit 6, add a brief teacher record of each child carrying out a taught classroom hygiene routine after modeling and feedback. Collect it during ordinary school routines across the unit. Carry this record into the unit and course-level judgments.
- In unit 15, retain the character option, but require every route to include an action performed by the child. A character can supply the purpose while the child carries out a safe classroom action, then reflects on that action.
- State explicitly: “A supplied fictional chart assesses interpretation. It does not, by itself, establish `NHES.S6.2.5`.”
- Score the steps and reflection, never health status, home compliance, athletic success or whether the goal succeeded. Preserve accessible actions and private personal plans.

This preserves the settled character alternative while making its evidence valid.

### 3. Goal-setting practice in a second health topic is not secured

**Location:** Standard claim, lines 31 to 32; goal-plan model, line 209; units 2, 9 and 15.  
**Severity:** Moderate. **LAYER:** frame. **REPEAT:** new. **Confidence:** likely.

**Problem:** `STANDARD.md` requires every skill standard to be practiced in at least two topics. All five progression rows carrying standard 6 are PHW rows. Units 9 and 15 also contain physical activity, but their goal work may still be entirely about washing or sleep. Sharing a unit with another topic does not ensure the goal-setting skill is practiced in that topic.

The earlier progression review’s checklist marked this requirement met and described standard 6 as occurring in PHW and safety. I disagree with that conclusion for the current rows: no selected safety row carries standard 6, and the frame does not name a required second-topic goal task.

**Cost:** Later writers can preserve every row while leaving goal-setting confined to one topic.

**Exact fix:** In unit 15, require one brief goal-plan application about an accessible movement break: identify the goal, helper and steps, take an accessible action, and look back. Link that application explicitly to the physical activity topic. Keep the PHW application and optional personal or character plan. This also supplies a practical route for finding 2 without adding a unit or indicator owner.

### 4. The kindergarten materials total omits one optional purchase

**Location:** Unit costs, lines 224 to 228; annual totals, lines 242 to 243; For the lead, item 6.  
**Severity:** Minor. **LAYER:** frame. **REPEAT:** new. **Confidence:** firm.

**Problem:** Kindergarten printing totals $14. Optional tasting adds $15, and buying the helmet adds another $15. The stated $29 total says it includes both.

**Cost:** The proposed $30 ceiling appears sufficient when the fully purchased option actually exceeds it.

**Exact fix:** Replace the kindergarten total with:

> Kindergarten: $14 in listed printing costs, assuming school soap and towels and a borrowed helmet. Optional tasting adds $15. Buying a helmet adds $15. Including both options totals $44.

Replace “$16 to $29” in the supplies-ceiling note with the corrected options. The grade 1 total of $17 and grade 2 total of $16 add correctly. Prices remain provisional; this finding concerns arithmetic, not verified purchasing prices.

### 5. Lead notes describe completed work and resolved script behavior as pending

**Location:** For the lead, items 1, 3 and 7, lines 294 to 325; Cross-subject, lines 258 to 283.  
**Severity:** Minor. **LAYER:** process. **REPEAT:** yes, stale availability and planning notes recur in earlier frame reviews. **Confidence:** firm.

**Problem:** Three instructions no longer describe the repository:

- Item 1 asks for `weeks=28`, which is already set. It also says calendar weeks continue across years, but the stored calendar resets school weeks to 1.
- Item 3 says `frame.py` treats “None” as an owned code. The current checker explicitly ignores `none` and `none owned`.
- Item 7 postpones coordination until the SEL and PE frames are written. Both now exist.

**Cost:** The lead can repeat finished work, commission an unnecessary script change, or leave existing seams unresolved.

**Exact fix:** Replace those instructions with:

1. **Calendar:** “The course-list weeks value is 28. Calendar course days continue through the band; school days and weeks restart each year. The stored calendar matches this frame.”
2. **Owned standards:** “Sensitive units own no indicator. Their Owned standards cells may be blank or say ‘None’; the current checker accepts either.”
3. **Existing neighbor frames:** “Reconcile against PE units 6, 12 and 18 and the existing SEL frame. Replace conditional timing statements with the actual order. SEL kindergarten unit 2 teaches feeling words and calming in weeks 5 to 10, before health unit 3 in weeks 14 to 18. Health grade 1 unit 9 teaches the health goal plan before SEL unit 12, so SEL reuses that earlier health work where applicable. Name one shared card and routine in both frames.”

Update the corresponding cross-subject text. Keep dated reviews as historical records.

## Coverage, sequence and time

The band structure is sound. Every year touches all eight standards, and all unique indicator owners remain in non-sensitive units. Sensitive units have replacement uses for their days, while units 4, 7 and 13 preserve annual non-sensitive help routes.

The major models appear before their stated later uses. The progression-based handoffs into grade 3 are coherent, but agreement with the receiving frame remains unverified because that frame is absent.

The annual arithmetic is correct: 28 lessons of 30 minutes gives 14 hours per year. The frame discloses its smaller dose and explains its check placement. The historical 40-hour comparison was read as a repository-attributed claim, not independently reverified here.

No unit is demonstrably far over or under its share at frame level. The fuller skill units receive five or six lessons, while the two-lesson sensitive units introduce no unique indicator. Actual feasibility still needs lesson-level timing, especially classroom washing, individual communication evidence and the additions identified above. HECAT asks for sufficient time to introduce, reinforce and develop the planned skills. [Appendix 5, PDF page 2, printed APX-19](https://www.cdc.gov/healthy-youth/hecat/pdfs/HECAT_Appendix_05.pdf).

## Health lens checklist

“Met” below means specified adequately at frame level, not verified in finished lessons.

| Lens requirement | Result |
|---|---|
| Named healthy behaviors and useful facts | Met as a planning commitment |
| Skills explained, modeled, practiced and given feedback | Met as a planning commitment; performance evidence needs finding 2 |
| Norms and social pressure addressed | Met at frame level through ads, refusal and pressure scenes |
| No fear, shame or blame | Met |
| Families, trusted adults and help routes included | Met |
| Inclusive participation without required disclosure | Met; retain these protections in finding 2 |
| Enough time and return across years | Met provisionally; classroom feasibility untested |
| All eight standards reached | Met each year |
| Each skill standard practiced in two topics | Missed in part: finding 3 |
| Coverage map identifies teaching locations | Unit-level topic/outcome tags present; full map remains due at scope stage |
| No topic left as a single isolated band lesson | Met at frame level |
| Sensitive units removable without losing unique skills | Met |
| Getting help taught outside sensitive units | Met every year |
| Indicators used within the correct span | Met |
| Each unit names behavior outcomes | Met |
| End-of-unit assessment goes beyond fact recall | Met in intent; action evidence needs finding 2 |
| Skills have steps, models and practice | Met in intent |
| Figures have sources and dates | Required by frame; actual lesson figures unjudged |
| Content fits the age | Provisionally met; module and medical reads remain due |
| Home links and required family notes | Met |
| NHES wording is expressed in original words | Met; paraphrases must retain full meaning, finding 1 |
| No tasks demand personal health or family history | Met |
| No scenarios blame bodies, illnesses or family types | Met |
| No weighing, calorie counting or good/bad food labels | Met |
| Suicide/self-harm method and crisis safeguards | Not applicable to this band’s content |
| Tools collect no health information or give medical advice | Met as an explicit constraint |
| Health uses science appropriately | Met: early plain facts are taught locally, without an unavailable science prerequisite |
| Health and PE divide their work | Met in principle; finish reciprocal references under finding 5 |

## What is right and should remain

- The Year column, continuous unit numbering and complete annual assessment structures.
- The non-sensitive ownership of every unique indicator.
- The removable sensitive units, advance family notes and disclosure-handling directions.
- Correct body names in the specifically settled non-sensitive location, with the existing person-read requirement.
- Paper access, read-aloud scenarios, communication accommodations and character alternatives.
- Safe-list goals, without grading children’s bodies, home circumstances or health outcomes.

## Settled by the expert

| Choice | Reason | File touched by a later fix |
|---|---|---|
| Keep 17 units, 84 lessons and existing indicator owners | No structural omission or allocation defect warrants reorganization | Health frame |
| Restore helper qualities and community effects inside existing units | These complete existing indicator claims | Frame, owner-row notes, local indicator description |
| Require observable action while retaining character alternatives | Evidence must match the claimed action without requiring disclosure | Frame assessment rules and units 6 and 15 |
| Name a physical activity goal application in unit 15 | Secures goal-setting across two topics | Health frame |
| Correct totals to $14 base and $44 with both kindergarten options | Direct sum of the listed costs | Health frame |
| Replace obsolete lead instructions with current status | Prevents duplicate work | Health frame; reciprocal seam text |

## For Cory

- **Money:** The proposed $30 materials ceiling is not settled. The listed kindergarten base is $14 under the stated school-stock assumptions; including both optional purchases totals $44. Decide the ceiling using those corrected figures.

No new audience, staffing or sensitive-topic scope decision is needed from this read.

## What I could not judge

- Finished lesson timing, assessment scoring quality or classroom effectiveness.
- Complete medical and scientific accuracy, which requires the separate dated unit/day read.
- Full coverage of all HECAT topic-module expectations. I checked the PHW PreK-to-2 knowledge table, not all nine modules. Its dental-care expectations confirm that the frame’s dental candidate needs a recorded disposition during module planning. [PHW module, PDF page 3, printed PHW-3](https://www.cdc.gov/healthy-youth/hecat/pdfs/hecat_module_phw.pdf).
- The receiving health grades 3-to-5 frame.
- Current purchase prices or the historical national-hours citation.

## Outside sources and memory

- [SHAPE America, 2024 NHES](https://shapeamerica.org/standards/health/new-he-standards/): checked the band’s indicator actions and required elements.
- [CDC HECAT 2021 edition](https://www.cdc.gov/healthy-youth/hecat/2021-edition.html): confirmed the review tool and module structure.
- [HECAT Appendix 5](https://www.cdc.gov/healthy-youth/hecat/pdfs/HECAT_Appendix_05.pdf): checked sequencing, cross-topic practice and time expectations.
- [HECAT Appendix 7](https://www.cdc.gov/healthy-youth/hecat/pdfs/HECAT_Appendix_07.pdf): checked assessment alignment.
- [HECAT Personal Health and Wellness module](https://www.cdc.gov/healthy-youth/hecat/pdfs/hecat_module_phw.pdf): checked the PreK-to-2 knowledge table.

**For the source list:** Appendix 7 is useful for the health assessment guidance. No source access workaround was used.

Saved memory supplied report-format guidance only. No substantive finding rests on memory.


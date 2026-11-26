# Independent frame read: Visual Arts, grades 6 to 8

Date: 2026-11-25  
Course: `visual-arts-grades-6-to-8`  
Read-only review. No files changed or report file created.

## Verdict

**Revise before writing the scope and sequence.** The ownership, three complete years, unit order and annual totals are sound, but two standards are narrowed in teaching, several assessment descriptions accept incomplete evidence, and the shorter schedules contain unresolved instructions. Correct those points while preserving the existing units and 64-session annual totals.

**Finding count: 8.**

## What I read and checked

- The complete course frame, its `course-list.csv` selector, `frames.csv` entry and calendar rows.
- All 24 progression rows selected by `grade:6|7|8&strand:va`, their 45 standards, words-file lines, prerequisite rows and outgoing handoffs.
- The neighboring visual arts frames’ seams, models and relevant units.
- `frame-read.md`, the after-core provisions of `frame-write.md`, `EXPERT.md`, the arts lens, arts `STANDARD.md` and `APPROACH.md`, and the shared core and arts part of `ADOPTION-BAR-SUBJECTS.md`.
- Foundation, approach, production guidance, relevant arts decisions, and earlier arts pre-work, progression and frame reviews.
- The cited Units rows in grade 6 social studies, grades 6 and 8 ELA, and grade 7 mathematics.
- Outside sources linked below.

There is no base text, so a base-text source map is not applicable.

| Check | Result |
|---|---|
| `python -B -X utf8 scripts/plan.py check visual-arts-grades-6-to-8` | One failure: the later plan stage requires `days.csv` and assessment data, which do not exist yet. Review continued. |
| `python -B -X utf8 scripts/frame.py check visual-arts-grades-6-to-8` | **0 failures:** 12 units, 180 unit sessions, 12 course check and respond sessions. |
| `python -B -X utf8 scripts/stale.py check` | **0 failures** across 121 files. Unmarked stale notes remain, described in finding 8. |
| Independent ownership comparison | All 24 skills and 45 IDs occur exactly once, in their correct years. |

The plan check was course-filtered because the repository instructions prohibit running it unfiltered. `-B` prevented bytecode-cache writes.

## Findings, most serious first

### 1. Grade 7 teaching narrows two owned standards

**Severity:** Major  
**LAYER:** frame, progression, standard  
**REPEAT:** yes, narrowing a standard through its local description recurs in the kindergarten-to-grade-2 reads.  
**Confidence:** firm.

**Location:** Frame units 6 and 7, lines 267 and 268; year 7 year-end check, line 282; `va-g7-ideas`, `va-g7-judge`, and their words-file lines.

Unit 6 teaches written production instructions, modeled on wall-drawing instructions, and checks whether a partner can follow them. That does not necessarily teach the student to establish success criteria for an intended result. Unit 7 teaches interpretation as finding meaning but never explicitly requires mood.

These distinctions are present in the national standards. [NCAS visual arts standards, PDF pages 1 and 7](https://www.nationalartsstandards.org/sites/default/files/Visual%20Arts%20at%20a%20Glance%20-%20new%20copyright%20info.pdf).

**Exact fixes:**

- For `VA:Cr1.2.7a`, retain the instructions activity, but add a student-written goal and three observable success criteria. Require the student to use those criteria while making and reviewing the perspective work. Score the goal, criteria and their use on the existing kept card. Make the year-end task ask for success criteria too.
- For `VA:Re8.1.7a`, add an explanation of both the work’s idea and its mood, supported by its making, form, structure, context, subject and media. Add mood to the unit item and year-end item.
- The lead should update the corresponding progression descriptions and words-file lines. Suggested short lines:
  - `VA:Cr1.2.7a`: “Set success criteria that guide making toward an identified artistic goal.”
  - `VA:Re8.1.7a`: “Explain ideas and mood through making, form, structure, context, subject, and media.”

**Why it matters:** A scope writer could follow the present frame exactly and leave these actions untaught.

### 2. Five end-of-unit evidence descriptions are narrower than the teaching

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, incomplete standard-to-evidence links recur in both earlier visual arts bands.  
**Confidence:** firm.

**Location:** Units 1, 4, 8 and 12, lines 262, 265, 269 and 273.

The frame’s teaching descriptions and local words file establish broader actions than these evidence lines require.

| Unit and ID | Gap | Exact fix |
|---|---|---|
| **1, `VA:Re7.2.6a`** | The item checks visual parts and persuasion but omits cultural associations. | Require one visual feature and one cultural association, explaining how each contributes to the intended influence. Carry this requirement into the mid-year item. |
| **4, `VA:Pr4.1.6a`** | “Flat” plus “3D or digital” permits one category to go unchecked. | Score the existing three-column chart covering flat, 3D and digital work, with comparisons addressing preservation and presentation. |
| **4, `VA:Cn11.1.6a`** | The item names era, custom and materials but omits cultural uses. | Add what each work was used for and how that use relates to its time, tradition and available materials. |
| **8, `VA:Pr4.1.7a`** | One technology affecting keeping, showing **or** seeing permits a single isolated effect. | Require a before-and-after comparison addressing preservation, presentation and viewer experience. Score a kept comparison card to protect sitting time. |
| **12, `VA:Pr6.1.8a`** | The item accepts how choices influence thoughts **or** beliefs; why and visitor experience disappear. | Require a reason for the exhibition’s influence, a mechanism in its arrangement or interpretation, and consequences for visitors’ ideas, beliefs and experience. |

**Why it matters:** Naming an ID beside an item does not establish that the full taught action was assessed. These corrections fit existing ownership and need no additional course days.

### 3. Two shorter-schedule instructions would produce an incomplete or impossible plan

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes for shorter-path assessment and calendar instructions; the quarter-wheel mismatch is new in the reports checked.  
**Confidence:** firm.

**Location:** “The once-a-week path,” lines 28 to 40; “Rotations,” lines 41 to 43; unit 11, line 272.

There are two separate problems:

- The once-a-week path moves unit 11’s analysis item to the year-end sitting. Unit 11 then lacks its own complete end-of-unit evidence and response for that ID.
- A daily quarter wheel cannot contain 64 sessions. This repository’s 160-day calendar gives a quarter about 40 teaching days.

**Exact fixes:**

1. In unit 11’s merged check, use one unseen work and one written response that combines the argued judgment with an explanation of how the work builds message and mood. Score `VA:Re8.1.8a` and `VA:Re9.1.8a` separately. Keep the year-end task as a new cumulative sample.
2. Replace the Rotations paragraph with:

   > A daily rotation with at least 64 meetings runs the full path in order. A quarter rotation with at least 32 meetings runs the marked 32-session path, retaining every unit, assessment, critique, revision and respond session. The school places its course checks on its rotation calendar.

**Why it matters:** The current wording either postpones a unit’s evidence beyond its respond session or promises more meetings than the named rotation supplies.

### 4. Several “free paths” do not work with the promised ordinary room

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** new in the earlier arts reports checked.  
**Confidence:** firm for the mismatch; judgment call for the particular substitutes below.

**Location:** Ordinary room and supplies bullets, lines 131 to 140; units 1, 5 and 9.

Unit 1 requires charcoal, ink wash and chalk pastel, but its free path supplies pencils and borrowed charcoal. Unit 5 assumes a shared watercolor set and pen. Unit 9’s free path explicitly buys new foam trays and still requires paint and additives. These are inexpensive options, but they do not fulfill the stated paper, pencils and found-material route.

**Exact fix:** Give each unit a complete alternative technique and matching evidence description:

- **Unit 1:** Permit experiments with graphite methods on different found paper and card surfaces. Assess genuine experimentation and reflection rather than requiring three named commercial media.
- **Unit 5:** Offer graphite drawing combined with layered found-paper collage, secured by folds or tabs, developed across at least four sessions. Keep the process log and persistence evidence.
- **Unit 9:** Offer a cardboard-relief rubbing edition using paper and graphite, with registration marks and three impressions. Keep the planned risk, source labels and reflection. Retain two-color foam printing as the supplied-material option.

Name the alternative step cards explicitly. A student using an alternative must be able to earn every owned ID without obtaining the optional materials.

**Why it matters:** Otherwise the first teacher without those supplies must invent a different unit.

### 5. The one-point-perspective example needs correction

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, inaccurate artwork explanations recur in the grades 3 to 5 read.  
**Confidence:** likely, with the access limit below.

**Location:** Unit 6, line 267.

The frame calls *Paris Street; Rainy Day* “a street in one-point perspective.” The Art Institute’s indexed technical account describes distinct vanishing points in the finished painting. The Musée Marmottan Monet’s account of its related study also describes multiple vanishing points. [Art Institute technical catalog](https://publications.artic.edu/caillebotte/reader/paintingsanddrawings/section/574/p-42), [Musée Marmottan Monet, related study](https://www.marmottan.fr/en/notice/5062/).

**Exact fix:** Replace the clause with:

> A complex street composition using multiple vanishing points. Students first learn one-point perspective from a Curio Class original diagram, then compare that simplified construction with Caillebotte’s composition.

Keep one-point perspective as the taught technique.

**Why it matters:** A teacher following the present description could ask students to force the painting’s receding lines toward one point and treat correct observations as mistakes.

**Access status:** The Art Institute catalog page returned **403, browser check**. It was not fetched another way. The independent museum account opened successfully.

### 6. The cross-band work-selection check is no longer merely pending

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** new for these cross-band repetitions.  
**Confidence:** firm.

**Location:** Units 1, 2, 7, 11 and 12; “For the lead,” item 4, lines 345 to 346.

The existing grades 3 to 5 frame already selects all five of these:

| Work | Earlier placement | Placement here |
|---|---|---|
| *The Migration Series* | Grade 3, unit 4 | Grade 6, unit 1 |
| *The Block* | Grade 3, unit 1 | Grade 6, unit 2 |
| *State Names* | Grade 5, unit 9 | Grade 7, unit 7 |
| *The Great Wall of Los Angeles* | Grade 4, unit 6 | Grade 8, unit 11 |
| *Nation to Nation* | Grade 5, unit 12 | Grade 8, unit 12 |

The higher-grade tasks are harder, but the brief asks writers to avoid repeating another grade’s picks. The frame instead leaves reconciliation to a future check.

**Exact fix:** Keep the earlier band’s selections and use these replacements here:

- Unit 1: Lawrence’s [*Street to Mbari*, 1964](https://www.nga.gov/artworks/79459-street-mbari).
- Unit 2: Bearden’s [*The Woodshed*, 1969](https://www.metmuseum.org/art/collection/search/480708).
- Unit 7: Smith’s [*Trade (Gifts for Trading Land with White People)*, 1992](https://whitney.org/guides/87?language=en&open=true&stop=14396), retaining Minard for the map-design example.
- Unit 11: Baca’s *La Memoria de Nuestra Tierra*, dedicated in 1996, documented in [the artist’s own record](https://www.judybaca.com/now/images/stories/downloads/2007_JudyBaca_CV.pdf).
- Unit 12: [*Native New York*](https://americanindian.si.edu/explore/exhibitions/item?id=981), retaining Davidson’s pole.

Update the associated setting and sensitivity notes, and use descriptions with links under the existing rights rule. Replace the pending lead note with the completed reconciliation list.

**Why it matters:** This preserves the intended growth in interpretation while widening the works students encounter.

### 7. The intensive vocabulary commitment exceeds the arts approach

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, the same mismatch appears in the grades 3 to 5 read.  
**Confidence:** firm.

**Location:** Reading load, lines 148 to 153.

The frame promises five or six words taught in depth. Arts `APPROACH.md`, “Supports,” specifies three to five.

**Exact fix:** Replace that commitment with:

> Each unit selects three to five discipline words for teaching in depth, with a picture, gesture and sentence frame. Other listed words are introduced in context and revisited.

Keep the vocabulary needed for the standards.

**Why it matters:** The next writer needs one consistent instruction about the fuller language-support treatment.

### 8. Unmarked process notes contradict accessible sources and completed repository work

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, obsolete implementation and calendar notes recur in the earlier arts reads.  
**Confidence:** firm for the inspected snapshot.

| Location | Problem | Exact fix |
|---|---|---|
| Frame Days bullet and “For the lead,” item 2 | The middle-school time source remains unread and pending. | Replace the pending text with: “The association’s middle-school checklist specifies no numerical weekly minimum. It permits several scheduling patterns. Our doses are 80 minutes weekly, or 40 on the shorter path; no numerical gap can be calculated from this checklist.” [Middle-school opportunity-to-learn checklist](https://www.arteducators.org/wp-content/uploads/2025/09/OTL-Middle_School_Visual_Media_Arts_Program.pdf). Update `STANDARD.md` 3.4 accordingly. |
| “For the lead,” item 1 | It says both checks avoid every core check week, although week 32 is shared under the finals exception. Its coordination note omits the other arts courses. | State that week 17 avoids core checks and week 32 uses the finals exception. Record the current same-day overlap with dance, media arts and theater on school day 83; physical education’s check window also spans that day. Leave scheduling changes to the lead’s shared calendar pass. |
| Grades 9 to 12 frame, lines 192 to 195 | It says this grades 6 to 8 frame has not been written. | Replace with: “The grades 6 to 8 frame places all eight grade 8 threads; the receiving Level 1 units below retrieve them after the bridge.” |
| `ADOPTION-BAR-SUBJECTS.md`, arts pre-work row | It still lists the standards gate and loading the 63 high-school music IDs as owed. | State that the gate and loading are complete, consistent with arts `STANDARD.md`, and retain only genuinely outstanding work. |

**Why it matters:** These notes would send later workers toward unnecessary checks or incorrect assumptions. The marked-note gate does not catch them.

The existing request to correct `VA:Cn10.1.7a` from generic documentation to a visual record remains valid. It is already recorded under “For the lead” and is not counted again here.

## Coverage, days and seams

| Year | Units | Skills | Owned IDs | Unit sessions | Course checks and respond | Total | Short path |
|---|---|---:|---:|---:|---:|---:|---:|
| 6 | 1 to 4 | 8 | 15 | 60 | 4 | 64 | 32 |
| 7 | 5 to 8 | 8 | 15 | 60 | 4 | 64 | 32 |
| 8 | 9 to 12 | 8 | 15 | 60 | 4 | 64 | 32 |

No skill or ID is missing, duplicated or assigned to the wrong year. All thirteen progression models are represented.

The longer opening studio units and the additional time for unit 11 have defensible reasons. No unit is demonstrably far over or under its load at frame level. The short-path arithmetic also works; finding 3 concerns its instructions and assessment placement.

The eight incoming and eight outgoing thread handoffs match the progression and neighboring frames. All four named core-subject dependencies are available before use:

| Dependency | Core availability | Visual arts use |
|---|---|---|
| Grade 6 early humans | Social studies unit 2, days 11 to 25 | Unit 4, school days 123 to 155 |
| Grade 6 argument | ELA unit 2, days 33 to 58 | Unit 3, school days 88 to 120 |
| Grade 7 scale drawings | Mathematics unit 1, days 1 to 12 | Unit 7, school days 88 to 120 |
| Grade 8 argument | ELA unit 2, days 31 to 62 | Unit 11, school days 88 to 125 |

Each lean has a local fallback. Mid-year checks avoid core checks; year-end checks use the permitted week 32 finals window.

## Arts lens checklist at frame level

“Met” describes a frame commitment, not verification of unwritten lessons.

| Lens check | Result |
|---|---|
| Correct band-year ownership; four processes each year | Met |
| Technique taught directly and becoming harder | Met, subject to finding 5 |
| Discipline words taught and used in responses | Met, with finding 7 |
| Original work, choice and a showing in every unit | Met |
| Critique protocol followed by revision | Met |
| Works from multiple regions, periods and living makers | Met in the annual design; reconcile finding 6 |
| Works taught with maker, time, place and purpose | Committed; precise sources and final work cards remain for unit planning |
| Assessment includes making, showing and response | Met in form; correct findings 1 to 3 |
| Growth, self-assessment and retained work | Met |
| Realistic non-daily schedule | Partly met, finding 3 |
| Setup and cleanup inside the period | Met as a stated commitment |
| Equipment and no-cost alternatives | Partly met, finding 4 |
| Visual arts hazards and controls identified | Met as a frame commitment; detailed safety read remains |
| Participation without solo performance | Not applicable to this design |
| Artistic responding distinguished from respond days | Met |
| Tools do not judge finished artwork | Met |
| Visual arts remains a distinct discipline | Met |
| Dance/PE duplication and music/fractions confusion | Not applicable |
| Original questions and assessment design | Met in the frame |

## What is right and should be preserved

Preserve the three complete years, four-unit annual structure, reciprocal handoffs, technique progression, critique followed by revision, and separate scores for individual contributions to group work.

Keep the paper and home paths, locally retained portfolios, public or invented alternatives to personal disclosure, community-source requirements, and explicit notice that leaving out a unit removes its standards claim.

## Settled by the expert

These are corrections for the caller to apply. No edits were made.

| Choice | Reason | Files affected |
|---|---|---|
| Separate success criteria from production instructions; restore mood | Preserve full owned actions | Frame, progression descriptions, words file |
| Expand the five evidence descriptions | Prevent incomplete evidence earning “met” | Frame |
| Combine unit 11’s analysis and argument on its short-path check | Keep assessment and response inside the unit | Frame |
| Use the 32-session path for a quarter rotation | Fit the stated calendar | Frame |
| Add complete dry and found-material alternatives | Make the ordinary-room promise usable | Frame and later unit plans |
| Correct the perspective explanation | Avoid teaching a false construction | Frame |
| Use the five named replacement works | Resolve cross-band repetition | Frame |
| Select three to five intensive vocabulary words | Match the approved approach | Frame |
| Refresh the identified process notes | Reflect current evidence | Frame and named shared documents, through the lead |

No standard needs to move between units.

## For Cory

- **Money:** The proposed ceiling of **$100 per class of 30 per year** remains Cory’s decision. The annual estimates of $60, $70 and $100 are planning figures, not verified prices. The complete no-purchase paths should remain regardless of that decision.

No new scope, audience or outside-person decision is needed for these corrections.

## Sources, confidence and limits

The standards sources used were the [NCAS visual arts handout](https://www.nationalartsstandards.org/sites/default/files/Visual%20Arts%20at%20a%20Glance%20-%20new%20copyright%20info.pdf), [official grades 6 to 8 handbook](https://www.nationalartsstandards.org/customize-handbook?discipline=Visual+Arts&grade_level=6th%2C7th%2C8th&process=Creating%2CPerforming%2FPresenting%2FProducing%2CResponding%2CConnecting), and [association-hosted standards handbook](https://www.arteducators.org/wp-content/uploads/2025/06/National-Visual-Arts-Standards-Custom-Handbook.pdf). Artwork and scheduling sources are linked beside their uses above.

The named [federal Art and Craft Safety Guide](https://www.cpsc.gov/s3fs-public/5015.pdf) and [California art-hazards guidance](https://oehha.ca.gov/risk-assessment/art-hazards) are accessible. This review confirmed their availability, not the safety of every proposed activity.

Two source pages returned **403, browser check**: the Art Institute technical catalog linked in finding 5 and the [holding museum’s *Trade* record](https://chrysler.emuseum.com/objects/29112/trade-gifts-for-trading-land-with-white-people). Neither was fetched another way. Independent museum sources opened for both.

Final permissions, supply prices, accommodations, scoring samples and classroom timing cannot be certified from this frame. The shared approach’s safety and critique background remains marked **from memory** pending its specified reads. **No curriculum finding here rests on model memory; prior-run memory was used only for review-format guidance.**

**For the source list:** Add the middle-school scheduling checklist, the accessible museum sources supporting the replacement works, and the two browser-check records with their access status.


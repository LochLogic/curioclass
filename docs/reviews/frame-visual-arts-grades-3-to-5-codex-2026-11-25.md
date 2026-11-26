# Independent frame read: Visual Arts, grades 3 to 5

Date: 2026-11-25  
Course: `visual-arts-grades-3-to-5`  
Read-only review. No files changed or report file created.

## Verdict

**Revise before writing the scope and sequence.** The three complete years, progression ownership, unit order and session totals are sound, but several assessment summaries do not establish the full actions they claim, and two artwork explanations need correction. Repair those links first, preserving the existing units and annual day totals.

**Finding count: 5.**

## What I read and checked

- The complete course frame, its `frames.csv` entry, its `course-list.csv` selector, and its calendar rows.
- All 24 progression rows selected by `grade:3|4|5&strand:va`, their 45 owned IDs and words-file lines, and the national visual arts standards for these grades.
- The neighboring visual arts frames’ seam and model tables, the departing grade 2 units and receiving grade 6 units.
- `frame-read.md`, the after-core provisions of `frame-write.md`, `EXPERT.md`, the arts lens, arts `STANDARD.md` and `APPROACH.md`, and the shared core and arts part of `ADOPTION-BAR-SUBJECTS.md`.
- Foundation, approach and production guidance; relevant arts decisions; earlier arts pre-work, progression and kindergarten-to-grade-2 frame reviews and fixes.
- The relevant Units rows in the grade 3 ELA and grade 4 mathematics frames.

There is no base text, so a base-text source map is not applicable.

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Stopped while checking another course because Python package `markdown` is unavailable. |
| `python -X utf8 scripts/plan.py check visual-arts-grades-3-to-5` | Reports the expected frame-stage absence of `days.csv` and assessment data. |
| `python -X utf8 scripts/frame.py check visual-arts-grades-3-to-5` | **0 failures:** 12 units, 180 unit sessions, 12 course check and respond sessions. |
| `python -X utf8 scripts/stale.py check` | One marked stale note in the physical education grades 9 to 12 frame; the visual arts review continued. |
| Ownership comparison | All 24 selected skills and 45 owned IDs occur exactly once, in their correct years. |
| Calendar comparison | All six course checks avoid core check weeks; the frame’s after-core clash note is outdated. |

## Findings, most serious first

### 1. Five IDs have assessment evidence narrower than their taught actions

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, incomplete standard-to-evidence links recur in both kindergarten-to-grade-2 visual arts reads.  
**Confidence:** firm.

**Location:** `docs/courses/visual-arts-grades-3-to-5/frame.md`, units 1, 3, 4 and 8, lines 261, 263, 264 and 268; “Scored evidence,” lines 85 to 105; grade 3 year-end check, line 279.

The frame now names evidence ID by ID, which is a substantial improvement over the pilot’s earlier form. Naming the ID does not resolve these remaining gaps. The national demands and the arts approach’s requirement to assess every part support the following corrections. [NCAS visual arts standards, PDF pages 2, 4, 5 and 7](https://www.nationalartsstandards.org/sites/default/files/Visual%20Arts%20at%20a%20Glance%20-%20new%20copyright%20info.pdf).

| Unit and ID | Problem | Exact fix |
|---|---|---|
| **1, `VA:Cr2.2.3a`** | Each child demonstrates one tool, selected from three processes. This cannot establish handling across different processes. | Record a brief handling demonstration for printing, collage and modeling for every child. Give unit 1 two check sessions within its existing 18 days: a practical check replacing one fluency session, followed by the written check. The practical session can use 3 minutes of setup, six five-minute groups and 6 minutes of cleanup. Within each group, observe children individually through the three brief actions. Revise the general check-day description to permit this studio check. |
| **3, `VA:Re8.1.3a`** | The learning line includes form; the scored item and grade 3 year-end item mention subject and mood but omit form. | Add a scored explanation of how the medium creates a visible feature of form, such as texture, shape or arrangement, and how that contributes to meaning. Add the same requirement to the year-end item. |
| **4, `VA:Pr6.1.3a`** | Teaching covers three cultures, but the item accepts an account of only one. | Require how and where **two cultures** record stories or history. Use a kept two-work card, scored with the showing, to avoid lengthening the written sitting. |
| **8, `VA:Pr4.1.4a`** | The learning line names emerging technology, but the item requires only one old and one new technology. | Require an earlier, a current and a developing technology, with an explanation of what each changes about keeping or showing art. Identify the developing example and its museum source in the teaching cards. |
| **8, `VA:Pr5.1.4a`** | The evidence asks children to name setting, duration and format. Naming these categories does not demonstrate analysis of their consequences. | Add a reason for each protection choice. Include brief paired cases covering indoor/outdoor, temporary/permanent and physical/digital conditions, with the child explaining how a changed condition changes the plan. Score these on the existing kept plan card. |

**Why it matters:** A writer could build exactly the stated items and award “met” while an owned action remains untested. Unit 1 also needs its wider practical evidence to fit an explicit, observable schedule.

These are evidence corrections within existing ownership. No standard needs to move between units.

### 2. Two artwork explanations would give teachers inaccurate context

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, exact artwork identification and source accuracy were findings in the kindergarten-to-grade-2 visual arts reads.  
**Confidence:** firm for the map correction; likely for removing the unsupported reception claim.

**Location:** Unit 9, line 269; unit 11, line 271.

**State Names:** The sensitivity note says the map names Native nations whose lands became states. The museum explains that Smith retained state names derived from Indigenous sources while removing European-derived names. Those are different claims. [Smithsonian American Art Museum, *State Names*](https://americanart.si.edu/artwork/state-names-73858).

**Exact fix:** Replace that sentence with:

> Smith leaves visible state names derived from Indigenous sources and removes European-derived names. The work challenges the division and naming of land already occupied by Native peoples.

**The Cradle:** The frame says this painting was called unfinished by the judges of its day. The holding museum instead reports limited attention at the 1874 exhibition and praise from important critics for its grace and elegance. The frame provides no source for its specific “unfinished” claim. [Musée d’Orsay, *Le Berceau*](https://www.musee-orsay.fr/en/artworks/le-berceau-1132).

**Exact fix:** Replace the reception clause with:

> Exhibited in 1874; the museum records little attention and some critical praise for its grace and elegance.

Build the comparison of judging standards from named, sourced criteria on the setting cards. Do not use the unsupported “unfinished” claim as the historical contrast.

**Why it matters:** These explanations carry the cultural interpretation and historical judging work. Errors here would become premises students are expected to repeat.

### 3. Unit 9 introduces neatness as a scoring condition

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** new in the earlier arts reports checked.  
**Confidence:** firm.

**Location:** Unit 9, line 269, evidence for `VA:Cr2.2.5a`.

The finished piece must show “clean edges, clean color.” These conditions can mark an intentional rough edge, bleeding wash or mixed color as deficient. The arts approach explicitly excludes neatness from scoring. The national craftsmanship demand centers on care and use of materials and equipment. [NCAS visual arts standards, PDF page 2](https://www.nationalartsstandards.org/sites/default/files/Visual%20Arts%20at%20a%20Glance%20-%20new%20copyright%20info.pdf).

**Exact fix:** Replace the product look-for with:

> The child uses and cares for the chosen materials and equipment appropriately: controls the wash or scratch-through as intended, protects shared supplies, and cleans and stores tools correctly. Deliberate rough edges, bleeding or mixed colors are accepted when they serve the child’s stated choice.

Keep the brush-and-palette demonstration. Remove “clean edges, clean color” as universal requirements.

**Why it matters:** The current wording risks grading stylistic conformity and motor control instead of the intended craftsmanship.

### 4. The English learner commitment exceeds the approved vocabulary load

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** new for this specific mismatch.  
**Confidence:** firm.

**Location:** “Reading load,” lines 150 to 154, and the unit word lists.

The frame promises to teach three to six words in depth per unit. Arts `APPROACH.md`, “Supports,” specifies three to five. The six-word lists need not be reduced, but the frame currently promises intensive treatment of all six.

**Exact fix:** Replace the relevant sentence with:

> Each unit selects three to five discipline words for teaching in depth, with a picture, a gesture and a sentence frame. Other listed words are introduced in context and revisited.

In each unit plan, identify the selected words. Keep the full vocabulary needed for the standards.

**Why it matters:** This preserves the agreed language support load and tells the next writer which words need the fuller instructional treatment.

### 5. Two lead notes describe work that the repository no longer supports

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, obsolete implementation and calendar notes recur in the earlier arts reads.  
**Confidence:** firm for the inspected snapshot.

**Location:** “For the lead,” items 1 and 3, lines 321 to 330.

The frame says there are four clashes, all with physical education, and none in grade 4. Current calendar rows and `frame.py calendar` show additional clashes. The spelling note also asks for a correction already present in `va-g5-design`.

**Exact fix:** Replace item 1’s clash list with this current snapshot, identifying the courses sharing each visual arts check week:

| Grade | Week | Other courses |
|---|---:|---|
| 3 | 18 | Physical education |
| 3 | 26 | Computer science, dance, media arts, physical education, SEL |
| 4 | 17 | Dance, media arts, theater |
| 4 | 25 | Media arts |
| 5 | 18 | Computer science, dance, ELD, media arts, physical education, theater |
| 5 | 26 | Dance, physical education, SEL |

Retain the instruction that the lead coordinates the shared calendar pass. Do not independently move another course’s checks.

Delete item 3’s outstanding spelling request: the progression row already says **“labeled.”** Remove its reference to nonexistent “Row changes below.”

**Why it matters:** The current notes understate coordination work and send the lead toward an unnecessary edit. These concurrent calendar clashes do not invalidate this frame’s compliance with the requirement to avoid core check weeks.

## Coverage, days and seams

| Year | Units | Skills | Owned IDs | Unit sessions | Course checks and respond | Total | Short path |
|---|---|---:|---:|---:|---:|---:|---:|
| 3 | 1 to 4 | 8 | 15 | 60 | 4 | 64 | 32 |
| 4 | 5 to 8 | 8 | 15 | 60 | 4 | 64 | 32 |
| 5 | 9 to 12 | 8 | 15 | 60 | 4 | 64 | 32 |

No skill or ID is missing, duplicated or assigned to the wrong year. Earlier-grade content is explicitly retrieved or practiced, including grade 4 symmetry used in grade 5.

The allocations have defensible reasons. The opening studio units establish routines and techniques; unit 8 receives additional time for five IDs and a made tradition piece; unit 10 receives additional time for the work and artist statement. No unit is demonstrably far over or under its load at frame level.

Both pacing paths add up. The short paths preserve the stated course check weeks, with response one week later. Exact day merges and the expanded practical assessment still need to be made explicit in the scope and sequence.

The eight incoming and outgoing thread handoffs match the neighboring frames. Grade 3 ELA introduces collaborative discussion before this course’s unit 2. Grade 4 mathematics teaches symmetry before its grade 5 use here. Both contacts have local retrieval or fallback provisions.

## Arts lens checklist at frame level

“Met” describes the frame commitment, not certification of unwritten lessons.

| Lens check | Result |
|---|---|
| IDs in the correct band year | Met |
| All four artistic processes each year | Met |
| Works span traditions and periods, including living makers | Met in the annual design |
| Technique becomes harder across units and years | Met |
| K to 8 schedule avoids a daily-period requirement | Met |
| Every unit has a showing | Met |
| Technique taught before independent making | Met |
| Discipline words taught and used in responses | Met, with finding 4 |
| Works taught with setting | Partly met: correct finding 2 |
| Critique follows a protocol | Met |
| Revision follows feedback | Met |
| Assessments go beyond vocabulary recall | Met; coverage needs finding 1 |
| Questions and assessments are original | Met in the frame |
| Setup, assessment and cleanup fit the session | Practical check needs finding 1 |
| Equipment has free alternatives | Met |
| Visual arts hazards and controls are identified | Met as a frame commitment; detailed safety read remains |
| Participation without solo performance | Not applicable to this visual arts design |
| Artistic responding distinguished from respond days | Met |
| Tools do not judge finished artwork | Met |
| Visual arts remains a distinct discipline | Met |
| Dance/PE duplication and music/fractions confusion | Not applicable |
| Growth, self-assessment and retained work | Met in the design; scoring needs finding 3 |

## What is right and should be preserved

Preserve the three complete years, four-unit annual structure, concrete technique progression, reciprocal handoffs, and critique followed by revision. Keep the paper and home paths, local portfolios, public or invented alternatives to personal disclosures, community-source requirements, and explicit notice that leaving out a unit removes its standards claim.

The published time comparison is correct: 80 minutes weekly on the full path and 40 on the short path are respectively 30 minutes above and 10 below the association’s elementary minimum. [Elementary visual arts opportunity-to-learn standards, PDF pages 3 and 4](https://www.arteducators.org/wp-content/uploads/2025/09/OTL-Elementary_Visual_Media_Arts_Program.pdf).

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Expand the five evidence descriptions in finding 1 | Assess the owned actions without moving ownership | Course frame |
| Separate unit 1’s practical and written checks within 18 days | Make the broader handling evidence observable | Course frame |
| Correct the two artwork explanations | Use the holding museums’ accounts | Course frame |
| Replace neatness conditions with material-use evidence | Preserve artistic choice and the approved scoring rule | Course frame |
| Select three to five words for intensive teaching | Match the arts approach while retaining needed vocabulary | Course frame; subsequent unit plans |
| Refresh calendar notes and remove the completed spelling request | Reflect the current repository snapshot | Course frame |

These are proposed corrections for the caller to apply. No edits were made.

## For Cory

- **Money:** The optional annual estimates remain $60, $50 and $50 per class of 30. The proposed $75 annual ceiling remains Cory’s decision; this review does not approve spending.

No new scope, audience or outside-person decision is needed for these corrections.

## Sources, confidence and limits

- [NCAS visual arts standards](https://www.nationalartsstandards.org/sites/default/files/Visual%20Arts%20at%20a%20Glance%20-%20new%20copyright%20info.pdf): checked the grade 3 to 5 actions against teaching and evidence.
- [Elementary visual arts opportunity-to-learn standards](https://www.arteducators.org/wp-content/uploads/2025/09/OTL-Elementary_Visual_Media_Arts_Program.pdf): verified the weekly time comparison.
- [Smithsonian American Art Museum, *State Names*](https://americanart.si.edu/artwork/state-names-73858): checked the map’s cultural explanation.
- [Musée d’Orsay, *Le Berceau*](https://www.musee-orsay.fr/en/artworks/le-berceau-1132): checked the painting’s date and reception.
- [Metropolitan Museum of Art, *The Block*](https://www.metmuseum.org/exhibitions/listings/2010/romare-bearden?persisted=true&sc_device=default): spot-checked the work’s date, medium and Harlem setting.
- [The Great Wall project history](https://sparcinla.org/programs/greatwallinstitute/history-description/): spot-checked the 1976 beginning and collaborative making.
- [Chicano Park Museum’s historical account](https://chicanoparkmuseum.org/logan-heights-archival-project/chicano-park/): checked the mural tradition and community context.
- [Federal Art and Craft Safety Guide](https://www.cpsc.gov/s3fs-public/5015.pdf) and [California art-hazards guidance](https://oehha.ca.gov/risk-assessment/art-hazards): confirmed the named safety sources are available; this was not the detailed safety read.

I could not certify final artwork permissions, actual supply prices, accommodations, scoring samples or classroom timing from a frame. The course’s safety and critique background remains marked “from memory” pending its specified source-based reads. **No curriculum finding here rests on model memory; prior-run memory was used only for report-format guidance.**

**For the source list:** Retain the specific Smithsonian and Musée d’Orsay records above beside the corrected artwork notes.


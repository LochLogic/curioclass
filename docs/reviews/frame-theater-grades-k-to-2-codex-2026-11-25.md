# Independent frame read: Theater, grades K to 2

**Course:** `theater-grades-k-to-2`  
**Date:** 2026-11-25  
**Mode:** Read only. No files changed.

## Verdict

**Requires changes before the scope and sequence is written.** The frame places all 21 progression rows and all 65 owned ids in their correct years, but several evidence lines narrow the standards, and the shorter path puts first-time assessment inside respond sessions. Correct the standards-to-evidence contract and the shorter-path assessment schedule while preserving the sound unit sequence, annual structure and practical classroom provisions.

**Findings: 6**, ordered most serious first.

This differs from the sound-and-buildable verdict in `docs/reviews/frame-theater-grades-k-to-12-2026-11-25.md`: the placement and arithmetic hold, but the substantive coverage problems below remain.

## What was read and checked

- The complete target frame, its `course-list.csv` selector, `frames.csv` entry and calendar rows.
- All 21 selected theater progression rows for K, 1 and 2, their owned ids and local words-file lines, and the grade 3 handoffs.
- The next theater frame’s course provisions, seams and opening units; the relevant kindergarten, grade 1 and grade 2 ELA Units tables.
- `frame-read.md`, the after-core provisions of `frame-write.md`, `EXPERT.md`, the arts lens, arts adoption bar, `STANDARD.md` and `APPROACH.md`.
- Relevant foundation, calendar, approach, decision and earlier arts review material.
- Outside sources linked below, including the official theater standards.

| Check | Result |
|---|---|
| `python -X utf8 scripts/frame.py check theater-grades-k-to-2` | Passed twice: 0 failures |
| `python -X utf8 scripts/plan.py check theater-grades-k-to-2` | One failure: this frame-stage course lacks the lesson-plan data the command requires; substantive review continued |
| `python -X utf8 scripts/stale.py check` | 121 files checked, 0 failures |
| Independent placement count | 21 selected skills, each placed exactly once |
| Independent annual counts | K: 17 ids; grade 1: 24; grade 2: 24 |
| Independent day count | Each year: 60 unit days plus 2 check and 2 respond days, totaling 64 |

## Findings

### 1. Grade 2 substitutes characters’ decisions for artistic choices

**Severity:** Serious  
**LAYER:** frame, progression  
**REPEAT:** new  
**Confidence:** Firm

**Location:** Target frame, unit 10, its question and `TH:Re7.1.2a` evidence; year 2 year-end check; Seams; progression row `th-g2-notice`.

**Problem:** The unit teaches and checks moments when characters decide something within the plot. `TH:Re7.1.2a` concerns recognizing artistic choices during guided drama. The local words file preserves the distinction by naming artists, but the progression note and frame lose it. The next frame then expects students to explain artists’ decisions. See the [official theater standards, PDF page 6](https://www.nationalartsstandards.org/sites/default/files/2021-11/Theatre%20at%20a%20Glance%20-%20new%20copyright%20info.pdf#page=6).

**Why it matters:** A child could satisfy every stated item without noticing a performer’s choice of voice, movement or delivery.

**Exact fix:**

- Replace the unit’s question ending with: “When do performers choose how to show a character?”
- Teach recognition through two versions of a moment, such as the same line delivered with different voices or gestures.
- Replace the audience-card item with: “Mark the moment a performer chose a voice, movement or gesture; point to or describe that choice.”
- Make the year-end sample and outgoing seam use that same action.
- Rewrite the relevant `th-g2-notice` note around performers’ artistic choices. Keep character problem-solving under `TH:Re9.1.2c`.

No ownership change is needed.

### 2. Several end-of-unit evidence lines omit required parts

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, incomplete assessment contracts also appear in `frame-computer-science-kindergarten-codex-2026-11-25.md`, finding 3  
**Confidence:** Firm

**Location:** Units 6, 7 and 10, “End-of-unit evidence.”

The teaching descriptions are often fuller than the evidence that supposedly establishes completion:

| Unit and id | Gap | Exact fix |
|---|---|---|
| 6, `TH:Pr4.1.1b` | The “no words” showing checks feeling through face, body and gesture, omitting voice and an explicit character trait. | Retain the silent exploration, then add a brief spoken line to the scored showing. The guide records a trait and feeling communicated through face, body, gesture and voice. |
| 6, `TH:Cr3.1.1b` | The talk item compares movements only. | Have the teacher demonstrate two characters with contrasting sounds and movements. Record a similarity and difference across those features. |
| 6, `TH:Re8.1.1c` | The card compares feelings, omitting choices. | Add a picture-supported comparison of what the child or offered invented person would choose and what the character chooses. |
| 7, `TH:Cr1.1.1b` | Instruction plans a costume piece **and** prop, but the evidence accepts either. | Require the collaborative sketch to show both, with each child’s contribution identified. |
| 10, `TH:Re8.1.2c` | The card compares feelings, omitting choices. | Add another person’s choice alongside the character’s choice, with same/different indicated and explained by pointing, drawing or speech. |

These omissions are confirmed against the [official theater standards, PDF pages 1, 3, 4 and 7](https://www.nationalartsstandards.org/sites/default/files/2021-11/Theatre%20at%20a%20Glance%20-%20new%20copyright%20info.pdf).

**Why it matters:** The teacher could mark an id met without observing its full action. Preserve the existing assessment days and consolidate the added components into the existing guides and cards.

### 3. The shorter path assesses new evidence during the respond session

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, the assessment timing problem was addressed in `prework-arts-fixes-2026-11-20.md`  
**Confidence:** Firm on the contradiction; likely on the proposed allocation

**Location:** “The once-a-week path,” especially its first 20 minutes of teacher’s-table items; four-session units 4, 8 and 12.

**Problem:** The full path separates showing, teacher’s-table assessment and response. The shorter path collects previously unassessed evidence during the respond session, contrary to the arts approach’s requirement that marks be available before that session begins. Twenty minutes also provides less than the frame’s own 24-minute table rotation, before setup or the teacher’s demonstration.

**Why it matters:** Response groups cannot be planned from all the evidence, and checking consumes the time promised for reteaching and a second try.

**Exact fix:** Remove first-time assessment from respond sessions. Keep a showing check, a separate teacher’s-table check and a subsequent respond session. Expand each four-session story unit to five sessions.

The following allocation retains 32 sessions and every unit:

| Year | Unit session counts | Course check weeks |
|---|---|---|
| K | 9, 9, 5, 5 | 19 and 26 |
| 1 | 8, 8, 7, 5 | 17 and 26 |
| 2 | 8, 8, 7, 5 | 17 and 26 |

Each row contains 28 unit sessions plus four course check/respond sessions. Fold the removed fluency practice into openers, preserving demonstration, critique, revision, both checks and response. Write the resulting session sequence explicitly before claiming the shorter path preserves every id.

The proposed check weeks avoid current core check weeks. Grade 2’s following respond session in week 18 still overlaps core math checking, as the frame already notes; that remains part of the lead’s calendar coordination.

### 4. The community-story fallback does not establish the required community connection

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** Likely

**Location:** Unit 8, works and evidence for `TH:Cn11.2.1a`.

**Problem:** A generic set of stories “told in one town” does not establish that they come from the learners’ own community. Nor does one visitor’s story necessarily supply the two stories the comparison requires. The local progression and [official standard, PDF page 10](https://www.nationalartsstandards.org/sites/default/files/2021-11/Theatre%20at%20a%20Glance%20-%20new%20copyright%20info.pdf#page=10) retain that community connection.

**Why it matters:** The default path can become a comparison of unrelated fictional stories while claiming the local-community outcome.

**Exact fix:** Make the default two teacher-authored stories created and shared within the class or school community. Identify their makers, shared school setting and telling context. A visitor is optional enrichment, and private family stories remain optional. The assessment compares those two identified stories.

This requires no visitor, purchase or family disclosure.

### 5. The grade 2 “first sharing” claim contradicts earlier units

**Severity:** Minor  
**LAYER:** frame, progression  
**REPEAT:** new  
**Confidence:** Firm

**Location:** Unit 9, its `TH:Pr6.1.2a` description and sequencing reason; `th-g2-show.notes`.

**Problem:** These describe sharing a scene with classmates “for the first time.” Unit 6 already shows a scene to the class, and earlier units show work to partner classes.

**Why it matters:** It gives later writers a false account of what changes between years.

**Exact fix:** Replace the first-sharing claim with:

> Students collaboratively invent and revise dialogue, then share the resulting scene with classmates.

Use that distinction in both the frame and progression note. Preserve earlier showings.

### 6. Completed work is still described as pending

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, the combined theater read identified the national-time ordering note and stale arts gate entry  
**Confidence:** Firm

**Locations and exact fixes:**

| Location | Problem | Replacement |
|---|---|---|
| Target frame, For the lead item 2 | Requests a source read before the grades 3 to 5 and 6 to 8 frames, which already exist. | Record that the linked 2016 opportunity-to-learn document was checked and addresses grades 6 to 12, without an elementary weekly-time recommendation. Remove the obsolete ordering request. |
| Arts `STANDARD.md`, theater time row | Broadly says the association gives no figure. | “No K to 5 weekly-time recommendation verified. The 2016 opportunity-to-learn document addresses grades 6 to 12.” |
| `ADOPTION-BAR-SUBJECTS.md`, introductory approach statement | Says no subject approach exists, although the arts approach is approved. | “Layer 3 requires a subject approach before its scope and sequence; current states are recorded below.” |
| Same file, arts row | Still owes L83 and the high school music id load. | State L83 completed 2026-11-21 and the 63 music strand ids and progression rows loaded. Remove both pending clauses. |

The [Educational Theatre Association document](https://schooltheatre.org/wp-content/uploads/2022/02/Opportunity-to-Learn-Standards-EdTA_2022.pdf) explicitly identifies its grade range. L83 is marked done, and the repository currently contains 28 high school music progression rows.

## Lens checklist at frame level

| Lens check | Result |
|---|---|
| Grade ids placed in their correct band year | Met |
| All four artistic processes each year | Met |
| Works span cultures and periods, including living makers | Met in the planned selections; item sources remain to be verified |
| Technique grows across units and years | Met, with the false distinction corrected by finding 5 |
| No daily K to 8 period required | Met |
| Every unit has a showing | Met |
| Five disciplines retain distinct techniques and purposes | Met |
| Dance/PE duplication and music/fractions boundary | Not applicable to this theater frame |
| Discipline words used in making and response | Met as a planning provision |
| Critique, revision, self-assessment and kept growth evidence | Met on the full path; shorter path missed, finding 3 |
| Room, equipment and safe use planned | Met as provisions; safety validation remains a later read |
| Unit/day execution checks | Not applicable until those layers exist |

## Calendar and seams

The current calendar matches the frame’s unit ranges and full-path course checks: K weeks 19 and 27; grade 1 weeks 20 and 27; grade 2 weeks 17 and 27. None falls in a current core check week.

Other after-core checks share K weeks 19 and 27, grade 1 week 27, and grade 2 weeks 17 and 27. The frame already assigns that coordination to the lead; these are not additional findings.

All seven grade 2 rows have the expected outgoing links, including `th-g2-notice` feeding both grade 3 notice and judge. The seven carried models are accounted for. ELA citations match the calendar, and the earlier theater uses have stated fallbacks.

## Settled by the expert

| Choice | Reason | Files affected |
|---|---|---|
| Keep the 12-unit sequence and 64-session full years | Placement, annual completeness and load are defensible | Target frame |
| Correct artistic-choice language without moving ownership | Restores the existing standard’s meaning | Target frame; `arts.csv` |
| Expand existing guides and cards as specified | Restores missing evidence within existing full-path assessment days | Target frame |
| Use class/school-created community stories by default | Preserves community connection without requiring outside people | Target frame |
| Use the revised shorter-path allocation as the scope-writing starting point | Preserves 32 sessions and separates assessment from response | Target frame |

## What is right and should not be touched

Preserve the annual ownership boundaries, practical paper path, picture-led reading load, classroom performance, explicit setup and cleanup, critique before scoring, portfolios, invented personal-tie options and culturally specific sensitivity instructions.

## What could not be judged

The future lesson materials, actual performance timing, complete rights lines and community-source suitability cannot be established from this frame. The frame’s movement and voice safety rules remain explicitly **from memory** pending its designated safety read. No finding in this report relies on unverified memory.

## For Cory

- **Money:** The frame proposes an optional $40 annual supplies ceiling per class. That remains Cory’s decision. The instructional fixes above require no additional purchase or outside reader.

## Sources and source-list follow-up

- [National Core Arts Standards: Theatre at a Glance](https://www.nationalartsstandards.org/sites/default/files/2021-11/Theatre%20at%20a%20Glance%20-%20new%20copyright%20info.pdf): checked the disputed standard actions against the original.
- [2016 Opportunity-to-Learn Standards for Theatre Education](https://schooltheatre.org/wp-content/uploads/2022/02/Opportunity-to-Learn-Standards-EdTA_2022.pdf): verified its grades 6 to 12 scope; it supplies no elementary weekly-time figure.
- [Art and Craft Safety Guide](https://www.cpsc.gov/Safety-Education/Safety-Guides/hobbies/art-and-craft-safety-guide): located the exact guide named by the frame.
- [Art Hazards and school materials guidance](https://oehha.ca.gov/risk-assessment/art-hazards): located the purchasing and safe-use guidance named by the frame.

Add the exact safety-guide links to the frame’s source provisions, replacing bare domains. Record the theater opportunity-to-learn document’s limited grade range in the source list.
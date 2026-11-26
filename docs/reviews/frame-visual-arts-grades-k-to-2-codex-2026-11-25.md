# Independent frame review: Visual Arts, grades K to 2

Date: 2026-11-25  
Course: `visual-arts-grades-k-to-2`  
Read-only review. No files changed or report file created.

## Verdict

**Revise before writing the scope and sequence.** The band structure, progression ownership and annual allocations are sound, but the kindergarten response standard loses part of its demand and several proposed assessments do not demonstrate all their claimed standards. Correct the standard-to-task-to-evidence links first, while preserving the units, technique progression and showing routines.

**Finding count: 5.**

## What I read and checked

I read the frame in full beside its `frames.csv` entry, the course-list selector, all 24 selected visual arts progression rows, the eight receiving grade 3 rows, the 45 relevant standards and their words-file lines, and the course’s calendar rows.

The governing reading included `frame-read.md`, the after-core provisions of `frame-write.md`, `EXPERT.md`, the arts lens, arts `STANDARD.md` and `APPROACH.md`, the shared core and arts part of `ADOPTION-BAR-SUBJECTS.md`, foundation and approach guidance, applicable decision entries, and the earlier arts pre-work, words-file and progression reviews. I also checked the relevant mathematics and social studies frame contacts.

There is no preceding visual arts course. The grades 3 to 5 frame does not yet exist, so the outgoing seam could be checked against its progression rows only. No base text is used, so a base-text source map is not applicable.

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check visual-arts-grades-k-to-2` | Failed because the course has no `days.csv` with assessment data yet; this is a frame-stage limitation, and the review continued. |
| `python -X utf8 scripts/frame.py check visual-arts-grades-k-to-2` | **0 failures.** |
| `python -X utf8 scripts/stale.py check` | **0 failures across 70 files.** Unmarked stale statements remain in finding 5. |
| Independent ownership comparison | Each year places its eight selected progression rows and 15 owned IDs exactly once. No missing, extra or duplicate IDs. |
| Calendar comparison | Each year contains 64 sessions. All six visual arts course checks avoid the core subjects’ check weeks. |

## Findings, most serious first

### 1. Kindergarten response work identifies locations of art but omits its uses

**Severity:** Major  
**LAYER:** standard, propagated into progression and frame  
**REPEAT:** yes, semantic drift in an own-words standard is the same kind identified in `arts-words-read-2026-11-20.md`; this particular ID was not corrected there.  
**Confidence:** firm.

**Location:** Frame unit 1, line 201; `va-k-look` in `data/progressions/arts.csv`; `VA:Re7.1.Ka` in the words file, line 1116.

The frame asks children to name where art appears. The national kindergarten standard asks them to identify its uses in their surroundings; recognizing nearby art is the preceding pre-kindergarten demand. Naming a mural or pointing to a quilt does not establish what it does for people. [NCAS visual arts standards, PDF page 6](https://www.nationalartsstandards.org/sites/default/files/Visual%20Arts%20at%20a%20Glance%20-%20new%20copyright%20info.pdf).

**Why it matters:** A writer following the current words file can teach the easier recognition task and still record the kindergarten ID as met.

**Exact fix:**

- Replace the words-file line with: **“Identify what nearby art is used for, with examples from your surroundings.”**
- In `va-k-look` and unit 1, require children to identify nearby art and explain one use, such as guiding people, telling a story, remembering something or decorating a shared place.
- Add that use question to unit 1’s scored talk and the kindergarten mid-year check. Keep the separate picture-description task for `VA:Re7.2.Ka`.

No ID needs to move between units.

### 2. Several assessment summaries leave owned actions without clear scored evidence

**Severity:** Major  
**LAYER:** frame, with related progression assessment templates  
**REPEAT:** yes, incomplete links between standards and assessment recur in the earlier arts reviews.  
**Confidence:** firm for the omitted evidence; likely for the pinch-pot ambiguity.

**Location:** Units 1, 4, 7, 8, 9 and 12, lines 201 to 212; course checks, lines 218 to 223.

The arts approach requires an end-of-unit item for every part. Several assessment summaries instead name a narrower task. This matters especially in units 4, 8 and 12 because the course-level checks expressly exclude those units.

**Exact fix:** Expand the existing assessment descriptions and record-sheet look-fors as follows, keeping the present unit allocations.

| Unit | Required correction |
|---|---|
| **1** | Add the child’s safe-supply selection and retained experiments across materials to the evidence. Handling one tool safely alone does not show both identification of suitable supplies and experimentation across media. Apply finding 1 to the response talk. |
| **4** | Keep selection and reasons. Add a spoken explanation of the portfolio’s purpose and a comparison of an art museum with another kind of building. The present “one use of art” talk does not establish those actions. |
| **7** | Require a visual grouping of everyday objects by use. A pinch pot alone can show one useful object without showing classification. Keep the pot as an option alongside a drawing, arrangement or diagram that makes the groups visible. |
| **8** | Record the child’s comparison of why objects are valued, questions and answers about preparing work, identification of museum worker and visitor responsibilities, and reasons the two studied works were made. A mounted piece plus one reason for making art is insufficient. |
| **9** | Add a scored description of features in natural and built surroundings. Sorting paintings by feeling does not establish this separate action. In the mid-year check, add corresponding evidence or remove `VA:Re7.1.2a` from that particular task’s claim. |
| **12** | Add identification of differences between display materials or techniques, plus a shared feature and a difference in the two cultural uses studied. Choosing a piece that fits the theme does not establish the display-preparation comparison. |

Update the corresponding progression assessment sentences where they repeat the narrower templates. These are item and evidence corrections within existing ownership, not requests for additional units.

### 3. The claim that the national association gives no weekly minutes is incorrect

**Severity:** Moderate  
**LAYER:** standard, propagated into frame  
**REPEAT:** yes, `prework-arts-gemini-2026-11-20.md`, finding 6, raised the elementary figure; the later fix pass recorded a contrary conclusion.  
**Confidence:** firm.

**Location:** Frame “Days,” line 23; arts `STANDARD.md`, section 3.4, lines 194 and 198.

The association’s specific elementary document states at least **50 minutes weekly**. Curio Class provides 80 minutes on the full path and 40 on the short path. The short path therefore falls 10 minutes below that published minimum. [Elementary visual arts opportunity-to-learn standards, PDF pages 3 and 4](https://www.arteducators.org/wp-content/uploads/2025/09/OTL-Elementary_Visual_Media_Arts_Program.pdf).

**Why it matters:** The current statement hides the short path’s time gap from schools and contradicts Cory’s decision to publish source-checked time figures.

**Exact fix:** Replace the frame sentence with:

> The national visual arts educators’ association recommends at least 50 minutes weekly for elementary visual arts. This course provides 80 minutes weekly on the full path and 40 on the short path, respectively 30 minutes above and 10 minutes below that figure.

Correct the elementary visual arts entry and concluding sentence in `STANDARD.md` section 3.4. Do not extend this elementary finding to media arts or middle school without checking their specific documents. Keep the settled 64-session and 32-session paths.

### 4. Three units do not yet identify two works by other artists

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm.

**Location:** Units 2, 4 and 10, lines 202, 204 and 210; “For the lead,” item 10.

The arts approach requires two to four works by other artists per unit. Unit 2 names one artist’s work plus children’s bridges. Unit 4 names an unspecified quilt and museum pages. Unit 10 names a sculpture series plus children’s solutions. Children’s work and a museum website do not supply the missing second artist work.

**Why it matters:** The next writer lacks the promised study set, and the assertion that every unit already names two works is inaccurate.

**Exact fix:**

- **Unit 2:** Revisit the Hokusai work from unit 1 beside Kandinsky, with a short comparison of how line and color support different ideas.
- **Unit 4:** Identify the particular Gee’s Bend quilt and revisit Ringgold’s *Tar Beach* beside it, comparing purposes and reasons for keeping or displaying the works.
- **Unit 10:** Identify the particular Asawa sculpture and add Lygia Clark’s *Bicho* (1960), described and linked under the existing rights rule. It provides another sculptural solution for comparison. [Walker Art Center collection record](https://www.walkerart.org/collections/artwork/bicho/).
- Give every selected work its maker, place, date, purpose and source link. Replace “a quilt” and an unspecified sculpture series with identifiable works.

These changes fit the existing units and do not require new material purchases.

### 5. Unmarked process notes contradict completed work and understate current calendar coordination

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale script and planning-status notes were findings in `prework-arts-read-2026-11-19.md`.  
**Confidence:** firm.

**Locations and exact fixes:**

| Location | Current problem | Replacement or action |
|---|---|---|
| Frame lines 43 to 44; arts `STANDARD.md` section 1 | The NCAS membership gate is described as still owed. | State that `scripts/standards.py` now checks NCAS IDs against the loaded list. `later.csv` L83 is done, and the implementation is present. Retain human checking of meaning and coverage. |
| Frame “For the lead,” item 4 | Band-year calendar mapping is proposed as future work. | Replace it with: **“frame.py already maps this band’s Year cells to K, 1 and 2, and calendar.csv carries its checks under those grades.”** |
| Arts row of `ADOPTION-BAR-SUBJECTS.md` | Loading the 63 high school music strand IDs remains listed as owed. | State that the IDs, words lines and high school music progression rows were loaded on 2026-11-21. |
| Frame “For the lead,” item 3 | Coordination is framed as a possible collision between arts courses only. | Name the actual current conflicts: visual arts shares its mid-year week with ELD and PE in all three grades, and week 26 with SEL in all three grades. Assign resolution to the lead and the affected course writers before declaring the shared calendar clear. |

The last item is a shared scheduling issue observed in this snapshot, not a reason to reject the visual arts dates solely because another course is being edited. Its dates already satisfy the brief’s explicit requirement to avoid core checks.

## Coverage, days and seams

| Year | Units | Selected rows | Owned IDs | Unit sessions | Course checks and response | Total |
|---|---:|---:|---:|---:|---:|---:|
| K | 1 to 4 | 8 | 15 | 60 | 4 | 64 |
| 1 | 5 to 8 | 8 | 15 | 60 | 4 | 64 |
| 2 | 9 to 12 | 8 | 15 | 60 | 4 | 64 |

The full-path allocations are reasonable: 18/16/14/12 sessions in K and grade 1, and 16/16/16/12 in grade 2. Studio routines justify the longer opening units; the final units use retained work. No unit is demonstrably far over or under its load at frame level.

The short-path unit counts total 28 sessions per year, leaving four for course checks and response. They preserve the stated check weeks, although the following respond session occurs a week later than on the full path.

The eight thread handoffs are reciprocal through grade 3’s progression rows. Cross-subject contacts have explicit local teaching or fallback provisions, so they introduce no unresolved prerequisite.

## Arts lens checklist at frame level

| Lens check | Result |
|---|---|
| Grade IDs placed in their own band year | Met |
| All four artistic processes in each year | Met |
| Works span traditions and periods, including living makers | Met in the annual design; complete unit sets under finding 4 |
| Technique becomes more demanding across units and years | Met |
| K to 8 pacing does not require daily periods | Met |
| Every unit has a showing | Met |
| Discipline words are taught and used | Met in the design |
| Critique has a protocol and revision follows feedback | Met in the design |
| Assessment includes kept work, growth and self-assessment | Met in the design; full coverage needs finding 2 |
| Room, supplies and safety are planned | Met as frame commitments; detailed safety remains to be checked |
| Screens support the physical work | Met |
| Five arts disciplines remain distinct | Met |

Day-level execution, model withdrawal, accessibility details and final assessment items cannot be certified from a frame.

## What is right and should be preserved

Preserve the three complete years, the four-unit progression within each year, the concrete technique steps, the distinction between artistic responding and respond days, and the critique followed by revision. Keep the paper and home paths, locally held portfolios, invented alternatives to private-life disclosures, and explicit notice that leaving out a unit removes its standards claim.

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Restore the use-of-art action within unit 1 | Corrects meaning without moving ownership | Words file, arts progression, frame |
| Expand existing check evidence within current unit days | Keeps teaching and assessment aligned | Frame and relevant progression assessment notes |
| Keep both settled pacing paths and publish the 50-minute comparison | Corrects information without changing dose | Arts `STANDARD.md`, frame |
| Complete the three study sets as specified in finding 4 | Supplies the required artist works within existing units | Frame |
| Replace obsolete implementation notes in place | Prevents duplicate or unnecessary work | Frame and shared arts guidance |

## For Cory

- **Money:** The proposed $75 annual class supply ceiling remains a proposal. The frame’s optional estimates are $70, $50 and $40 by year, with free alternatives retained. No spending approval is inferred.

No new scope, audience or outside-person decision is needed to apply these findings.

## Sources, confidence and limits

- [NCAS visual arts standards](https://www.nationalartsstandards.org/sites/default/files/Visual%20Arts%20at%20a%20Glance%20-%20new%20copyright%20info.pdf): checked grade demands against the frame and own-words lines.
- [Elementary visual arts opportunity-to-learn standards](https://www.arteducators.org/wp-content/uploads/2025/09/OTL-Elementary_Visual_Media_Arts_Program.pdf): verified the weekly minimum directly.
- [Walker Art Center, *Bicho*](https://www.walkerart.org/collections/artwork/bicho/): verified the proposed additional work’s artist, title, date and medium.

No finding rests on model memory. The frame’s safety rules and critique background remain marked “from memory” pending their specified source-based reads; this review does not certify their detailed implementation or every artwork’s reuse rights.

**For the source list:** Add the specific elementary opportunity-to-learn PDF above, with PDF pages 3 and 4 as the time reference. It corrects the earlier “no minutes named” conclusion for elementary visual arts.
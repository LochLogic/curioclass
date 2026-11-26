# Second-model frame read: computer-science-grade-9

Date: 2026-11-25  
Read-only review. No files were changed or created.

## Verdict

**Needs fixes before scope and sequence writing.** The six-unit structure, progression placement and 64-session calendar are sound, but the frame assumes students took the previous elective and allocates too much teaching time to standards owned by later grades. Preserve the structure while adding entry bridges, reducing that allocation and tightening the assessment promises.

**Eight findings:** two serious, four moderate and two minor.

## What I read

- The complete Grade 9 frame, its `frames.csv` entry and calendar rows.
- The `grade:9` selection in `course-list.csv`, all 17 selected progression rows, and the Grade 8 and Grade 10 handoffs.
- Adjacent frames, especially their units, prerequisites and incoming and outgoing seams.
- `frame-read.md`, the applicable `frame-write.md` rules and after-core changes, `EXPERT.md`, the computer science lens, subject standard and approach, and the computer science adoption bar.
- Relevant foundation, shared approach, glossary, production-path and recorded decision rules.
- Earlier computer science prework, progression and frame reviews, including the combined Grades 6 to 12 read.
- All 12 owned standard statements and their boundaries in the published standards PDF. Outside sources are linked below.

No finding rests solely on memory.

## Checks and calendar

| Check | Result |
|---|---|
| `python -B -X utf8 scripts/frame.py check computer-science-grade-9` | Passed: zero failures |
| `python -B -X utf8 scripts/stale.py check` | Passed: 121 files, zero marked failures |
| `python -B -X utf8 scripts/plan.py check computer-science-grade-9` | Failed because the later plan-stage files do not exist; this does not block the frame verdict |

The plan check was course-filtered to respect the repository prohibition on running it unfiltered.

The calendar matches the frame:

| Part | Course days | Weeks |
|---|---:|---:|
| Unit 1 | 1 to 13 | 1 to 7 |
| Unit 2 | 14 to 25 | 7 to 13 |
| Unit 3 | 26 to 32 | 13 to 16 |
| Mid-year check and respond | 33 to 34 | 17 |
| Unit 4 | 35 to 43 | 18 to 22 |
| Unit 5 | 44 to 55 | 22 to 28 |
| Unit 6 | 56 to 62 | 28 to 31 |
| Year-end check and respond | 63 to 64 | 32 |

The totals are 60 unit days plus four course-check and respond days. The frame identifies 52 teaching days after excluding assessments and response time.

Week 17 avoids Grade 9 core check weeks, although ELD also checks that week. Week 32 overlaps core finals, as permitted. This is a single-grade course, so the band-course Year column is not applicable.

## Findings

### 1. Students who skipped Grade 8 have no entry bridge

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, combined Grades 6 to 12 read, S1  
**Confidence:** firm

**Location:** `Seams`, opening paragraph and incoming table; Units 1 to 6.

The frame explicitly treats every Grade 8 prerequisite as retrieval, “never as a reteach or a readiness check.” This assumes the previous elective was taken. Rule 32 requires an optional-course prerequisite to have a bridge or a course-order fallback.

The largest risk is Unit 1: its opening trace already assumes Python, variables, lists, loops and procedures. Repeating an unfamiliar program does not establish those prerequisites. Similar assumptions appear in the model, data, security and society strands.

**Exact fix:** Replace the opening seam paragraph with:

> Grade 8 computer science is optional. Students who took it retrieve the named work. Every unit also names the prerequisite ideas it teaches through supplied worked examples when those ideas are missing; no student depends on having taken Grade 8.

Add an entry-evidence and fallback column to the incoming table. Place Unit 1’s ten-minute entry check at the end of its first day. Place later units’ checks before those units open, following rule 16. Pair each check with named trace, modify and guided-practice tasks inside the receiving unit.

Do not describe one ten-minute explanation as sufficient for a student missing the whole programming foundation. The scope must budget the actual bridge tasks; any resulting change to audience or course length goes to Cory.

### 2. Later-owned content exceeds C1’s teaching-time limit

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, outside-standard accounting in the combined read, S2  
**Confidence:** firm

**Location:** Days bullet; Units 3, 4, 5 and 6.

The frame correctly names contributions to later grades, but naming their owners does not exempt their teaching time from C1.

The present allocation includes:

| Later-owned work | Full sessions |
|---|---:|
| Unit 3, lessons 4 and 5: AI types | 2 |
| Unit 3, lessons 6 and 7: algorithm impacts | 2 |
| Unit 4, lesson 7: large-scale collection | 1 |
| Unit 5, lesson 7: network diagram reading | 1 |
| Unit 6, lesson 7: career interests | 1 |
| **Minimum** | **7** |

That is **7 of 52 teaching days, about 13.5 percent**, before counting Unit 6’s human-choice contribution. C1 permits no more than 10 percent outside the course’s standards.

**Exact fix:** Keep all 17 progression rows and the existing unit lengths, but revise the allocation:

- Combine Unit 3’s AI introduction and first matches into lesson 4.
- Combine its worked audit, claim and refinement into lesson 6.
- Use lessons 5 and 7 for additional owned deterministic/probabilistic work.
- Keep Unit 4’s collection case and Unit 5’s network lesson.
- Use half of Unit 6 lesson 7 for the private career note and half for owned society work.
- Limit the additional human-choice contribution to one-quarter of a lesson equivalent.

This gives a provisional maximum of **4.75 of 52 teaching-day equivalents, about 9.1 percent**. State the allocation in the Days bullet and require the scope to confirm actual minutes. Count bridge time honestly rather than assuming it is automatically exempt.

### 3. The history assessment permits students to omit a required dimension

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm

**Location:** Unit 6, lessons 3 and 4; year-end check.

Teaching names societal and environmental influences, but both the revised analysis and the unseen check ask for a claim about **one factor**. A student can complete both through policy or economics without demonstrating an environmental relationship.

The owned standard joins historical development to both societal and environmental factors. See [CSTA, PDF page 95](https://csteachers.org/wp-content/uploads/2026/07/2026-CSTA-PK%E2%80%9312-Computer-Science-Standards.pdf#page=95).

**Exact fix:** Change the lesson 3 draft and lesson 4 revision to require:

> Explain two points on the technology’s trajectory: one where a societal factor influenced development or adoption, and one where an environmental factor did so. Support both explanations using the supplied sources.

Give the rubric separate look-fors for trajectory, societal causation, environmental causation and source support. The year-end check may then use one brief transfer item while carrying the complete revised analysis as the scored evidence for the other dimensions.

### 4. The algorithm check needs evidence beyond repeated outputs

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm

**Location:** Mid-year check, HS-ALG-PS-04 task.

The check emphasizes three runs and their outputs. Identical outputs do not establish that an algorithm is deterministic. A randomized search can follow different paths and still find the same target; random choices can also repeat by chance.

The standard’s boundary distinguishes the algorithm’s logic and execution, including possible runtime variation. See [CSTA, PDF page 44](https://csteachers.org/wp-content/uploads/2026/07/2026-CSTA-PK%E2%80%9312-Computer-Science-Standards.pdf#page=44).

**Exact fix:** Specify that each check item supplies the algorithm’s pseudocode, including any random-choice operation, plus short execution traces. Include one randomized example whose final output stays the same while its path changes.

Ask students to classify from the logic, explain what can vary and name an appropriate use. Add a key explanation that three matching outputs alone are insufficient evidence.

### 5. The year-end sitting has no bounded task budget

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, combined read S3 and earlier course-check findings  
**Confidence:** likely

**Location:** Course-level checks, especially day 63.

The year-end check combines a new two-source history packet, an emerging-technology comparison and six earlier-unit tasks in 40 minutes. The frame gives no reading cap, response cap or time allocation. A scope writer could reasonably build several substantial performances from this list.

The revised history requirement in finding 3 makes a bounded plan particularly necessary.

**Exact fix:** Keep the current check dates and adopt a 35-minute student-task budget:

| Year-end component | Maximum |
|---|---:|
| Read the two-source packet, at most 200 words total | 5 minutes |
| Brief history transfer response | 7 minutes |
| Emerging-technology comparison | 8 minutes |
| Three earlier-unit micro-items | 9 minutes |
| Review | 6 minutes |

Name the three sampled earlier-unit tasks. Carry the other units’ existing records unscored. Score the revised history product before the sitting.

Give the mid-year check a corresponding task budget. Include directions, collection and any device opening and saving inside the 45-minute period.

This differs from the combined read’s proposed universal two-session rule: a bounded sample is a defensible repair without changing this course’s calendar.

### 6. Some first teaching is labeled Fluency

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** likely

**Location:** Day kinds bullet; Unit 1 lessons 2 and 4.

The Day kinds bullet identifies these modify lessons as Fluency, but their descriptions introduce list mutation and record operations, including missing-key handling. Earlier lessons do not explicitly teach all those operations.

The glossary defines first teaching as Understanding. Calling an activity “modify” does not establish that its underlying operations were already taught.

**Exact fix:** Mark lessons 2 and 4 as **Understanding, followed by guided modification**. Name the worked example and trace before students change the program. Reserve Fluency for later practice using those same operations.

Update the Day kinds examples accordingly. Keep the lesson counts unchanged.

### 7. Unmarked stale notes contradict the current repository

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, combined read M4  
**Confidence:** firm

**Location:** Incoming seams, lines 148 to 150; For the lead, lines 252 to 262.

The Grade 8 frame now exists. The progression already names satellite positioning and quantum computing, and the simulation note already says “within a stated range.” The stale checker currently passes, so the claim that it “now fails” on the career frame is obsolete.

**Exact fix:**

- Replace the claim that Grade 8 has no frame with its frame path.
- Add these source-unit references to the incoming seam table:

| Grade 8 source unit | Prerequisites supplied |
|---|---|
| 1 | System choice, network failure, cyberattacks |
| 2 | Text project |
| 3 | Relationships, investigation summary, biased decisions |
| 4 | Model evaluation, modifying algorithms for bias |
| 5 | History, emerging technology, career sketch |

- Delete the obsolete stale-check failure item.
- Replace the pending history and emerging-technology row-change item with: “The progression now records satellite positioning and quantum versus classical computing; retain those choices.”
- Replace the simulated-height item with: “The progression now specifies heights within a stated range; no distribution change is pending.”
- Renumber For the lead consecutively.

### 8. Two UK spellings and two ambiguous references remain

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, combined read minor findings  
**Confidence:** firm

**Location:** Header, Unit 1 and references reading “lesson 13” and “lesson 16.”

**Exact fix:**

- Change `catalogue` to `catalog` in the header and Unit 1.
- Change the seam reference to `frame-write.md rule 16`.
- Change the simulated-data reference to `frame-write.md rule 13`, if retained after finding 7.

These references currently look like numbered student lessons.

## Lens checklist: course-frame layer

| Lens requirement | Status | Evidence or limitation |
|---|---|---|
| All five concepts receive teaching | Met | All appear in the owned-unit allocation |
| Constructs are ordered before dependent work | Part met | Internal order is sound; optional-course entry is unresolved |
| Read, predict and modify precede independent creation | Met in design | Retain this sequence; correct finding 6’s labels |
| Unplugged work in every unit | Met | Each unit names at least one task |
| Notional machine is explicit | Met | Trace tables, named boxes and assignment wording |
| Debugging and testing are taught | Met | Tests, comparison and revision recur |
| Practices are taught inside content | Met | Practices are attached to unit tasks |
| Later-owned and Specialty work is identified honestly | Part met | Owners are named; time allocation fails C1 |
| AI is connected to algorithms and data | Met | Units 3 and 4 link algorithm choices and data |
| Assessment includes code, projects and reasoning | Part met | Forms are suitable; findings 3 to 5 need repair |
| Society uses dated evidence and multiple views | Promised | Finished packets remain to be checked |
| Non-specialist teacher support is planned | Promised | Solutions, bugs and adult explanations are specified |
| No accounts or installation; tools have named jobs | Met as a requirement | Implementation remains untested |

## What is right and should remain

- All 17 selected progression rows are placed once, and all 12 owned IDs are assigned.
- The order from structures to modular programs, randomized algorithms and simulated data is coherent.
- The Grade 10 handoffs pick up the intended structures, data dictionaries, network reading and society work.
- The Grade 7 probability prerequisite is named and checked before Unit 3. The course avoids requiring later statistical distributions.
- The paper path explicitly identifies the three device-dependent IDs as partial without a device.
- Privacy, toy-system security, optional hardware and sensitive-case controls are concrete.
- The course needs no Grade 9 base-text source map under the settled subject rule.

I do not repeat the combined read’s census finding as an automatic defect. A new census-history packet can assess transfer after a different census-data lesson. Its text, evidence and expected answer must be genuinely new.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Retain six units and 64 sessions | Structure and calendar reconcile | Grade 9 frame |
| Count outside-standard time against 52 teaching days | Matches C1 and the glossary | Days bullet and scope allocation |
| Use the 4.75-day provisional contribution cap | Preserves every selected row within the limit | Units 3 to 6 |
| Require societal and environmental evidence in the revised history analysis | Makes the attainment claim inspectable | Unit 6 and rubric specification |
| Classify algorithms from logic and traces | Avoids an invalid inference from outputs | Mid-year check |
| Retain one-session course checks with bounded samples | Fits the current calendar | Course-level checks |
| Correct first-teaching labels and stale references | Prevents downstream copying errors | Day kinds, seams and lead notes |

## For Cory

- **Entry scope:** If the scope cannot fit a sufficient bridge for students without prior programming inside 64 sessions, decide between additional entry provision and a published prerequisite. The frame must not silently assume the earlier elective was taken.

No new spending or outside-person decision is required by these repairs.

## What I could not judge

Actual assessment duration, individual attainment records, scoring reliability, tool behavior and the completeness of future teacher and society packets cannot be established from a frame.

The proposed NIST bias-background HTML page returned an access error. Its contents were not used as evidence. The historical packet still needs verification of its receiver-cost and atmospheric-correction claims.

## Outside sources

- [2026 CSTA PK-12 Computer Science Standards](https://csteachers.org/wp-content/uploads/2026/07/2026-CSTA-PK%E2%80%9312-Computer-Science-Standards.pdf): checked the 12 owned statements and boundaries.
- [PRIMM research seminar account](https://www.raspberrypi.org/blog/primm-talk-in-programming-lessons-research-seminar/): supports retaining the progression from reading working code toward modification and creation.
- [Archived Key Stage 4 curriculum](https://www.raspberrypi.org/curriculum/archived/key-stage-4): comparison for programming dependencies and the breadth of systems, data and society content; not a proposed base text.
- [GPS advisory board history, May 2023](https://archive.gps.gov/governance/advisory/recommendations/2023-05-white-paper-GPS-50.pdf): corroborates the 1973 program origin and 1983 civilian-access decision.
- [GPS.gov, Selective Availability](https://www.gps.gov/selective-availability): verifies the May 2000 removal of deliberate civilian-signal degradation.
- [NIST, finalized post-quantum standards, August 2024](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards): verifies the dated encryption milestone selected for Unit 6.

## For the source list

Record the exact GPS history, Selective Availability and NIST 2024 links above as opened on 2026-11-25. Distinguish the GPS advisory board’s policy position from the chronology used in the lesson.
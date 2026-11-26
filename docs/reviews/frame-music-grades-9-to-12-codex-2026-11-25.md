# Second independent frame read: Music, grades 9 to 12

Date: 2026-11-25  
Course: `music-grades-9-to-12`  
Read-only review. Report returned here; no report file created.

## Verdict

**Revise before writing the scope and sequence.** The four-level structure, ownership inventory and annual calendar are sound, but several instructions permit incomplete standards evidence or advancement without the necessary prerequisites. Restore those requirements first, particularly the drafting work, placement evidence and no-device listening route.

**Finding count: 9.**

## What I read and checked

- The complete [course frame](S:/CurioClass/docs/courses/music-grades-9-to-12/frame.md), its `course-list.csv` selector, `frames.csv` entry and calendar rows.
- All 28 selected music progression rows, the eight incoming grade 8 rows, the owned standards inventory and corresponding words-file entries.
- The preceding music frame, including its grade 8 units and handoffs. There is no following music course.
- `frame-read.md`, the after-core provisions of `frame-write.md`, `EXPERT.md`, the arts lens, arts `STANDARD.md` and `APPROACH.md`, and the arts adoption bar.
- Relevant foundation, production-path, approach, baseline, calendar, source and decision guidance.
- The high school ELA contacts and earlier arts progression and frame reviews, consulted after the independent reading for repeat classification.
- The outside sources linked below.

There is no base text, so a source-map audit is not applicable.

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check music-grades-9-to-12` | One failure: the later plan stage requires `days.csv` and assessment tables. Review continued. |
| `python -X utf8 scripts/frame.py check music-grades-9-to-12` | **0 failures.** |
| `python -X utf8 scripts/stale.py check` | **0 failures across 121 files.** Unmarked stale prose remains below. |
| Skill placement | All 28 selected rows occur exactly once. |
| Standards inventory | Exactly 63 owned ids, 21 in each of Levels 1 to 3, with no missing, extra or duplicate owned ids. Level 4 contributes to 11 existing ids. |
| Full calendar | Each level has 156 unit days plus two check days and two respond days, totaling 160. All 640 days match the calendar rows. |
| Short path | Each level has 76 unit days plus four course-level days. Mid-year days 39 and 40 and year-end days 79 and 80 fit the stated allocations. |

The aggregate `gate.py` wrapper was not run because it writes logs and baselines, contrary to this review’s read-only restriction; its relevant read-only checks are reported above.

## Findings, most serious first

### 1. Several owned standards are narrowed by the teaching or evidence instructions

**Severity:** Serious  
**LAYER:** frame, progression, standard  
**REPEAT:** yes, incomplete creating and response requirements recur in the music 6 to 8 second read, findings 1 and 3.  
**Confidence:** firm.

**Location:** Units 3, 8, 12 to 15 and the associated progression notes and words lines.

The national text requires variety in later drafting, function in Advanced performance analysis and interpretation, and form and style in Advanced performance evaluation. Connecting and listening analysis also contain dimensions lost in the abbreviated instructions. These are substantive requirements, beyond placing the correct codes. [National composition and theory handout, PDF pages 1 to 4](https://www.nationalartsstandards.org/sites/default/files/2021-11/Music%20Theory%20and%20Composition%20Strand%20at%20a%20Glance.pdf).

**Why it matters:** A writer can build the stated tasks faithfully and award completion for partial standards.

**Exact fix:**

| Location | Required correction |
|---|---|
| Unit 8, `MU:Cr2.1.C.IIb` | Replace development in “a binary, rondo or ternary form” with dated draft development in at least two forms. Use brief binary and rondo studies; one may become the substantial finished piece. Assess the explanation across both draft trails. |
| Unit 13, `MU:Cr2.1.C.IIIb` | Require draft development and analysis in at least two moderately complex or complex forms. Use theme and variations and through-composed studies; a longer sonata-form project remains an option. |
| Units 13 and 14, `MU:Pr4.2.C.IIIa` and `MU:Pr4.3.C.IIIa` | Add the work’s function explicitly to the analysis, interpretation and evidence requirements. |
| Unit 15, `MU:Pr5.1.C.IIIb` | Add form and style to the performance-analysis note, alongside techniques and historical or cultural setting. |
| Units 3, 8 and 13, `MU:Re7.2` | Require the analysis record to identify the relevant setting and explain one specific use of the analysis in the student’s subsequent composing, performing or listening. Retain that record as assessed evidence. |
| Units 2, 7 and 12, `MU:Cn10.0` | Add brief evidence connecting interests, knowledge and skills to choices in performing as well as creating and responding. |
| Units 5, 10 and 15, `MU:Cn11.0` | Replace the single either/or connection with a compact connection map covering another art, another subject, context and daily life. |

Correct the corresponding progression notes and words lines where they permit the same narrowing. Keep ownership in the existing units.

### 2. Placement and Advanced completion claims exceed the evidence required

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, incomplete placement evidence appears in the visual arts 9 to 12 second read, finding 2.  
**Confidence:** likely.

**Location:** “Entry and placement,” “Standard,” units 6 and 11, and Level 4’s evidence lines.

Unit 6’s placement task contains a sketch, listening analysis and revised passage. It does not require evidence of the preceding level’s performance, rehearsal or feedback prerequisites. Unit 11 follows that arrangement.

Separately, the statement that a student finishing Level 3 at “partly” has Level 4 to reach Advanced is too broad. Level 4’s rows revisit 11 of the 21 Advanced ids. For example, they do not explicitly reassess `MU:Cr2.1.C.IIIb`, `MU:Cr3.2.C.IIIb`, `MU:Pr5.1.C.IIIc` or `MU:Re9.1.C.IIIb`.

**Why it matters:** Students can enter work they are unprepared to undertake, or receive a completion claim without resolving their actual gaps.

**Exact fix:**

- In units 6 and 11, require a placement checklist covering the previous level’s creating, performing, responding and connecting prerequisites. Accept existing work; use targeted live demonstrations where evidence is missing. Include a rehearsed performance and a feedback-to-revision example. State that the abbreviated sitting alone does not authorize advancement.
- At entry to Level 4, review the student’s Level 3 record id by id. Carry forward established achievement and list unresolved ids. Require targeted evidence for those gaps within the existing portfolio, criticism, capstone or program work before claiming Advanced completion.
- Replace the unconditional recovery sentence with: “Level 4 can provide another opportunity to demonstrate unresolved Advanced requirements; completion is claimed only when the record establishes them.”

### 3. The no-device route can substitute descriptions for musical evidence

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, music 6 to 8 second read, finding 4.  
**Confidence:** likely.

**Location:** “Devices,” lines 141 to 147; dependent listening and interpretation tasks.

The frame says that a work without a public domain score is met through its description and a score-card reduction. That does not establish that students can hear the musical features they must analyze. It also leaves unexplained how a reduction of a protected work becomes available under the frame’s own rights rule.

**Why it matters:** The route promised to a teacher without equipment can become reading about music while claiming listening outcomes.

**Exact fix:** State:

> Descriptions support contextual study and never replace the musical evidence a task requires. Every no-device listening task supplies a legally usable, performable printed exemplar, preparation guidance and any contrasting versions needed for the comparison. Protected works remain described and linked; no reduction is copied without a verified permission or license.

Identify which exemplar carries each no-device assessed action. Preserve the study of the protected work through its permitted description and link.

### 4. The leave-out route does not make the named units independent

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, music 6 to 8 second read, finding 8; adult-student leave-out wording also recurs in the visual arts 9 to 12 read.  
**Confidence:** firm.

**Location:** “Leave-out,” lines 126 to 130; units 3, 4, 12 and 13.

The frame says each unit stands alone, but unit 4 requires unit 3’s drafts, and unit 13 requires unit 12’s sketch. Leaving out either named sensitive unit therefore removes the next unit’s starting material. The leave-out rule also assigns the choice to a school or family without expressly including students aged 18 or older.

**Why it matters:** A permitted leave-out can prevent participation in retained units.

**Exact fix:**

- Unit 4 supplies a neutral Curio Class draft packet when unit 3 is omitted.
- Unit 13 supplies a neutral extended-idea sketch when unit 12 is omitted.
- Apply the same rule to every later dependency: provide a prepared starting artifact and teach its use inside the retained unit’s existing days.
- Name omitted ids on the course page and family note, without treating the supplied artifact as evidence that the omitted unit was completed.
- Add: “A student aged 18 or older receives the family note directly and makes their own leave-out and consent choices; the school’s rules still apply.”

### 5. Level 4’s assessment arrangements do not fit the stated room

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, check-day feasibility recurs in earlier arts frame reads.  
**Confidence:** firm on the timing conflict; likely on the showing omissions.

**Location:** Level 4 mid-year check, line 275; general check-day paragraph; units 16 to 18.

The mid-year check requires each student to present and defend a portfolio to the teacher. The operating paragraph allows 35 minutes for the sitting with one adult and 30 students. Even three minutes per student requires 90 minutes, before transitions or marking.

Units 16 to 18 also lack explicit showing arrangements comparable to the other thread units.

**Exact fix:**

- Make the mid-year check a simultaneous written defense using fresh prompts. Carry the already scored portfolio record unscored; assess the new defense.
- Give the teacher response moves keyed to those fresh answers, with marks available before the respond day.
- Specify these showings within existing application time: unit 16 shares a portfolio selection with a partner group; unit 17 delivers reviews to their intended readers or listeners; unit 18 shares the capstone with the class or home adult.
- Retain individual oral conferences as optional teaching conversations, outside the required whole-class check.

### 6. The rehearsal-plan model is taught after its first required use

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, late model retrieval appears in the music 6 to 8 second read, finding 9.  
**Confidence:** firm.

**Location:** “Models carried,” practice-plan row; unit 3.

The model table places first use of the practice plan in unit 5. Unit 3 already requires students to plan rehearsal from their analysis, including an assessed rehearsal step.

**Why it matters:** A novice entering through the bridge can be assessed on a planning routine that the frame postpones.

**Exact fix:** Introduce a short analysis-to-rehearsal card in unit 3 before independent work: identify a musical feature, choose a rehearsal action, explain the connection. Change the model table to show unit 3 as its introduction here and unit 5 as its later development into the full repetition-and-variation rehearsal plan. Keep the standards’ existing ownership.

### 7. Important sources and work selections remain unspecified

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, unspecified works appear in the music 6 to 8 second read, finding 6.  
**Confidence:** firm.

**Location:** Works and sensitivity columns throughout; particularly units 3, 7 and 13; “Safety read.”

The frame contains no actual source URLs. Phrases such as “a holding archive’s page” do not identify evidence. Unit 3’s gamelan work, unit 7’s katajjaq example and unit 13’s raga recording remain selections for a later writer. The sensitivity reader consequently lacks the specific community sources the brief requires.

**Exact fix:**

- Supply an item-level source link for every named work and factual anchor.
- Complete the gamelan, katajjaq and raga selections now, naming the work or documented performance, performer or ensemble, date, source and intended analytical feature.
- Add the relevant community or practitioner source beside each sensitivity instruction.
- For unit 13, the [Ali Akbar Khan Library video catalog](https://aliakbarkhanlibrary.com/video/) provides identified performances. Its listed extracts do not establish the promised complete alap, jor and jhala sequence. Select a verified complete example or revise that description to match the chosen extract.
- Replace the safety guide shorthand with linked titles: [Protect Your Hearing Every Day](https://nasm.arts-accredit.org/wp-content/uploads/sites/2/2016/02/4a_NASM_PAMA-Student_Guide-Standard.pdf) and [Protecting Your Vocal Health: Student Information Sheet](https://nasm.arts-accredit.org/wp-content/uploads/sites/2/2016/02/6a_NASM_PAMA_NMH-Student_Information_Sheet-Standard-Vocal_June-2014.pdf).

Retain the planned safety and sensitivity reads. A source that refuses automated access receives the required “browser check” status.

### 8. The pending national scheduling question can be resolved without inventing a minute figure

**Severity:** Minor  
**LAYER:** frame, standard  
**REPEAT:** yes, the combined music read identified the unresolved source question.  
**Confidence:** firm.

**Location:** Days bullet, lines 25 to 28; “For the lead,” item 1; arts `STANDARD.md` section 3.4.

The directly accessible composition and theory section specifies a schedule equivalent to other academic subjects. It does not give a fixed weekly-minute minimum. [National Opportunity to Learn Standards, PDF page 21, printed page 19](https://nafme.org/wp-content/uploads/2023/05/NAfME-Opportunity-to-Learn-Standards-2020.pdf).

**Exact fix:** Replace the pending passage with:

> National scheduling guidance: composition and theory receives the same schedule as other academic subjects in the school. This course provides 225 minutes weekly on the full path. The 80-day path provides 225 minutes weekly over a semester, or an average of 112.5 minutes weekly when spread over 32 weeks. Compare that arrangement with the school’s academic schedule.

Add the source and nonnumeric recommendation to `STANDARD.md` section 3.4 through the lead. Remove the nonexistent pending anchor and the request to find a fixed figure.

### 9. Unmarked stale and inaccurate wording remains despite the stale check passing

**Severity:** Minor  
**LAYER:** process, frame  
**REPEAT:** yes, the combined music read identified the seam, finals-week, spelling and owed-list issues.  
**Confidence:** firm.

**Location:** Opening line; “For the lead,” items 3, 5 and 6; incoming seam explanation.

| Problem | Exact fix |
|---|---|
| “catalogue id” uses UK spelling. | Change to “catalog id.” |
| Item 3 calls weeks 16 and 32 “both finals weeks” for every level. | Write: “The full path checks in weeks 16 and 32; week 32 is finals. A daily semester short path ends in its week 16 finals.” |
| Item 5 says the preceding frame is being written. | Replace with: “The music 6 to 8 frame exists and its eight outgoing handoffs match this frame’s incoming rows.” |
| The incoming seam omits available unit locations. | Add grade 8 units 11 for invent/document, 12 for revise/perform, 9 for read/respond and 10 for express/choose. |
| The shared adoption-bar row still owes the standards gate and strand-id load. | Replace its owed sentence with: “NCAS id-membership checking and the 63 composition and theory strand ids were completed 2026-11-21.” |

I verified `later.csv` L83 is **done** and the 63 strand ids are loaded. This disagrees with the combined music report’s suggestion to leave L83 open. Apply corrections to living documents; retain dated reviews as records.

## Lens checklist

“Met” describes the frame’s provision, not certification of unwritten lessons.

| Lens requirement or error | Result |
|---|---|
| Correct year or level ownership | Met |
| All four processes in each level | Met |
| More than one tradition and period, including living composers | Met |
| Technique increases in difficulty | Met |
| K to 8 daily-period restriction | Not applicable |
| A showing in each instructional unit | Missed in Level 4’s explicit arrangements, finding 5 |
| Technique or model taught before use | Missed for rehearsal planning, finding 6 |
| Discipline words taught and used | Met |
| Works taught with their setting | Provision present; sources incomplete, finding 7 |
| Structured critique | Met |
| Revision after critique | Met |
| Assessment through musical work and response | Met in form; coverage and feasibility need findings 1, 2 and 5 |
| Original assessments rather than copied cornerstone tasks | Met at frame level |
| Set-up and collecting time inside the session | Met generally; Level 4 check fails feasibility, finding 5 |
| Equipment with a free alternative | Met in provision; listening equivalence needs finding 3 |
| Safe room and equipment use | Controls and reads planned; source links need finding 7 |
| Participation without compulsory solo performance | Met |
| Artistic responding distinguished from a respond day | Met |
| Tools support rather than judge finished work | Met |
| Five disciplines retain their own techniques and work | Met |
| Dance and PE boundary | Not applicable |
| Music does not replace mathematics instruction | Met |
| Sensitive works studied with community context | Provision present; specific sources need finding 7 |
| Individual work suitability and full rights verification | Not yet judgeable |

## What is right and should not be touched

- Levels are based on demonstrated preparation, not student grade.
- The bridge and review units respect the settled day limits.
- The full and short paths retain every unit.
- Ownership is complete and correctly distributed.
- The longer concert units reasonably receive more time for their eight ids and multiple evidence forms.
- Critique, revision, portfolios, teacher judgment and participation choices are built into the course.
- The core-subject contacts include fallbacks and do not assume optional courses.

I disagree with the combined music report’s overall “sound and buildable” verdict. Its inventory conclusion holds, but direct comparison with the national requirements reveals the substantive omissions above.

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Use two short form-development studies in units 8 and 13 | Establish variety without adding units | Course frame |
| Introduce the short rehearsal-planning card in unit 3 | Teach the model before its assessed use | Course frame |
| Use a simultaneous written Level 4 checkpoint | Fits one adult and 30 students | Course frame |
| Supply neutral starting artifacts after permitted omissions | Keeps retained units runnable | Course frame |
| Resolve national scheduling guidance without a numeric minimum | Matches the source actually read | Course frame; arts `STANDARD.md` |
| Close both obsolete adoption-bar owed items | Ledger and standards inventory confirm completion | `ADOPTION-BAR-SUBJECTS.md` |

## For Cory

- **Money:** The existing proposal is a printing ceiling of $40 per class per level, beside the free plain-paper route. This review makes no spending decision.
- No new scope, audience or outside-person decision is needed for these corrections.

## Sources and limits

The national handout was used to check complete actions; the scheduling document resolved finding 8. The two musician-health publications and the practitioner archive were opened to verify the proposed source links.

No finding rests on unverified subject-matter memory. The critique routine’s research basis and safe-use rules remain background claims as marked in the repository; this was not a full safety review.

Finished scoring guides, actual listening exemplars, individual rights statements, detailed 45-minute workloads and numbered senior calendars remain to be judged at the later stages. Nothing in this report establishes that the course has been tested with students.

## For the source list

Record the directly accessible composition and theory scheduling section, the two musician-health documents and the Ali Akbar Khan Library catalog. The scheduling section resolves the pending question without a browser takeover or a fabricated weekly minimum.
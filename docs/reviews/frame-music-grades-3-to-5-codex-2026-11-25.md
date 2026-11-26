# Second independent frame read: Music, grades 3 to 5

Date: 2026-11-25  
Course: `music-grades-3-to-5`  
Report returned in chat. No files changed.

## Verdict

**Needs correction before the scope and sequence is written.** The grade ownership, annual day totals, core-calendar placement and adjacent-course handoffs are sound, but several assessment instructions permit incomplete evidence or conflict with the stated schedule. The priority is to restore every owned standard’s requirements in the teaching and assessment instructions.

**Finding count: 9.**

## What I read and checked

- The complete [course frame](S:/CurioClass/docs/courses/music-grades-3-to-5/frame.md), its `frames.csv` entry, course-list selector and calendar rows.
- All 24 selected progression rows, the neighboring grade 2 and grade 6 music rows, and the 63 owned standards’ words-file lines.
- The adjacent music frames’ seams, models and relevant units.
- `frame-read.md`, the after-core provisions of `frame-write.md`, `EXPERT.md`, the arts lens, arts `STANDARD.md` and `APPROACH.md`, and the shared and arts adoption criteria.
- Relevant foundation, production-path, baseline, calendar, decision and earlier arts-review guidance.
- The cited math and ELA unit contacts, checked against their frames and calendar rows.
- The outside sources linked below.

There is no base text, so a source-map check is not applicable.

### Checks

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check music-grades-3-to-5` | Failed because day-level plan files do not exist yet; frame review continued. The command was course-filtered under the repository instruction. |
| `python -X utf8 scripts/frame.py check music-grades-3-to-5` | **0 failures.** |
| `python -X utf8 scripts/stale.py check` | **0 failures across 121 files.** Unmarked stale prose remains, as finding 9 explains. |
| Progression ownership | All 24 selected skills appear exactly once, in their own grade year. |
| Standards inventory | Each year lists 21 distinct ids, 63 across the band. Listing is complete; action and evidence coverage need correction. |
| Days | Each year has 60 unit days, two course-check days and two respond days: 64. Band total: 192. |
| Short path | Annual allocations total 32 sessions. |
| Calendar | Course checks in weeks 15 and 24 avoid every current core-check week for their grade. |
| Cross-subject timing | Math contacts and the grade 3 discussion contact match the calendar. The grade 5 writing reference needs the update in finding 9. |

## Findings, most serious first

### 1. Creating requirements are narrowed in teaching or assessment

**Severity:** serious  
**LAYER:** frame, progression  
**REPEAT:** yes, incomplete creating evidence was raised in the music K to 2 second read, finding 2.  
**Confidence:** firm

**Location:** Units 6, 10 and 11; `mu-g4-invent` and `mu-g5-invent`.

The national requirements include work across related tonalities and meters in grades 4 and 5, and craftsmanship in grade 5’s finished composition. These demands are not secured by the frame’s stated checks. [National music handout, PDF pages 1 and 3](https://nationalartsstandards.org/sites/default/files/2021-11/Music%20at%20a%20Glance.pdf), [New Mexico’s published music standards, PDF pages 3 to 5](https://web.ped.nm.gov/wp-content/uploads/2024/12/2022_F.24-Music-Grades-K-5.pdf).

| Location | Problem and student cost | Exact fix |
|---|---|---|
| Unit 6, `MU:Cr1.1.4b` | Teaching and evidence reduce the task to an ostinato in one given key and meter. The progression note makes the same reduction, although the words file retains the wider requirement. | Teach and keep two brief ideas: one in a teacher-supported major/duple setting and one in its relative minor/triple setting. Record tonal and metric evidence separately. Replace the progression note’s single-key-and-meter wording accordingly. |
| Unit 10, `MU:Cr1.1.5b` | Teaching mentions related keys and meters, but the evidence and mid-year sample accept one accompaniment in one given key and meter. | Require two brief accompaniments in the paired settings above, each using simple chord changes appropriate to that setting. State both settings in the kept-card evidence and update the cumulative sample. |
| Unit 11, `MU:Cr3.2.5a` | “Well-crafted” appears in teaching, but its evidence is only a talk item explaining intent. A weak finished product can receive a met mark through a good explanation. | Score the performed finished piece as well as the explanation. Add look-fors for intentional motif development, coordinated melody and two-chord accompaniment, and a finished version that incorporates the documented revisions. |

Keep these ids in their existing units. These corrections restore their requirements without moving ownership.

### 2. Listening checks allow structure or musical elements to be omitted

**Severity:** serious  
**LAYER:** frame  
**REPEAT:** yes, partial assessment coverage is the same kind as the music K to 2 second read, finding 2.  
**Confidence:** firm

**Location:** Units 1, 5 and 9, `MU:Re7.2.3a`, `.4a` and `.5a`; corresponding course-check samples.

The evidence asks for a feature of form **or** an element, together with setting. A student can therefore pass without addressing structure or without addressing musical elements. The national requirements join structure, elements and context, with explanation and evidence becoming more demanding across the grades. [National music handout, PDF page 7](https://www.nationalartsstandards.org/sites/default/files/Music%20at%20a%20Glance%20rev%2010-2-14.pdf).

**Why it matters:** The inventory looks complete while the check can certify a partial response.

**Exact fix:** Replace the either/or wording with one short response card containing three labeled prompts:

1. A structural feature.
2. A musical element.
3. A contextual feature.

Require students to connect all three to their response: describe in grade 3, explain in grade 4, and explain with evidence in grade 5. Allow annotated listening maps and teacher-scribed responses within the existing reading-load rule. Carry this wording into the cumulative samples.

### 3. Adjacent course checks duplicate the unit assessment window

**Severity:** moderate  
**LAYER:** frame  
**REPEAT:** yes, music K to 2 second read, finding 6.  
**Confidence:** firm

**Location:** “Days,” “Scored evidence,” units 2, 3, 6, 7, 10 and 11, and “Course-level checks.”

Each affected unit ends with its own assessment and respond day. The immediately following course check then samples that same unit. Carrying its earlier artifact unscored prevents duplicate artifact scoring, but still creates consecutive assessment windows for overlapping learning.

The after-core brief says the adjacent course check serves as that unit’s end-of-unit assessment when it covers the unit.

**Why it matters:** This consumes practice time and gives the scope writer conflicting assessment instructions.

**Exact fix:** For these six units:

- Make the following course check the unit’s end-of-unit assessment.
- Include its complete per-id evidence alongside the cumulative sample.
- Use the following course respond day for both purposes.
- Convert the displaced internal check and respond sessions into supported practice, revision and rehearsal.
- State this exception in the Days bullet, affected unit rows and course-check cells.

Keep the annual totals and current check weeks.

### 4. The timed assessment omits the compulsory warm-up

**Severity:** moderate  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm

**Location:** “Day kinds,” lines 93 to 95, and the assessment timetable under “Scored evidence.”

The frame requires a five-minute warm-up on **every day**. Its assessment timetable already totals 39 minutes without that warm-up. Following both instructions takes 44 minutes in a 40-minute session.

**Why it matters:** A writer must silently drop an instruction or shorten assessment and clean-up.

**Exact fix:** Replace the universal warm-up sentence with:

> Teaching, practice and rehearsal days open with five minutes of fluency. Check days use their stated assessment timetable, including any brief vocal or instrumental preparation within the allotted task time.

Retain the stated 39-minute assessment allocation. Later unit plans must time their actual tasks within it.

### 5. The leave-out promise lacks entry routes into dependent units

**Severity:** moderate  
**LAYER:** frame  
**REPEAT:** yes, music K to 2 second read, finding 4.  
**Confidence:** likely

**Location:** “Leave-out”; units 3, 7 and 11; concert units 4, 8 and 12.

The frame says each unit stands alone. Composing units nevertheless draw on the preceding improvising unit’s idea bank, drone or chord accompaniment. Concert units use the piece chosen in the opening unit. The retrieval provision addresses earlier-year learning, rather than an omitted unit from the same year.

**Why it matters:** Exercising the promised leave-out choice can remove the material or technique needed for the next unit.

**Exact fix:** Add these entry provisions:

- Units 3, 7 and 11: create a fresh personal idea during existing supported-practice time, with a demonstration of the minimum melody, drone or chord technique needed.
- Units 4, 8 and 12: offer a neutral Curio Class original concert piece and teach it by ear if the opening selection unit was omitted.
- Record the omitted unit’s ids as unclaimed. Entry support does not award them.
- State these routes in the Leave-out bullet and affected unit rows.

Preserve critique, revision and respond time.

### 6. Model retrieval is assigned after earlier units use the models

**Severity:** moderate  
**LAYER:** frame  
**REPEAT:** yes, music K to 2 second read, finding 5.  
**Confidence:** firm

**Location:** “Models carried,” especially `critique-protocol` and `rhythm-syllables`; “Day kinds.”

Every unit requires critique and revision, but the models table assigns the critique protocol’s first retrieval to unit 3. Rhythm syllables are used before unit 4, including warm-ups and the beat-count notation route, yet their first-use cell names unit 4.

**Why it matters:** The table puts essential retrieval after use, particularly for students entering without the optional preceding music course.

**Exact fix:**

- Set `critique-protocol` first use to **unit 1, before its first critique**. Describe unit 3 as its application to the owned composition-revision standards.
- Set `rhythm-syllables` first use to **unit 1’s first rhythm practice**. Describe unit 4 as adding fractional note values after math.
- Include the existing entry reteach at these first uses.

Keep progression ownership unchanged.

### 7. Some evidence instructions require recording despite the live alternative

**Severity:** moderate  
**LAYER:** frame  
**REPEAT:** yes, recording privacy and alternatives were addressed in `prework-arts-read-2026-11-19.md`, finding 14.  
**Confidence:** firm

**Location:** “Scored evidence,” the idea-bank model, units 2, 6 and 10, and unit 12’s rehearsal-log candidate.

Several instructions require a card **and** its sound recording, or specify sound-only kept takes. The subject approach permits live observation when a student declines recording. The frame also promises a route without a device.

**Why it matters:** Sound-only recording still records a voice. The current wording can make recording a condition of credit.

**Exact fix:** Add:

> Every recording is optional. A student may demonstrate live, with the teacher’s dated mark on the same guide serving as evidence. Improvement over time may be shown through three dated live observations and the student’s change notes.

Replace mandatory “and its recording” wording with “and its recording or dated live-observation record.” Apply the same alternative to the idea bank and rehearsal log.

### 8. Work anchors lack source links, and several remain unselected

**Severity:** moderate  
**LAYER:** frame  
**REPEAT:** yes, incomplete identification of works is the same kind as the music K to 2 second read, finding 7.  
**Confidence:** firm

**Location:** “Processes, anchors and works” throughout, particularly units 5, 6, 8, 10 and 11.

The frame contains no source URLs. Several entries identify an artist or event while leaving the piece or performance to a later writer: AlHaj, Kidjo, Shankar, the Silkroad Ensemble, Panorama and Tate.

**Why it matters:** The frame cannot yet establish the exact setting, teaching purpose or sensitivity scope of those anchors. “Concert music” alone also does not establish the absence of sacred material. Tate’s own description of *Chokfi’*, for example, identifies a church-hymn source. This is an illustration of the selection risk, not a recommendation to use that piece. [Composer’s work page](https://jerodtate.com/chokfi/).

**Exact fix:** Before the scope is written:

- Replace each artist-only placeholder with a named work or performance, including date and performer where relevant.
- Attach a free primary source link to every anchor’s identification and contextual claims.
- State the particular musical feature the selected work will teach.
- Match the sensitivity note to that work’s actual cultural and sacred content.

Leave edition-specific recording rights checks at the assigned unit-plan stage.

### 9. Unmarked coordination notes describe outdated repository state

**Severity:** minor  
**LAYER:** process  
**REPEAT:** yes, stale coordination prose recurs in the music K to 2 second read, findings 8 and 9.  
**Confidence:** firm for the repository snapshot read

**Locations and exact fixes:**

| Location | Stale or mismatched statement | Exact replacement |
|---|---|---|
| Frame, Cross-subject, grade 5 ELA row | It identifies `mu-g5-respond` with `W.5.1`, although the current progression specifies prior-year `W.4.1`. The fallback already uses that earlier learning. | “Unit 9 uses `mu-g5-respond`, `ela:W.4.1`, taught in English language arts grade 4 unit 3, days 81 to 119, the preceding year. Retrieve the opinion structure and model its application to musical evidence.” Remove the obsolete same-year dependency. |
| Frame, For the lead, item 1 | Week 24 is said to hold no other check. Current rows include computer science grade 4 there. Grade 4 week 15 also includes ELD, omitted from the note. | “Music’s checks avoid current core-check weeks. The lead’s after-core calendar pass must resolve shared weeks across individual courses, using current calendar rows.” |
| `ADOPTION-BAR-SUBJECTS.md`, arts pre-work row, line 568 | It still lists L83 and loading the 63 high school music ids as owed. L83 is marked done, and the ids are present. | “L83 completed: the standards gate checks NCAS ids against the loaded inventory. The 63 high school composition and theory ids, words lines and progression rows were loaded on 2026-11-21.” |

**Why it matters:** These notes send later workers toward completed work or an incorrect dependency. Keep dated review records unchanged.

## Lens checklist at the course-frame layer

“Met” means specified in the frame, rather than demonstrated by finished lessons.

| Lens check | Result |
|---|---|
| Grade ids remain in their own band year | Met |
| All four artistic processes appear each year | Met |
| Technique grows across units and years | Met in design; finding 1 restores omitted requirements |
| Discipline words support making and responding | Met |
| Students make choices and show work each unit | Met |
| Critique follows a protocol and leads to revision | Specified; first retrieval needs finding 6 |
| Works span cultures, periods and living makers | Met in intended range; exact selections and sources need finding 8 |
| Works carry maker, place, time and purpose | Partial; finding 8 |
| Assessment includes performance, response, self-assessment and kept work | Met in form; findings 1 to 4 correct coverage and timing |
| Schedule avoids a daily arts period | Met |
| Set-up and clean-up fit inside the period | Included; check-day warm-up conflict needs finding 4 |
| Equipment has free alternatives | Met generally; recording needs finding 7 |
| Hazards and controls are named | Met as planning provisions; safety read remains owed |
| No forced solo | Met |
| Artistic responding is distinguished from respond days | Met |
| Software supports rather than judges finished performance | Met |
| Arts disciplines remain distinct | Met |
| Music does not teach fractions ahead of math | Met, including the grade 5 beat-count fallback |
| Copied cornerstone tasks or questions | None apparent |

## What is right and should not be touched

- Four units per year, with each grade complete on its own.
- All 24 progression rows placed once and all 63 current owned ids listed.
- The 16, 12, 16 and 16-day unit allocation. The larger composing and concert allocations have defensible workload reasons.
- Matching grade 2 and grade 6 handoffs.
- Fractional note values placed after the relevant math teaching, with explicit fallbacks.
- Original music-making, critique, revision, nonsolo participation and invented or public alternatives to personal disclosure.
- The honest weekly-time gap: 80 minutes here versus the association’s 90-minute recommendation, and 40 minutes on the short path. [Opportunity-to-learn standards, printed page 11](https://nafme.org/wp-content/uploads/2020/08/NAfME-Opportunity-to-Learn-Standards-2020.pdf).

## Settled by the expert

These are recommendations for the caller to apply. No edits were made.

| Choice | Reason | File touched |
|---|---|---|
| Use paired major/duple and relative-minor/triple creating tasks | Makes tonal and metric coverage explicit | Frame units 6 and 10; affected progression notes |
| Score unit 11’s finished music as well as its explanation | Craftsmanship needs product evidence | Frame unit 11 |
| Require structure, element and context on listening-response cards | Prevents an either/or partial pass | Frame units 1, 5 and 9; cumulative samples |
| Combine adjacent unit and course assessment windows | Follows the after-core brief and restores practice time | Frame |
| Exempt check days from the universal five-minute warm-up | Resolves the 44-minute conflict | Frame |
| Retrieve critique and rhythm models at their first use | Supports entry without earlier optional music | Frame models table |
| Accept dated live observations beside every recording route | Preserves privacy and the device-free path | Frame |
| Retain annual totals, ownership and core-safe check weeks | Those checks are sound | Frame |

## For Cory

- **Money:** The proposed $75 annual class ceiling remains Cory’s decision. This frame estimates $30, $25 and $25 across the three years, plus an optional $20 initial rhythm-stick purchase. This review did not price or authorize purchases.

No new scope, audience or outside-person decision is needed for the corrections above.

## Limits and source follow-up

This is a frame review. It does not establish classroom feasibility, completed assessment-guide quality, recording rights or the suitability of every eventual work selection.

The frame’s safety controls remain **from memory**, as its own Safety read bullet states, until the specified safety read checks them. The critique routine is an adopted repository procedure; this report makes no research-effect claim for it. No substantive finding rests only on recalled subject knowledge.

For the source list, retain the linked national music handout, New Mexico’s standards document and the association’s scheduling guidance. The composer’s page illustrates why work-specific cultural sourcing must precede a final selection.

Prior session memory supplied only general review-workflow guidance. Findings were checked against current repository content and the linked outside sources.


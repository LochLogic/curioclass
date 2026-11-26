# Independent frame read: Physical Education, grades 6 to 8

Date: 2026-11-25  
Course: `physical-education-grades-6-to-8`  
Findings: **9**  
Read-only review. No files changed or report file created.

## Verdict

The frame has a sound overall sequence, complete structural placement of its progression rows, and three complete grade years. It needs corrections before scope and sequence writing, chiefly because several assessments permit partial evidence of owned indicators and the held fitness assessment lacks a workable response schedule. Preserve the 22-unit structure and default annual allocation while repairing those instructions, proving the shorter path, and updating the source and coordination notes.

## What I read and checked

- The frame-read brief, applicable after-core frame-write rules, EXPERT guidance, PE lens, PE adoption bar, STANDARD and APPROACH.
- Relevant foundation, shared approach, production, decision and calendar rules.
- The complete course frame, its course-list selector and frames.csv entry, all **58 selected progression rows**, the span-8 standard paraphrases, and **34 calendar rows**.
- Incoming and outgoing PE unit and handoff material, the progression edge document, and relevant earlier PE reviews and fix dispositions.
- Referenced core Units tables, relevant health material, and the dance frame that landed during this review.
- Outside sources linked below. No substantive finding rests on memory.

## Checks

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check physical-education-grades-6-to-8` | Fails because downstream plan-stage files do not exist yet |
| `python -X utf8 scripts/frame.py check physical-education-grades-6-to-8` | Initially passed; final run reports one stale dance Pending marker at frame line 361 |
| `python -X utf8 scripts/stale.py check` | Final run reports four failures: this frame’s dance marker and three in other frames |
| Course gate | Not run because it writes output and baseline files, contrary to the read-only boundary |

The missing downstream files and unrelated stale-note failures do not prevent this content verdict.

## Findings, most serious first

### 1. The named assessment evidence does not secure several owned outcomes

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, the same assessment-contract problem appears in the earlier K to 2 and 3 to 5 reads  
**Confidence:** firm

**Location:** Units 1, 10, 12, 13, 16, 17, 18 and 21, especially their Ends cells.

**Problem and cost:** The teaching descriptions are often broader than the evidence required at assessment. A writer can follow the frame literally and award coverage without observing or eliciting an owned part. BASELINE rule 23 requires teaching and checking every part; PECAT separately examines outcomes, content and assessments. [CDC PECAT](https://www.cdc.gov/assessing-improving-school-health/pecat/index.html).

**Exact fix:** Add the following evidence and explicitly name when its mark is collected.

| Unit | Gap | Required correction |
|---|---|---|
| 1 | “Two throwing forms” can omit rolling and other named forms | Require separate observed evidence of rolling, underhand, sidearm and overhand technique. Carry practiced observations into the final judgment where necessary. |
| 10 | Changing a written plan does not establish implementation of the exercise principles; the aerobic-fitness explanation is absent | Observe students carrying out and adjusting activities using the principles. Add an explanation connecting aerobic fitness, perceived effort and activity effort. |
| 12 | Five unspecified serves and one unspecified rally can omit required serve types, strokes or implement lengths | Name hand underhand and overhand serves, implement underhand and overhand serves, and forehand and backhand evidence with both implement lengths. |
| 13 | The knowledge tasks address choice but omit how social interaction affects involvement | Add a prompt explaining how working with others changed an invented participant’s engagement. |
| 16 | A picture question replaces performance of getting open; shooting evidence does not specify both forms | Observe multiple get-open moves in play and shots with and without an implement. |
| 17 | Selecting a shot for a picture does not check applying it | Observe a suitable shot and technique selected and executed during play. Specify volley evidence with both implement lengths. |
| 18 | Explaining only two leadership connections leaves two optional | Require connections for communication, feedback, teamwork and courtesy. |
| 21 | The promised reach rescue disappears from the specified skill evidence | Carry a separately observed dry-land reach-rescue mark from practiced work; retain the throw rescue and life-jacket tasks. |

Use named observations after teaching and practice, not additional unbudgeted tasks in the same four-minute visit. Preserve the respond days.

### 2. Unit 15’s held assessment has no allocated response day after it

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, contradictory assessment and response timing appears in the 3 to 5 read  
**Confidence:** firm

**Location:** Assessment bullet; units 15 and 18; For the lead 2; grade 8 calendar interpretation.

**Problem and cost:** Unit 15 allocates 12 days as eleven early days plus its held assessment on course day 47. It also promises a respond day after that assessment. Unit 18 claims day 48, and course-level checks occupy days 49 and 50, followed by their own response on day 51. The unit response is therefore missing or would consume another promised day.

Unit 15 also contradicts the general rule that units longer than eleven days receive two check days.

**Exact fix:** Keep the existing unit totals and course-check dates, but state this explicit exception and schedule:

| Grade 8 course days | Allocation |
|---|---|
| 1 to 10 | Unit 15’s initial teaching and practice |
| 11 to 25 | Unit 16, 15 days |
| 26 to 38 | Unit 17, 13 days |
| 39 to 46 | Unit 18, eight days, including its assessment and response |
| 47 | Unit 15’s held assessment |
| 48 | Unit 15’s response |
| 49 and 50 | Mid-year course-level check |
| 51 | Course-level response |

Revise both unit descriptions and For the lead 2 together. Explicitly identify unit 15 as the one-check-day exception, with practiced evidence collected beforehand. Require days.csv to encode the split allocation when that layer is written; the current calendar remains an even-spread frame projection.

### 3. The shorter path substantially understates the practice it removes

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, shorter-path arithmetic was a major issue in the K to 2 read  
**Confidence:** firm

**Location:** Day kinds; Shorter path; For the lead 1.

**Problem and cost:** Reducing 96 sessions to 64 removes 32 sessions per year. After the frame’s unit checks and responses, the default teaching allocations are approximately **70, 69 and 70 days**. With Fluency and Application each about one-third of teaching days, removing 32 of those days removes roughly **69 percent of that combined practice**, not one-third.

The frame also protects the last Fluency and Application days, but provides no allocation demonstrating that 32 eligible days remain removable in every year.

**Exact fix:**

- Replace “A third of the practice goes” with: “The shorter path removes one-third of all sessions and a substantially larger share of Fluency and Application.”
- Provide a per-unit table showing default Understanding, Fluency, Application, Check and Respond allocations, the exact removals totaling 32 per year, and retained allocations.
- Verify that every unit retains its protected days and all owned teaching and assessment evidence.
- Treat 64 sessions as an unverified target until that table works. If it cannot work, bring a changed dose to Cory with the completed comparison.

### 4. Upstream paraphrases still narrow three indicators that the frame correctly broadens

**Severity:** Moderate  
**LAYER:** standard and progression  
**REPEAT:** yes, “or” replacing required breadth appears in the 3 to 5 read  
**Confidence:** firm

**Location:** Local paraphrases of `SHAPE.S1.8.12`, `SHAPE.S1.8.13` and `SHAPE.S1.8.17`; progression rows `g7-strokes`, `g8-volley` and `g8-shoot`.

**Problem and cost:** The published indicators require both implement lengths for strokes and volleys, and shooting with and without an implement. The local paraphrases and progression notes instead permit alternatives. Units 12, 16 and 17 correctly restore that breadth, but later writers can regress by following the underlying data. [2024 PE standards](https://shapeamerica.org/standards/pe/new-pe-standards/).

The `g8-volley` note additionally offers a hand volley as though it could satisfy this implement indicator.

**Exact fix:**

- Change the stroke and volley paraphrases and progression notes to require **short-handled and long-handled implements**.
- Change shooting to require **with and without an implement**.
- Remove hand volleying as a substitute for `S1.8.13`; it may remain explicitly labeled review.
- Align the assessment notes with finding 1.
- Preserve the frame’s existing full-breadth teaching language.

### 5. Cultural selections appear settled before their required checks are complete

**Severity:** Moderate  
**LAYER:** process, affecting frame  
**REPEAT:** yes, cultural-source decisions recur in the progression and earlier PE frame reads  
**Confidence:** firm

**Location:** Base text and Sensitivity reads bullets; units 6, 13 and 22; For the lead 5.

**Problem and cost:** The frame calls activities “Picks” and says each was spot-checked, while unit 6 explicitly says Virginia Reel was not checked and unit 22 says Naadam was not checked. Several educational-use decisions are deferred until after the unit already names its selection.

Useful primary evidence is available. The Philippine education department publishes Tinikling instruction; Belo Horizonte’s education department documents capoeira workshops in municipal schools. These support educational contexts, without establishing every proposed adaptation or permission to reproduce materials. [Tinikling teaching resource](https://lrmds.deped.gov.ph/detail/21899), [school capoeira program](https://prefeitura.pbh.gov.br/educacao/a-escola-na-roda-de-capoeira).

**Exact fix:**

- Link the Tinikling teaching resource directly in unit 6.
- Label remaining unresolved selections **Candidate**, specifying the outstanding cultural description, educational-use or adaptation check.
- Replace “Each pick was spot-checked” with an accurate selection-by-selection status.
- Use the [Serbian national heritage register](https://nkns.rs/cyr/popis-nkns/kolo-kolo-u-tri-kolo-u-shest) for kolo’s cultural context; distinguish the sourced pattern from students’ subsequent choreography exercises.
- Keep unresolved activities replaceable within the existing outcomes and days.

The linked UNESCO kolo and capoeira entries returned human-verification walls. Record both as **browser check**; they were not fetched another way.

### 6. The untimed mile option has no defined progress measure

**Severity:** Moderate  
**LAYER:** frame and progression  
**REPEAT:** new  
**Confidence:** likely

**Location:** Unit 15; progression row `g8-fitness-test-track`.

**Problem and cost:** Students may select a mile walk or run with no time recorded, yet must track results, compare baseline and retest, and plot progress. Distance is fixed and time is excluded, so that option supplies no defined changing measure. Students choosing it cannot follow the same goal cycle as those choosing counts or reach distance.

**Exact fix:** Replace that option with a **fixed-duration, self-paced walk or run**, recording distance privately. Keep duration, route and recording method consistent between baseline and retest. Allow adaptations and a different assessment choice, and grade the goal-setting and monitoring process rather than the result.

Make the same correction in the progression note. Explicitly connect the assessment information to the student’s participation goal.

### 7. Unit 17 refers to using its new problem-solving method in an earlier unit

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, using a model before its introduction is an established frame-review issue  
**Confidence:** likely

**Location:** Unit 17, What students learn and Why this unit, here.

**Problem and cost:** Unit 17 introduces the problem-solving method but says it is “also used on unit 16’s game.” Its placement reason says it follows unit 16 so the method can be tested on two game types. The likely reading asks the writer to use the method before its stated introduction.

**Exact fix:** Replace that clause with:

> After the method is taught here, students apply it to the net game and to a reprise of unit 16’s invasion game within this unit.

Keep `g8-problem-methods` in unit 17. Name a recorded problem, tested change and result in both settings.

### 8. The graphing dependency names the wrong mathematics content

**Severity:** Minor  
**LAYER:** frame and progression  
**REPEAT:** yes, imprecise cross-subject leans appear in earlier progression reviews  
**Confidence:** firm

**Location:** Unit 15; Cross-subject mathematics table; `g8-fitness-test-track.cross_subject`.

**Problem and cost:** The frame cites `6.SP.B.4`, math unit 8, for plotting a student’s results across weeks. That unit teaches distributions using dot plots, histograms and box plots. It does not provide the stated time-and-result graph model.

The needed earlier content is available: math grade 6 unit 6 explicitly moves two related quantities between tables and first-quadrant graphs.

**Exact fix:** Replace the lean with `math:6.EE.C.9`, referencing **math grade 6 unit 6, days 96 to 117**, two years earlier. Specify a supplied time-and-result grid with labeled axes and private student records. Update the progression cell and both frame references together.

### 9. Refresh the landed dance coordination and several inaccurate summary statements

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale coordination notes recur in earlier PE reads  
**Confidence:** firm

**Location:** Cross-subject after-core introduction and dance row; Safety read bullet; unit 7 placement reason; For the lead 3 and 6.

**Problem and cost:** Dance landed during this review, leaving a stale Pending marker. Other summary statements disagree with the frame’s own unit or check tables.

**Exact fix:**

- Replace the dance Pending note with the landed placements: dance units **1 and 2, grade 6 weeks 1 to 16; units 5 and 6, grade 7 weeks 1 to 16; unit 9, grade 8 weeks 1 to 9**.
- Add `da-g6-technique`, `da-g7-technique` and `da-g8-technique` to the dance coordination row. State that PE retrieves relevant earlier dance work before its own movement applications.
- Retain the SEL Pending marker while that frame remains absent.
- Add unit **6**, moving poles, to the global safety-read list, matching its unit note.
- Change unit 7’s claim that the year-end check samples it to: “Its unit assessment provides its evidence; the year-end check carries that record unscored.”
- Update the calendar-pass record to include the grade 6 English language development overlap on school day **82**, alongside the existing health overlaps on day **84** in grades 6, 7 and 8. Leave resolution with the lead’s after-core calendar pass.

## Data checks and lens checklist

| Requirement | Result |
|---|---|
| Owned skills | Met: 58 selected rows, comprising 18 in grade 6 and 20 each in grades 7 and 8, placed once |
| Indicator ownership | Met structurally: all 61 span-8 indicators assigned |
| Full teaching and assessment | Needs findings 1 and 4 |
| Outcomes for all four standards in every grade | Met |
| Outcome-led units rather than a year of games | Met |
| Developmental order | Broadly sound; problem-solving wording needs finding 7 |
| Dance and fitness recur | Met across years and later applications |
| Annual totals | Met: 90 unit sessions plus six course-check and response sessions each year |
| Unit allocations | Broadly reasonable; held assessment and shorter path need findings 2 and 3 |
| Every year whole | Met in structure |
| Core calendar clashes | None found on PE’s mid-year check days |
| After-core calendar clashes | Present; lead calendar pass required |
| Incoming and outgoing seams | Relevant skills are picked up and handed on |
| Core subject dependencies | Ratio, science and cultural-background ordering works; graph citation needs finding 8 |
| Health coordination | Responsibilities and fallback teaching are distinguished |
| Dance coordination | Landed frame supplies the missing placements |
| SEL coordination | Still pending |
| Most students moving; at least half the lesson active | Required by the approach and supported by the planned stations; actual timing untested |
| Safe place to try; no punishment, elimination, human targets or public team picking | Explicitly protected |
| Disability, injury, skill and language adaptations | Required throughout; detailed adequacy awaits unit plans |
| Fitness privacy and growth | Protected; measurement option needs finding 6 |
| Space, weather and equipment | Addressed, with provisional required access and costs |
| Cues, skill-before-game instruction, closure and daily evidence | Framework provided; lesson-level checks remain for later reads |
| Base text and source map | Not applicable |

## What is right and should not be touched

- Preserve skill analysis before its later motor applications.
- Preserve the complete grade years, recurring fitness and dance, and progression from practice to changing conditions and games.
- Preserve private fitness records, growth against the student’s own baseline, and separation of language demands from movement judgments.
- Preserve dry-land water safety and the school’s control of any in-water program.
- Preserve the explicit disclosure that 135 weekly PE minutes fall below the national recommendation of 225. [National PE guidelines](https://shapeamerica.org/standards/guidelines/).

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Collect the missing evidence in finding 1 through named practiced observations | Checks existing owned content without moving ownership | Frame Ends cells |
| Use the explicit grade 8 split schedule in finding 2 | Provides both unit responses while retaining all totals and course-check dates | Frame units 15 and 18 |
| Require both implement lengths and both shooting forms upstream | Preserves the published indicators’ breadth | Standard paraphrases and progression notes |
| Give the aerobic assessment a private measurable result | Makes baseline and retest comparable | Frame unit 15 and progression note |
| Reprise invasion play inside unit 17 | Removes the backward instructional dependency | Frame unit 17 |
| Cite math unit 6 for the supplied graph | Matches the actual prior model | Frame and progression lean |
| Replace the landed dance Pending note | Prevents duplicate planning | Frame Cross-subject and For the lead |

## For Cory

- The existing equipment question remains: confirm the acceptable required-access provision and spending ceiling for a course listing approximately **$785 across the band**, particularly sticks, compasses and life jackets.

No new scope, audience or outside-person decision is needed for the corrections above.

## What I could not judge

- Whether the 64-session path preserves sufficient practice until its allocations are demonstrated.
- Actual movement time, observation workload and adaptation quality before lessons exist.
- Final SEL coordination while its neighboring frame is absent.
- Complete cultural-source and adaptation decisions for every candidate.
- School-specific equipment, supervision and medical arrangements.

## Sources and reading limits

- [2024 PE standards](https://shapeamerica.org/standards/pe/new-pe-standards/): checked span-8 actions and required breadth.
- [CDC PECAT 2019](https://www.cdc.gov/physical-activity-education/media/pdfs/18_300595-A_PECAT_042619_508tagged.pdf): targeted standards-analysis method and grade-band material; its earlier standards edition remains distinct.
- [National PE guidelines](https://shapeamerica.org/standards/guidelines/): verified the secondary weekly-minute recommendation.
- [Tinikling teaching resource](https://lrmds.deped.gov.ph/detail/21899): primary evidence of educational use; linked modules were not downloaded or adapted.
- [Serbian national heritage register, kolo](https://nkns.rs/cyr/popis-nkns/kolo-kolo-u-tri-kolo-u-shest): cultural context and pattern description.
- [Belo Horizonte school capoeira program](https://prefeitura.pbh.gov.br/educacao/a-escola-na-roda-de-capoeira): primary evidence of school workshops.
- [SPHEReS floor hockey guidance](https://myspheres.ca/en/curricular-activities/floor-hockey/): targeted safety reference, not a completed safety certification.
- UNESCO’s [kolo entry](https://ich.unesco.org/en/RL/kolo-traditional-folk-dance-01270) and [capoeira entry](https://ich.unesco.org/en/RL/capoeira-circle-00892): **human-verification wall, browser check**. Alternative primary sources were used for the limited claims above.

## For the source list

Add the direct Tinikling teaching resource, Serbian kolo register entry and Belo Horizonte school capoeira page. Record the two UNESCO entry URLs as browser checks rather than successfully opened sources.
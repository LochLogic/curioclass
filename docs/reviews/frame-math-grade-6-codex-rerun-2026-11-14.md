# Independent frame review: Math Grade 6

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/frame-math-grade-6-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files were changed.

## Verdict

The eight-unit sequence, progression ownership and 160-day allocation provide a sound foundation, but the frame needs targeted corrections before the scope and sequence is written. The largest risk is that writers will follow incomplete descriptions of required performances, an unjustified division limit, and inconsistent assessment-day instructions. Make those contracts explicit while preserving the unit order and total days.

## What I read and checked

- `docs/agents/EXPERT.md`, the mathematics lens, mathematics rubric, foundation, teaching approaches, applicable ROADMAP sections and BASELINE rules 20 to 24.
- The complete Grade 6 frame, its `frames.csv` row, all 26 Grade 6 progression rows, and the local Grade 6 standards.
- The neighboring Grade 5 and Grade 7 frames and their progression handoffs.
- Relevant calendars and cross-subject provisions in Grade 6 science, ELA and World Geography and Ancient Civilizations I.
- The inline source map, the base-text record, the stored base lesson inventory, selected preparation and student pages, and the base pacing and dependency diagrams.
- Earlier mathematics progression and frame reviews, including both existing Grade 6 reports and relevant fix dispositions.
- The module source and generated records referenced by the frame’s finance-tag proposal.
- Outside primary sources linked below. No curricular finding rests on memory.

**Gate limitation:** `python -X utf8 scripts/plan.py check` could not complete because importing `lesson.py` raised `ModuleNotFoundError: No module named 'markdown'`.

| Required check | Result |
|---|---|
| `python -X utf8 scripts/frame.py check math-grade-6` | Passed: 0 failures; 8 units, 160 days |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files, 0 failures |
| Independent ownership audit | All 26 owned skills placed exactly once; all 47 local codes accounted for |
| Independent source-map audit | All 147 base lessons accounted for once, with no missing or duplicated lesson |
| Requested source-map CSV | Absent; the frame-writing brief expressly defers the day-level CSV to the scope and sequence |

The incomplete full gate does not withhold this verdict, following the user’s current instruction. No dependency installation, turn mutation or defect-ledger write was performed.

## Findings, most serious first

### 1. The culminating geometry application is cut without a named required replacement

**Severity:** Moderate  
**LAYER:** base text  
**REPEAT:** yes, existing Grade 6 expert finding 1  
**Confidence:** likely

**Location:** Unit 1 and source-map row cutting 6.1.19.

**Problem and consequence:** The cut leaves the extended design application as an extension candidate. Unit 1 names real surface-area problems but does not identify a required contextual task joining polygon area, nets and material estimation. A writer can therefore preserve the computations while losing the substantial application.

The [base preparation page](https://im.kendallhunt.com/MS/teachers/1/1/19/preparation.html) identifies lesson 19 as the culminating modelling lesson. However, the earlier report overstates its uniqueness: retained [lesson 15](https://im.kendallhunt.com/MS/teachers/1/1/15/index.html) already includes a wrapping-paper context. The concern is the missing required replacement, rather than a claim that all contextual surface-area work disappears.

**Exact fix:** Keep Unit 1 at 17 days. Adapt the retained lesson 15 net-building activity into a bounded, given-dimension shelter problem: students draw its net, calculate floor and triangular-face areas, estimate covering material, and justify which faces they include. Name this required task in Unit 1 and the source-map reason for cutting lesson 19. Use MP7 and MP4 as Unit 1’s two named practices; retain the extended design investigation as an extension.

### 2. Assessment-day descriptions promise more days than the allocations contain

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, existing Grade 6 expert finding 2  
**Confidence:** firm

**Location:** “Days” bullet and source-map totals for Units 2, 3, 4, 6 and 7.

**Problem and consequence:** The opening rule promises major-work units a mid-unit check, its respond day and mixed-practice days, in addition to the end-of-unit assessment and respond day. Units 2 and 6 have only four added days. Units 3, 4 and 7 have three; Unit 3 explicitly names a mid-unit check but no associated response allocation. Writers cannot implement the stated rule consistently.

**Exact fix:** Replace the blanket rule with:

> Every unit has an end-of-unit assessment day and a following respond day. Units 2 and 6 also have separate mid-unit check and respond days. Units 3, 4 and 7 have one combined mid-unit check and respond day, planned as approximately 20 minutes checking and 30 minutes responding. Spaced, mixed practice runs in daily openings.

Spell out those compositions in every affected source-map row. Preserve all existing totals.

### 3. The division row imposes an unsupported Grade 5 size ceiling

**Severity:** Moderate  
**LAYER:** progression  
**REPEAT:** new  
**Confidence:** firm

**Location:** `data/progressions/math.csv`, `m6-long-division`.

**Problem and consequence:** The row limits numbers to four-digit dividends and two-digit divisors. That imports the previous grade’s size boundary into Grade 6’s algorithm-fluency standard. It also conflicts with retained [base lesson 12](https://im.kendallhunt.com/MS/students/1/5/12/index.html), whose main work includes larger dividends and divisors. A writer following the row could remove intended work.

**Exact fix:** Replace the number-limit sentence with:

> Begin with manageable multi-digit whole numbers, then vary dividend and divisor lengths and include zeros and context-appropriate remainders. The four-digit dividend and two-digit divisor boundary belongs to Grade 5 strategies and is not a Grade 6 ceiling.

Carry that clarification into Unit 5’s description. The [official standards](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf), printed pages 35 and 42, distinguish these expectations.

### 4. Two equation-standard performances remain implicit

**Severity:** Moderate  
**LAYER:** standard  
**REPEAT:** yes, standard-completeness findings in the earlier Grade 6 read  
**Confidence:** firm

**Location:** Unit 6 and `m6-one-step-equations`.

**Problem and consequence:** Unit 6 describes solving equations and writing expressions, but does not explicitly require testing supplied equations **and inequalities** by substitution from a specified set. It also leaves unstated the distinction between an unknown and a variable ranging over a set. These are required performances, not vocabulary refinements.

The [Expressions and Equations Progression](https://commoncoretools.files.wordpress.com/2011/04/ccss_progression_ee_2011_04_25.pdf), PDF pages 2 and 6, supports these distinctions. The retained [inequality lesson](https://im.kendallhunt.com/MS/teachers/1/7/9/preparation.html) explicitly teaches substitution, so the source already supports the work.

**Exact fix:** Add to Unit 6 and its owning progression row:

> Students substitute candidates from specified sets into equations and supplied simple inequalities, justify whether each statement is true, and distinguish a variable representing an unknown from one ranging over an allowed set.

Use nonnegative candidates here. Unit 7 applies the idea to signed rational numbers and teaches writing and graphing inequalities. This preserves ownership.

### 5. Progression lesson pointers misidentify where instruction occurs

**Severity:** Moderate  
**LAYER:** progression  
**REPEAT:** yes, existing Grade 6 expert finding 6  
**Confidence:** firm

**Location:** Grade 6 progression notes.

**Problem and consequence:** Several pointers direct writers past the actual introduction or toward omitted material. Most significantly, `m6-long-division` points to lessons 12 to 15, although [lesson 10 introduces long division](https://im.kendallhunt.com/MS/teachers/1/5/10/preparation.html) and [lesson 11 develops non-whole quotients](https://im.kendallhunt.com/MS/teachers/1/5/11/preparation.html).

**Exact fix:**

| Row | Correct the source pointer to |
|---|---|
| `m6-long-division` | 6.5.9 to 11: partial quotients, algorithm introduction and non-whole quotients; reinforcement in 6.5.12 |
| `m6-order-absolute-value` | 6.7.3 to 7 |
| `m6-inequalities` | 6.7.8 to 10 |
| `m6-four-quadrants` | 6.7.11 to 15 and 19 |
| `m6-summarize-data` | Retain 6.8.12 to 18; remove the implication that omitted 6.9 is needed for completion |

List these corrections under “For the lead” for the progression fixer.

### 6. The focus-counting question is already answered by the evidence guide

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, existing Grade 6 expert finding 7  
**Confidence:** firm

**Location:** “Major work” and “For the lead” item 2.

**Problem and consequence:** The frame defers whether connected supporting work counts, although the [evidence guide, indicator 1e, PDF pages 13 to 15](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf) explicitly includes it. The strict unit fraction is also left as “5 of 8” without its 62.5 percent value. This makes an unresolved rule appear to govern later day transfers.

**Exact fix:** Close item 2 with:

> Count supporting work where its connection to major work is explicit. Report strict counts alongside connected counts: 5 of 8 units strictly, 62.5 percent; 6 of 8 with connected supporting work, 75 percent. Current day estimates are 104 of 160 strictly and 123 of 160 with connections. The scope and sequence verifies lesson and minute allocations, including assessments and daily practice.

Do not transfer days merely because the strict unit count is below 65 percent.

### 7. Cross-subject notes still speculate about calendars now on file

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, existing Grade 6 expert finding 3  
**Confidence:** firm

**Location:** Cross-subject table and “For the lead” items 5 and 6.

**Problem and consequence:** Science Unit 4 is already placed at days 93 to 116, hazards at 117 to 136, and ELA research at 63 to 86. The mathematics frame still uses conditional language about their placement. Item 5 also says the current order ends on major work, although Unit 8 is additional work, and incorrectly dismisses the timing benefit of swapping Units 7 and 8.

**Exact replacement:**

> Science Unit 4 follows mathematics rates and ratio scaling. Science hazards precedes mathematics histograms and teaches frequency, intervals and reading supplied histograms locally. ELA research precedes mathematics Unit 8. Before mathematics histograms, ELA uses tables, bar graphs and line graphs.

Replace item 5 with:

> Keep the base unit order because science provides its own histogram bridge. A swap could move mathematics histograms into science’s hazards window, but is unnecessary under that bridge.

Close item 6 as resolved. Keep conditional bridges for schools that change the calendars.

### 8. The proposed finance-tag fix targets generated data

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, the same regeneration problem is recorded in `frame-math-k-2-fixes-2026-11-14.md`  
**Confidence:** firm

**Location:** “For the lead” item 4.

**Problem and consequence:** The instruction says to edit `data/modules.csv`. Its source, `data/modules/math.txt:71`, still supplies `NSPFE.Earning Income`, and `scripts/build_db.py` regenerates the CSV from those text files. The coverage ledger also retains the mathematics tag. Editing only the generated CSV makes the correction temporary.

**Exact fix:** Rewrite item 4:

> Remove `NSPFE.Earning Income` from the dependent-and-independent-variables entry in `data/modules/math.txt`; regenerate the derived module records through the normal build; remove the corresponding mathematics finance claim from `data/coverage.csv`. Preserve 6.EE.C.9 and hourly-pay contexts.

### 9. Unit 1 incorrectly calls letters standing for numbers new

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, existing Grade 6 expert finding 4  
**Confidence:** firm

**Location:** Unit 1, “Why this unit, here.”

**Problem and consequence:** “The first use of letters standing for numbers” contradicts earlier-grade work. It invites unnecessary introductory teaching instead of retrieval. The [Expressions and Equations Progression](https://commoncoretools.files.wordpress.com/2011/04/ccss_progression_ee_2011_04_25.pdf), PDF page 4, explicitly traces unknown letters to Grade 3.

**Exact replacement:**

> Its formula work retrieves earlier use of letters for numbers and begins this year’s systematic work with variables and expressions, completed in Unit 6.

### 10. The mathematics lens describes existing handoff work as missing

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, Grade 1 independent review finding 6 and the K to 2 fix report  
**Confidence:** firm

**Location:** `docs/agents/lenses/math.md:61`.

**Problem and consequence:** The lens says only Grades 3 to 5 have progression work and other bands need equivalent handoffs. The assembled progression already records ownership, prerequisites, handoffs, models and limits through Grade 11. This can send readers back into completed structural work.

**Exact replacement:**

> data/progressions/math.csv records core mathematics ownership, handoffs, models and limits from kindergarten through Grade 11. The Grades 3 to 5 narrative remains a supplementary explanation. Course frames check these handoffs against actual unit order.

This does not claim equivalent narrative essays exist for every band.

### 11. The preceding frame still says other subject frames will be written later

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale-status findings in earlier frame reads  
**Confidence:** firm

**Location:** Grade 5 mathematics frame, Cross-subject introduction.

**Problem and consequence:** The parenthetical “their frames are written later” is stale: the relevant science frame exists. It obscures the opportunity to check actual receiving-unit calendars.

**Exact replacement:**

> The same-year needs form the availability calendar; compare the mathematics availability dates below with the receiving units in the current subject frames.

## Coverage, order and days

| Unit | Days | Retained base lesson days | Added days | Load judgment |
|---|---:|---:|---:|---|
| Area and surface area | 17 | 15 | 2 | Reasonable with required application secured |
| Ratios | 21 | 17 | 4 | Appropriate sustained major work |
| Rates and percentages | 20 | 17 | 3 | Appropriate once response composition is explicit |
| Fraction division | 20 | 17 | 3 | Appropriate for meanings, algorithm and fractional volume |
| Decimal arithmetic | 14 | 12 | 2 | Compressed but defensible with later spaced practice |
| Expressions and equations | 23 | 19 | 4 | Appropriate for five substantial progression rows |
| Rational numbers | 22 | 19 | 3 | Appropriate, including inequalities and GCF/LCM |
| Data | 17 | 15 | 2 | Defensible with the stated merges and retained application |
| Course checks and response | 6 | 0 | 6 | Three checks, each followed by response |
| **Total** | **160** | **131** | **29** | Fits the full-year yardstick |

Against a 180-day school year, this leaves 20 days beyond the planned course. No unit is demonstrably far over or under its share.

All 26 owned skills have one home. Grade 5 prerequisites are picked up, Grade 7 receives the stated handoffs, and older factor and graphing skills have re-entry provisions. Early expression work is explicitly identified as beginning standards completed later.

The base dependency order is respected. Every one of 147 source lessons has a disposition; the retained lessons occupy 131 days after merges. No non-commercial or reference-only curriculum is mapped for adaptation.

## Mathematics lens checklist

| Course-frame check | Result |
|---|---|
| Major-work share checked by units, lessons and time | **Missed in completion:** counting rule can be settled now; lesson and minute evidence remains for the scope and sequence. Finding 6 |
| Supporting clusters practise major work | **Met:** geometry connects to expressions and fraction operations |
| Every source-map row has a disposition | **Met:** all 147 lessons accounted for; application replacement needs clarification |
| Ownership and grade handoffs | **Met:** no missing or duplicated skill |
| Models introduced before dependent use | **Met:** ratio representations precede their use; four quadrants extend Grade 5 coordinates |
| Algorithms introduced at the proper grade | **Met:** Grade 6 owns division and decimal algorithm fluency |
| Grade limits respected | **Missed:** unsupported division ceiling, finding 3 |
| Unit-task and day-level lens requirements | **Not applicable to final verification at this layer:** actual tasks, exits, keys and accommodations require later plans |

## What should be preserved

- The eight-unit order and 160-day total.
- Both meanings of fraction division, models linked to algorithms, and later mixed practice.
- Explicit completion of the ratio strand across Units 2 and 3.
- The Grade 5 and Grade 7 seams and readiness checks for older skills.
- Paper paths, neutral contexts, and the separation of signed-number placement from Grade 7 arithmetic.

## Earlier-read reconciliation

The earlier Grade 6 findings about response allocations, stale calendars, lesson pointers and the false “first” claim remain open.

I do not carry forward the earlier claim that 6.G.A.3’s side-length work is absent: the frame names grid-line distances and polygons, and its cited progression row explicitly connects coordinates to polygon side lengths. I also narrow the earlier geometry-application finding as explained in finding 1.

The earlier independent report’s gate-based withholding is superseded by this completed content review and the user’s current gate instruction.

## Settled by the expert

| Choice | Reason | Files affected when applied |
|---|---|---|
| Retain eight units and 160 days | Ownership, dependency order and overall allocation are coherent | Grade 6 frame |
| Require bounded geometry application within retained lesson 15 | Preserves required application without transferring days | Unit 1 and source map |
| Use combined mid-unit check and response in the three-day allocations | Makes the stated checks fit their budget | Units 3, 4 and 7 |
| Remove the inherited division size ceiling | Grade 6’s standard and retained source work exceed it | Progression and Unit 5 |
| Make substitution and variable-set meanings explicit in Unit 6 | Completes its existing contract without moving ownership | Progression and frame |
| Count explicit supporting-to-major connections | The evidence guide answers the deferred rule | Focus statement |
| Retain data last with science’s local bridge | Existing calendars can function without reordering | Cross-subject notes |
| Correct the finance tag at its source and ledger | Prevents regeneration of the removed claim | Lead instruction and data records |

## Limits and sources

This is a frame review. It does not establish classroom timing, assessment quality or successful teaching. Those require written days, items and trial evidence.

- [Official mathematics standards](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf): grade boundaries and required performances.
- [Ratios and Proportional Relationships Progression](https://commoncoretools.files.wordpress.com/2012/02/ccss_progression_rp_67_2011_11_12_corrected.pdf): ratio representations and the Grade 7 handoff.
- [Expressions and Equations Progression](https://commoncoretools.files.wordpress.com/2011/04/ccss_progression_ee_2011_04_25.pdf): variables, substitution and earlier-grade foundations.
- [Statistics and Probability Progression](https://commoncoretools.files.wordpress.com/2011/12/ccss_progression_sp_68_2011_12_26_bis.pdf): distributions, displays and measures.
- [Base scope and sequence](https://im.kendallhunt.com/MS/teachers/1/scope_and_sequence.html): pacing, dependencies and source order.
- [Fishtank Grade 6 pacing](https://www.fishtanklearning.org/curriculum/math/6th-grade/pacing-guide/): comparison sequence and school-year allowance; used as reference only.
- [K to 8 Publishers’ Criteria](https://achievethecore.org/content/upload/Math_Publishers_Criteria_K-8_Spring_2013_FINAL.pdf): focus, coherence and rigor.
- [Federal problem-solving practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/16/Published): representations, reflection and strategy comparison.

The compiled 2023 Progressions exceeded the web tool’s size limit. Smaller author-issued drafts were read instead; they are identified as drafts. Separate Number System and Geometry draft retrievals failed, so those judgments use the official standards and inspected base lessons.

**For the source list:** Add the working [archived Progressions index](https://archive.math.arizona.edu/ime/progressions/) and its accessible individual-draft routes as fallbacks.

## For Cory

- Assign the qualified mathematics content reviewer required for the completed course’s checks and keys, including any payment decision.
- No standard transfer, additional course scope or audience change is proposed.

**Verdict:** Sound foundation; targeted corrections required before the scope and sequence. **Finding count:** 11. **Report path:** `docs/reviews/frame-math-grade-6-2026-11-14.md`, supplied here only.
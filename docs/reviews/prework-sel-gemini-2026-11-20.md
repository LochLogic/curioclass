# Social and emotional learning pre-work: second-model cold read, 2026-11-20

> Filed by the lead 2026-11-20. Gemini 4 Neon (medium effort) in Antigravity, pasted by Cory from S:/CurioClass-gemini/ (prompt 10 to 18 for this subject), after it passed calibration (docs/reviews/calibration-*-gemini-2026-11-20.md). Its saved report is S:/CurioClass-gemini/reports/prework-sel-read.md; text unchanged here except wording the repository checks flag.

Independent second-model cold read of social and emotional learning (SEL) stage 1 pre-work, written as the curriculum expert (docs/agents/EXPERT.md) with the SEL lens (docs/agents/lenses/sel.md). Read only; nothing in the repository was edited. Outside sources were checked via web search and named by link below; anything resting on memory is marked "from memory". The first read (docs/reviews/prework-sel-read-2026-11-19.md) was not opened until all findings below were finalized; the closing section compares the two reads.

## What I read

- AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/sel.md; docs/COURSE-RUN.md; docs/FOUNDATION.md; docs/APPROACH.md; docs/courses/UNIT-PLAN.md; docs/pipeline/briefs/prework-codex-read.md; docs/pipeline/briefs/sensitivity-read.md.
- SEL pre-work under review: docs/courses/sel/STANDARD.md; docs/courses/sel/APPROACH.md; data/standards/casel-5.txt; docs/ADOPTION-BAR-SUBJECTS.md (pass rule, C1 to C16, part 9, the SEL row of "Before a scope and sequence in this subject", and the sources table); docs/reviews/sel-open-material-2026-11-16.md; docs/reviews/sel-ownership-check-2026-11-21.md.
- Comparison and verification files: docs/courses/health/APPROACH.md (finished approach page); data/courses.csv (SEL rows, lines 41 to 44); scripts/progression.py (`STD_FILES`, `ANCHOR`, `code_grades()`, `codes()`, and ownership checks, lines 1 to 275); data/standards/nhes-2024.txt (lines 1 to 100); targeted slices of data/progressions/ela.csv and data/progressions/social-studies.csv to verify every cross-subject lean id named in STANDARD.md section 7.
- Opened only after my own findings were written: docs/reviews/prework-sel-read-2026-11-19.md.

## Verdict

The CASEL 5 standards list is sound: all 40 sub-skill ids match the published framework in count, competency assignment and order, are unique, are rewritten in Curio Class's own words, and appear once and only once in every grade from kindergarten through grade 12. The biggest risk is that three operational foundations will break when Stage 2 (progression) and Stage 3 (frames and unit plans) begin: `scripts/progression.py` enforces single-grade ownership across K to 12 and will reject all 40 sub-skills under SEL's settled four-band owner rule, the 64-session and 32-session pacing math does not add up for 6 units of up to 8 sub-skills, and `docs/courses/sel/APPROACH.md` misplaces or drops several required `UNIT-PLAN.md` fields (including the C8 student self-check). The one change that matters most before Stage 2 is reconciling the progression gate rules, the session-and-short-path arithmetic, and the `APPROACH.md` field map so downstream writers do not build uncheckable progressions or non-compliant unit plans.

## What I counted

| Check | Result |
|---|---|
| Ids in `data/standards/casel-5.txt` | 40 unique ids (`CASEL.Self-Awareness.1` to `9`, `CASEL.Self-Management.1` to `7`, `CASEL.Social Awareness.1` to `8`, `CASEL.Responsible Decision-Making.1` to `7`, `CASEL.Relationship Skills.1` to `9`); all 40 verified against the published CASEL 5 "Such as:" lists |
| Own-words check (`casel-5.txt`) | All 40 statements rewritten in Curio Class's own words; no copied CASEL sentences or long verbatim runs |
| Grade table (`STANDARD.md` section 3) | 13 grades (K to 12), 6 units per grade (78 units total); every grade covers all 40 sub-skills once and only once; unit sizes run 4 to 8 sub-skills (34 of 78 units hold 8 sub-skills) |
| Courses in `data/courses.csv` | 4 SEL band rows (`sel-k-2`, `sel-3-5`, `sel-6-8`, `sel-9-12`), lines 41 to 44; `sel-k12` and "Light shelf" are already removed |
| Cross-subject leans (`STANDARD.md` section 7) | Health: NHES S4, S5, S6 verified in `data/standards/nhes-2024.txt`. Social studies: `ssk-rules-why`, `ssk-talk-together`, `ss1-group-rules`, `ss1-community-problems` all verified in `data/progressions/social-studies.csv`. ELA: `ek-discussion` through `e5-discussion`, `e6-collab-discussion` through `e8-collab-discussion`, `e9-sl-discussion`, `e10-sl-seminar`, `e11-seminar`, `e12-seminar` all verified in `data/progressions/ela.csv` |
| `scripts/progression.py` SEL support | None: `'sel'` is absent from `STD_FILES`, `ANCHOR` and `code_grades()`; `codes()` still splits on whitespace (collapsing 24 of 40 CASEL ids); lines 272 to 274 fail any code owned by more than one grade |
| `UNIT-PLAN.md` field placement in `sel/APPROACH.md` | 1 misplaced item (student voice inside Unit field 10), 1 direct contradiction (Section field 2), 1 missing bar-C8 requirement (student self-check), 1 field-4 gate conflict (`Retrieval only:` / K to 2 timing), and 4 partial drops (Section fields 1, 3, 5 and 7) |

## Findings, most serious first

### 1. `scripts/progression.py` needs four changes for SEL, not one, and its ownership gate will fail all 40 sub-skills

- **Where:** `docs/courses/sel/STANDARD.md` section 3 ("Ownership, for the progression", lines 87 to 98); `scripts/progression.py` (`STD_FILES` lines 51 to 62, `ANCHOR` lines 68 to 70, `code_grades()` lines 87 to 141, `codes()` lines 150 to 156, single-grade ownership check lines 272 to 274).
- **What is wrong:** `STANDARD.md` line 97 says only that the gate needs the `codes()` tab-split fix because 24 sub-skill names contain spaces. In reality, `scripts/progression.py` needs four changes before it can check `data/progressions/sel.csv`:
  1. `'sel': ['casel-5.txt']` is missing from `STD_FILES` and `'sel': 'casel-5.txt'` is missing from `ANCHOR`.
  2. `codes()` (line 155) splits on whitespace and collapses the 24 `Social Awareness`, `Relationship Skills` and `Responsible Decision-Making` ids.
  3. `code_grades()` has no `'sel'` branch to enforce that owner rows sit only in grades `2`, `5`, `8` and `12` while `~` rows may sit in any grade K to 12.
  4. Lines 272 to 274 fail any anchor code owned by more than one grade (`len(gs) > 1`). Because `casel-5.txt` has 40 ungraded ids and SEL's settled rule gives each id four owner grades (`2`, `5`, `8` and `12`, totaling 160 owned rows), every single one of the 40 sub-skills will fail the gate once `'sel'` is registered.
- **Cost:** Stage 2 will stall at the progression gate with 40 false ownership failures, or a writer will work around the gate by inventing unapproved band-suffixed codes that fail `scripts/standards.py`.
- **Fix (replace the last sentence of the "Ownership, for the progression" paragraph in `docs/courses/sel/STANDARD.md`, lines 97 to 98):**

> Before the first SEL progression check runs, `scripts/progression.py` needs four updates: (1) add `'sel': ['casel-5.txt']` to `STD_FILES` and `'sel': 'casel-5.txt'` to `ANCHOR`; (2) change `codes()` to split on the tab only, since 24 sub-skill ids contain spaces; (3) add a `'sel'` branch in `code_grades()` returning `(['2', '5', '8', '12'], GRADES)`; and (4) in the ownership check, require each SEL anchor id to be owned by all four band-end grades (`gs == {'2', '5', '8', '12'}`) instead of failing when `len(gs) > 1`.

- **Confidence:** Firm.

### 2. Session arithmetic and the 32-session short path contradict each other in `STANDARD.md` and `APPROACH.md`

- **Where:** `docs/courses/sel/STANDARD.md` section 2 (lines 59 to 66) and section 3 (lines 75 to 77); `docs/courses/sel/APPROACH.md` ("What a good SEL session does", line 9; "Kinds of day in SEL", lines 30 to 31).
- **What is wrong:** Three stated rules cannot hold at the same time:
  1. Section 2 sets 64 sessions a year across 6 units, which is 10 to 11 sessions per unit. Taking 2 sessions per unit for the Check and Respond days leaves 8 to 9 teaching sessions per unit.
  2. Section 3 caps each unit at 8 sub-skills (34 of the 78 units across K to 12 hold 8 sub-skills) and states "so each has time to be rehearsed (about two sessions a sub-skill)". Eight sub-skills at two sessions each requires 16 teaching sessions plus Check and Respond (18 sessions per unit, or roughly 92 to 108 sessions a year), not 64.
  3. Section 2 defines the 32-session short path as "it drops the second Application session in each unit and never drops a unit". Dropping one session from each of 6 units removes 6 sessions (leaving 58), not 32. Even across 6 units, 32 sessions leaves only 5 to 6 sessions per unit total.
- **Cost:** Frame writers in Stage 3 cannot satisfy C2 ("days add up to the stated year" and a working short path) without either silently breaking the 64-session cap, cramming 8 sub-skills into discussion-only sessions with no rehearsal (a bar part 9 fail), or inventing different short-path cuts in every grade.
- **Fix (replace lines 61 to 63 and lines 75 to 77 of `docs/courses/sel/STANDARD.md`; confirm with Cory if dose changes):**

> One session a week (32 sessions a year, 5 to 6 sessions per unit) is the stated short path (C2): it never drops a unit, bundles each unit's related sub-skills into two sections of two sessions (Understanding with guided Fluency, then Application), and pairs the unit Check and Respond review into the unit's closing session.

> In every grade all 40 sub-skills are taught once and only once as a unit's own, across six units of 10 to 11 sessions each (8 to 9 teaching sessions plus 1 Check and 1 Respond). No unit teaches more than eight sub-skills first. Because 8 to 9 teaching sessions cannot give two full sessions to each of eight separate sub-skills, a unit groups closely related sub-skills into two or three sections of two to four sessions (for example pairing a self-awareness cue with a self-management routine, or two linked relationship steps), so each session still names one focus skill and gives every student rehearsal time; a sub-skill that suits a late unit better comes back there in practice, not as a first teaching.

- **Confidence:** Firm.

### 3. Multiple unit and section plan fields in `docs/courses/sel/APPROACH.md` are misplaced, dropped, or contradict `docs/courses/UNIT-PLAN.md`

- **Where:** `docs/courses/sel/APPROACH.md` lines 43 to 99, checked field by field against `docs/courses/UNIT-PLAN.md` lines 145 to 280 and `docs/ADOPTION-BAR-SUBJECTS.md` part 9.
- **What is wrong:** Six field entries do not match `UNIT-PLAN.md`:
  1. **Unit field 10 (Sources, lines 70 to 71):** Places an instructional activity rule ("Student voice (class norms, or a school improvement the class proposes and carries out) is placed in the unit's Application sessions") inside Unit field 10 ("Sources and what is still to make"). It belongs under `Kinds of day` (Application) and `Section field 6` / `Section field 7`.
  2. **Section field 1 (Standards and practices, lines 72 to 73):** Drops the shared contents of Section field 1 (the section's sub-skill ids, this section's share of each sub-skill in our own words, limits that bite here, and connections to other standards of the grade with the day). It also puts "before you teach" only in Section field 1, whereas `ADOPTION-BAR-SUBJECTS.md` part 9 item 13 and `STANDARD.md` section 4, E require "before you teach" at the top of **each unit's teacher page** (and `STANDARD.md` section 5 item 4 requires the reporting route in **each unit's teacher notes**).
  3. **Section field 2 (Where it sits, line 74):** Reads "what the section builds on and leads to, in the unit." `UNIT-PLAN.md` line 240 explicitly states: "Not here: builds on, leads to and comes back (unit field 3)." It also drops the actual Section field 2 items: what comes just before and just after, which readiness items it uses, and where its own results go.
  4. **Section field 3 (Checks, written first, line 75):** Omits "the numbers of the unit assessment items this section owns" (`UNIT-PLAN.md` line 242).
  5. **Section field 5 (What is carried, and instruments, lines 78 to 81):** Omits the instrument judgment ("ideal instrument and spec verdict", or "None; print and cards only") and "what a room with nothing does" (`UNIT-PLAN.md` lines 252 to 253).
  6. **Section field 7 (Talk and writing, lines 84 to 86):** Omits "two or three planned questions with their days; one written task; the look-fors the teacher judges it by" (`UNIT-PLAN.md` lines 260 to 261), even though `STANDARD.md` section 3 requires reflection and writing for self-awareness, social awareness and decision-making.
- **Cost:** Unit and section writers following `docs/courses/sel/APPROACH.md` will put content in the wrong fields, fail `UNIT-PLAN.md` structure checks, omit required section-level standards shares and written tasks, and leave "before you teach" off unit teacher pages (violating bar part 9 item 13).
- **Fix (update the Application row in `Kinds of day` and replace the corresponding bullets in `docs/courses/sel/APPROACH.md`):**

> | Application | Use the skill in a new invented case, a scene card or a planned class moment (a group task where the skill is needed), including student voice tasks (class norms or a school improvement the class proposes and carries out). |

> - Unit field 2: the sub-skill ids the unit teaches first (STANDARD section 3), in our own words; the skill names and steps the unit fixes for the year; what is carried (the class's skill names, step cards and carry-out cue), the day the model is withdrawn and the day the student first does it alone; and the unit teacher page's "before you teach" note (the skill as an adult uses it and one thing to model, STANDARD section 4, E) plus the unit's disclosure and reporting note (STANDARD section 5, item 4).
> - Unit field 10 (sources): a sources table with what was read and how much, what is from memory, no claim of effect, what is still to make, and a line pointing to the course-level logic model (C16).
> - Section field 1 (standards and practices): the section's sub-skill ids and its share of each in our own words; limits that bite in this section; connections to other grade standards with the day; and what the section teacher page must explain (the adult "before you teach" focus for this section's skill, the sensitive topics the section touches, and the school and home disclosure routes).
> - Section field 2 (where it sits): what comes just before and just after in the unit, which readiness items this section uses, and where its own results go (not builds on, leads to or comes back, which sit in unit field 3).
> - Section field 3 (checks, written first): the numbers of the unit assessment items this section owns, followed by the day's evidence as above, with its look-fors.
> - Section field 5 (what is carried, and instruments): the skill's step card and carry-out cue for the school day. The teacher holds the model on the first session; pairs hold the card on the second; the card is withdrawn on the first Application session, which the plan names, and the check is taken without it. K to 2 use the same steps as three or four pictured words said aloud. Name each key moment's ideal instrument and spec verdict (or "None; print and cards only"), and state what a room with nothing does (board or spoken steps).
> - Section field 7 (talk and writing): two or three planned questions with their days, one written task (or drawn/dictated reflection in K to 2) with its look-fors, the talk routine (the same discussion norms as ELA that grade), the sentence frames, the rehearsal set-up, and the role-play rule (invented, low-stakes, no victim or perpetrator roles, no real classmates; the teacher or a card plays any pressure).

- **Confidence:** Firm.

### 4. `docs/courses/sel/APPROACH.md` omits the per-unit student self-check required by adoption bar C8

- **Where:** `docs/courses/sel/APPROACH.md` ("Daily evidence", lines 33 to 41; "Unit field 5", lines 57 to 58) vs `docs/ADOPTION-BAR-SUBJECTS.md` C8 (line 67).
- **What is wrong:** Core bar C8 requires "students judging and tracking their own work" and "a student self-check page per unit" (Fails if: "Students never judge or track their own work in a unit"). Neither `Daily evidence` nor `Unit field 5` in `docs/courses/sel/APPROACH.md` includes a student self-check (compare `docs/courses/health/APPROACH.md` line 73).
- **Cost:** Every SEL unit built from `APPROACH.md` will fail C8 on an adoption review, or a writer will add an ad-hoc feelings survey that violates FOUNDATION promise 2.
- **Fix (add one sentence to "Daily evidence" and one phrase to Unit field 5 in `docs/courses/sel/APPROACH.md`):**

> Once per unit, students complete a short skill-step self-check ("Which steps can I do on my own, and which step will I practise next?"): it stays with the student, checks only the skill's steps, never rates feelings or personal traits, and is never collected as student data (C8, promise 2).

> - Unit field 5 (end-of-unit assessment): a rehearsal with look-fors, scenario items (each teacher-judged item with two sample answers), and the unit's one-page student skill-step self-check (kept by the student). Nothing personal in any item.

- **Confidence:** Firm.

### 5. Unit field 4 (Readiness check) in `APPROACH.md` conflicts with `UNIT-PLAN.md` field 4's `Retrieval only:` gate and K to 2 session length

- **Where:** `docs/courses/sel/APPROACH.md` line 55 to 56 vs `docs/courses/UNIT-PLAN.md` lines 162 to 183 and `docs/courses/sel/STANDARD.md` lines 60, 93, 123 to 124, 247 to 249.
- **What is wrong:** `UNIT-PLAN.md` lines 166 to 170 state that any unit assuming only rows used the year before (or earlier the same year) opens as `Retrieval only:` inside a day, with no separate readiness check; `scripts/unitplan.py` also requires field 4 to start with `Given:`, `Retrieval only:`, or (in unit 1) `Start-of-year check:`. Because every SEL grade 1 to 12 assumes only the previous year's row, `APPROACH.md` line 55 to 56 ("one scenario item on the skills the unit builds on; the ten-minute reteach is the earlier skill modelled again") neither declares which of the three `UNIT-PLAN.md` forms applies nor states when the check is given. In addition, a 10-minute reteach consumes half of a 20-minute K to 2 session.
- **Cost:** SEL unit plans will fail `scripts/unitplan.py` on field 4, and K to 2 reteaches will crowd out half the lesson.
- **Fix (replace Unit field 4 in `docs/courses/sel/APPROACH.md`, lines 55 to 56):**

> - Unit field 4 (readiness): because every SEL grade 1 to 12 builds on the previous year's row, units use `Retrieval only:` (one opening scenario item on the skills the unit builds on, five minutes at most) when the previous year's unit was taught, and `Start-of-year check:` in unit 1 (in kindergarten unit 1, checking only arrival skills per STANDARD section 3). Where a school left out the previous year's unit (STANDARD section 5, item 6), the unit also names a one-step fallback check (`Given:` the last five to ten minutes of the prior unit's last session). Reteach is the earlier skill modelled again: five minutes in K to 2, five to ten minutes in grades 3 to 12.

- **Confidence:** Firm.

### 6. Sensitive-ground rules have four gaps across `STANDARD.md` and `APPROACH.md`

- **Where:** `docs/courses/sel/STANDARD.md` lines 125 to 128, 211 to 212, 239 to 240, 245 to 249; `docs/courses/sel/APPROACH.md` lines 67 to 68, 72 to 73, 96 to 99.
- **What is wrong:**
  1. **Leave-out note absent from `APPROACH.md`:** `STANDARD.md` section 5 item 6 settles that a school may leave out an SEL unit, must be told which sub-skill ids that year no longer teaches, and states that on the course page. `APPROACH.md` Unit field 9 (Family note) and Section field 11 never mention the leave-out note or the parent/school opt-out line (compare `docs/courses/health/APPROACH.md` lines 117 to 118).
  2. **No home-room disclosure or crisis route, and no "do not promise secrecy" line:** `STANDARD.md` line 239 to 240 and `APPROACH.md` line 73 cover only schools ("follow the school's reporting policy and refer to the counselor"). Under `FOUNDATION.md` section 2, a parent teaching one child at home is the second audience, and `docs/courses/health/APPROACH.md` lines 103 to 106 explicitly include "listen, do not promise to keep it secret, follow the school's duty to report" plus the national child abuse hotline and 988 crisis line by purpose for parents at home.
  3. **Incomplete health-handoff unit list:** `STANDARD.md` lines 126 to 128 list only six grade 6 to 12 unit titles that hand off to health. Other grade 6 to 12 units teach `RS6` (saying no to pressure) or `SM2` (stress coping) and sit right next to health topics, including Grade 6 "Friendships that change" (`RS6`), Grade 7 "Under pressure" (`RS6`) and "Big feelings, steady choices" (`SM2`), Grade 8 "Values and integrity" (`RS6`), and Grade 12 "Steady under change" (`SM2`) and "Hard choices" (`RS6`). Naming only six titles will lead writers to omit the health handoff on the others.
  4. **Sensitivity-read timing too narrow:** `STANDARD.md` line 211 says these rules are "read at the Finish check by the fresh sensitivity agent". Both `docs/pipeline/briefs/sensitivity-read.md` (line 64) and `docs/COURSE-RUN.md` (line 127) require sensitivity reads at Stage 4 (unit plans) and Stage 6 (days) as well as Stage 7 (Finish).
- **Cost:** Writers could ship Grade 7 "Under pressure" without a health handoff, omit opt-out lines from family notes, leave parents teaching at home without a crisis/disclosure route, or defer sensitivity reads until Stage 7 when rewrites are most expensive.
- **Fix (update `docs/courses/sel/STANDARD.md` lines 126 to 128, 211 to 212 and 239 to 240, and `docs/courses/sel/APPROACH.md` Unit field 9 and Section field 10):**

> In `STANDARD.md` lines 126 to 128: Every grade 6 to 12 unit that teaches SM2 (coping with stress) or RS6 (saying no to pressure), or touches stress, pressure or close relationships (including "Stress and strong feelings", "Friendships that change", "Under pressure", "Big feelings, steady choices", "Values and integrity", "Stress, focus and rest", "Stress and coping", "Relationships that are good for me", "Saying no, setting limits", "Help, support and pressure", "Steady under change" and "Hard choices"), names the corresponding health unit in its teacher notes and hands those topics to it.

> In `STANDARD.md` lines 211 to 212: SEL touches family, identity and mental health, so these rules hold in every SEL unit, checked by the fresh sensitivity agent at Stage 4 (unit plans), Stage 6 (days) and Stage 7 (Finish check) per `docs/pipeline/briefs/sensitivity-read.md` (FOUNDATION promise 7, BASELINE rules 5, 6 and 8).

> In `STANDARD.md` lines 239 to 240: Each unit's teacher notes say: if a child discloses harm or risk, listen, do not promise to keep it secret, follow the school's reporting policy and refer to the counselor; for a parent teaching at home, name the national child abuse hotline and the 988 crisis line by purpose and state that a child's disclosure is not handled alone.

> In `APPROACH.md` Unit field 9: in English and Spanish: the skill's name and steps, the words the class uses, one thing to try at home (the family activity), and a short leave-out note (what the unit covers, which sub-skill ids are skipped if left out, and how to opt out: through the school in a classroom, or by the parent at home).

- **Confidence:** Firm.

### 7. The within-band depth ladder defines three yearly steps, but the 9 to 12 band has four grades

- **Where:** `docs/courses/sel/STANDARD.md` section 3 ("Depth ladder, by band", lines 83 to 85).
- **What is wrong:** Lines 83 to 85 state: "Within a band the first year uses cases from the school day, the second adds a second person's point of view, and the third adds a cost or a pressure. The progression row for each sub-skill says which of the three a year is." K to 2, 3 to 5 and 6 to 8 each have three grades, but grades 9 to 12 have four (9, 10, 11 and 12), leaving grade 12 unassigned.
- **Cost:** The Stage 2 progression writer for high school has no rule distinguishing grade 11 from grade 12 on the depth ladder, risking two high school grades taught at the same depth (which triggers the "a band taught the same way every year" fail in `ADOPTION-BAR-SUBJECTS.md` part 9).
- **Fix (replace lines 83 to 85 of `docs/courses/sel/STANDARD.md`):**

> Within each three-year band (K to 2, 3 to 5, 6 to 8), the first year uses cases from the school day, the second adds a second person's point of view, and the third adds a cost or a pressure. In the four-year 9 to 12 band, grade 9 uses school-day cases, grade 10 adds a second person's point of view, grade 11 adds a cost or a pressure, and grade 12 applies and judges a self-designed plan across post-school, workplace or community settings. The progression row for each sub-skill names which step its year is.

- **Confidence:** Firm.

### 8. `docs/courses/sel/APPROACH.md` lacks a standalone Pacing section (with the published dose benchmark check) and lacks what a tool may do

- **Where:** `docs/courses/sel/APPROACH.md` lines 47 to 48 and 64 to 66; `docs/courses/sel/STANDARD.md` section 2 (lines 59 to 63); compare `docs/courses/health/APPROACH.md` lines 120 to 137.
- **What is wrong:**
  1. Neither `STANDARD.md` nor `APPROACH.md` states what national or professional bodies publish on SEL time/dose, and `APPROACH.md` has no standalone `## Pacing` section. Checking the sources: CASEL's Program Guide and 2020 criteria paper do not prescribe a fixed minimum minutes-per-week or sessions-per-year quota (rated programs vary widely, roughly 8 to 140 sessions a year, while SAFE requires dedicated "Focused" time); the Education Endowment Foundation (EEF) primary SEL guidance highlights regular brief sessions (such as two 30-minute sessions a week) over infrequent long sessions.
  2. `APPROACH.md` Unit field 8 states only what a tool may not do ("No tool collects feelings, answers or names, and none scores a child"), omitting what a tool may do and omitting that a tool may not stand in for rehearsal with people (unlike `docs/courses/health/APPROACH.md` lines 132 to 136).
- **Cost:** Adoption reviewers checking C2 and C13 see no benchmark note explaining the chosen dose, and tool builders have no clear positive boundary for acceptable SEL tools.
- **Fix (add `## Pacing` and `## What a tool may and may not do` sections to `docs/courses/sel/APPROACH.md` before `## Where the evidence is thin`):**

> ## Pacing
>
> Settled 2026-11-16 (STANDARD section 2): two sessions a week for 32 weeks (64 sessions a year) in every grade, at 20 minutes in K to 2, 30 minutes in grades 3 to 5 and 6 to 8, and 40 minutes in grades 9 to 12, with a 32-session short path (one session a week, never dropping a unit). A frame may adjust its band's minutes with a reason. No national SEL body sets a single mandatory minute minimum: CASEL's program guide reports sessions per year descriptively across rated programs (roughly 8 to 140 sessions a year) and requires dedicated, focused time; primary SEL guidance from the Education Endowment Foundation favors regular short sessions (such as two 30-minute sessions a week) over infrequent long ones.
>
> ## What a tool may and may not do
>
> A tool may display a skill's step card, present invented scenarios for sorting or choosing a next step with feedback on the steps, or offer a private unrecorded skill-step self-check. A tool may not collect feelings, personal answers or student names, score a child, store anything off the device (C15, promise 2), or stand in for live rehearsal with people (bar part 9 item 5).

- **Confidence:** Likely.

### 9. Stale status lines, imprecise high school ELA lean ids, and minor cross-file drift

- **Where:**
  - `docs/courses/sel/STANDARD.md` line 3 (`**DRAFT, 2026-11-16.**`), line 18 (`Draft for Cory's yes`), lines 50 and 56 to 58 (still says `data/courses.csv has one SEL track row (sel-k12)` and `Recommended: replace...`, when `data/courses.csv` lines 41 to 44 already hold `sel-k-2`, `sel-3-5`, `sel-6-8`, `sel-9-12`).
  - `docs/courses/sel/STANDARD.md` section 7 line 272: writes `e10-sl-seminar and on`, whereas grades 11 and 12 in `data/progressions/ela.csv` drop the `-sl-` infix (`e11-seminar`, `e12-seminar`).
  - `docs/courses/sel/STANDARD.md` section 3 lines 135 to 138: the SO6 placement note jumps from "kindergarten and grade 1" to "grades 3 and 4", silently omitting grade 2 (even though section 5 item 5 says "playground fairness in K to 2").
  - `docs/ADOPTION-BAR-SUBJECTS.md` lines 443 to 453 (items 9 to 13 tagged `[I]` though added from Curio Class's own deeper review in `STANDARD.md` section 4, where items 9 to 12 adapt registry concepts into Curio Class's own rules), lines 458 to 459 (still says `**marked for a deeper review**` after the review was finished and applied), line 569 (still says `Owed: the read's fixes, the progression, the reader's calls and the approach page's yes (Desk q-prework-open-1)` even though `APPROACH.md` line 3 says Cory approved it on 2026-11-21), and line 672 (sources table still lists `Writer, pp 23 to 25; expert, pp 21 to 27` while `STANDARD.md` and `lenses/sel.md` state `pp 1 to 3 and 20 to 35 in full`).
- **Cost:** Contradicts `AGENTS.md`'s living-doc rule, confuses writers about whether `data/courses.csv` and `APPROACH.md` are settled, and could cause a progression writer to type `e11-sl-seminar` and fail `scripts/progression.py`.
- **Fix:**
  - In `docs/courses/sel/STANDARD.md`: update line 3 and line 18 to reflect Cory's 2026-11-21 approval; rewrite line 50 to state `data/courses.csv holds four band rows (sel-k-2, sel-3-5, sel-6-8, sel-9-12), matching docs/COURSES-STATUS.md` and remove the superseded `Recommended: replace...` clause; change line 135 from `kindergarten and grade 1` to `K to 2`; change line 272 from `e10-sl-seminar and on` to `e10-sl-seminar, e11-seminar and e12-seminar`.
  - In `docs/ADOPTION-BAR-SUBJECTS.md`: update line 458 to note the deeper review was completed 2026-11-16 (`docs/courses/sel/STANDARD.md` section 4); update line 569 to reflect that the 2026-11-19 read's fixes and Cory's 2026-11-21 approval are applied and list the remaining owed work (the progression gate changes, the second-model read's fixes, and `data/progressions/sel.csv`); align line 672's page range to `pp 1 to 3 and 20 to 35`.
- **Confidence:** Firm.

## What is right and should not be touched

- `data/standards/casel-5.txt`: all 40 sub-skills match CASEL's published framework in count, competency and order, are cleanly rewritten in Curio Class's own words, and respect CASEL's all-rights-reserved reuse terms.
- The 13-grade table in `docs/courses/sel/STANDARD.md` section 3: every grade from K through 12 teaches all 40 sub-skills once and only once, with every unit capped at 8 sub-skills and distinct transition-year themes.
- The year-before handoff chain (`K -> 1 -> 2 -> ... -> 12`) settled via `docs/reviews/sel-ownership-check-2026-11-21.md`: no skipped grades, `~` rows treated as full teaching rows at their year's depth, and other subjects leaning on the specific grade row whose depth they need.
- The privacy and non-therapy guardrails in `STANDARD.md` section 5 and `APPROACH.md` ("Daily evidence"): invented cases first, optional sharing, no surveys or screening, class sheet held only for one named day and discarded at unit end, role-play pressure played by the teacher or a card, and plain body-skill calming routines with no religious framing.
- Section field 9 (supports) in `APPROACH.md`: thorough coverage of English learners (6 to 8 words in depth, sentence frames, language gap vs content gap), access (no student required to speak aloud), reading load (at most 5 short sentences; K to 2 read aloud and pictured), check accommodations, and same-skill extension.
- The base-text scout (`docs/reviews/sel-open-material-2026-11-16.md`): honest "no whole-course open base" verdict and clear licence boundaries on Oak National Academy Collection 2 (OGL v3.0) vs Collection 1 (non-commercial, excluded).

## What I could not judge

- `data/progressions/sel.csv` does not exist yet, so actual row-level handoffs (`assumes`/`hands_on`), full sub-skill coverage inside each row's notes, and `scripts/progression.py` execution could only be checked against the rules stated in `STANDARD.md`, not against progression rows.
- `scripts/unitplan.py` and `scripts/plan.py` were not opened; the `UNIT-PLAN.md` field 4 gate requirements were checked from `docs/courses/UNIT-PLAN.md` itself.
- The full text of CASEL's December 2020 criteria paper (`11_CASEL-Program-Criteria-Rationale.pdf`) was not downloaded and read page by page in this run; only the CASEL framework page's 40 sub-skills and CASEL/EEF dose guidance were verified via web search.

## Sources

- CASEL, "What Is the CASEL Framework?" (`https://casel.org/fundamentals-of-sel/what-is-the-casel-framework/`): used to verify all 5 competencies, all 40 "Such as:" sub-skills, their order, and that `data/standards/casel-5.txt` is rewritten in Curio Class's own words.
- CASEL Program Guide and criteria overview (`https://pg.casel.org/` and `https://files.casel.org/11_CASEL-Program-Criteria-Rationale.pdf`, searched via web): used to verify that CASEL sets no fixed minimum minutes-per-week or sessions-per-year mandate, reports sessions per year descriptively across rated programs (roughly 8 to 140 sessions), and uses SAFE criteria.
- Education Endowment Foundation, "Improving Social and Emotional Learning in Primary Schools" (`https://educationendowmentfoundation.org.uk/education-evidence/guidance-reports/primary-sel`, searched via web): used to check published primary SEL dose guidance (favoring regular brief sessions such as two 30-minute sessions a week over infrequent long ones).

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Define grade 12 as a fourth within-band step (applying and judging a self-designed plan across post-school, workplace or community settings) | Fixes the 3-step ladder for the 4-year 9 to 12 band without moving any standard | `docs/courses/sel/STANDARD.md` section 3 |
| Add a per-unit skill-step student self-check (kept by the student, never rating feelings or traits) | Required by adoption bar C8 while keeping FOUNDATION promise 2 | `docs/courses/sel/APPROACH.md` ("Daily evidence", Unit field 5) |
| Move student voice out of Unit field 10 into Application (`Kinds of day`) and restore dropped shared parts of Section fields 1, 2, 3, 5 and 7 | Enforces `docs/courses/UNIT-PLAN.md` field placement | `docs/courses/sel/APPROACH.md` |
| Extend the health-handoff rule in `STANDARD.md` to every grade 6 to 12 unit teaching SM2 or RS6 (including Grade 7 "Under pressure" and Grade 12 "Hard choices") | Prevents missing health handoffs on pressure and stress units | `docs/courses/sel/STANDARD.md` section 3 |
| Reconcile Unit field 4 with `UNIT-PLAN.md`'s `Retrieval only:` / `Start-of-year check:` gate and cap K to 2 reteach at 5 minutes | Matches `UNIT-PLAN.md` and fits 20-minute K to 2 sessions | `docs/courses/sel/APPROACH.md` Unit field 4 |
| List all four `scripts/progression.py` changes needed for SEL and fix stale status lines and `e11-seminar` / `e12-seminar` ids | Prevents Stage 2 gate failures and living-doc drift | `docs/courses/sel/STANDARD.md`; `docs/ADOPTION-BAR-SUBJECTS.md` |

## Questions for Cory

1. **Reconciling the 64-session and 32-session math (Finding 2).** Keeping 64 sessions a year across 6 units (10 to 11 sessions per unit) means an 8-sub-skill unit cannot give two sessions to each sub-skill separately, and dropping one Application session per unit removes 6 sessions rather than 32. **Recommended pick:** keep your settled 64-session full path and 32-session short path, bundle 2 to 3 related sub-skills into 2-to-4-session sections so rehearsal fits inside 8 to 9 teaching sessions per unit, and define the 32-session short path as 5 to 6 bundled sessions per unit (never dropping a unit). The alternative is raising the annual session count to ~90+ sessions.
2. **Home-room disclosure and crisis hotline lines in SEL teacher notes (Finding 6).** `docs/courses/health/APPROACH.md` includes "do not promise to keep it secret" plus the national child abuse hotline and 988 crisis line (by purpose) for parents teaching at home; SEL's notes currently address schools only. **Recommended pick:** carry the same school-and-home disclosure wording in SEL unit teacher notes so home-room families (FOUNDATION section 2) have the same safety guidance as health.

## Against the first read

Compared with `docs/reviews/prework-sel-read-2026-11-19.md` (and its 2026-11-20 fixes applied):

- **Already caught by the first read:** The need to register `'sel'` in `scripts/progression.py`'s `STD_FILES` and `code_grades()` (first read Finding 1, part of my Finding 1); the original missing/wrong `APPROACH.md` fields, missing pacing section and missing tool limits (first read Finding 4, overlapping part of my Findings 3 and 8); and the still-unapplied `ADOPTION-BAR-SUBJECTS.md` cleanups (bar item `[I]` tags, bar status line and mismatched CASEL paper page ranges, first read Findings 11 and 13, overlapping part of my Finding 9).
- **New in this second read (including faults introduced or left behind by the 2026-11-20 fix pass):**
  1. `scripts/progression.py` lines 272 to 274 fail any anchor code owned by more than one grade, which will reject all 40 ungraded CASEL ids under the settled four-band owner rule (`2, 5, 8, 12`) unless the ownership gate itself is updated (Finding 1).
  2. The 2026-11-20 unit cap ("about two sessions a sub-skill" for 8 sub-skills inside 10 to 11 sessions per unit) and 32-session short path ("drops the second Application session in each unit", which drops only 6 sessions, not 32) do not add up mathematically (Finding 2).
  3. The 2026-11-20 `APPROACH.md` rewrite placed Student voice inside Unit field 10 (Sources), wrote Section field 2 in a way `UNIT-PLAN.md` explicitly forbids, dropped required shared items from Section fields 1, 3, 5 and 7, and left "before you teach" off unit teacher pages (Finding 3).
  4. `APPROACH.md` omits the per-unit student self-check required by adoption bar C8 (Finding 4).
  5. Unit field 4 in `APPROACH.md` conflicts with `UNIT-PLAN.md`'s `Retrieval only:` / `Start-of-year check:` gate and puts a 10-minute reteach inside a 20-minute K to 2 session (Finding 5).
  6. Four sensitive-ground gaps: missing leave-out note in `APPROACH.md` Unit field 9, no home-room disclosure/crisis route or "do not promise secrecy" line, an incomplete 6-unit health-handoff list that misses Grade 7 "Under pressure" and Grade 12 "Hard choices", and `STANDARD.md` line 211 limiting sensitivity reads to the Finish check instead of Stages 4, 6 and 7 (Finding 6).
  7. The 2026-11-20 within-band depth ladder defines 3 steps for a 4-year 9 to 12 band, leaving grade 12 unassigned (Finding 7).
  8. External web verification of all 40 CASEL 5 sub-skills (which the first read checked from memory only) and of CASEL/EEF published SEL dose guidance (Finding 8).
  9. Post-2026-11-21 stale `sel-k12` / `DRAFT` / `Owed` lines, the imprecise `e10-sl-seminar and on` ELA lean wording (`e11-seminar`, `e12-seminar`), and the grade 2 gap in the SO6 placement note (Finding 9).

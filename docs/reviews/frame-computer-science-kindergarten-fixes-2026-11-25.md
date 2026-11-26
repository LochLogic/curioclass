# Frame fixes: Computer Science, Kindergarten (2026-11-25)

The one fix pass of COURSE-RUN stage 3 for the after-core pilot frame
docs/courses/computer-science-kindergarten/frame.md, from the expert read
(docs/reviews/frame-computer-science-kindergarten-2026-11-25.md, "E") and the second-model read
(docs/reviews/frame-computer-science-kindergarten-codex-2026-11-25.md, "C"). Disputed points were settled against the
2026 CSTA standards PDF in the source store (S:\CurioClass-sources\computer-science\csta-2026-11-21, boundary
statements read, not copied) and data/plans/calendar.csv.

## Gates

| Gate | Result |
|---|---|
| `python -X utf8 scripts/frame.py sync` | frames.csv 66 courses, calendar.csv 962 rows |
| `python -X utf8 scripts/frame.py check computer-science-kindergarten` | 0 failures; 5 units, 32 days (28 in units, 4 for checks and respond days) |
| `python -X utf8 scripts/progression.py check computer-science` | 202 rows, 0 failures |
| `python -X utf8 scripts/stale.py check` | 70 files, 0 failures |

Calendar after sync: units in weeks 1-6, 7-11, 14-22, 23-26, 29-32; checks weeks 12 and 27 (off the K core weeks 14 to
17 and 29 to 32); respond weeks 13 and 28. After-core clashes left for the lead's calendar pass, not moved: grade K
week 12 (computer science, health) and week 27 (computer science, health, library).

## Findings

| Read | # | Applied or rejected | What changed, or why not |
|---|---|---|---|
| E | 1 | Applied | Mid-year and year-end checks now stand for units 2 and 4's end-of-unit assessments; each check's respond day is the unit's. Days: unit 1 6, unit 2 5, unit 3 9, unit 4 4, unit 5 4; teaching sessions 18 to 22. New sessions split unit 1's overloaded session 2 (rules, then a separate first device turn), split unit 2 (modify, then a think-aloud on how people plan, then make), and gave unit 3 a modify session before its make. Both "What it checks" cells rewritten: each scores its unit in full and samples earlier units. Pattern line proposed for APPROACH.md (For the lead 2). |
| E | 2 | Applied | Base text bullet, Source map heading and STANDARD.md name the archived edition (raspberrypi.org/curriculum/archived, 2023, no longer maintained) and that Oak holds England's current lessons. Sign-in claim removed ("checked when the folder is made"). BASE-TEXTS.md row added (store folder none, not loaded); Pending marker retargeted to the folder name. |
| E | 3 | Applied | Unit 2: session 2 modifies a working game set, session 5 makes one. Same as C 4. |
| E | 4 | Applied in part | Clashes named and left for the lead's calendar pass (task rule: no check-week moves for after-core clashes). The proposed stagger rule went to For the lead 1 as the pick; the CALENDAR.md and frame.py changes are the lead's. |
| E | 5 | Applied | Days bullet: 32 sessions for 14 rows is the read's "about two sessions a row" counted with checks; 22 teach. |
| E | 6 | Applied | Sensitivity pack named: ASAN Identity-First Language (from C 6), NCDJ Disability Language Style Guide, Section508.gov Hardware ICT Overview as background only; agent widens to the brief's five, two community-owned. |
| E | 7 | Applied | Unit 5 may be left out (society still met through EK-SOC-HU-15 in unit 2); unit 4 swap only, so the three DAT ids are always claimed (bar part 5 fail line "nothing on data or society"). |
| E | 8 | Applied | Unit 3 now says weeks 14 to 22 include the core check weeks 14 to 17. Left-out units read "Lessons 1 to 6", "page not found" dropped. |
| C | 1 | Applied | Confirmed at source: the EK-SOC-HI-14 boundary is visible changes between older and newer computing devices; activity comparison is E1. Unit 5 session 2, compelling question, anchor, end-of-unit, model row and handoff rewritten to older and newer devices; Computer History Museum timeline as the teacher's fact source. Row k-then-now notes rewritten. |
| C | 2 | Applied | Confirmed at source: EK-ALG-IM-03 asks for a simple description of how people develop an algorithm, and EK-ALG-PS-01 asks that the word algorithm be taught in context. Unit 2 session 3 teaches the human planning process with the teacher; Out line now excludes only independent decomposition. Rows k-follow-steps (word algorithm) and k-people-steps (planning process, game-maker example) updated. |
| C | 3 | Applied, inside E 1's shape | Unit 3's end-of-unit adds arranging a route (EK-PRO-PD-04); fix noted, not scored. Mid-year check scores IM-03 and HU-15 as separate spoken look-fors. Year-end check scores DI-09 (child poses a question), DC-08 (child places answers on a graph mat) and IM-10; unit 4 gains a group investigation session and children pose the second question. C's "retain five unit assessment sessions" rejected: the evidence fits the check sittings, and E 1's time case and the math kindergarten precedent stand. Row k-ask-and-count notes add child-posed questions. |
| C | 4 | Applied | As E 3; session 5 labeled make (Application), re-sort kept as retrieval; Day kinds bullet updated. |
| C | 5 | Applied | Source map states the publisher's number order and why Grouping data and Technology around us are split; robot lessons 1-3 to session 2, 4 to session 3, 5-6 to sessions 6 and 7, sessions 1, 4, 5 ours; left-out units "Lessons 1 to 6, all left out". |
| C | 6 | Applied | As E 6. |
| Own | - | Applied | Row k-ask-and-count's examples "which snack, which pet" replaced by neutral ones (the frame's own values line forbids food and pet questions); UK words in rows touched fixed (shop till, human-centred); "licence" to "license" outside the licence's proper name. |

## Pattern notes for the other computer science frames

- A course-level check right after a unit stands for that unit's end-of-unit assessment; never an assessment and a
  respond day directly before a check.
- Inside every unit: understanding, then modify, then make, with the session numbers in that order.
- Read each owned id's boundary in the source store before writing the unit: the EK misses here were a next-grade
  example (HI-14) and an over-wide Out line (IM-03).
- Every "make", "pose" or "explain" id gets its own look-for in the scored sitting, not a recognition item.
- Name the archived base edition and give left-out base units their lesson counts.
- Sensitivity lines name a starting pack of sources, not source categories.
- Leave-out names only units whose ids leave the bar's data and society coverage intact.
- Check weeks: avoid core weeks only; after-core overlaps wait for the lead's calendar pass.

## Left for the lead

1. Calendar pass: grade K week 12 (computer science, health), week 27 (computer science, health, library); pick in frame For the lead 1.
2. Confirm the check-stands-for-unit pattern and add the proposed APPROACH.md Pacing line (frame For the lead 2), with a DESK-ANSWERS line.
3. Add "For computer science, head the C3 column Practices and concept areas" to frame-write.md item 5.
4. Add the archive, Oak, ASAN, NCDJ and Computer History Museum entries to docs/APPROACH-SOURCES.md.
5. I added the Teach Computing row to docs/sources/BASE-TEXTS.md (a shared doc, done because the job asked); check it. I also ran one read-only `git diff --stat` by mistake.

## For Cory

- Edition: confirm the archived Teach Computing Curriculum (2023, no longer maintained) as the fixed K to 8 partial base; Oak's current Year 1 keeps only the units left out here.
- Download: loading the archive into the source store is a download; whether it needs a sign-in (an account) is unknown until tried.
- Scope: a kindergarten-to-grade-2 picture-block mode for our own editor (frame For the lead 5); the course runs on paper without it.

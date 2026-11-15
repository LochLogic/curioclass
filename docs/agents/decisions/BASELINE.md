# Cory's decision baseline

Cory's standing rules for deciding questions in Curio Class, drawn from his answers on the decision board (raw
answers: `answers.json`, id -> choice and note; questions: `decisions.json`) and from his later decisions in
DESK-ANSWERS.md. Rule numbers are cited across the repository and never change.

Every spec, build and review agent reads this before deciding anything itself. Settle questions with these rules.
Bring Cory only questions these rules cannot settle and that matter (see "What goes to Cory").

## The rules

1. **Quality over saved work.** Never merge, shorten or share something only to save effort. Spans, shared engines and
   shared figures are fine only when nothing is lost for any grade or subject. If something is lost, build it
   separately (gf-04, w1-21).
2. **Every standard is taught well, above the minimum.** A code on a topic must be really taught in that tool. If it
   cannot be taught well there, remove it from the topic and make sure another tool teaches it well. Never add a thin
   activity just to make a code honest (gf-07, w2-01, w2-21, w2-22, w1-15).
3. **Better graphics by default.** When there is a choice between drawn-in-code placeholders and real illustrated art,
   choose the better art (w1-42).
4. **Every tool stands alone.** The site is public and a student, parent or young child may open any tool with no
   teacher present. Defaults must work for a solo user; teacher toggles are extras, never the main experience.
   Example: in fair-use-review, the student makes their own call first and Theo's call shows after (w1-53, w1-30, w1-31).
5. **Facts stay plain, with the human side.** Don't soften history or science. Present it with care for the people
   involved. Sensitivity and accuracy checks on cultural, Native or hard-history content, in a tool or a course, are
   done by a fresh sensitivity agent; once that read passes, the content can go live (proj-03). No outside reader is
   looked for. The sensitivity agent reads every unit after studying the community's own published voice and the
   scholarship (docs/pipeline/briefs/sensitivity-read.md), and we teach with honesty and dignity at an age-appropriate
   level (settled 2026-11-14, see DESK-ANSWERS).
6. **Classroom-safe language.** No slurs or expletives. A grawlix (#@$!) stands in where a curse would be (w1-28).
7. **Privacy is stated.** Wherever a tool records or stores anything, say on screen that it never leaves the device
   (w1-20).
8. **Teacher notes name where the standards cover sensitive topics** (for example, dating in the 6-8 health standards)
   (w1-46).
9. **Lean toward the real-world factor.** Show the realistic version by default (the carbon price slider is on by
   default in grid-operator) (w3-33).
10. **Good ideas become tools.** When a question surfaces a new tool idea, add it to the concept pipeline for a later
    spec wave. Queued: "fact-check a chatbot" (generative AI, from ai-evaluator); a resume builder, near term (w1-02,
    w2-12).
11. **People art is drawn, and checked.** Codex may draw people. Every people asset carries `"people": true`, every
    people image is on a contact sheet Cory sees before the tool ships, and a fresh agent checks each set for
    stereotypes and representation. Reviews add people where a scene needs them.
12. **2 MB is a goal, not a blocker.** Over 6 MB, notes.md says why in a `Size:` line (`scripts/check_tools.py`
    enforces only that).
13. **Shared code is grown, not planned.** A kit engine is promoted only after three finished tools use the same code.
    Older tools pick it up later and only when needed: they work today, and the gain is efficiency, not capability.
14. **Finish before scaling.** At most about 10 Codex tools built and not yet reviewed. Finish a small cohort end to
    end before a new wave, and log repeat problems in the issue ledger.
15. **Public copy names no companies.** The ambition in docs/VISION.md (replace paid curriculum) stays inside the
    vision; the site says "a free, complete classroom toolkit".
16. **The first tap may cut the welcome.** A tool does not have to let its welcome line finish after the student's
    first tap; acting at once beats listening. Specs, builds and reviews do not flag a welcome cut short by a tap.
    What the welcome told the student must still be reachable (the on-screen hint or Read), and a line the tool needs
    later (a premise, a role) is said again where it is needed, not only in the welcome.
17. **Curiosities finish on Cory's desk review.** Span and Spire, Pocket Universe and later Curiosities get Cory's
    final review on the Review Desk; plate wording ("Instruments" to "Curiosities") and any areas to lift are noted
    there and fixed after it, not before. Expect larger design work back on the first two.
18. **Curiosities ship together.** The home page Curiosities entrance is built after every planned Curiosity is fully
    built. Each Curiosity's voice goes on the Forge as it passes its exit check, added to the end of the running Forge
    queue; they are not held to be recorded together.
19. **Curiosities may keep a little game essence.** Don't be too strict about removing gamification. A Curiosity must
    stay purely fun and exploratory; a light game touch (a challenge to try, a surprise, a setup to break) is fine
    when it adds to that. A goal ladder, a grade, a forced finish or a game-over still does not belong. Lenses flag a
    game element only when it narrows play or turns exploring into scoring.
20. **State adoption is the bar we build to.** Full-course materials (units, Tracks, the Binder and the shelves that
    feed them) are built to meet the substance of state and national curriculum reviews. We do not pursue formal
    adoption now; if later data says it is a good path, we pivot and are already well placed. The bar never overrides
    "What we will not do" in docs/VISION.md (no accounts, tracking or student analytics). What the bar asks, what we
    took and what we left out: docs/ADOPTION-BAR.md.
21. **A tool teaches a standard only when it passes the teaching test.** A student alone, following the tool's lead,
    meets a model, does the standard's own verb (solve, write, explain, record) on every part of its wording, on five
    or more items that differ, with a check where thinking is cheaper than guessing, and none of it can be skipped.
    For writing and talk a tool cannot mark, a model, a guide while working and a self-check on screen against a shown
    guide count. Every tool states a role: `teach` (passes the test), `see why` (lets a student explore the idea and
    names what the unit adds) or `practice`. A tool claims a code only for work on its main path; a readout, an
    optional mode or a teacher note never carries a code. Recess games and Curiosities take the role `recess` or
    `curiosity` and claim no code.
22. **Topics name standards.** A topic page covers one teachable topic. It is split only when it holds two unrelated
    topics, and then properly: a split script, redirects for the old pages, and its Word Wall, chart and games divided
    by hand (its id keys all of them and about 762 live pages; docs/ECOSYSTEM.md). It is never split just to reach
    standard-level detail; the ledger does that. Split candidates come to Cory as exceptions. A topic's standards are
    spelled out in place, never a bare cluster, each tool carries its own codes, and data/coverage.csv records where
    every standard is taught in full, so an untaught standard shows. The section plan decides how many tools a unit
    gets (rule 23); a major unit may run on print with no key tool (grade 4 math unit 3 does). Fluency volume, long
    writing, discussion, year-long reading and topic threads across texts belong to units and sections, worksheets
    and the Reading Room, and are recorded there, not claimed by a tool.
23. **A section plan comes before a tool.** A tool is the end piece of instruction. No tool is built or refined until
    a section plan names its job, and the plan marks it key (the one a day is planned around; built first) or light
    (lighter, added over time, same standard of correctness). An existing spec or tool carries no weight against what
    the unit needs (rule 1). A teacher judges open work; a tool gives it structure and marks only what has a right
    answer. Grades 3 to 12 assume one device per student with a one-line projector path; kindergarten to grade 2 may
    assume one shared classroom device, always with a paper path; and a parent teaching one child at home is a named
    audience. Always cover the whole standard: a plan teaches and checks every part of each standard it claims, in
    both directions where the standard has two (4.NF.A.1: multiplying and dividing both numbers), even where a scope
    and sequence title names only one part (docs/courses/UNIT-PLAN.md, rule 19). All of this, with the promises it
    rests on, is in docs/FOUNDATION.md, which every spec, unit, section and review agent reads first.
24. **Core subjects first (a soft goal).** Math, English language arts, science and social studies (107 courses: 105
    active, 2 world languages shelved; 52 core courses in the four core subjects plus 6 core electives) are the first
    focus; the other subjects follow. This bends where work is complementary (a shared rule, a bar page, a standards
    fix that serves both). When a choice has to be made, the core subjects come first. Every course is still finished
    to the bar; this sets the order, not the scope.
25. **Plan top down, test with a probe and a guard.** The core subjects are planned layer by layer before more days
    are written: progressions and course frames for all four together, then scope and sequence and units one subject
    at a time (social studies first, math last), each with a review and a baseline. A probe (a few days written from
    each subject's units) and a guard (a few days per subject before full writing) test the plans, with "on" and "off"
    set beforehand. Sections, days and tools come after. The order is docs/PRODUCTION-PATH.md, section 3 (settled
    2026-11-13, see DESK-ANSWERS, "the build order for the core subjects").
26. **Old tools and specs are sorted by demand.** Three bins, set by script, never by inspection: (a) named by a
    section plan, as key or light: gets course work; (b) live and passing the teaching test but not named: stays on
    the shelf as a free-standing tool and claims no course coverage; (c) everything else: frozen, no further spend.
    Spec fixing in batches has stopped. A tool moves to bin (a) only when a section plan asks for it.
27. **A machine checks what a machine can.** Every keyed item (check items, exit questions, answers, named wrong
    answers) is kept as data, and a script recomputes every answer that can be computed. A key the script cannot
    reproduce fails the build. "Worked twice by an agent" is not a check. A lesson day is written to one template
    (docs/courses/LESSON-DAY.md) so its parts can be counted and checked.
28. **The reads a course needs are named.** docs/FOUNDATION.md section 7 holds the table. Every row is an agent read
    (expert, Codex, answer key, safety, sensitivity, rights, Spanish); no outside human reader is planned (settled
    2026-11-14, see DESK-ANSWERS). No money is spent and no outside person is approached without Cory's yes.
29. **Course texts are newer and relatable below grade 9.** Kindergarten to grade 8 anchor on newer texts, mostly
    original Curio Class texts written to a per-grade text spec and read by the expert agent (not a teacher), plus
    recent public-domain government nonfiction; a deeper search for fitting open texts is allowed. Older Reading Room
    texts appear there only as a paired or optional read. Grades 9 to 12 may anchor on Reading Room texts, and favour
    recognizable and recent literature: beyond the texts the standards name, anchors come from the newest
    public-domain works (published 1930 or earlier now, one more year each January), recent open texts, and short
    excerpts of well-known recent books; never a library or paid copy. The Reading Room itself stays an
    independent-reading shelf (settled 2026-11-12 and 2026-11-13, cards `q-course-texts` and `q-ela-progression-1`,
    see DESK-ANSWERS).
30. **A timer needs a grounded purpose.** A timer is allowed where it has a grounded purpose, such as a pace cue, a
    movement game or classroom management (the reading pie timers, the movement timer, the projector timer and Game
    Night all qualify). The rule is against timers with no purpose (settled 2026-11-14, see DESK-ANSWERS).

## One tool Cory reviews personally

**growing-up-q-a** (grade 4-5 puberty). It opens on a splash cover page that makes the educational purpose clear,
framed as education, not a warning. It uses proper anatomical terms, and every fact is sourced. **Cory reviews it before
any live push.** This is the only tool with that gate. Its open wording and default questions are brought to Cory
together with that review, not before (w1-29 to w1-32).

## Specific calls

- dance-pattern-puzzle: drop Mayim Mayim; keep Seven Jumps and Tinikling (w1-22).
- levels-and-pathways: do not share one dancer figure between PE and dance; each gets its own (w1-21).
- pressure-point: illustrated portraits, not drawn-in-code (w1-42).
- dance-styles-explorer: instead of a disclaimer, a fresh agent checks each style's phrases for respect and accuracy,
  then it ships (w1-24, rule 5).
- algebra-tile-studio: remove A-SSE.B.3c and B.4 from its topic. Add them to exponent-rule-builder and savings-plan,
  which teach them in full (w2-01, rule 2).
- work-rate-crew: keep the extraneous-roots audit, set inside the story (the crew lead's checking sheet), so A-REI.A.2
  is taught in full (w2-05, rule 2).
- input-or-output: add E2-SYS-SE-12 only if a real activity teaches it well; otherwise move the code to a tool that does
  (gf-07).
- K-2 span topics: the builder confirms each grade gets full depth; split any span where a grade loses something
  (gf-04).
- target-toss: the default setup is a target taped to the wall beside the screen, not on it. The screen shows the
  target and keeps score; students throw soft balls at the wall target. A setup card shows this (w1-49).
- ASL tools are graphics only: no video, no photos of people. Do not re-pitch video. The ASL collection may change its
  format to fit: storyboard panels per sign (start, movement, end, face), high-quality renderings, labeled sign
  parameters. The design path is in docs/agents/roadmap/ASL-SIGN-STRIP.md; a sample build waits until Cory asks.
- Native and hard-history review requests in waves 2 to 4 (computing-team-stories, lake-commons, source-portfolio,
  rhetorical-situation-simulator, premise-inspector) follow rule 5: a fresh review agent, then live.
- Parent-preview requests (wave 4 ELA) follow rule 4: a "Content notes" line on the tool page and in teacher notes; no
  separate preview step.
- art-01 to art-06 (wave 1 people images, Kofi, despill, placed assets, The Child's Bath, the siku): judge them in the
  built tool, apply rule 3, and draw the siku.
- Board items w3-44 to w3-49 and the 21 wave 4 items take the board's recommendations, the wave 4 items adjusted by
  rules 4 and 5.

## What goes to Cory

Cory decides scope, audience, money, outside people, and anything that moves a standard between sections. Bring him
only questions that:

- change what a tool teaches, or who it is for;
- touch growing-up-q-a or a topic that is just as sensitive;
- need money, accounts, outside people or a live deploy;
- or that these rules cannot settle.

Item-level choices inside the standards' limits (number sizes, which fraction pairs, how many items on a check, day
swaps inside a unit, word caps) are settled by the curriculum expert, written under "Settled by the expert" in its
report, and collected in a weekly digest for Cory (docs/reviews/DIGEST.md). Cory can overturn any of them from the
digest.

Each question comes with full context: what the tool is, what the student sees, what the choice changes, and a concrete
example.

# Cory's decision baseline

Drawn from Cory's answers on the decision board (2026-10-27: 172 of 208 answered, 157 recommendations accepted, 3
own calls, 12 held with notes). Raw answers: `answers.json` (id -> choice, note); questions: `decisions.json`.

Every spec, build and review agent reads this before deciding anything itself. Settle questions with these rules.
Bring Cory only questions these rules cannot settle and that matter (see "What goes to Cory").

## The rules

1. **Quality over saved work.** Never merge, shorten or share something only to save effort. Spans, shared engines and
   shared figures are fine only when nothing is lost for any grade or subject. If something is lost, build it
   separately (gf-04, w1-21).
2. **Every standard is taught well, above the minimum.** A code on a module must be really taught in that tool. If it
   cannot be taught well there, remove it from the module and make sure another tool teaches it well. Never add a thin
   activity just to make a code honest (gf-07, w2-01, w2-21, w2-22, w1-15).
3. **Better graphics by default.** When there is a choice between drawn-in-code placeholders and real illustrated art,
   choose the better art (w1-42).
4. **Every tool stands alone.** The site is public and a student, parent or young child may open any tool with no
   teacher present. Defaults must work for a solo user; teacher toggles are extras, never the main experience.
   Example: in fair-use-review, the student makes their own call first and Theo's call shows after (w1-53, w1-30, w1-31).
5. **Facts stay plain, with the human side.** Don't soften history or science. Present it with care for the people
   involved. Sensitivity and accuracy checks on cultural, Native or hard-history content are done by a fresh review
   agent; once that review passes, the content can go live. We don't wait on outside human reviewers (proj-03).
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

## One module Cory reviews personally

**growing-up-q-a** (grade 4-5 puberty). It opens on a splash cover page that makes the educational purpose clear,
framed as education, not a warning. It uses proper anatomical terms, and every fact is sourced. **Cory reviews it before
any live push.** This is the only module with that gate. It also has open wording and default questions; they are
brought to Cory together with that review, not before (w1-29 to w1-32).

## Specific calls

- dance-pattern-puzzle: drop Mayim Mayim; keep Seven Jumps and Tinikling (w1-22).
- levels-and-pathways: do not share one dancer figure between PE and dance; each gets its own (w1-21).
- pressure-point: illustrated portraits, not drawn-in-code (w1-42).
- dance-styles-explorer: instead of a disclaimer, a fresh agent checks each style's phrases for respect and accuracy,
  then it ships (w1-24, rule 5).
- algebra-tile-studio: remove A-SSE.B.3c and B.4 from its module. Add them to exponent-rule-builder and savings-plan,
  which teach them in full (w2-01, rule 2).
- work-rate-crew: keep the extraneous-roots audit, set inside the story (the crew lead's checking sheet), so A-REI.A.2
  is taught in full (w2-05, rule 2).
- input-or-output: add E2-SYS-SE-12 only if a real activity teaches it well; otherwise move the code to a tool that does
  (gf-07).
- K-2 span modules: the builder confirms each grade gets full depth; split any span where a grade loses something
  (gf-04).
- target-toss: the default setup is a target taped to the wall beside the screen, not on it. The screen shows the
  target and keeps score; students throw soft balls at the wall target. A setup card shows this (w1-49).
- ASL tools are graphics only: no video, no photos of people (Cory, 2026-10-27). The ASL collection may change its
  format to fit: storyboard panels per sign (start, movement, end, face), high-quality renderings, labeled sign
  parameters. Design path (roadmap, awaiting a sample build when Cory asks) in docs/agents/roadmap/ASL-SIGN-STRIP.md. Do not re-pitch video.
- Native and hard-history review requests in waves 2 to 4 (computing-team-stories, lake-commons, source-portfolio,
  rhetorical-situation-simulator, premise-inspector) follow rule 5: a fresh review agent, then live.
- Parent-preview requests (wave 4 ELA) follow rule 4: a "Content notes" line on the tool page and in teacher notes; no
  separate preview step.

## Unanswered items (resolved by these rules, not sent back)

- **art-01 to art-06:** wave 1 people images, Kofi, despill, placed assets, The Child's Bath, the siku. Judge them in
  the built tool, apply rule 3, and draw the siku.
- **w3-44 to w3-49:** take the recommendations.
- **Wave 4 (21 items):** take the recommendations, adjusted by rules 4 and 5.

## What goes to Cory

Only questions that:

- change what a tool teaches, or who it is for;
- touch growing-up-q-a or a topic that is just as sensitive;
- need money, accounts, outside people or a live deploy;
- or that these rules cannot settle.

Each one comes with full context: what the tool is, what the student sees, what the choice changes, and a concrete
example. Several of Cory's holds were "need more info".

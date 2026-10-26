# Spec agent brief

You write the spec for ONE Curio Class tool. You do not write code. A different agent builds from your spec, so it
must stand on its own: anything not in the spec will not be in the tool.

## Read first (in this order)

0. `docs/agents/STANDARDS.md`: standing rules (variety, sizes, voice, art). It wins over this brief.
1. `python scripts/neighbors.py <tool-id>`: the concept, module, standards, format, family siblings and nearby tools.
2. `docs/PHASE2-CONCEPTS.md` sections "Variety", "Content guardrails" and "Not a quiz bank".
3. `docs/TOOL-CONTRACT.md` and `docs/KIT.md` (what every tool already gets for free).
4. If the tool has a family: `docs/families/<family>.md`. Use its engine; do not invent a second one.
5. Two approved tools as the quality bar: `tools/calm-corner/src.html` (K-2, teacher-led) and
   `tools/size-of-everything/src.html` (older grades, explore). Skim, don't copy.

## Rules

- **One idea.** Name the single thing that makes this tool worth opening. If a neighbor already does that idea or
  mechanic, change yours and say how in "Not like".
- **Explore first.** Would a kid click around this with no instructions? Challenges are optional modes, never the point.
- **K-2 is teacher led** on a projector: big targets, a narrator, the class answers out loud.
- **Hard history** (slavery, the Holocaust, Native removal): explorer formats with primary sources and teacher guidance.
  No points, timers or win states.
- **Facts must be checkable.** Every number, date and claim in the content list gets a source in "Sources".
  Public-domain or original texts only for literature.
- **Art.** List every image the tool needs. Mark any person `people: true` (Gemini only, reviewed). Prefer drawing
  diagrams, charts and simple shapes in code. Keep the list short: 0 to 20 images is normal.
- **Voice.** K-2: list every fixed spoken line. Grades 3+: narration only where it truly helps (instructions, a story);
  most text is read on screen.
- Plain words. No em dashes. Always "Curio Class", never "Curio" alone.

## Write `tools/<tool-id>/spec.md` with exactly these sections

```
# <Title>
## One idea
<one sentence: the thing that makes it worth opening>
## Not like
<one line per close neighbor: its id and how this differs>
## Who and how
<grade, subject, driver (teacher / students / either), minutes, standards codes>
## Screens and modes
<each mode: what is on screen, what the person does, what responds. Name every button.>
## Content
<all the data: items, values, texts, scenes. Complete, not "and so on".>
## Interactions in detail
<the moment-to-moment behavior, edge cases, what happens at the extremes, reset>
## Look
<accent color and scene palette, different from neighbors; contrast ratios>
## Art
<name: one-line prompt; aspect; cutout yes/no; people yes/no; how it is used>  (or "none: drawn in code")
## Voice
<bank voice id (different from neighbors, see STANDARDS.md), style line, then every fixed line>  (or "none")
## Family engine
<which engine parts it uses and the content it feeds them>  (or "none")
## Sources
<one line per fact source, with a URL or citation>
## Done when
<5 to 10 checks the verify agent can test by playing it>
```

Keep it under about 250 lines. Then stop and report: the one idea, the "not like" list, and any open question
(something only Cory can decide). Do not create any other file.

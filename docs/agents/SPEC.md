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
- **Art (Cory's reviews, 2026-10-25 to 10-29).** Paint what a student looks at: scenes, places, characters, animals,
  creatures, objects and props are painted images. Draw in code only diagrams, charts, graphs, maps of data, grids,
  controls and labels, or a shape the tool must move or bend in ways an image can't. Half of Cory's fix notes were "the
  graphics need work", most of them about code drawings of things that should have been painted (career town, pets,
  hands, kids); "none: drawn in code" is right only when the whole tool is a diagram or chart. Plan art that
  animates: separate cutouts per moving part or pose (Biscuit's head turns, Bix's six faces), not one flat scene.
  Mark any person `people: true` (Gemini only, reviewed by Cory; never a local model). Text on signs, labels and
  screens stays in code over a blank painted surface. 0 to 30 images is normal; more is fine if each earns its place.
- **Voice.** K-2: list every fixed spoken line. Grades 3+: narration only where it truly helps (instructions, a story);
  most text is read on screen. Tag every line `how` (spoken the first time, then hint only) or `event` (spoken every
  time it happens), and say when it stops fitting ("stale when the guess shows"). A waiting line names the action and
  the control ("Tap Cat or Dog"), and never names a control that is disabled at that moment.
- **Check your own numbers.** Run every rule, score table, tolerance and worked answer on real values (Python) before
  you hand off, including the worst cases: noisy data, zero, the largest input, every ending. Half-Life Dice's "within
  0.5 rolls" failed ordinary noisy runs; a career tool's data contradicted its own claim. Say what you ran in Sources.
- **Name the focus.** For each mode, say what the student's eye should be on, and lay the screen out so it is the
  biggest, central thing (Cory moved Trails' job cards onto the map). Anything that plays on its own (a run, a parade,
  a song) keeps every control live: a tap changes what is shown at once, never at the next beat.
- **Fit the kit and the scope.** Sound starts as the kit sets it (on); Read, Motion and Sound are the kit's. No
  feature that makes students move work between devices by hand (codes to copy, print cards): Save on this device is
  enough. Keep auto-plays short (a run over about 30 s needs a reason).
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
<each mode: its focus (what the eye is on), what is on screen, what the person does, what responds. Name every button.>
## Content
<all the data: items, values, texts, scenes. Complete, not "and so on".>
## Interactions in detail
<the moment-to-moment behavior, edge cases, what happens at the extremes, reset>
## Look
<accent color and scene palette, different from neighbors; contrast ratios>
## Art
<name: one-line positive prompt (what is in it, never "no X"); aspect; cutout yes/no; people yes/no; how it is used>
 (or "none: drawn in code" with one line on why the tool is all diagram or chart)
## Voice
<bank voice id (different from neighbors, see STANDARDS.md), style line, then every fixed line as
 "how" or "event", when it plays, when it goes stale, and the text>  (or "none")
## Family engine
<which engine parts it uses and the content it feeds them>  (or "none")
## Sources
<one line per fact source, with a URL or citation; then the number checks you ran and their results>
## Done when
<5 to 10 checks the Refine lenses can test by playing it; include one for the focus and one for a tap while anything plays>
```

Keep it under about 250 lines. Then stop and report: the one idea, the "not like" list, and any open question
(something only Cory can decide). Do not create any other file.

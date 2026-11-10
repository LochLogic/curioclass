# Spec agent brief

You write the spec for ONE Curio Class tool. You do not write code. A different agent builds from your spec, so it
must stand on its own: anything not in the spec will not be in the tool.

## Read first (in this order)

0. `docs/agents/STANDARDS.md`: standing rules (variety, sizes, voice, art). It wins over this brief. Then
   `docs/agents/decisions/BASELINE.md` (Cory's standing calls) and `docs/VISION.md`.
1. `python scripts/neighbors.py <tool-id>`: the concept, module, standards, format, family siblings and nearby tools.
2. `docs/PHASE2-CONCEPTS.md` sections "Variety", "Content guardrails" and "Not a quiz bank".
3. `docs/TOOL-CONTRACT.md` and `docs/KIT.md` (what every tool already gets for free).
4. If the tool has a family: `docs/families/<family>.md`. Use its engine; do not invent a second one.
5. Two approved tools as the quality bar: `tools/calm-corner/src.html` (K-2, teacher-led) and
   `tools/size-of-everything/src.html` (older grades, explore). Skim, don't copy.
6. If `tools/<tool-id>/research.md` exists (a Gemini Flash research packet, Cory 2026-11-09): read it, then build your
   Sources from it instead of searching from scratch. Follow "For the spec writer" in `docs/agents/RESEARCH-PACKET.md`
   (spot-check its sources; say in your report how much of it you used and any claim that failed). Packets are
   paused since 2026-11-09 (a spot check found half their quotes were not on the cited page), so none are in main:
   research from scratch. Sara wrote every remaining spec (`docs/agents/claims/sara.txt`, done 2026-11-10); new ideas get specs only when Cory asks.

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

### Lessons from ten full Refines (2026-11-05)

Half the Refine blockers on Codex-built tools traced to the spec, not the build: the builder built what it was told.
These rules close those gaps. Each names the tool that taught it.

- **Two sources for every claim.** Each real-world claim (a fact, date, credit, health or safety step, science rule)
  goes in the Sources claims table with two independent sources that agree. Health and safety steps follow the current
  guidance of the named authority (AHA, Red Cross, CDC, NWS), in full: not half a rule (First Aid: the seizure rule
  was half of it; heat stroke got cool cloths instead of cold-water immersion). Where good sources disagree, the tool
  says so; it never ships one side as fact. A claim you cannot back twice is cut.
- **Credit and dates from the culture's own history.** Date a tradition by its own history, not when Europeans met it,
  and name the people who made it, especially Black, Native and colonized creators (Music History Radio: gamelan
  scored against 1889 Paris; swing headlined by Goodman without Fletcher Henderson). Flag such content for the
  sensitivity review in the report.
- **Models say what their numbers mean.** A readout names its unit and what it is measured against (Living Earth's
  plate SPEED showed the model's reference-frame drift). A projection keeps shapes true where the student looks (Sky
  Dome stretched the constellations). A claim about how a picture behaves is checked against the drawing rules you
  give (City Skyline's "tiers above your eye show their undersides" was false).
- **Scores and checks reward the right thing.** Run every score through the wrong behaviors too: doing nothing,
  stopping, mashing, the common wrong answer, a shortcut through the readouts. The right practice must score best and
  the common wrong answer must fail (First Aid's CPR score rewarded stopping; City Skyline's check passed flat lines
  and any three upright lines, and its camera puzzle could be read off the percents).
- **The tool's own numbers agree with each other.** A rate, size or setting that a lesson teaches matches what the
  starters and defaults use (Flipbook taught "on twos" at 24 per second while every starter ran at 12; Virtual
  Gallery's 145 cm center line was not what its cited guide says).
- **Standards map.** For each code, write the student action that teaches it, what they see, and the Done when check
  that proves it. Read the code's grade wording: K-2 theater asks the child to connect a character's feeling to their
  own (Puppet Show's "When did you feel worried?" never mentioned Pom) and to give their own reason (its vote handed
  them the reason). A skill the tool claims (plan, revise, justify) needs a step that does it. A code with no real
  step is dropped (BASELINE rule 2).
- **Make the outcome visible.** When the point is "watch it change", list what the picture shows for every outcome,
  and make each one different at a glance, with its own art states if needed (Moon Base: three endings looked alike
  and "the plants are droopy" played over healthy tomatoes).
- **Art fits its subject and its spot.** Give each image the aspect of the real thing (a tall artwork is 3:4; Virtual
  Gallery drew seven of them wide). Say where each cutout sits in every mode and that all of it shows (Puppet Show:
  Pom cut off mid-body, Dot hidden behind the curtain). List every pose the tool shows (Levels and Pathways' dancer
  broke apart at Low). Faces or icons the student must tell apart differ clearly at button size.
- **Pre-readers (K-2).** Every choice is a picture (painted or SVG), never a text glyph or emoji (Moon Base's
  battery was "▣" and its door an empty box). Every question and every choice is spoken, so a child alone can play
  (BASELINE rule 4).
- **The first screen starts the main thing.** Say what plays on load and what the first tap on each control does. The
  first hint must name an action that starts the tool's main path (Puppet Show's "tap Next" skipped all of scene 1).
  The welcome may be cut by that tap (BASELINE rule 16), so a premise or role the tool needs (Moon Base's "Teacher,
  you are Commander Ada") also lives in the hint, in Read, and where it is next needed.
- **Fits a school laptop.** Lay out each mode for 1366x768 full screen: the focus and every control the mode needs
  sit above the fold, and a list the student must see whole (a checklist) fits or is paged, never a scroll panel
  (City Skyline, Virtual Gallery, Living Earth under 1050 px wide). Say what folds away at 680x425.
- **Lines that must be heard.** Mark a line that must not be cut (a story beat, a tour stop, a result) and make what
  follows wait for it (Virtual Gallery's tour cut every jump line). Say how often a repeated line may play: a warning
  once per cause, not per action (Flipbook's "too big" on every stroke); a coaching line a set number of times, then
  hint only (First Aid's coach every 8 s, forever). A line meant for after a blocking step (print) plays before it.
- **Personal prompts.** When a prompt invites a student to share feelings, family or health, "Who and how" says what
  the teacher does with a serious disclosure (a pass option on screen, follow school procedure) (Puppet Show).

### Spec test result (2026-11-06): the lessons above were read but not applied

Five specs written under these lessons came back from Refine with 1.2 blockers and 12.6 should fix a tool (old
specs: 0.9 and 9.9), and about half still traced to the spec, mostly checks a child could pass without the skill and
pre-reader lines heard out of order (docs/agents/MEASURE-FIRST.md). A rule in a list gets read; a table you must fill
gets done. So "Can it be beaten?" and "Heard in order" are now sections of the spec itself, filled row by row.

## Write `tools/<tool-id>/spec.md` with exactly these sections

```
# <Title>
## One idea
<one sentence: the thing that makes it worth opening>
## Not like
<one line per close neighbor: its id and how this differs>
## Who and how
<grade, subject, driver (teacher / students / either), minutes, standards codes; disclosure note if prompts are personal>
## Standards map
<one row per code: code | the student action that teaches it | what they see | the Done when check that proves it>
## Screens and modes
<on load and first tap: what plays, what each first tap does, the first hint. Then each mode: its focus, its layout
 at 1366x768 (what is above the fold) and what folds at 680x425, what the person does, what responds. Name every
 button. For "watch it change" tools, what the picture shows for every outcome.>
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
 "how" or "event", when it plays, when it goes stale, "whole" if it must not be cut, how often it may repeat, and the
 text>  (or "none")
## Family engine
<which engine parts it uses and the content it feeds them>  (or "none")
## Can it be beaten?
<one row per check, score, meter or verdict: what it asks | every way to pass it without the skill | why each fails.
 Try at least: guessing, elimination (the options repeat or shrink), the answer's position or size or color, a total
 or count that only the right option has, the answer already on screen (a strip, chart, highlight, label or counter
 that shows it before the child answers), doing nothing, mashing, and the common wrong answer. Any way that works is
 a design change here, not a note.>
## Heard in order
<K-2 tools, and any tool where a line must be heard: for each step, the lines in the order they play, which ones the
 next line or tap waits for, and the next action spoken. A sound inside a sentence is its recorded clip, never a bare
 letter (a voice reads "t" as "tee"). Feedback for an answer plays before the next question. (Other grades: "none".)>
## Sources
<claims table: claim | source 1 | source 2 | agree? Then the number checks you ran (scores through the wrong
 behaviors too) and their results>
## Done when
<6 to 12 checks the Refine lenses can test by playing it; include one for the focus, one for a tap while anything
 plays, one for the 1366x768 fold, and the Standards map rows>
## Open questions
<only what Cory or the sensitivity review must settle>
```

Before you hand off, reread the spec as the Refine lenses will (docs/agents/REFINE.md: Teaching, Play, Craft) and
fix what they would find. Keep it under about 300 lines. Then stop and report: the one idea, the "not like" list,
the claims count (backed twice / cut), anything flagged for sensitivity review, and any open question. Do not create
any other file.

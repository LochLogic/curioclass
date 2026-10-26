# Batch note: Social and Emotional Learning (2026-10-26)

Cory asked for the remaining tools in the Social and Emotional Learning section. The two K-2 ones (feelings-weather-report,
calm-corner) are already live, so this batch is the six grades 3-12 tools, in build order:

walk-in-their-shoes (3-5, story), not-yet-gym (3-5, creature), conflict-coach (6-8, roleplay), decision-tree (6-8,
builder), resilience-map (9-12, explorer), community-project-planner (9-12, tycoon).

The SEL subject is a light shelf (CASEL framework). These six are its whole 3-12 offering, so each should be a tool a
teacher would actually open for an advisory or morning-meeting period.

## Rules for this batch (on top of your brief and STANDARDS.md)

- **Sensitive by default.** BUILD-PLAN.md puts mental health in Cory's full-review tier, and every tool here touches
  feelings. Nothing in a tool asks a student to disclose something real about themselves, their family or a classmate.
  Scenarios are fictional and ordinary (a group project, a lost game, a borrowed jacket, a new kid), never abuse,
  self-harm, drugs or bullying severe enough to need an adult's intervention. Where a tool lets a student type or pick
  something personal (resilience-map's plan, community-project-planner's project), it stays on the device: no
  localStorage of personal text unless the student presses Save, and a clear Clear button. Print is fine.
- **Help lines.** resilience-map (9-12) shows where to get help, in a calm footer, not as the centerpiece: a trusted
  adult at school, and the 988 Suicide and Crisis Lifeline (call or text 988 in the US, from 988lifeline.org). Check the
  wording against the source in the spec. No other tool needs a help line, but every tool's notes.md says the
  teacher's school counselor is the right next step if a student is upset.
- **No diagnosis, no scores on feelings.** No tool tells a student what they feel or labels them. Win states and points
  are fine where the format calls for them (not-yet-gym's challenges, community-project-planner's budget), never for
  emotions themselves. Conflict-coach grades the moves (an I-statement, a reflective listen), not the person.
- **People in art.** Local FLUX must never draw people, and these are people stories. Draw characters in code (simple,
  friendly, varied skin tones, like tools/feelings-faces), or use animal characters, or scenes without figures. Do not
  plan any Gemini people art for this batch.
- **Bands.** 3-5 and 6-8 set their own `:root` colors (no band theme file exists for them yet; do not write one). 9-12
  links `kit:theme-912` and sets its own `--brand`. 9-12 is students on laptops, minimal celebration.
- **Voice.** Each tool its own bank voice, different from its neighbors' (STANDARDS.md "Variety"). Recorded references
  for this batch: warm-teacher, hs-narrator, gentle-storyteller, big-sister, clear-teacher, upbeat-guide, soft-breath,
  wise-mentor, casual-peer (check `voices/<id>/ref.wav` exists before naming one). Two tools in this batch may not share
  a voice. Grades 3+ narration only where it helps (STANDARDS.md); 3-5 story beats are a good use of it.
- **Facts.** SEL claims (what an I-statement is, the stress response, growth mindset) come from a named source in the
  spec: CASEL, the American Psychological Association, the CDC, a state SEL standard. Do not overstate the research
  (growth mindset effects are small in large studies; say "practice helps" rather than "your brain grows").

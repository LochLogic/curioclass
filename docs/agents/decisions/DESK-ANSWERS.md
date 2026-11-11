# Answers from the Review Desk

Cory's answers to question cards, and what each still needs. Remove a line once it is applied to the specs.

## 2026-11-10

**Catalog direction (q-catalog-direction) and catalog pilot (q-catalog-pilot): Cory agrees with the assessment, in
chat; every pick stands.** Tool building is paused until the path in docs/ROADMAP.md ("The path from here") reaches
step 5. Now BASELINE rules 21 and 22. To apply, in the roadmap's order:
- Rule edits (docs/agents/catalog/judge/live-core.md, part C, six edits): SPEC.md "Explore first" (the mode that
  carries a "do" standard is on the main path), SPEC.md Standards map (quote the verb, list the parts, who does the
  verb; five differing checked items per "do" code, a predict before the reveal per "understand" code), SPEC.md "Can
  it be beaten?" (which-way feedback, running totals), REFINE.md Teaching lens item 1 (test by parts and key step; a
  code only in an optional mode, readout or plan.md is a blocker), docs/TOOL-CONTRACT.md (`role` and what the unit
  adds in tool.json; `outcome` claims main-path work only), data/modules.csv (standards, not clusters).
- Extract row: format 2 stays (already in docs/agents/CATALOG-EXTRACT.md), with the two wording changes from
  live-core.md part A (narrow `beatable` to "trial is cheaper than thinking"; add depth `explored` with `unit_adds`
  for understand, model and investigate verbs only). Re-run the 36 pilot tools as the test, then the full read.
- Year standards (RL.6.10, RI.6.10, W.6.10 and their like) are recorded as met by the year spine and the Reading
  Room, with tools as helpers.
- The six grades 6 to 8 tools that reuse one text get a text per grade, as spec additions before Build.
- Lettered parts of W.6.1 to W.6.3 each get a named, checked student action in the tool's draft step.
- climbing-reads: held; reshape as a climbing view over Reading Room texts after the ten-story pilot.
- recipe-scaler: one tool, two full modes (adding, multiplying).
- 4.OA.3: no new tool now; growth-spurt grows to all four operations and the year spine brings multistep problems
  back in three later units. Look again after the unit pilot.
- 4.NBT.4 fluency lives in the number-ops generator and the unit's daily practice; road-trip-logbook links to them.
- 4.MD.5b: one counted-steps job added to skate-park-angles at Refine.
- Built tools, in order: two-trains and smoothie-lab; sight-words (irregular words stay whole-word, decodable ones go
  through sounding out; check the word list's licence first); the six cheap "tool does the key step" fixes;
  moon-phase-model (seasons) and how-animals-see; three grade 11 fixes; then the code moves. Lists and sizes:
  docs/agents/catalog/judge/live-core.md, part B.
- Spec notes from the two pilot judge files (about 30 tools) are applied without asking.
- Amended the same day after the shelf survey (docs/ECOSYSTEM.md): modules are not split or renamed; their standards
  are spelled out in place and each tool carries its own codes. Math codes are written with the cluster letter
  (4.NBT.B.5); the judge files and this list use the short form and are read that way.
- Amended again the same day (Cory asked whether whole modules were the best choice or the easy one): a module is
  one teachable topic, split only when it holds two unrelated topics, and then properly (split script, redirects,
  Word Wall, chart and games divided by hand); never split just to reach standard-level detail. Candidates are
  flagged in step 2 and come to Cory as exceptions in step 4. Cory also agreed: Recess and Curiosities claim no
  standards; a course is a "course", a unit is the Track 7 package. Major-work marks: Cory has no preference, so
  they are filed (data/standards/ccss-math-focus.csv, ids and one-word marks only, licence note in its header).

## 2026-11-08

**Recess first collection (Go, Chess, Checkers, Cargo Hold, Untangle)**
- Cory takes the default on every open question in the five specs ("we'll tweak them later"). Each spec's Open
  questions section is marked "Owner: default accepted, Cory 2026-11-08; may tweak later." Untangle keeps its name.
- Computer opponents cover a real range in every board game, gentle to genuinely strong (applied to Chess, Checkers
  and Go, and in CODEX-RECESS.md).
- Chess: the top puppet (Lion) plays at about 2250 Elo, the ladder in even steps of about 300, calibrated against
  Stockfish at dev time (applied to the spec, 3cf5d85b). Chess is built first.
- Untangle and Cargo Hold: a progressive difficulty ladder with room for 500+ levels without a big file (generated,
  verified and packed). Cargo Hold is queued after its update; Untangle's design goes to Cory before it is queued, and
  it is the second build.
- front-line: the real-data day takes its default (a later round, already in the spec's "Later round (decided)").

## 2026-11-06

**Second spec test (estimation-station, which-way-is-down, box-plot-builder, story-graphs, illusion-lab)**
- box-plot-builder keeps Luka Doncic's 2023-24 game log as its sports set (applied to the spec).
- box-plot-builder's data-desk engine addition, box plot option `whiskers: 'range'`, is approved; it is built with the
  tool and goes into docs/families/data-desk.md in the same change.
- People art in these five: Codex can paint it; Cory has no concerns there.
- The Codex prompt file needs nothing for these; the queue picks them up as SPEC_TEST_2.

**Third spec batch (vibration-station, skate-park-angles, cooler-challenge, lunch-survey-cleanup, trade-island)**
- Spec cost: use 200k tokens as the average for a new-format spec and stop measuring it per batch.
- trade-island: drop the Rana Plaza case card. Redesign the factory-move policy with a less difficult issue (no deaths or disasters); fix lands with the next spec batch.
- lunch-survey-cleanup's two open questions (made-up survey, blanks moved to grade 6): Cory has no issue with either. Both stand as specced.

**Fifth spec batch (tap-to-start-puppets, paper-plane-assembly-line, box-packer, front-line, leaf-factory), 2026-11-07**
- front-line: yes to one real-data day (archived hourly station readings, for example a spring cold front across Kansas from the Iowa Environmental Mesonet), added in a later round after the exit check. This build ships with model days only (applied to the spec).

## 2026-10-30

**People pictures (q-people-images)**
- Gemini is back. It was only paused for one session. People images go to Gemini again (`scripts/art.py`).
- globe-theatre-stage keeps Bianca and the Widow: all 19 cutouts.
- growing-up-q-a: painted kids, kept safe and professional, with Cory checking each one.
- fitness-circuit and the dance family: people images if they are not too big. Art averages about 29 KB an image, so 24
  images come to about 700 KB, well inside the 2 MB limit. Use the people images. To apply: change each spec's figure
  from the code figure to painted poses.
- Follows from Gemini returning: keep people where the person is the point (the card's first question).

**Grown-up voices (q-voice-bank):** Claude's pick. Add 3 or 4 grown-up voices before the first voice night for these
tools, then move the 25 grade 6 and up specs and the 5 neighbor pairs onto them.

**Five calls from the spec revision (q-spec-calls):** Claude's picks.
- path-planner: the military route sits side by side with the others, same facts, no recruiting tone.
- algorithm-audit: name income plainly.
- Print is fine when paper is the product. chore-flowcharts gets its wall print back.
- director-s-chair: paint the 5 masks locally, seen by Cory at review.
- music-history-radio: add one station from outside the European and American line.

**Arts and Music specs (q-arts-specs):** Claude's picks except number 3.
- name-song-practice keeps the microphone. place-mood-makeover stays a playground. audience-talkback needs no voice
  sample. stage-lighting-plot's light model moves to `kit/stage.js` after that tool is approved.
- neighborhood-issue-play: Cory asked for whichever teaches better, even if harder. That is the new family who speaks
  another language, with people puppets (Gemini) and a fresh sensitivity review. To apply: restore the third problem
  from the idea card. Write the problem as neighbors who can't yet talk to each other, never the family as the problem.

## 2026-11-04

**Super tool specs: Claude's picks on every question.** To apply: write each pick into the spec (tools/<id>/spec.md)
before that tool is built.
- pocket-universe: exaggerated sandbox masses with a line saying so; the Figure eight goal nudges a ready-made
  three-body dance; keep the Gravity dial; keep the black hole in the grade 6 tray; Real Solar System starts 1 Jan 2000.
- living-pond: retire Food Web Wobble fully; label the minnow color drift "sped up" on screen; keep the fish food
  winterkill; if art pushes past 2 MB, cut to two shore backdrops and tint seasons in code, keep the creature poses.
- molecule-forge: keep the FDA caffeine range; keep the sodium metal crystal; unfound Book pages keep the silhouette and
  atom-count hint.
- span-and-spire: add one real earthquake record if a public record checks out at build; game prices; the Old farm
  bridge sample shows only after the first save.
- cipher-vault: Mary, Queen of Scots' trial stays a plain fact; keep the Leeson gravestone quote; doors open in order
  with a confirm-gated Open all doors for teachers.

**Codex test tools (q-codex-tests):** yes to 1 to 3, Claude's pick on 4 and 5.
- Network Help Desk and Half-Life Dice get a graphics and gameplay pass with the new brief rules before voice and Final
  look.
- Corrected by Cory the same day: Codex IS the primary builder and the phase 1 reviewer (the cold CODEX-REVIEW.md pass
  in a new chat), with Claude's Refine lenses after it. Judge the builds on Cory's play test too.
- Half-Life Dice: add a student action on the energy ladder (tap the rung where a balanced card's energy lands).
- Half-Life Dice keeps 5,730 years for carbon-14 and mentions 5,700 in the teacher notes.
- The audit stops flagging "welcome not heard after a first tap".

**Worksheet backlog (q-worksheet-backlog): Claude's picks.**
- Trim to about 30 authored sheets per unit (about 6,450 in all), cutting first where rows repeat a type. A fresh agent
  proposes the cuts per unit; Cory sees the list before anything is removed.
- Next writing waves favor world languages, SEL and English learners, then science and social studies. Math waits for
  its generators.
- Arts lists stay; arts rows a generator makes are backed after a strict sift (done 2026-11-04).

**Ten new generators (q-new-generators): Claude's picks.**
- Spanish vosotros is off by default (Latin American usage); the setting stays. Applied 2026-11-04.
- Can-do and ACTFL statements ship as paraphrases with the note; ask a world-language and an ASL teacher to check them
  when a contact turns one up.
- Stage areas from the performer's view and the class count-sheet key stay.
- Statistics thresholds stay, labeled as classroom rules on the key.

## 2026-11-10, Sara's spec questions (q-sara-specs, q-sara-specs-2)

**Settled by Claude at Cory's request ("you might be able to do it knowing my intent already"), from BASELINE and
the adoption bar. Cory can reverse any of them; one call is left open on the Desk.** The 220 notes behind the two
cards each used a default, and every default stands except where a line below says otherwise.

By class, all 220 notes:
- Sensitivity flags (about 70): the default stands. Each gets the fresh-agent sensitivity read before Build (BASELINE),
  hard history is told plainly at grade level with sources on screen, and no images of suffering.
- Data sources (about 35): the default stands. Data is bundled with its pull date, no network at runtime, each figure
  rechecked at Build and at the yearly check.
- Code moves (about 25): every move stands. Tools carry their own codes now (ECOSYSTEM.md), so the specs are already
  right; data/modules.csv is brought into line when module standards are spelled out in path step 4, and the full
  read (step 2) checks each receiving tool really teaches the code it was handed.
- Overlaps (about 20): each "Not like" split stands; the step 2 tables confirm or flag them.
- Format changes (nine): accepted.
- Trapezoids: inclusive definition everywhere, teacher note naming the other.

The thirteen calls:
- Because Bridge: swap the helmet-law line for a third safety reason, so the tool is true in every state.
- Idiom Illustrator: add the grade 4 deck (L.4.5a, L.4.5b) as its own content, so it counts for grade 4 in the ledger.
- Myth Museum, Fire room: keep the Cherokee Water Spider story, the Cherokee Nation's own telling credited first,
  fresh-agent sensitivity read before Build.
- Ten Spanish tools: a fresh agent checks the Spanish text at spec revision; a person listens to a 20-line sample
  per tool at the Art and voice step. Who listens is asked then, not now.
- Mundo Hispano: bank voices with regional accents; a speaker per place only if a funder or volunteer appears.
- Eleven ELD tools: English only with pictures and read-aloud; home-language glossaries later as one shared kit
  feature.
- Code moves and the two module titles (Skateboard Fund Chances, Behind the Podcast): apply, in path step 4.
- Nine format changes: accept.
- State Story Timeline: Nebraska first as the model, other states in waves, each with its own sensitivity read.
  It is not in either proof course, so nothing is built until its course comes up in step 6.
- Changemaker Cards: keep the six.
- CSTA 2026 text: file it in data/standards with its licence noted, together with the other subjects' texts still
  owed from step 1 (science first, since the ledger cannot measure a course without its texts).
- Many Voices Book: bank voice for the whole book; native-speaker greetings only with volunteers and consent.
- Settle the Valley: SETTLED by Cory on the Desk, 2026-11-10 ("Use Claude's picks on all of these", card
  q-sara-specs-2). Hold the tool and rebuild it on one real nation's own published teaching materials when its
  course comes up, then ask that nation's education office to look at it before it goes live. No paid consultant
  unless a funder covers it. Why: a made-up first people is the kind of generic portrayal state reviews mark down.

## 2026-11-10, the maps (card q-maps-1)

- Live rework tools: yes. Fix the 26 live tools sorted as rework first in step 3; the 36 built ones wait until their
  course comes up.
- High school math: yes. Leave it until grade 4 math has proved the pattern.
- Thin specs: changed by Cory. Sara takes the spec fixes, and not only the 62 thin ones: the whole spec catalog.
  Claude builds a folder listing which spec needs which kind of fix (docs/spec-fixes/); after all are fixed Sara
  does a final review to confirm they meet the end standard (docs/spec-fixes/FINAL-REVIEW.md). This replaces
  "revise just before Build" as the default: specs are fixed ahead of Build.

## 2026-11-10, late: Shape before fixing (Cory, in chat)

- Cory asked why fixing came before Shape. Agreed change: Shape runs first, one course at a time, then the fixes for
  that course (specs by Sara, live tools by Claude). Only fixes that hold whatever the shape (a wrong fact, a broken
  control on a live tool) run ahead of it. This replaces "fix the 26 live rework tools first".
- Sara's order follows: courses that have been shaped, starting with the two proving courses.

## 2026-11-10, late: the first shape cards

- Grade 4 math (q-shape-math-4): yes to a second lesson tool for multiplying a fraction by a whole number
  (4.NF.B.4; Recipe Scaler keeps 4.NF.B.3). Yes to a second lesson tool for division (4.NBT.B.6; Area Model Builder
  keeps 4.NBT.B.5). On Angles and Line Plots Cory did not accept "do not split" as analysed: he thinks it could be
  two tools in the same module and asked for a reassessment. Reassessed and re-asked on the same card; the rule that
  came out of it is in docs/agents/catalog/shape/math-3.md ("The rule for a module with two topics").
- Grade 6 ELA (q-shape-ela-6): Claude's picks. The fourteen grade 6 to 8 band tools are part of the grade 6 course,
  each with a grade 6 path, and are Sara's next batch. A second lesson tool for drafting the argument (W.6.1c to e).
- Grade 5 math (q-shape-math-5): Claude's picks. Grocery Run keeps decimals and spending; a new lesson tool for
  whole-number multiplication and division (5.NBT.B.5, 5.NBT.B.6). Zoom by Tens keeps place value and powers of
  ten; a new lesson tool for reading, comparing and rounding decimals (5.NBT.A.3, 5.NBT.A.4).
- The five approved tools are not written as ideas yet. Each gets an idea card and a spec when its course's Build
  opens; until then the shape file is the record.

## 2026-11-11: grade 3 math, and the two-topic rule

- Grade 3 math (q-shape-math-3): "Use Claude's picks on all of these." All four second lesson tools approved, each
  in its existing module: unknowns, properties and unknown-factor division (3.OA.A.4, 3.OA.B.5, 3.OA.B.6; Equal
  Groups Zoo keeps 3.OA.A.1 to 3); equivalent fractions and comparing (3.NF.A.3; Fraction Trail keeps 3.NF.A.1 and
  3.NF.A.2); area as multiplication and addition (3.MD.C.7; Tile the Floor keeps 3.MD.C.5, 3.MD.C.6, 3.G.A.2); time
  to the minute and elapsed time (3.MD.A.1; Kitchen Lab keeps 3.MD.A.2).
- The two-topic rule (one module, two tools when the topics sit in separate modes or cannot both fit one sitting of
  about 35 minutes; otherwise one tool): Cory said in chat he likes the rule. It now stands for every course.
- Still open: the re-asked line plot question on q-shape-math-4.

## 2026-11-11: standing calls made while shaping the rest (Claude, under the Desk defaults)

- Shape questions go to the Desk only where a tool over four codes cannot be fixed inside one sitting and part of
  its load already reads as taught, so there is a line to split along. Four new cards: q-shape-math-6,
  q-shape-math-8, q-shape-ela-5, q-shape-ela-11 (five questions).
- Not asked, by rule: loaded tools where nothing reads as taught (fix the spec first), close calls (fix inside the
  tool), band tools (a path per grade first), high school math (waits for grade 4 math), and every subject outside
  math and ELA (rough reads).
- Two hand overrides, in shape/decisions.csv: Turn and Talk Wheel (kindergarten ELA) and Socratic Seminar Board
  (grade 10 ELA) keep their discussion standard; the rule would have moved the very thing each tool is for.

## 2026-11-11: the cold review, and five changes (Cory, in chat)

Cory asked for a cold review of the plan. Claude's own read and an independent agent's agreed: the diagnosis and
rules hold, but the plan measured specs, not courses, and proved a course too late. Cory: "Let's make all the
changes, the new findings seem sound."

1. Sara's queue stops at batch 4 until grade 4 math is proved.
2. The proof moves ahead of further fixing (ROADMAP step 4) and starts now: spine, three tools, one unit, a real
   rubric, a working teacher.
3. The measure is split: full on paper, full and live, verified, unit days.
4. Every spec carries three hooks: a check the teacher can see, English learner supports, access.
5. Subjects outside the core are parked, not dropped. (The agent proposed dropping them from the bar; Cory's goal
   keeps them.)

Also taken: a top-model spot-check on every re-read; Sara's final review is no longer the last word on a course.

## 2026-11-11: close every gap in the plan itself (Cory, in chat)

Cory: "improve the plan as written to close all the gaps we've found." Added to ROADMAP: "What a finished course
holds" (nine items; the definition of done for a course) and "Gaps found, and how each closes" (nineteen rows, each
with a step and a test for closed). Defaults Claude chose, open to change: about 150 teaching days per spine; three
sizes of assessment; public claims follow the ledger by script; two teachers before step 6 opens; a logic model
instead of any claim of results; Sara's time after batch 4 goes to unit pieces (asked on q-proof-math-4).

## 2026-11-11: every proposed second tool accepted (Cory, in chat)

Cory: "any questions that recommended a new tool, go ahead and accept that recommendation." Six approved, which
makes fifteen in all: the grade 4 line plot lesson (Skate Park Angles keeps angles; Jump Log is practice), grade 6
math Smoothie Lab (new tool takes 6.RP.A.2 and 3), grade 8 math Transformation Dock (new tool takes 8.G.A.1 and 5),
grade 5 ELA Fact Fusion (RI.5.6 and 7) and Slow-Mo Writer (W.5.3), grade 11 ELA Personal Essay Studio (W.11-12.3).
All in shape/decisions.csv. The proof card (q-proof-math-4) is not answered: Cory will review it soon. He also said
yes to drafting the grade 4 math year spine.

## 2026-11-11: the proof card and the spine card (Cory, in chat; the Desk was out of reach)

Yes to all eight picks.

- Build first: Community Plot Planner, Fraction Wall Duel, Road Trip Logbook.
- Teacher reader: Cory's mom, a grade 2 teacher. Cory asks her. (The pick was a grade 3 to 5 teacher; grade 2 is
  close enough for a first read, and she is someone who will say what she thinks.)
- Rubric: EdReports K-8 math. Licence checked: all rights reserved, so docs/RUBRIC-MATH-K8.md links and
  summarises, and keeps no copy. Reading it added six gaps to the roadmap table.
- Sara after batch 4: unit pieces for the two proving courses, and her final review.
- A spine plans for about 150 days.
- The grade 4 math spine: order approved, line plots after adding fractions and angles near the end, day counts
  as a first cut. Its 46 rows are in data/units.csv as planned.

## 2026-11-11: the curriculum expert, and its first review (Cory, in chat)

Cory asked for a cold, informed pedagogical review of the grade 4 math spine and suggested a standing expert agent.
Both done: docs/agents/EXPERT.md (and .claude/agents/curriculum-expert.md), and
docs/reviews/math-4-spine-2026-11-11.md. Cory: "I really liked the analysis", and asked for two more spines with
expert reviews (grade 6 ELA and grade 4 science chosen by Claude: the second proving course, and the science a
grade 4 classroom teacher also teaches). He offered his Chrome session or to fetch any source that cannot be reached.

Taken without asking: the 65 percent line is confirmed in the evidence guide's own text; the spine's header counts
are corrected. Waiting on Cory (q-review-math-4): checks at the stretch level with respond days; 4.OA.A.3 split so
its full form follows division; the revised order (measurement after division, all major work done by day 123);
lines before angles, 16 days of geometry.

## 2026-11-11: two more spines and their expert reviews (Cory asked in chat)

Drafted by fresh agents, then reviewed cold by the curriculum expert: docs/courses/science-4-spine.md with
docs/reviews/science-4-spine-2026-11-11.md, and docs/courses/ela-6-spine.md with
docs/reviews/ela-6-spine-2026-11-11.md. Neither spine is approved and neither has rows in data/units.csv.

Waiting on Cory:

- **q-review-science-4:** move energy resources (4-ESS3-1) beside the energy and device stretch; life science and
  light to 21 days with two anchors (a cat at night, a plant that cannot move) and a plant in the end task; the
  revised 108-day sequence, with a 90-session path marked for ordinary schools; a signal device in place of the
  chain-reaction contraption, with three days on circuits.
- **q-review-ela-6:** settle a named, verified, licensed text set for every stretch before any unit is written, and
  add an informational shelf to the Reading Room; state a reading load per stretch and stop saying "read whole"
  where it does not fit; fold each cumulative check into the stretch end check and give it two periods; keep the
  child labor topic but move the written argument and debate to a live question; keep small units as rows in
  data/units.csv with a stretch column, and pilot a five-day stand-alone slice of stretch 2.

To be folded in without asking when each spine is revised: the smaller findings in each review (practices used more
than once, limits, safety, materials tiers, sensitivity notes, vocabulary and language fixes). Rubrics to file next:
EdReports Science K-5 v2.0 and the EQuIP rubric (science); EdReports ELA 6 to 12 v2.0 (ELA).

## 2026-11-11: "Yes, all" to the three expert reviews (Cory, in chat)

Cory approved every proposed change on q-review-math-4 (four), q-review-science-4 (four) and q-review-ela-6 (five).
The three spines were revised once each, with the smaller findings folded in. Site rule changed with it: readiness
and end checks sit at the stretch, not the unit, and each cumulative check has a respond day (ROADMAP, "What a
finished course holds", item 4). Grade 4 math rows in data/units.csv were regenerated from the revised spine.
Grade 4 science and grade 6 ELA stay drafts with no rows until Cory's final yes on each.

## 2026-11-11: the layers, and what a tool is for (Cory, in chat, a long discussion)

Cory asked whether the full curriculum should come before any tool. His view: tools are the end piece of
instruction, and if the structure is sound a tool is a means to a defined end. Where the discussion landed, all
agreed by Cory ("yes they sound right"; "this seems right to me"):

- The defined end lives in a unit plan, not the spine. A unit plan for every unit of a course comes before its
  tools. No tool is built or refined until a plan names its job.
- A tool can be whatever the unit needs; the limits are the site's promises, the physical world, open work only a
  person can judge, and cost. So: few key tools built first, lighter practice tools over time.
- We own the full course. Open courses are evidence and source material, not something to stitch together.
- Score codes and print sheets are fine as the record. A teacher judges open work.
- Grades 3 to 12 are designed for one device per student. Home school is a named audience.
- The curriculum expert's frequent cold reads are the main review, "and that has to be okay".
- The work is layered (foundation, standards, approach, progressions, spine, unit plan, lessons and tools). Layers
  are made solid enough to build on, not finished in the abstract. Layer 1 was scattered and is now one file,
  docs/FOUNDATION.md. Layer 3, the approach to teaching, is unwritten and is next.
- The unit plan has fixed fields, not a fixed length; two pages at most.

Written into: docs/FOUNDATION.md (new), docs/ROADMAP.md ("The layers", step 4a to 4f), BASELINE rule 23, EXPERT.md.
Open: the device assumption for K to 2; what happens to tools and specs no unit plan asks for.

## 2026-11-11: the approach to teaching, first and second draft (Cory asked for it in chat)

Cory: "go ahead and start writing the approach. ensure it is well sourced and backed ... get as far as you can and
we will take another pass later". Done so far: docs/APPROACH.md and docs/APPROACH-MATH.md drafted from sources
actually opened, read cold by the curriculum expert (docs/reviews/approach-2026-11-11.md: 34 claims checked, 27
confirmed as written, none invented), and revised once. The revision moved the math-shaped promises (daily exit
question, daily warm-up, understanding/fluency/use day marks) out of the shared core because the approved science
spine contradicts them; merged twelve principles into ten; replaced a hard "from grade 6" line on problem-first
openings with a condition; cut both pages roughly in half with the study detail moved to APPROACH-SOURCES.md; and
added proposed unit plan fields. Nothing is approved. Open with Cory on Desk card q-approach: tool timers, the
SPEC.md wording, the teach-first default.

## 2026-11-11: q-approach answered (Cory, in chat: "All three sound good to me. Let's also move forward with out the library")

1. No countdown timer is shown to a student in any tool. A teacher or parent may run a short paper sprint on taught
   facts, the student comparing only with their own last score. Written into docs/APPROACH-MATH.md.
2. SPEC.md "Explore first, then do" is renamed "Try it, see it, do it", with a line that the model follows at once.
3. In grades 2 to 5 teaching first is the default for anything new; a short opening task is allowed when students
   can attempt it and the goal is an idea; science sets its own rule on its own page. Already in docs/APPROACH.md,
   principle 4.

No library access: paywalled sources stay unread and nothing may rest on them (docs/APPROACH-SOURCES.md).
The approach as a whole still waits for Cory's read.

## 2026-11-11: step 4b, the grades 3 to 5 math progression (Cory: "Go ahead with the next piece")

docs/courses/math-3-5-progression.md drafted from the standards and the 2023 Progressions, read cold by the
curriculum expert (docs/reviews/math-3-5-progression-2026-11-11.md: nearly every code, quote and pointer checked
out; 31 of 33 findings right as written; about a dozen corrections), revised once. Applied without asking, as
corrections that change no day, order or unit: spine builds-on and sets-up pointers (A1 to A9, E4), 15 builds_on
links in data/sequence.csv (B1 to B14), and the stretch 16 limit in the progression (grade 4 does find unknown
angles on a line and where lines cross, per 4.MD.C.7; the first draft had wrongly pushed that to grade 7). With
Cory on Desk card q-progression-math-4: C1, D4, E1, E2.

Also this day: docs/agents/EXPERT.md now tells the expert to start from what earlier runs left in the repo (the
source list and evidence notes, the approach, the progression, earlier reviews) and to end each report with new
sources for the list. Cory asked whether gathering sources had improved the expert; it had not, until this.

## 2026-11-11: q-progression-math-4 answered (Cory, in chat: "yes to all 4. also, the overage on file word size is acceptable")

1. The pilot unit stays on days 89 to 93. Areas there are products within 100 or a one-digit number times a
   multiple of 10; area with larger sides returns in stretches 12, 13 and 14.
2. A facts check in days 1 to 6, repeated before day 94; help in warm-ups only.
3. The decimals rule for stretches 7 and 15: decimals may appear and be read, compared and renamed; every
   calculation is in whole numbers of the smaller unit or fractions over 10 and 100.
4. Unit 8.3 keeps three days; the third is rounding used to estimate and check.

Written into docs/courses/math-4-spine.md and docs/courses/math-3-5-progression.md. No day, order or unit moved, so
data/units.csv is unchanged. The progression page's length is accepted as it is.

## 2026-11-11: Sara's work after batch 4 (Cory, in chat)

Cory asked whether Sara can work the rest of the spines. Agreed: yes, math grades 3 and 5 first, as drafts with an
expert read each. Cory then: "give her a bit more to do, even if it needs corrected later" and "maybe she can also
do the drafts for the approach pages and rubric files for science and english". Her list is
docs/courses/NEXT-SPINES.md: grade 3 and 5 math spines; science rubric files and approach page; ELA rubric file,
approach page and the grade 6 text plan; then K to 2 and 6 to 8 math progressions and spines. All drafts; no
units.csv rows, no tool work, and anything that changes what a course teaches goes to Cory as a card. This bends
"one course finished before the next is started" on purpose: drafts of lower layers only. Unit pieces wait for 4c.

# The decision log

Who decided what, when and why: Cory's answers (from the Review Desk, chat and Remote Control) and the lead's rules.
This is the one home for the reasoning behind a rule. Living docs state each rule once, as it stands, with a short
pointer here, such as "(settled 2026-11-14, see DESK-ANSWERS)". The log is append-only: entries are never removed
or rewritten, and a later entry that changes an earlier one says so. Whether a decision is applied is tracked in
data/plans/later.csv and the docs, not here (settled 2026-11-15, see the entry of that date).

**Words:** entries before 2026-11-12's "course level names" (card 112) keep the words of their day. Read their
"unit" (the short package) as today's section, "stretch" as unit, "spine" as scope and sequence, "end check" as
end-of-unit assessment, "check day" as assessment day, "exit slip" as exit ticket, "module" as topic and the tool
role "lesson" as teach (docs/GLOSSARY.md).

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

## 2026-11-11: step 4c, q-unit-plans answered (Cory, in chat)

The unit plan fields were tried on units 3.1, 9.1 and 11.1 and read cold by the curriculum expert
(docs/reviews/unit-plans-2026-11-11.md: every key right; the stretch needs its own sheet; check items reused taught
examples; pilot day 92 was grade 3 work). Revised once. Cory: "for the questions i agree with you on all cases. On
decision 8, i see value in both your point and the experts, please take the one with more structural rigor."

1. A stretch sheet is written before the unit plans of a stretch; the unit plan has 11 fields. Yes.
2. Unit 9.1 is days 72 to 73, unit 9.2 days 74 to 77. Yes; in the spine and data/units.csv.
3. Numbers rule, days 89 to 93: a perimeter used to find a side is even and 100 or less. Yes.
4. Readiness check timing: the expert's option was taken as the more rigorous structure. It is given before the
   stretch opens (last ten minutes of the previous stretch's last day, or of the respond day between), so it is
   marked before day 1. Cost: the respond half of a stretch's last day is twenty minutes, not thirty.
5. FOUNDATION: a key tool is the one a day is planned around, paper the fallback; the other kind is a light tool. Yes.
6. APPROACH principle 6: one job per use of a tool. Yes.
7. Community Plot Planner stays a key tool; Road Trip Logbook becomes a light tool; Fraction Wall Duel is held
   until units 3.3 and 3.4 are planned. The final first three are named at step 4e.
8. Word caps: unit plan 1,500, stretch sheet 700 plus its check tables, one-unit stretch 2,500. Yes.

Same day: Cory asked whether 93 courses is well grounded. It is a count of catalog pages. Counted as a school would
schedule them there are 105 (56 in the four core subjects): docs/COURSES-STATUS.md, generated by
scripts/course_status.py and shown on the Desk's new Dashboard tab. Cory: finishing every course to the adoption bar
is a firm bar to success; do not describe it as unrealistic. The Desk now has three tabs: Questions, Dashboard,
Roadmap.

## 2026-11-11: shared band modules (Cory, in chat: "use option 1")

Six sets of modules belong to a band, not one course: four English language arts sets (45 modules, 187 tool specs)
and single modules in English language development and physical education. Of three options (each spine claims
them; a shared shelf beside the courses; split each into one per grade), Cory chose the first. The module and its
tools stay shared; each grade's spine places the skill on its own days with that grade's standard and texts. The
two single modules fold into their nearest course.

Also: the spine's balance table gained a check column, and "practice tool" became "light tool" wherever it meant
the mark. Where it means the role (lesson, see why, practice) it stays.

## 2026-11-11 (evening): three cards answered (Cory, in Desk comments)

The full record, with what each answer means and what is still to apply, is in docs/HANDOFF.md.

**q-plans-4d-1 (grade 4 math plans, 9 choices).** Cory: "1, yes. 2, yes. 3, yes but mark for follow up after more
progress. 4, agree. 5, yes. 6, yes, always cover the whole standard. 7, yes. 8, yes. 9, yes."
So: stretch 3 teaches benchmarks before common denominators; word caps become 1,000 (unit plan, not counting
checks, errors, days) and 800 (stretch sheet, not counting check tables and error register), with one tool-asks
file per course; Fraction Wall Duel is a light tool, to be looked at again after more progress; the number line
splitter waits for stretch 7; the facts check (36 and 36, untimed, mark 32, a 9 by 9 table through stretch 3);
day 14 both directions, and as a standing rule always cover the whole standard; the fractions no-reuse rule;
stretch 10 number sizes; stretch 2 limits.

**q-bar-subjects (11 choices).** Cory: "1 needs a better option. this may require a unification of content
standards or possibly a "high watermark" method. 2 shelf foreign languages for a later pass (ASL included). 3 all.
4 they can stay separate but are allowed to be smaller than other courses by nature of the subject. 5 is another
place where i feel a "high watermark" may be best (follow the higher quality or rigor). 6 i lean to once per year,
but up to three times if the evidence indicates a need for more. 7 accept for now. 8 i agree for now but this is a
future area of growth. 9 yes and it might be small and thats okay. 10 yes but mark this for a deeper review. 11,
agreed"
Open after this: 1 (social studies content standards: work up unified and high watermark options) and 5 (what
"higher" means where instruments conflict on values). World languages, ASL included, are shelved.

**q-standards-currency (5 gaps).** Cory: "1, agree. 2 agree, lets fully update and cleanup where needed. 3, yes.
4, yes, fix with an opus model later. 5, agree but dont lose the note to load them when writing the spine."
The note for 5: the 26 AP and psychology modules get marked as not yet standards-checked now, and the course
framework is loaded when that course's spine is written.

They were applied later the same night; where each landed is in docs/HANDOFF.md, "Applied on 2026-11-11 (late)".

## 2026-11-11 (evening): core subjects first (Cory, in chat)

"set the soft goal that the core subjects are the initial focus, then the rest. this can be malleable where work is
complementary but when a choice needs to be made, the core subjects come first." Recorded as BASELINE rule 24,
in ROADMAP above the layers, and in docs/HANDOFF.md.

## 2026-11-11 (late): the evening's answers applied (Cory, in chat)

"go ahead and action anything that you recorded but wasnt delt with yet. then lets look at applying that to the
spine, template and plans"; "the course status table can stay as-is ... its a reminder for me"; "the stretch
expert reads can be done by sara"; on Sara's list: "add all of it and order it by what the biggest blockers are.
whichever item has the most waiting on it goes first." Where each decision landed is in docs/HANDOFF.md, "Applied
on 2026-11-11 (late)". The licence page was left for a later session with an Opus model, as Cory asked.

## 2026-11-11 (night): the cold strategic review accepted in full (Cory, in chat)

"i accept all of the reviewers recommendations, even the ones that overturn my decisions earlier. please action
those decisions so they take effect. Also i agree that the AI expert needs to be good enough, thats why i pushed
for added data (esp in pedagogy). that may need more work soon." And: "please redo saras work so she can get
started when we are done here."

The review is docs/reviews/strategic-review-2026-11-11.md. All twelve recommendations are decided. Three overturn
earlier answers: spec fixing stops now, not after batch 4; a qualified person is required for courses where
FOUNDATION section 7 says so (BASELINE rule 5 narrowed); the licence page was fixed the same night, not left for a
later session. The order of steps 4d, 4e and 4f changed: the pilot unit 11.1 is built first. New rules: BASELINE
25 to 28 and the narrowed "What goes to Cory". Where each landed: docs/HANDOFF.md, "Decided 2026-11-11 (night)".

Cory also asked whether the plan is still too heavy when an AI manages it, and what the fix is. The answer and
the proposed design are in docs/HANDOFF.md, "Plan weight"; it is a proposal to be tried on the pilot, not decided.

## 2026-11-11 (night): the plan architecture built (Cory, in chat)

"Let's implement those architectural fixes that you laid out. Then, if it changes anything in saras queue, make
the update". Built for grade 4 math stretch 11: data/plans/, scripts/plan.py (gates, tables, reading pack, defect
ledger), docs/courses/math-4/DEFAULTS.md, and the section "Facts live in data" in docs/courses/UNIT-PLAN.md.
Sara's pieces 1 and 4 changed to use it. The other five planned stretches are not yet in data.

## 2026-11-12: pilot unit plan, cold expert read (Sara's piece 1)

No decision by Cory was needed. The curriculum expert read docs/courses/math-4/s11.md cold: 15 findings, all
settled at item level, report in docs/reviews/unit-plan-s11-2026-11-12.md. The plan was revised once: part (g)
and end-check item 7 added, part (f) renamed, new stems for E92 and items 2, 3, 4, 5 and 6, a fraction exit
on day 91, minutes for days 89, 91 and 92, error C widened, the generator sheet and record sheet defined, tool
asks 7 and 8 added. `scripts/plan.py check` passes (18 items, 31 wrong answers). The verdict: the build can
start. Still owed: "Sara's read" at the top of the report. Two notes for the main session: the prose count is
1,898 words against the 1,800 cap, and the generator sheet's twelfth problem (one "times as long" area) was
added in revision to make the expert's count of twelve add up.

## 2026-11-11: ELA rubric page, approach page and stretch 2 rights list (Sara's piece 2)

No decision by Cory has been made; six are asked. Three drafts were written, each read cold by the curriculum
expert and revised once: docs/RUBRIC-ELA.md (report docs/reviews/rubric-ela-2026-11-11.md, 12 findings),
docs/APPROACH-ELA.md (report approach-ela-2026-11-11.md, 10 findings) and docs/courses/ela-6/RIGHTS.md (report
rights-ela-6-s2-2026-11-11.md, 12 findings). Settled by the expert at item level: which rubric indicators the
five-day pilot is read against; the pilot passage is Colum Part II chapters IV to VI whole; it sits below the
grade 6 to 8 band by measure (5.9) and stays, placed on judgment, with the text record saying so; the way-in
story is Baldwin's "The Cruel Tribute"; unit 2.5 reads a 2,000-word cut of the Monkey King chapter; background
text one is "The Ancient Greek City-States". Waiting for Cory's yes, written out as six cards in
docs/reviews/piece-2-cards-for-cory-2026-11-11.md because the Desk could not be opened from Sara's session:
whether grades 3 to 5 ELA claim foundational skills; new wording for APPROACH.md principle 3; text record,
question set and word list as data rows outside the word cap; the fallback second hero; the Monkey King as a
digest; background text two. Every rights row is "found, not yet second-read"; fifteen questions for the second
reader are listed in RIGHTS.md. Still owed: "Sara's read" on the three reports; the spine edits listed in the
cards file (for the main session); the findings are not logged with scripts/plan.py defect.

## 2026-11-12: Sara's pieces 1 and 2 taken in (Cory, in chat)

"sara did a little bit of work. i need to get this over to the opus 5.5 model. please take her work in, action
it, and update. then prep for changing models". Done by the main session: the six ELA questions placed on the
Desk as card q-ela-piece-2 (order 104), not yet answered; the expert's settled edits applied to
docs/courses/ela-6-spine.md; the new sources added to docs/APPROACH-SOURCES.md; the ELA findings logged in
data/plans/defects.csv; docs/reviews/DIGEST.md started; docs/pilots/COST.md started; the tool bins script
written (scripts/tool_bins.py, docs/TOOL-BINS.md). Settled by the main session at item level: the pilot plan's
prose stays at 1,898 words against the 1,800 cap until the pilot is built (the overage is the generator sheet
and record sheet definitions). Corrected: data/standards/ccss-math-focus.csv does have a header; the licence
page and the handoff page said it did not. Still open with Cory: card q-ela-piece-2; whether the other five
planned stretches move into data now or when next opened; in or not-now on the six extra pieces of a finished
course.

## 2026-11-12: card q-ela-piece-2, ELA rubric, approach and pilot texts (Cory, on the Desk)

"1, yes. 2, I agree with you.  3, i agree with you. 4, lets do our own research and find our own preferred
document. 5, i agree with you but if it doesnt work later, we find a new story. 6, use your suggestion but add a
note to upgrade to a free source later."

So: grades 3 to 5 ELA teach foundational skills; APPROACH.md principle 3 takes the expert's wording; ELA text
records, question sets and word lists are data rows outside the word cap; the fallback second hero is found by
our own research (report docs/reviews/fallback-hero-ela-6-2026-11-12.md); the Monkey King cut is taught now, a
labeled Curio Class retelling follows, and a new story replaces it if that does not work; background text two is
a short labeled Curio Class explainer with a note to upgrade to a free source later. Applied the same day to
RUBRIC-ELA.md, APPROACH.md, APPROACH-ELA.md, UNIT-PLAN.md, the grade 6 spine and RIGHTS.md.

Also 2026-11-12, in chat: Cory asked why the main CurioClass folder is no longer used and whether the several
folders risk version control trouble. Answer and a proposed clean-up are in docs/HANDOFF.md, "The folders".
Nothing was changed; it waits for his yes.

## 2026-11-12: the fallback hero and the folder clean-up (Cory, in chat)

"The Ogre of Rashomon sounds fine to me, lets go with that. yes, do the clean up as you described. the
Antigravity folders are no longer needed. be very sure that no useful work is lost in the cleanup."

Done: "The Ogre of Rashomon" (Ozaki, Japanese Fairy Tales) is the fallback second hero, row 5 of
docs/courses/ela-6/RIGHTS.md. The Word Wall work in S:\CurioClass was checked, committed and pushed; that folder
is level with GitHub and is where the main session works from now on. The Antigravity working copy was removed
after its ignored files were archived and compared; its branch stays on GitHub. Details and what is left for
Cory: docs/HANDOFF.md, "The folders".

## 2026-11-12: the Codex branch (Cory, in chat)

"Review, then merge". Reviewed: 141 new files and 5 changed, all under tools/, no conflict, no tool goes live,
the checkers pass. Merged codex/queue into main the same day. The tools stay in the frozen bin.

## 2026-11-12: the lesson-day template (Cory, in chat; card q-lesson-day)

"yes i approve lesson day."

So: docs/courses/LESSON-DAY.md draft 2 is the shape of every lesson day, proved on grade 4 math only until the
ELA and science pilots run. Questions 2 (no slides) and 3 (build the rest of unit 11.1 now) were not answered
separately; the card stays open on them. Cory also asked where the older shelves (sub day, Word Wall and the
rest, each tied to a tool) fit now that the lesson day exists; answered in chat the same day.

## 2026-11-12: the rest of q-lesson-day, the feedback note, the shelves, and course texts (Cory, on the Desk and in chat)

Card `q-lesson-day`: "Yes, no slides." and "Yes, build it now. Day 90 stays 'not ready' until its tool and sheets
exist." So lesson days ship with no slide decks, and the rest of unit 11.1 is built now.

Card `q-banner-hide`: "the x should stash it in a small peak panel so it can be brought back by the user if
needed". Done and live the same day: × tucks the home page note into a small "Feedback?" tab that brings it back.

Card `q-shelves-in-courses`: yes to all four. A lesson day names shelf items by id and the gate fails on an id that
does not exist; a course day's Sub Day packet is generated from the day; per-tool lesson plans stay for using a
tool on its own and link to the course days; unit 11.1 fills its own shelf gaps as pilot pieces, the generator
sheet as a preset of the existing generator, counted in COST.md.

In chat: "all questions answered. i have an additional comment though, i dont agree with your proposal for the
Reading Room. the rest of the proposals are good but that one needs changed. the reading room is too unrefined to
use as content for ELA. i have found that it is pretty good at higher levels but in mid and lower levels, im
finding that on average the stories are either very old or from other countries and cultures. thats fine for a
reading room but id like something newer and more relatable for course content."

So the Reading Room stays a shelf for independent reading and is not the source of course texts below the higher
grades (ECOSYSTEM.md). Where the newer texts come from, where the line falls, and what it means for the grade 6
ELA pilot (every one of its texts is an old Reading Room book) are on card `q-course-texts`.

## 2026-11-12: course texts (Cory, card q-course-texts)

1. Where newer course texts come from: "yes to your idea, but we can also probably do another deep dive for more
   fitting content if needed." So: mostly original Curio Class texts written to a per-grade text spec (present-day
   settings, children like the class), each read by a qualified ELA teacher before use; recent US government
   nonfiction (public domain) for informational texts; a further search for fitting open texts stays allowed.
2. The line: yes. Grades 9 to 12 may anchor on Reading Room texts. Kindergarten to grade 8 anchor on newer texts;
   an older text appears there only as a paired or optional read, never the anchor.
3. The grade 6 ELA pilot: yes. Keep heroes and their trials; the anchor becomes a new Curio Class hero story set
   today, with one myth retold in our own words as the paired text. The rights list is redone for the new texts,
   and stretches 3 and 4 get the same treatment when next opened. Grade 4 math goes first.

## 2026-11-12: after unit 11.1 (Cory, card q-plan-after-11-1, all three picks accepted)

1. Review cadence: not a full expert read on every day forever, and not spot checks yet. Lessons from the four day
   reads are folded in (47 of 50 fixed, 13 new gates). The next unit built gets a full expert read on every day, once,
   to measure whether the fixes worked. Then spot checks: scripts plus one cheap focused read on every day, a full
   expert read on one day in five plus every check day, and a teacher on a sample. Step back up if a spot check finds
   a new process defect. Written up in docs/pilots/REVIEW-CADENCE.md.
2. Order: grade 4 math is the main thread. The two five-day pilots (grade 6 ELA, then science) run once 11.1 has its
   teacher read, alongside grade 4 math. No other math course is built until they are in.
3. Tools: held until the frame is built, with two exceptions. Community Plot Planner stays first in the Codex queue
   (day 90 and the taught run need it). Codex keeps draining the non-course queue (Curiosities, Recess) until Pro ends
   2026-11-30. Claude Refine on those waits until the frame is built.

Applied: HANDOFF "Start here" and "The order after the pilot". Next unit opened: stretch 10 (days 79 to 88), moved
into data first.

## 2026-11-12: homeschool parents and the site's shape (Cory, in chat)

Asked in chat after stretches 1 and 9 landed: how much do we accommodate homeschooling parents (teachers stay the
primary users), and what should the site be now that tools are a piece of the course rather than the focal point.
Research behind the answer: homeschooling is 3.4% to 6% of K-12 students and growing; most families piece
resources together; about 3 in 4 parents have no teacher preparation; a home day is 2 to 4 hours for all subjects;
the popular free home curricula are a numbered page per day over 36 weeks; free classroom math curricula offer no
home path and lean on partner work.

1. Homeschool: option 1, "I agree with you on option 1." One course, no separate home track. Every lesson day
   carries a required "at home" block built from the same data (a 30 to 40 minute one-child path, what the parent
   says where the class has partner talk, which items to do, home swaps for materials), shown as an At home view of
   the day. At the course level: readiness checks double as placement, a 36-week numbered calendar, and a record
   sheet that works as a portfolio. Not now: separate home courses or multi-age plans.
2. The site: "you really found a good answer. I would love to see the mock-ups." The direction: two equal front
   doors (teach a course; find something for tomorrow) and a smaller Explore door for students; the course page as
   the heart (the year at a glance, numbered days, honest status per unit, print and offline per unit); one page per
   lesson day with Teach, Project, Student, Key, Print and At home views; tools as ingredients that keep their own
   pages and say where they are used; unbuilt courses still useful and plainly labelled; community without accounts
   (report a problem on every day, a public errata list, sign up to try a unit). Cory asked for a check that every
   existing piece still has a home before anything is built. Mock-ups and that check come next; no build yet.

## 2026-11-12: the home check, the mock-ups and names (Cory, in chat)

Shown the three mock-up boards (course page, day 74, where every piece lives) and the three overlaps the home check
found. Cory: "the draft pages look great! lets take the next step in solidifying the new design."

1. Teaching map: "I really like the teachers map but i agree with your perspective. can we meet in the middle and
   hide the map for now, then bring it back as a newly imagined visual representation of the spines and courses
   after they are all built?" Done the same day: the map is off the deploy build (`--map` builds it locally); its
   data is kept.
2. Sub Day: "sub day, i agree with you, your idea works." One sub-ready day per unit in each course; the per-tool
   packets stay on the Supply Closet shelf.
3. Names: "i prefer accuracy and standardization. lets go with the best known word for each thing we build and lock
   it in both internally and externally." A deep scan writes docs/GLOSSARY.md and a staged rename plan; obvious
   fixes are made, the rest come back as a plan.
4. The design is written down in docs/SITE-DESIGN.md, with a proposed build order.

## 2026-11-12: course level names (Cory, in chat; card 112 q-course-level-names, both picks accepted)

> okay, lets do the naming updates everywhere. use your recommendations. include secondary things like the review
> desk so all naming conventions are standard everywhere.

1. The course levels take the words teachers know: stretch becomes **unit**, unit becomes **section**, spine becomes
   **scope and sequence**, end check becomes **end-of-unit assessment** (check day becomes **assessment day**). Ids,
   item ids and folders keep their names (`s11-...`, `sNN.md`, `uNN-N/`).
2. Sub-ready days: one per unit in the new sense, 18 a year in grade 4 math.
3. The rest of the naming scan's staged plan goes ahead on its recommendations: exit slip becomes exit ticket, the
   day kind `Use` becomes Application, topic pages move from /modules/ to /topics/ with redirects (the `module_id`
   code name lags, as the glossary records), the tool role "lesson" becomes "teach". The Review Desk follows the
   same words. Entries above this one are history and keep the words of their day.

## 2026-11-12: unit 4 readiness sheet (Cory, on the Desk; card 113 q-unit4-readiness, pick accepted)

> Yes. Write unit 4's readiness sheet now from the four chosen items (about one short sheet), and day 24's last 10
> minutes use it instead of rereading items 2 and 5. The rest of unit 4 waits for its turn.

Done the same day in the unit 3 fix pass (75f0c406): `courses/math-4/u04-1/readiness.md`, rows s04-R1 to R4.


## 2026-11-12: math base text and the social studies content standard (Cory, in chat)

> okay, i like your suggestion for IM being our base and eureka being a reference. that covers math [...] for
> social studies, i like option D "hybrid" and Massachusetts is great. im also okay with the 8 of 14 outline
> adjustment.

1. **Math:** Illustrative Mathematics (CC BY 4.0) is the base text Curio Class adapts into its own days, tone and
   format, with a credit line that says it was changed. Eureka Math / EngageNY (CC BY-NC-SA 4.0) is a reference
   only: its sequence, models and ideas, never its problems or wording, so every page stays CC BY 4.0. First step:
   adapt the matching grade 4 unit into our unit 4 days and run it through the same reads as units 2 and 3.
2. **Social studies:** option (d), Path 1: C3 for skills, Massachusetts 2018 as the content anchor in
   Massachusetts's course order (about 8 of 14 course outlines redrawn), checked unit by unit against a named few,
   every addition recorded. Paper: docs/reviews/social-studies-content-standard-2026-11-12.md. Not yet decided:
   the "your state" plan for state study and the values order (both in that paper).

## 2026-11-12: framework, state study and the values rule (Cory, in chat)

> would this change our foundational framework or would we mold the curriculum we find to fit our site? for the
> two social studies points, i think we should skip the individual state content and replace it. we can build our
> own filler and borrow or reference to make it solid. for the values question, the first two examples show that
> higher courts disagreed, we will always side with the higher court. in the case of the LGBTQ history, we always
> side with human kindness and openness. we do not hide humanity, we teach with dignity and respect using facts and
> backed sources. we do take grade level and life experience into consideration though. Gay sex isnt a 2nd grade
> topic.

1. **Framework:** we mold what we find to fit Curio Class. FOUNDATION section 1 now names a "base text": an open
   program with terms as open as ours (CC BY or public domain), adapted into our days and voice with credit.
   NC or SA programs stay evidence only.
2. **State study:** the anchor's own-state content (Massachusetts grade 3) is not taught. Curio Class writes its
   own replacement for that year, borrowing from and referencing open sources, held to the same reads.
3. **Values rule,** in order:
   a. Where a court has ruled, side with the higher court.
   b. Facts and backed sources decide claims (the discipline's evidence first).
   c. People are taught with dignity, respect, kindness and openness; we do not hide humanity. LGBTQ people
      appear where history includes them.
   d. Grade level and life experience set how and when: the subject is taught at the depth suited to the age
      (for example, sexual content is not a grade 2 topic).
   Note from the lead session: of the paper's cases, only Oklahoma was a court ruling, and it was on procedure
   (open meetings), not content; Florida's African American history strand was disputed by scholarly bodies,
   not courts. Those cases fall to rule b.

## 2026-11-12: science and ELA base texts (Cory, in chat)

> yes use both and begin downloading and storing all the needed data to build on

1. **Science 6 to 8:** OpenSciEd Middle School (CC BY 4.0) is the base text. K to 5 and high school: reference
   only (OpenSciEd Elementary and high school are NC), Curio Class writes its own; NASA, USGS, NOAA and pre-2026-03-29
   PhET simulations are free extras.
2. **ELA K to 5:** EL Education K-5, 2017 edition (CC BY 4.0) is the base text, its trade books replaced with our
   own texts. Never mix in the 2025 edition or Skills Block 2024 (CC BY-NC). ELA 6 to 12: our own, on public-domain
   texts; everything else reference only. CommonLit is not used at all (its terms bar AI tools).
3. Copies are stored outside the repo in S:\CurioClass-sources\ (README there); the repo record is
   docs/sources/BASE-TEXTS.md.

## 2026-11-13: science 6 to 8 order and equipment (Cory, in chat)

> I think we should lean towards redrawing our science order to match theirs as long as we don't lose overall
> quality. For science equipment, I think all three are possible. ... substitutes where possible and the no kit
> otherwise ... Can we use [our online tools] to fill in our own simulations? ... It could also show bigger
> experiments that could never be done in class like large reactions, ecosystem models, etc.

1. **Order:** grades 6 to 8 science are redrawn to OpenSciEd's 18 units, on the condition that overall quality holds.
   Before the redraw lands, a short check lists anything our current order teaches better or that the redraw would
   lose (topics, standards coverage, grade fit), and each loss is either kept inside a unit or brought to Cory.
2. **Equipment:** household substitutes wherever safe; a no-kit data path otherwise. All three paths are allowed.
3. **Simulations:** Curio Class's own online tools may serve as simulations, both as a no-kit path and for
   experiments no classroom could run (large reactions, ecosystem models and the like). Each is a tool build through
   the normal tool pipeline; tools stay held until the frame is built (card q-plan-after-11-1), so simulations are
   listed per unit now and built later.

## 2026-11-13: pipeline audit questions (docs/reviews/pipeline-audit-2026-11-13.md, section 8)

1. Course order: no preference; do what is pedagogically best. Where a base text exists, its order is the default
   frame only when the loss check finds it at least as good for learning.
2. Grade 4 math: same answer. Keeping the approved order is fine if it does not harm learning.
3. Teacher reader: the expert agent reads in the teacher's place for now (Cory 2026-11-13).
4. Budget for the control reliability read and the unit 8 base-text-first test: approved. Keep it small, but quality
   comes first.
5. Login-gated IM material (cool-downs, teacher guides, assessments): take it. Cory signs in himself in Chrome; the
   lead downloads under his session. Same light-rigor credit rule.

## 2026-11-13: unit 4 sections 2 to 4 (docs/PRODUCTION-PATH.md, section 6, question 1)

> Go with your recommendation to replan

1. Unit 4 sections 2 to 4 (days 29 to 38) are re-planned from unit 4's source map and cross-day CSVs before any of
   their days are written, then written, read and fixed (PRODUCTION-PATH step 3).
2. The separate unit 8 base-text-first test is dropped; unit 4 is the harder case. Unit 8 comes back only if unit
   4's result is unclear.

## 2026-11-13: IM login-gated material withdrawn (Cory, in chat)

> i dont think ill get the IM login. it wants to verify that im an educator and i dont have that credential. can we
> proceed without it?

1. Answer 5 of the pipeline audit questions above is withdrawn. Curio Class uses only IM's free public pages (lesson,
   prep, student task PDFs, blackline masters, unit practice problems without solutions). No account, no gated
   download, no work-around.
2. Our exits and assessments stay our own, as they always were. The math content reviewer (PRODUCTION-PATH step 7)
   is the outside check on them.

## 2026-11-13: days 29 to 38 held for the grade 4 course map (Cory, in chat)

> Yes, pause those days.

1. Days 29 to 38 are not written until grade 4's course-level source map exists (every IM grade 4 lesson mapped to
   our units) and an expert has read it for unit edges and day counts. Top-down means the course level is settled
   before a unit is: the unit 4 re-plan held 10 days only so later day numbers would not shift, which let existing
   work set a limit the plan should decide.
2. If the map leaves unit 4's edges and day count standing, the days are written on the re-plan as fixed. If it
   moves them, unit 4 is re-planned again first.

## 2026-11-13: all math mapped at the course level first (Cory, in chat: "Option A")

1. Every math course, K to 12, gets a scope and sequence and a course map against IM (every IM lesson placed in one
   of our units, scripted from IM's free pages, then judged), with the handoffs between grades checked, before any
   more math days are written. Order: grade 4 (running), grades 3 and 5 with grade 4's edges rechecked, the rest
   of K to 8, then high school. An expert reads the maps; scope and sequence changes come to Cory.
2. Unit and section plans stay one unit ahead of writing (BASELINE rule 25); they are not planned in advance.
3. Fixes to written days keep running, except days 25 to 28 (unit 4), held until the grade 4 map is read.
4. All other math day writing is paused. The ELA and science pilots are not affected by this; when they start, the
   same top-down rule is settled for them.

## 2026-11-13: course mapping paused too (Cory, in chat)

> Actually, pause the mapping as well. We need the master plan to finish being settled.

1. The grade 4 course map was stopped before it wrote anything. The scripted table of IM's 149 grade 4 lessons is
   kept outside the repo for when mapping resumes.
2. All new math planning and writing waits until the master plan (docs/PRODUCTION-PATH.md) is settled. Fixes to
   written days may still run (except days 25 to 28).

## 2026-11-13: a progression layer above the course (Cory, in chat, PRODUCTION-PATH question 4)

> yes i agree with a progression layer.

1. Step 0 of docs/PRODUCTION-PATH.md is approved: a progression per subject, all its grades, kept as data with
   gates (data/progressions/<subject>.csv), above the course level.
2. Cory then proposed an order for the whole build (progressions for the four core subjects, then courses, then
   baselines with social studies first and math last). It is being assessed; nothing is built until he settles it.

## 2026-11-13: the build order for the core subjects (Cory, in chat, after two rounds of assessment)

1. Pre-work, settled before the plan starts: the social studies content standard (unified set or "high
   watermark"); a scout for an openly licensed social studies base text (if none fits, social studies stays the
   clean-slate subject and science goes second); BASELINE rule 25 replaced by this order.
2. Progressions for the four core subjects, then a review. Course framing for all four, then a review,
   a whole-structure check and a website design check: baseline 1.
3. Social studies first: scope and sequence, review, units, review, a probe (a few days written to test the unit
   template), then a full review from the progressions down: baseline 2.
4. The same cycle for the other subjects, math last (science second if social studies has no base text).
   A final all-subject, all-course review.
5. Then sections, days and lessons, starting with a guard: a few entries written below the full unit level, with
   "on" and "off" defined beforehand. Then tools are unlocked.
6. The 49 non-core courses come after the core subjects.

## 2026-11-13: the standard stands, no people yet, Codex, no ceiling (Cory, in chat)

> yes it stands unless you have reason to believe it isnt solid enough for our new plan. if thats the case we do
> more pre-work and make it good enough. [...] we have no people, part of the pre-work will need to be ensuring our
> expert reviewing agent is well built enough to handle this work. codex can absolutely be used. [...] no spend
> ceiling. lets be judicious and efficient with our tokens but again, we dont sacrifice quality.

1. **Social studies option (d) of 2026-11-12 stands.** The lead found it sound as a decision but not yet usable for
   a progression (anchor not loaded, course list still in California's order, check states not named, the
   replaced state-study year not designed). That work is pre-work P1a to P1e in docs/PRODUCTION-PATH.md.
2. **No people yet.** Pre-work P5 makes the expert agent good enough first: subject lenses, a science bar and the
   social studies bar, briefs for the new layers, and a calibration test with planted faults, read by the expert
   and by Codex. FOUNDATION 7.3 still applies: nothing is called finished without qualified people.
3. **Codex is used freely** (its weekly budget resets; large use is open when needed).
4. **No spending ceiling.** Judicious and efficient with tokens, never at the cost of quality.

## 2026-11-13: card q-ss-course-list, the social studies course list (Cory, in chat)

> yes to the dashboard question, go with your recommendation. [...] when we fill in grade 3, can we use other
> states standards to help fill in that year? if so, lets do that. whatever makes the curriculum the best.

1. **The course list is redrawn to Massachusetts 2018 order** as in docs/courses/social-studies/STANDARD.md
   section 2, with the lead's pick for high school: World History I and II in grades 9 and 10, US History I and II
   in 11 and 12, Government and Economics as half years in 11 and 12. Core social studies goes from 13 courses to 15.
2. **Grade 3 draws on other states' grade 3 standards** wherever they make the year better (read only, our own
   words), on top of the Massachusetts skills kept in general form and C3.


## 2026-11-13: cards q-probe-guard, q-ss-partial-bases, q-hs-science-core (Cory, on the Desk)

- **q-probe-guard:** "this seems overly complex but i think i agree. these only happen after unit writing but
  before baseline 1?" The lines stand (docs/pipeline/PROBE-GUARD.md, now with a short version at the top). On the
  timing: no. Baseline 1 comes first, after the course frames (step 2). The probe runs once a subject's units are
  planned (social studies first, step 4, before baseline 2), and the guard runs once every subject's units are
  planned, before full writing (step 7). Both write a few days from unit plans; neither writes full units.
- **q-ss-partial-bases:** (1) the UK Open Government Licence v3.0 joins the base-text bar, with each Oak item
  checked for third-party material and Oak named only in the credit line. (2) On the OpenStax line about AI:
  "these are not being used to train AI. AI isnt "taking them in" i say we are fully fine to use them under that
  clause." The retired CC BY OpenStax books (American Government 3e, Economics 2e, Psychology 1e) are partial base
  texts; the current CC BY-NC-SA editions stay reference.
- **q-hs-science-core:** yes. Physics is core; the Earth and space standards are folded into Biology, Chemistry and
  Physics; Earth and Space Science and Environmental Science stay electives. data/courses.csv updated.

## 2026-11-13: card q-calibration-1 (Cory, on the Desk)

- **q-calibration-1:** "they are good to go as you suggested." Both readers (the expert agent and Codex) are
  trusted for progressions, frames, scopes and sequences and unit plans, and both read the progressions and frames.
  Codex runs by script with no clicks (scripts/codex_read.py; Cory 2026-11-13: "use a script to send it over there
  automatically, no approval or interaction from me is needed"). The re-run with fresh plantings stays L10.

## 2026-11-13: card q-ss-progression-1 (Cory, on the Desk)

- **Government and Economics:** open to grade 11 or 12. Their rows stay at grade 12 in the data, but no row
  assumes a US History I skill any more: 23 links removed, the content examples retaught in brief in the row, and
  the skills rewired to grade 8 civics, grade 7 and grade 10 rows (data/progressions/social-studies.csv).
- **The writers' eight calls:** kept as drafted (shared grades 1 and 2 economics split once; "your own state";
  survey plus one in depth for World History's one-example standards; Rwanda as the grade 10 genocide anchor,
  Srebrenica second; C3 economics inside grade 3 to 8 history units with a named activity; the added grade 4 and 5
  hard history with teacher notes; Native nations as present-day governments in grade 8; economics in both US
  History II, as a review toolkit, and Economics).

## 2026-11-13: card q-ela-progression-1 (Cory, on the Desk)

- **The dash (L.6.2a, L.8.2a):** taught, as picked. A dash appears only inside the exercise sentences students
  punctuate and the texts they read; all Curio Class prose stays free of em dashes.
- **Long texts in grades 9 to 12:** "i would really like more recognizable and recent literature. lets figure out
  how to do that without messing with the standards." The standards name few texts (Shakespeare, foundational
  American works, the founding documents) and those stay. Every other anchor text in grades 9 to 12 is picked for
  being recognizable and as recent as the licence allows: the 20th-century works now in the US public domain
  (published 1930 or earlier, one more year each January, for example The Great Gatsby, Mrs Dalloway, Passing, A
  Farewell to Arms, The Weary Blues), recent open-licence texts, and short quoted excerpts of well-known recent
  books inside Curio Class's own lessons. No student is sent to a library or a paid copy. The ELA 9 to 12 course
  frames (step 2) run a text search to this rule and say which pick each year anchors on.

## 2026-11-13: card q-cross-progression-1 (Cory, on the Desk)

- **ELA grade 5 unit 4 topic:** yes, as picked. Unit 4 becomes water (how much of Earth's water is usable and how
  communities share it), read beside grade 5 science's water and resources rows (s5-water-distribution,
  s5-protect-resources). The reading and writing standards are unchanged; only the topic moves off the base text's
  disaster module. Nine grade 5 rows and e6-reading-range updated in data/progressions/ela.csv.

## 2026-11-14: card q-ss-frames-1, social studies course frames (Cory, on the Desk)

1. **Time a day:** yes, as picked (40 to 45 minutes in grades 3 to 12; 64, 96 and 96 days in K to 2).
2. **Community and qualified readers:** "We have no support for this, it's just us. Ensure that the sensitivity
   agent is well educated, and we will make the best effort we can to teach with honesty and dignity at an age
   appropriate level." No outside readers are looked for. The fresh sensitivity agent is the read, and it must study
   the community's own published voice and the scholarship before it judges (docs/pipeline/briefs/sensitivity-read.md).
   This reverses the 2026-11-11 change to BASELINE rule 5 and the community row of FOUNDATION 7.3.
3. **Grade 12 timetable:** yes, as picked (Government in the fall, Economics in the spring; either may be taken in
   grade 11).
4. **Personal Finance:** "I don't think it needs to be a course but it can be lightly integrated. Since it's covered
   elsewhere, that will be the main education point." No core course. Economics keeps its credit and budgeting rows as
   the main teaching; light touches elsewhere (math percent and interest problems, a family budget case) only where a
   unit already fits them, no added days. The career and technical elective stays listed.
5. **History and science literacy standards (RH, RST, WHST):** yes, as picked. Load them; the 6 to 12 social
   studies and science courses meet them alongside their own standards, no extra days.
6. **Since Time Immemorial:** "Honor it mostly. It still needs to fit our structure and tone. The content shouldn't
   change though." Where Curio Class adapts its lessons: the content (facts, the tribes' own words and framing) is
   kept as written; the lesson shape and voice follow Curio Class; the credit line says it is adapted from Since Time
   Immemorial and that the content is theirs.

## 2026-11-14: card q-frames-ela-sci-math-1, ELA, science and math course frames (Cory, on the Desk)

1. **Time a day:** yes, as picked (160 days everywhere with the named condensations; shorter-period paths decided at
   each course's scope and sequence).
2. **Qualified readers:** "We have no support. Our agents are our best hope for success." No math content reviewer,
   science safety teacher or ELA teacher is looked for. Agent reads take those places: an answer-key read that solves
   every item cold beside the script check (BASELINE rule 27), a safety read against published school science safety
   guidance, and the expert's text read (docs/pipeline/briefs/sensitivity-read.md names all three).
3. **Community and cultural readers:** "Same as the last answer": the well-educated sensitivity agent, no outside
   readers.
4. **Science materials:** approved as picked (about $40 a class K and 1, $50 grade 2, $25 a unit grade 3, $30 a unit
   grades 4 and 5; no-kit routes in Chemistry and Physics unit 5 count as partial coverage, said plainly).
5. **Math paths:** not now, as picked (later.csv L15).
6. **ELA 6 to 8 texts:** "Yes, I agree but our agent is the check, not a teacher." Primary documents may anchor a unit
   where the standard's work is on them; the original literary pieces are written in house and read by the expert
   agent, not a teacher.
7. **ELA 9 to 12 check set:** yes, as picked (the college-level English language and literature frameworks and New
   York's Next Generation 11 to 12 standards, as the check set only).
8. **Smaller calls:** yes to all three (ELA 10 and World History II share one research product; grade 9's long text
   as planned; K to 2 may assume one shared classroom device, always with a paper path).

## 2026-11-14: card q-baseline-1, question 2 (Cory, in chat, before the card showed)

2. **Course pages:** "I think I want all units to go forward, not just grade 4 math." Course and unit pages are built for all 52
   core courses from the frames, not grade 4 math first. They stay hidden from the live site until Cory says (the site is
   not launched). Questions 1 and 3 wait on the Desk.


## 2026-11-14: card q-baseline-1, baseline 1 (Cory, on the Desk)

1. **Site design changes:** yes, as picked. Written into docs/SITE-DESIGN.md now (unit page, section URLs nested under the unit, a place
   for course-level check days, the course page showing the frame, fixed day addresses, courses on the find pages); built
   when the first course pages are built.
2. **Course pages:** now, from the frames, for all 52 core courses (chat answer above: all units go forward). Hidden
   from the live site until Cory says.
3. **Government unit 9 (NML.T5.5):** an optional outside-expert step the teacher arranges, with the paper path always
   complete on its own (docs/courses/us-government-and-politics/frame.md, For the lead 1).


## 2026-11-14: readiness check timing, every course (Cory, in chat, confirming card q-unit-plans of 2026-11-11)

Cory confirmed his Desk choice of 2026-11-11 (card q-unit-plans, decision 4 above) and made it the one timing for every
course, grade 4 math included.

1. **When:** a unit's readiness check is given before the unit opens, so its results shape day 1: in the last ten
   minutes of the previous unit's last day, or of the respond day or course-level check respond day where one sits
   between the two units. A unit 1 readiness check is served by the start-of-year check.
2. **Refinements approved:** a few days ahead at most, never weeks, so the results stay fresh; day 1 of every unit
   stays clean for the hook and the compelling question.
3. **Which units hold one does not change:** sequence-write.md rule 2 (a row used the year before or earlier the same
   year opens as a retrieval task inside a day; a row last used two or more grades back gets a readiness check).
4. **Applied:** UNIT-PLAN.md (header, fields 4 and 11, the field template), GLOSSARY.md, the sequence-write,
   sequence-read, frame-write, plan and plan-read briefs; the 15 social studies scopes and sequences and days.csv files
   (45 checks moved off a unit's first day: 39 to the respond day before the unit, 6 unit 1 checks to the start-of-year
   check); scripts/sequence.py now fails a readiness day on a unit's first day. Report:
   docs/reviews/readiness-timing-2026-11-14.md.

## 2026-11-14: unit plans and days by script, Codex and Claude reads (Cory, in chat)

1. **Unit plans, now:** scripts/unit_skeleton.py fills the mechanical fields; Codex fills the judgement fields on its
   own quota (scripts/codex_units.py, docs/pipeline/briefs/plan-codex.md), gated by scripts/unitplan.py; then a Claude
   expert read and a Codex read of every plan, a Claude fix pass, and one structure pass. No local model.
2. **Skeleton scripts for math, ELA and science** are built now and edited before each subject uses them.
3. **Sections, days and lessons will use the same workflow** (script skeleton, Codex writes, code gates, Codex reads
   every day, Claude reads deeply on a sample and on flags), replacing the step 8 plan of a full Claude read on every
   day. Its test waits until the unit plans are done or nearly done, so the lessons and findings from unit
   development shape the test first.

## 2026-11-14: science standards base, NGSS over Massachusetts STE (Cory, in chat)

Cory prefers NGSS over the Massachusetts 2016 STE framework, with the better teaching outcome as the tiebreak. Lead
reading: NGSS stays the base for every science course. The 23 codes Massachusetts leaves out stay taught, the
crosscutting concepts stay in the standards, and NGSS wording governs. Massachusetts becomes a crosswalk only: a
plan may note where Massachusetts folds, splits or regrades a code, and never drops an NGSS code to match it.
Source: docs/reviews/science-data-gaps-2026-11-14.md (Massachusetts codes).

## 2026-11-14: K to 2 science meets three times a week (Cory, in chat)

Kindergarten, grade 1 and grade 2 science had more days than two meetings a week allow (64, 68 and 76 days against
58, 58 and 56). Cory: "three meetings a week for k-2 science is fine." The days stay; the frames and frames.csv
move to three meetings a week (per_week 3), and the calendar is regenerated with `frame.py sync`. Applied in the
science scope fix pass, after the Codex scope run, so running jobs are not disturbed. Source:
docs/reviews/sequence-science-grade-2-codex-2026-11-14.md, finding 1.

## 2026-11-14: four open questions from the continuity review (Cory, in chat: "Yes, all four")

1. Rights and Spanish readers become agent reads now; the funding rows stay, marked "only if funded".
2. Through scope and sequence and unit plans, each subject's lens (docs/agents/lenses/) plus its rubric stands in
   for an approach page. A short approach page per subject is written before days.
3. Timers (narrowed by Cory the same day, after the live site check): a timer is allowed where it has a grounded
   purpose, such as a pace cue, a movement game or classroom management. The rule is against timers with no
   purpose. Cory, on the reading pie timers, the movement timer, the projector timer and game night: "all those
   timers seem fine to me, they all have a grounded purpose." GAMES.md timed modes stay where each has a purpose
   (check each; do not strip). Every doc that said "no timers shown to students" takes this wording.
4. Course counts, said the same way everywhere: "107 courses (105 active, 2 world languages shelved); 52 core
   courses in the four core subjects plus 6 core electives".

## 2026-11-14: grade 2 science mid-year check moves to week 20 (Cory, in chat: "Yes, move it")

So grade 2 science fits three meetings a week with every day kept, its mid-year course-level check moves from week
17 to week 20 (docs/reviews/sequence-science-grade-2-2026-11-14.md, For Cory). The science scope fix pass applies it
to the frame's calendar pin and days.csv, and `frame.py sync` regenerates the calendar.

## 2026-11-15: Religious texts are read as literature where a standard calls for them (Cory, in chat)

RL.8.9 and RL.9-10.9 name religious works such as the Bible as examples of source material. Cory: "yes, as
literature is fine." Where a standard calls for it, a religious text may be read as literature or history (its
story, its language, how later writers drew on it), never as scripture: no religious text is an anchor, the class
studies what a text says and how later works use it, and no student is asked to state or perform a belief. Grade 8
unit 4 stays with myths and folk tales (no change needed). Grade 10 day 86 (Paradise Lost) and grade 11's Winthrop
sermon stand as planned, read as literature and as a seminal US document. Each such day gets the sensitivity read
with its unit plan. The ELA fix pass replaces the "open with Cory (progression stitch, item 11)" lines in the
grade 8 frame (unit 4 row and For the lead item 6) with this ruling. Source: expert reads of ELA grades 8 to 11,
2026-11-15.

## 2026-11-15: later list calls (Cory, in chat, on Remote Control)

- ELA text records: edition and rights are filled as the units are written. Unit writers give each text's edition
  and rights basis in field 10; the lead copies them into data/plans/ela-texts.csv after each batch (later.csv L32).
- Day skeleton: built now as a living draft, before its first real need. Cory: "im hoping that having a file there
  longer will help accumulate improvements along the way to its first real need." scripts/day_skeleton.py writes a
  sidecar per day; DAY-SKELETON.md keeps its draft log (L31).
- Contrasting audiences in ELA grade 12 (L30): "L30 is good." One spine, two routes: the contrast is the audience's
  relationship and expertise, not headcount. Classroom: student panels, the teacher as lead judge, a second audience
  of another class, staff or an outside venue. Single-parent home: the parent is the live first audience and lead
  judge, and the second is a real listener outside the home from a menu (a relative or family friend by phone or
  video; a library, co-op or community group; a written public piece). Fallback: two contrasting pieces to two
  outside audiences, the parent asking live questions. Why: a home of one parent and one child has no second
  listener, and quality must match the classroom; the same rubric rows, a planning sheet showing what changed between
  audiences and a short reflection hold it equal. One outside audience serves ELA 12 unit 8 and US History II unit 12.
- Day pages (L23): "use your recommendation as long as it holds useful through the future growth." One source file
  per day, published as one page per section with each day as an anchor. Why: about 13,000 files for 105 courses
  against the free host's 20,000 (one page per day would be about 30,000); each new course adds its section count,
  not its day count.
- Licence and "first free complete" claim (L16): "leave it for now."
- Long day notes (ELA kindergarten to grade 2 most of all): "something that can be a bit long in the unit but should
  reduce when the teacher gets them unless they have a need to be that long." A days.csv note may run long as writer
  input; the teacher page keeps only what the teacher needs in the room.

## 2026-11-15: flatten the living docs; this file becomes the one decision log (Cory, in chat)

Cory: "please ensure you understand the underlying request. if you feel that you do, please go ahead with the
flattening", approving the lead's recommendation of 2026-11-14: keep a single decision log as the home for who
decided what, when and why, and flatten everything else. Why: every agent and Codex job reads AGENTS.md, HANDOFF,
PRODUCTION-PATH, the glossary and its brief before working; layered dated changes make each read longer and costlier
and leave readers to work out which paragraph wins, which is where most continuity problems came from. A flattened
doc states each rule once, as it stands, with a short pointer here; the full reasoning and Cory's words live only in
this file, which is append-only; git keeps every earlier version; dated reports are records and are not flattened.
The habit from now on: a decision updates the doc that holds the rule in place and adds one entry here, never a new
dated paragraph under the old rule. HANDOFF holds only the current state and next steps.

## Decisions carried here by the flattening (2026-11-15)

The flattening moved the dated reasons and Cory's words out of the living docs. The lines below are those reasons,
oldest first, with the doc and section each came from. Where several docs held the same decision, it appears once.

- 2026-10-27, Cory: answered the decision board (172 of 208 answered, 157 recommendations accepted, 3 own calls, 12
  held with notes); BASELINE rules 1 to 10, its specific calls and its growing-up-q-a gate were drawn from those
  answers (raw answers answers.json, questions decisions.json). Why: so spec, build and review agents settle
  questions with these rules and bring Cory only what they cannot settle; several of the 12 holds were "need more
  info", which is why every question to Cory comes with full context. (BASELINE.md, intro and "What goes to Cory")
- 2026-10-27, Cory: ASL tools are graphics only, no video and no photos of people; do not re-pitch video. Why: not
  recorded beyond Cory's call; the collection may change its format (storyboard panels, renderings, labeled sign
  parameters) instead. (BASELINE.md, "Specific calls")
- 2026-11-03, Cory: BASELINE rules 11 to 15 adopted (people art drawn by Codex, on a contact sheet Cory sees and
  checked by a fresh agent; 2 MB a goal, with a `Size:` line over 6 MB; a kit engine promoted only after three
  finished tools share the code; at most about 10 Codex tools built and not yet reviewed; public copy names no
  companies). Why: for rule 13, older tools work today and the gain from shared code is efficiency, not capability;
  the others record no reason. (BASELINE.md, rules 11 to 15)
- 2026-11-05, Cory: BASELINE rules 16 to 18 adopted (the first tap may cut the welcome; Curiosities finish on Cory's
  desk review, with plate wording "Instruments" to "Curiosities" and areas to lift fixed after it; the Curiosities
  entrance is built after every planned Curiosity is fully built). Why: for rule 16, acting at once beats listening;
  the others record no reason. (BASELINE.md, rules 16 to 18)
- 2026-11-06, Cory: Curiosity voices go on the Forge as each passes its exit check, at the end of the running Forge
  queue. Why: "recording them all together was a wish, not a hard rule." (BASELINE.md, rule 18)
- 2026-11-06, Cory: Curiosities may keep a little game essence (rule 19): a light game touch is fine, a goal ladder,
  grade, forced finish or game-over is not. Why: a Curiosity must stay purely fun and exploratory, and a light touch
  can add to that; lenses flag a game element only when it narrows play or turns exploring into scoring.
  (BASELINE.md, rule 19)
- 2026-11-11, Cory: the section plan, not BASELINE rule 22, decides how many tools a unit gets; rule 22's line "in
  math, ELA and science, the major work of a grade gets two or three tools or full modes (see why, do it, use it);
  the trade is fewer tools on supporting topics for now" is dropped, and a major unit may run on print with no key
  tool (grade 4 math unit 3 does). Why: tools are the end piece of instruction and are planned from what the unit
  needs (rule 23; see "2026-11-11: the layers, and what a tool is for"). (BASELINE.md, rule 22)
- 2026-11-11, lead: a plan's lighter tool mark is "light" ("light tool"), renamed from "practice". Why: so the plan
  mark is not confused with the tool role `practice` (rule 21) or read as the job "practise with feedback".
  (BASELINE.md, rule 23; UNIT-PLAN.md, rule 9)
- 2026-11-11, lead: the readiness check, the end-of-unit assessment, the error letters, "where it sits", the family
  note and the sources belong to the unit plan, not the section plans. Why: split across section plans they could
  not be balanced or read whole, and the grade 4 math pilot had cut two unit assessment items to fit a page.
  (UNIT-PLAN.md, "What the expert read changed" 1)
- 2026-11-11, lead: unit plan rules 4 to 7 and the marking step of field 7 were added after the expert's cold read
  of the three trial plans. Why: in all three trial plans a check item repeated something already taught; items
  shared out "by share of days" left the pilot's assessment without perimeter with multi-digit sides; readiness
  items for later sections had no reteach slot; "many" was undefined; and the respond half followed a thirty-minute
  check with no time to mark it. (UNIT-PLAN.md, "What the expert read changed" 2 to 6)
- 2026-11-11, lead: every unit plan rule and field is marked "shared" or "math fills". Why: rules and fields that
  were math in disguise (kinds of day, tie and withdrawal, the exit question, the fluency target) needed shared
  wording before other subjects used them. (UNIT-PLAN.md, "What the expert read changed" 7)
- 2026-11-11, Cory: the word caps were raised to 1,250 for a unit plan and a section plan and set at 1,800 for a
  one-section merged document, replacing the 1,000 and 800 of the same morning. Why: the unit 3 and unit 10 files
  of grade 4 math ran over; Cory: "the other files should get their cap raised again to 1250 words" and "1,800
  words is fine". (UNIT-PLAN.md, "Decided, Cory, 2026-11-11, evening" and "Length")
- 2026-11-11, Cory: the curriculum expert settles item-level choices inside the standards' limits (number sizes,
  which pairs, day swaps inside a unit) and lists them under "Settled by the expert"; the caller copies them into
  docs/reviews/DIGEST.md weekly for Cory to reverse if he wants. Why: to cut the number of small questions Cory is
  asked. (EXPERT.md, "What it settles, and what goes to Cory")
- 2026-11-12, Cory: the teacher reader (Cory's mom) looked briefly at unit 11 and found no hard issues on the
  surface; Cory judged that enough to build on and lifted the planning freeze, with a full teacher read still owed.
  Why: the brief read showed no hard issues, so the freeze set by the strategic review no longer needed to hold
  (later replaced by the 2026-11-13 build order, where the expert agent reads in the teacher's place). (HANDOFF,
  "Old next action", renames entry)
- 2026-11-12, lead: the 900-word cap on teacher prose was kept after day 90. Why: day 90's first draft ran 1,074
  words and was cut to 880 without losing a part; the two worked examples take about 200. (LESSON-DAY.md, "What day
  90 showed" 2)
- 2026-11-12, lead: a tool's own notes and exit items are rows in items.csv, like every other question. Why: day
  90's five family notes lived only in the tool's spec, so the no-reuse gate could not see them. (LESSON-DAY.md,
  "What day 90 showed" 4)
- 2026-11-12, lead: day 90's Plot notes table on the student page shows only the family and the numbers given; the
  full note stays in the tool and the key. Why: writing boxes for the fixes and "On your own" had pushed the page to
  four sides, and the family and numbers are all a student needs to solve it. (LESSON-DAY.md, "What day 90 showed"
  8)
- 2026-11-12, lead: lesson-day draft 2 made the expert's seven "before the yes" changes, among them pictures on the
  display, the tool's exit in data, the leans_on header with "not ready", questions counted in the student reading
  cap, and a new exit answer for day 90. Why: the cold read found the display carried no pictures, the tool's exit
  was outside the data (one item tested nothing on the day's goal), a day could look ready while leaning on missing
  pieces, the student count left out the questions (98 words became 247), and the exit's answer was 9, the same as
  the worked example's. (LESSON-DAY.md, header and "What day 90 showed" 7)
- 2026-11-13, Cory: every layer (progressions, frames, scopes and sequences) is written blind, then reconciled with
  the earlier Curio Class work: writers may not open earlier planning for the subject, a separate reconcile step
  compares the blind result with that work and settles each difference by a named source with the pull measured, and
  a read is done without the earlier course pages and reviews. Cory: "write blind, then reconcile". The reconcile
  settles and logs every difference itself and sends Cory only a difference that changes which grade or course
  teaches a standard, or what a grade teaches, when no source settles it, or a pull measure that shows the old work
  steering. Cory: "let the process do the work and save only the big stuff that really needs my attention for the
  desk". Why: so the layer is decided by the standards and the evidence, not by what happened to be written first or
  what days were already built on; good earlier work comes back in on evidence; Cory's attention is kept for the
  questions that need it. (PRODUCTION-PATH.md step 1; progression-write, progression-reconcile, frame-reconcile and
  sequence-reconcile briefs, intros; EXPERT.md, "Before it judges anything", step 3)
- 2026-11-13, Cory: BASELINE rule 25 ("prove at the bottom before planning wider") is replaced by the top-down build
  order. Why, in Cory's reasoning in chat: well-made units in a sound progression leave fewer problems below, and
  fixing back up the chain is a cost that cannot be avoided anyway. (PRODUCTION-PATH.md draft 5, section 1, item 1)
- 2026-11-13, Cory: all pre-work is finished before step 1 starts; in Cory's words it "should be a solved issue
  before the plan gets started". Why: the plan should not start on an unsettled standard, base-text question or
  reviewer. (PRODUCTION-PATH.md draft 5, section 3, Pre-work)
- 2026-11-13, lead: social studies goes first and math last. Why: social studies had nothing planned, so the process
  is learned without bending old work into it; math holds the most old work (grade 4 scope, unit plans, 48 written
  days) and gets every lesson learned before converting it. (PRODUCTION-PATH.md draft 5, section 1, item 3)
- 2026-11-13, lead: the pilots are retired; a new course instead runs a probe (a few days written from finished unit
  plans and read the full way) and every subject runs a guard before full writing (docs/pipeline/PROBE-GUARD.md).
  Why: Cory's build order of 2026-11-13 put the probe and the guard in the pilots' place. (docs/pipeline/README.md,
  "Beyond math")
- 2026-11-13, lead: the probe and guard measures (P4) are set before any plan is written, as the lead's addition
  agreed in chat as part of the probe. Why: "on" and "off" must be defined beforehand so the result cannot be read to
  fit. (PRODUCTION-PATH.md draft 5, section 3, P4)
- 2026-11-13, lead: the unit 4 test (days 25 to 28 on IM against unit 2 days 7 to 9) is read as "at least as
  clean", not "cleaner", and base texts stay for quality where a subject has one. Why: residual problems were 12
  against 13 with none in source-adapted parts and the writer only 3.6% over unit 2, but the fix passes ran under
  different briefs and the units differ; two experts named something the source offered that the day did not carry,
  so the gain is real but not automatic. (PRODUCTION-PATH.md draft 5, sections 1 and 2)
- 2026-11-13, lead: planning well is expected to prevent up to about 9 of unit 4's 26 expert-only problems (the
  cross-day and stale-plan kinds), not the 11 in the day itself, and the probe and guard measure whether that holds.
  Why: the reclassified table found 7 cross-day, 2 stale-plan, 6 builder and 11 day-level problems, and the
  plan-time read of unit 4 caught 11 cross-day problems, 9 in the 10 planned days, before writing.
  (PRODUCTION-PATH.md draft 5, sections 1 and 2)
- 2026-11-13, Cory: credits stay light: a day adapted from a base text carries one short credit, once in the foot and
  once under Credit, and the source's name appears nowhere else. Why: light licence rigor with few tokens spent on
  it, and minimal and clean on the live site. (LESSON-DAY.md, rule 4; sensitivity-read.md, "1. Study first")
- 2026-11-13, Cory: stale notes are to be expected often and caught well: a note that waits on other work starts
  `Pending(...)`, scripts/stale.py fails a marker whose work has landed, read briefs check for stale notes the script
  cannot see, and write and fix briefs resolve the markers their work lands. Why: Cory, "expect them often, be good
  at catching them". (HANDOFF, 2026-11-13 block, "Stale notes")
- 2026-11-13, lead: the expert reads an exit, item or practice set that could pass or fail as a busy writer and a
  student would, not at its best, and reports the fault if the likely reading fails. Why: in calibration run 1 both
  readers passed real faults on the benefit of the doubt. (EXPERT.md, "Rules it keeps")
- 2026-11-14, Cory: the ELA, science and math course frames (all 37) go ahead as planned: "plan is good, please do
  it". Why: the plan to write them blind with the 15 social studies lessons in frame-write.md was accepted as shown.
  (HANDOFF, 2026-11-14 block, course frames)
- 2026-11-14, lead: frame-write.md carries a numbered lessons list (1 to 16), and scripts/frame.py gates lessons 1,
  2, 3, 4, 12 and 14 with the frame's section and id checks. Why: the expert and Codex reads of the 15 social studies
  frames found the same faults course after course (docs/reviews/frame-*-fixes-2026-11-13.md); the gating came with
  the baseline 1 structure fixes. (frame-write.md, Lessons section)
- 2026-11-14, Cory: the pause is lifted for social studies, and all 15 of its scopes and sequences run together,
  then review, unit plans, units review and the probe, to baseline 2: "Social studies is overall our test bed. Let's
  go ahead and do the whole scope and sequence section together and follow the chart on the dashboard". Why: social
  studies is the test bed subject, so its whole scope step is run at once, following the Dashboard's plan flow.
  (HANDOFF, 2026-11-14 block, "Pause lifted for social studies")
- 2026-11-14, Cory: scopes are unpaused for science, ELA and math; Codex writes all 37 remaining scopes and
  sequences in one unattended run (scripts/codex_scopes.py: write blind, gate, a scope reconcile for math grade 4,
  ELA grade 6 and science grade 4, then a Codex first read), while units keep the order subject by subject with math
  last. Why: the math pause was about older work, which writing blind and then reconciling already handles.
  (HANDOFF, 2026-11-14 block, "Scopes unpaused"; PRODUCTION-PATH.md draft 5, step 5)
- 2026-11-14, lead: step 3 gets its own brief, file and day kinds (sequence-write.md: scope-and-sequence.md,
  days.csv, the five kinds). Why: baseline 1 structure finding 2 found step 3 had no brief, no file and no day kinds,
  and step 4's brief and template were grade 4 math only. (sequence-write.md, opening paragraph)
- 2026-11-14, lead: Cory's call on a scope and sequence is at the baseline, not a yes per course, as run for social
  studies. This supersedes the 2026-11-11 rule that the grade 4 science and grade 6 ELA pilot drafts wait for Cory's
  final yes: Cory retired those pilots and their open questions with the build order on 2026-11-13, and the new
  science-grade-4 and english-language-arts-grade-6 scopes replace the drafts. Why: the expert and Codex reads plus
  one fix pass carry each course, and Cory decides go or no-go at the baseline. (PRODUCTION-PATH.md draft 5, step 3)
- 2026-11-14, lead: count readiness and retrieval by grade number, and this wins over a frame's wording: a row last
  used in grade g gets retrieval in grade g+1 and a readiness check in grade g+2 or later; a row counts as used only
  where a day teaches or assesses it. Why: nine science reads found three readings of "idle two or more grades".
  (sequence-write.md rule 2, "Count by grade number")
- 2026-11-14, lead: the expert reads of the first social studies unit plans settled standing rules for every Codex
  unit plan (two-part kindergarten to grade 2 exits with a rotating spoken group, observation only after teaching,
  official-source checks of holiday, symbol, civic and current-event facts, evidence spread across days, varied Native
  nations, a sensitivity study list naming every frame source, assessments counted against real minutes, exit
  tickets of one question, UTF-8 with LF, days.csv day numbers, no pipeline notes, measured population figures,
  general form first, no campaign sources, exact citations, dated background lines for 2025 and 2026 events, bounded
  reteach stations, withheld sources kept off teaching days, no identity labels without a source), and the six that
  fit every subject (UTF-8 with LF, exit tickets, assessment minutes, days.csv day numbers, no pipeline notes, dated
  background lines) were copied into the math, science and ELA Codex briefs. Why: the reads found these faults in the
  social studies plans and the same faults would recur in every subject. (plan-codex.md, "Settled by the expert
  reads"; plan-codex-math.md, plan-codex-science.md, plan-codex-ela.md, "Settled by the social studies plan reads")
- 2026-11-14, lead, superseding the last sentence of item 1 and the "day 1 of every unit stays clean" part of item 2
  in "2026-11-14: readiness check timing, every course" above: where unit 1 has readiness rows, its readiness check
  (the start-of-year check) takes the last ten minutes of course day 1, after the hook and the compelling question;
  days.csv marks day 1 `assess` = `readiness` (sequence.py accepts it) and the reteach sits in day 2 or 3 inside
  existing time; where unit 1 has none, the plan says "Start-of-year check: none needed; retrieval only". Day 1 of
  every other unit stays clean. Why: unit 1 has no previous unit or respond day, and no sitting comes before day 1,
  so the end of day 1 is the earliest point that still leaves day 1 its hook. (sequence-write.md rule 2, "When";
  sequence-read.md; GLOSSARY.md, readiness check; UNIT-PLAN.md, field 4; plan-codex briefs, "Settled")
- 2026-11-15, lead: one hop counts as use: a day that teaches a row whose progression `assumes` names an earlier row
  uses that earlier row too; a retrieval or readiness day counts this way only where its kind is Understanding or
  Application; the skeleton and the scope gate count it this way. Why: such a day builds directly on the earlier row.
  (sequence-write.md rule 2, "Count by grade number")
- 2026-11-15, lead: the rows a readiness check samples for the next unit are named by id in that day's note, never in
  its `skills` column. Why: the unit skeleton reads an earlier-grade id in `skills` as a row of the day's own unit.
  (sequence-write.md rule 2)
- 2026-11-15, lead: collect once: evidence gathered child by child is taken once per assessment window; a check or
  end day within ten days reuses that record, and a course-level check never repeats a task form given in the last
  two weeks. Why: the same fault was found in all six ELA K to 5 courses. (sequence-write.md rule 2, "Collect once")
- 2026-11-15, lead: every goal, note and source-map cell is written fresh in Curio Class words, never copying or
  lightly editing a base text's lesson purpose, goal, title sentence or teacher note, even where the licence allows
  it. Why: math grade 1 copied 140 base lesson purposes. (sequence-write.md rule 2, "Our words")
- 2026-11-15, lead: a lean on a math row in another subject opens with retrieval by default; it gets a readiness
  check only where a performance expectation rests on it and no math course uses the row after its grade, and
  same-year order decides which subject retrieves and which checks. Why: students take math every year.
  (sequence-write.md rule 2, "Math leans in other subjects")
- 2026-11-15, lead: one source-map.csv layout in every subject (`source,title,goals,standards,unit,days,decision,
  why,order_conflict,harms_learning`, then `url`), gated by sequence.py. Why: the scope reads found a different
  layout in each map. (sequence-write.md rule 8)
- 2026-11-15, lead: every scope and sequence has a "Shorter path" section whose fold-in days each name the minutes
  they save, with the total stated against the frame's day count, one rule for every subject. Why: FOUNDATION
  section 5 and adoption bar C2 ask for a shorter-period path. (sequence-write.md rule 10)
- 2026-11-15, lead: every elective and later subject passes the four-point "Before a new subject's scopes" checklist
  (gated layouts, one pilot course then a frozen brief, rule 2 count in the scope gate, unit skeleton on the pilot
  first) before Codex writes its first scope. Why: in the science, ELA and math round the skeleton run found 21
  source maps in 21 layouts and readiness gaps the reads had missed. (PRODUCTION-PATH.md, After the core subjects)
- Open, found by the flattening: "2026-11-12: course level names" item 2 says 18 sub-ready days a year in grade 4
  math, while GLOSSARY.md says one per unit (9 a year in grade 4 math). The rule (one per unit) is the same; the count
  is checked when the grade 4 math units are written (later.csv L42).

## 2026-11-15: science, ELA and math units move forward together (Cory, in chat)

Cory: "the plan is to have all the units for all three subjects move forward together. now that we have
reconciliation tactics, math doesn't need to wait." After social studies' probe and baseline 2, step 5 runs the unit
cycle for science, ELA and math at the same time; math's unit plans are written blind and then reconciled with grade
4's old work (later.csv L13). This replaces "math last" for units (PRODUCTION-PATH section 1 item 3 and step 5, the
2026-11-13 lead line above); the scopes already ran together (2026-11-14). Why: the math pause was about older work,
which writing blind and then reconciling handles. Applied: PRODUCTION-PATH.md, HANDOFF.md, later.csv L13 and L25.

Same message: "split out the other items so we dont lose them and go ahead and take care of any that can be done
now." The non-math items in L13 became L43 to L48; the overlap tags fix and the PECAT address check were done the
same day.

## 2026-11-15: the four untracked files (Cory, in chat: "go with all your recommendations")

The US Curriculum Design Blueprint moved to S:\CurioClass-sources\us-curriculum-design-blueprint.pdf (ADOPTION-BAR.md
points there); docs/Curio-Class-Plan.pdf and docs/agents/audit/wordwall-movement-cards.jpg moved to
S:\CurioClass-archive\untracked-docs-2026-11-15; docs/Return/ stays as Cory's private folder and is now git-ignored
whole. AGENTS.md's never-touch list updated to match. Why: the repository is public, the Blueprint is a reference
source, the plan PDF is replaced by VISION, ROADMAP and PRODUCTION-PATH, the image was a one-time art check, and
docs/Return/ holds private drafts (Sara's language-partner draft is marked not public).

## 2026-11-15: ELA questions live in items.csv (lead, later.csv L47; Cory: "do L47")

The question set of card q-ela-piece-2 is stored as rows of each course's shared items.csv, not a separate
questions.csv, with three ELA columns: text_id, text_ref and needs_text. plan.py check gates them, including the
80 percent text-dependent rule of plan-codex-ela.md. Why: one file means every existing item gate (keys, no reuse,
exits, assessment minutes, the day pages) works for ELA without a second set of checks, and the 80 percent rule
becomes a count instead of a reader's estimate. Applied: UNIT-PLAN.md, data/plans/README.md, APPROACH-ELA.md,
plan-data.md, scripts/plan.py.

## 2026-11-15: the blind rule names courses/math-4/, not all of courses/ (lead; Cory: "go with your judgement on the rule change")

The blind lists in plan-codex-read.md and scripts/codex_scopes.py named all of courses/, which would bar a writer
from the social studies day folders the probe creates. They now name courses/math-4/, the only old written days;
progression-write.md bars a subject's own written days. Why: the rule exists so old work cannot steer the new
layers, and the only old days are grade 4 math's; new days written from the new unit plans are the work itself.
Applied: HANDOFF.md, plan-codex-read.md, codex_scopes.py, progression-write.md.

## 2026-11-15: SEL and library "smaller", and the informed action evidence (Cory: "L43 and L44 can go with your recommendation")

L43: a smaller SEL or library course has fewer minutes a week (one or two sessions, the frame says which), never
fewer units, so every standard is still taught, spaced and checked. L44: once a year stays the default; a second
informed action only where one action cannot teach and check all of the course's C3 informed action indicators, a
third only in civics, never to fill time, and every action keeps a classroom-only version. Why: quality and fairness
first; cutting units would cut standards, and a school with less staff still gets the whole course. Applied:
ADOPTION-BAR-SUBJECTS.md (pass rule, criterion 8, choices 4 and 6); social studies baseline 2 applies L44.

## 2026-11-15: day gates and rules from the social studies probe fix (fixer, US History I days 78 to 82)

Edited in place: LESSON-DAY.md (credit `ours` exactly; error and source letters in words; placeholders fail; a repair never cuts the next day's worked example; hand-backs follow handbacks.csv; revision-note box; no typed Name line), UNIT-PLAN.md rule 6 (social studies repair), DAY-WRITER.md (fixed facts, check 16), CHEAP-READ.md (check 7), data/plans/README.md (`defect --status`). Gates: scripts/lesson.py (placeholder, bare letter, typed Name line, hand-backs and Tomorrow letters read handbacks.csv, error letters to K, grade 9 to 12 source sheets at 11 point), scripts/plan.py (`defect --status`), scripts/day_skeleton.py (credit and Word Wall lines). Why: the expert and cheap reads of days 78 to 82 (docs/reviews/*-2026-11-15.md) traced these to the template.

## 2026-11-15: after the social studies probe (Cory, and the lead's rules)

Cory, in chat: use free sources instead of buying the Quarles, Fields-Black and Green books (park service pages and
the primary texts; a paraphrase we cannot check is cut). Cory: fix the social studies units first, with Codex. Lead,
from the probe (docs/reviews/probe-social-studies-2026-11-15.md): one misconception per register letter (UNIT-PLAN
field 6, all four plan-codex briefs, and a unitplan.py gate); a part scored from earlier work only after written
feedback and a chance to revise, never from the day a topic is first taught (UNIT-PLAN field 5 and the briefs; this
replaces "a part made earlier on a product day comes off the sitting" as a scoring rule, the minutes rule stands);
day exits answered from material not just worked that day. Why: the probe read Off (plan share 60%, units changed
88%), and science, ELA and math units should start with the rules. Applied: docs/pipeline/briefs/unit-correct.md,
the Codex correction pass per social studies course.

## 2026-11-15: the probe's last two questions, and the source rule (Cory: "Yes to both questions")

Cory: run the Native nations sensitivity read for day 79 and error K now, the same way as the u05-2 read; day 79's
map task waits for our own map in the art step (later.csv). Cory approved the order: commit the social studies
corrections, fix US History I unit 5 and the probe days, add the source rule, probe a second section, then science,
ELA and math units together. Lead: sources are verified or none (UNIT-PLAN field 10, the four plan-codex briefs,
plan-data.md step 3; lesson.py already fails a placeholder). Why: the probe's placeholder source sheets changed
facts once checked, and free sources were settled earlier today.

## 2026-11-15: the US-Dakota War and Sand Creek are taught in unit 6.2 (Cory: "Go with unit 6.2")

US History I unit 5 keeps one teacher-background line on day 79 naming both; unit 6.2's day 103 now teaches the
Plains wars from the US-Dakota War (1862) and the Sand Creek Massacre (1864) to Wounded Knee (1890). Why: they sit
beside the treaties and removals of unit 6.2, and unit 5's days are full (Native nations sensitivity read, finding
for Cory). Applied: data/plans/us-history-i/days.csv day 103, s06.md day list, scope-and-sequence.md unit 6 topics.

## 2026-11-15: paid-only texts are described from a free secondary source (Cory: "Stay with free sources")

Cory: stay with free sources; where a text exists only in paid editions, keep it if the information can still be
verified, perhaps through a secondary source. Rule: such a text (a people's own chronicle, epic or inscription) may
be named and described, never quoted, when a free secondary source we have read says what it holds; the day credits
that source and its link goes in sources.csv. Why: the World History I 3.4 sensitivity read found every source on
the sheets is an outsider's, and no free, checkable English text by the peoples themselves. Applied: UNIT-PLAN field
10, plan-data.md step 3; the probe 2 fix pass names the griots, the Tarikh al-Sudan, the Kilwa Chronicle, Ezana's
inscriptions and the Secret History this way.

## 2026-11-16: the later subjects' standards questions (Desk cards q-later-arts-health-pe, q-later-cs-career-library, q-later-sel-eld)

Cory answered all 17 items; the lead's pick stood except where noted. Arts: high school music is composition and
theory, and the way forward for an instrument-centered subject is researched (docs/reviews/arts-hs-music-and-levels-2026-11-16.md);
high school levels follow what a student has done, with an optional fourth year, on the best evidence found (same
review); pacing as picked (K to 8 arts 64 sessions with a 32-session path, high school arts 160 days, high school
health one semester, elementary PE 2 to 3 a week). Health: "no outside readers available. use a self built expert
agent", so a health expert agent's dated read meets criterion 7 and there is no paid read (later.csv L45 done).
Computer science is one course per grade K to 12, and library one per grade K to 5 then one each for middle and high
school (changed from the pick; 120 courses, 118 active). Career education: 2024 national career development
guidelines, own goals as fallback; one-year courses. The UK computing curriculum is a partial base for CS K to 8,
checked unit by unit and "rephrased for an American audience when needed"; the library 6 to 12 partial bases are in.
SEL and ELD as picked; Spanish accessibility across the site is parked for later (ROADMAP item 14, later.csv L60);
Cory requests the WIDA rubric form himself. Why: Cory's answers. Applied: scripts/course_status.py (PER_GRADE),
ADOPTION-BAR-SUBJECTS.md (health criterion 7, SEL part 9, course count), BASELINE rule 24, HANDOFF, ROADMAP, and the
subject STANDARD and APPROACH drafts.

## 2026-11-16: the later subjects' follow-ups (Desk card q-later-followups-1, all as picked)

Computer science meets one session a week in K to 5 (a specials rotation) and two to three a week in 6 to 12 (a
real elective). Library 6 to 8 and 9 to 12 each spread across their grades, about one session every two weeks,
taught alongside other classes. High school music is a full composition and theory course with an ensemble companion
page, not a stub. Why: Cory took the picks. Applied: the computer science, library and arts STANDARD and APPROACH
drafts, and the owed table in ADOPTION-BAR-SUBJECTS.md.

## 2026-11-16: Hamburger Paragraph bear line approved (later.csv L53)

Cory approved the student wording "Burp! All gone. Thank you, chef! Press Build another to make a new burger." for the bear meal moment. Why: Cory's yes in chat. Applied: tools/hamburger-paragraph/spec.md already carries the line; no change needed.

## 2026-11-16: lessons from below the frame go into every frame

Frames for every later subject carry the unit-level lessons of the core courses (day kinds, readiness evidence, scored evidence placed, checks that claim samples, minutes inside the period, named safety guides, sourced facts, depth and devices, tools, texts and costs per unit, side standards, textbook source maps, focus method, code labels, sensitivity by unit, the grade 12 calendar, core-only leans). Why: Cory asked that lessons learned reach the unit level and be kept for the next frames. Applied: docs/pipeline/briefs/frame-write.md lessons 17 to 32 (evidence in docs/reviews/frame-unit-lessons-2026-11-16.md); sequence-write.md points its safety words at the frame's last Units column; the six elective frames.

## 2026-11-16: section boundaries found for every unit before any section plan

Cory: find only the start and end of each section first, by a Sonnet agent per course with judgement calls passed up
to the lead, not by a script alone. Done the same day: 216 units still held as one placeholder section, 1,007
sections, gated by `scripts/section_cuts.py`. ELA scores end-of-unit parts across its closing weeks, so an end check
before later teaching is a note, not a failure. Recorded in PRODUCTION-PATH step 7.

## 2026-11-16: how section plans will be authored (planned, not built)

Cory asked whether Haiku skeletons, a Sonnet rough draft, a Codex final with lens reads and a Claude refine would
work. Settled: the skeleton stays a script; no Sonnet pre-draft. Cost comes down instead from unit-batched Codex
writing, a sliced brief, gates before reads, per-unit reads with patch-only fixes, a stable prompt prefix, and
Claude reading on flags, a sample and a per-unit cohesion pass. Piloted on the first social studies unit before it
becomes standard. Cory picks this up next session; nothing is built yet. Written into PRODUCTION-PATH step 7.

## 2026-11-17: word caps raised to 1,600 and 2,300

Cory: a cap that keeps causing rejections is too tight, so raise it unless there is a valid reason not to. In the
Claude second lens pass 489 of 708 rejected findings cited the cap. A section plan and a unit plan go from 1,250 to
1,600 words, a one-section merged document from 1,800 to 2,300, counted as before. The cap still marks a contract,
not the lesson: edition and rights detail belongs in ela-texts.csv and source-map.csv, not in field 10. Applied:
UNIT-PLAN.md "Length", scripts/unitplan.py, ROADMAP. Science 8 s06 (1,290 words) now passes. The findings rejected
for the cap are picked up in the lead sweep.

## 2026-11-17: six calls from the lens pass (Desk card q-lens-pass-1)

Cory answered six calls; applied the same day (report: docs/reviews/desk-answers-lens-pass-2026-11-17.md).
US History I unit 8: students choose one listed women's organization; the 1869 National Woman Suffrage Association
is the teacher's worked example. Social studies grade 3 unit 2: the Menominee Indian Tribe of Wisconsin stays on day
43 for the constitution comparison only; the 24-month news check runs before days are written. Science grade 1 unit
1: stars present but hidden by day stays, weighted lightly (never costs a core point), sourced to a NASA page. ELA
grade 11: Occom's 1768 Narrative (first printed 1982) gives way on day 109 to two excerpts of his Moses Paul sermon,
1788 printing, bounds checked on the scan; the day 14 cold story is Poe's The Oval Portrait, with Chopin kept for
day 139; Jacobs chapter I is kept for day 93 (no better period text found) and the scope and sequence now agrees; the
frame's slur note covers Narrative chapters 4, 6, 9 and 10.

## 2026-11-17: the six core elective frames (Desk card q-electives-frames-1, ten calls)

Cory answered the frames' For the lead questions for Precalculus, Statistics, Calculus, Earth and Space Science,
Environmental Science and Psychology. Precalculus then Calculus on the accelerated path (L15), Precalculus the stated
prerequisite, straight from Algebra II a named alternative with a bridge of about 20 lessons. L49 done: an owned-outcome
account for focus 1a to 1c and one 15 percent cap of unit minutes for review and readiness, in RUBRIC-MATH-HS.md.
Earth and Space Science typical grade 12, open to grades 10 to 12 after (or alongside) Biology, Chemistry and Physics
(judgement left to the lead, so advanced students can reach it). Base texts loaded into the source store. Environmental
Science unit 5 keeps the Navajo Nation case on released material only, no contact, a fresh sensitivity read first (L68).
Cost ceilings for a class of 30: about $400 Precalculus and Calculus, $450 Statistics, $1,000 each science with shared
kit, a cheaper route for any unit over $150. Same-grade seams stay in prose; the gate change is L67. The widened
science outcomes stay. Calculus extensions stay extensions, first cut on the accelerated route. Psychology unit 15 is
required. Statistics reads take a data-teaching lens (docs/agents/lenses/statistics.md, GAISE in our own words).
Record: docs/reviews/desk-answers-electives-frames-2026-11-17.md.

## 2026-11-17: day kinds, the Fluency mislabel fixed where calendars are made (later.csv L64)

Cory (2026-11-16, "do not forget") asked that the Fluency mislabel the unit lenses kept finding be fixed at the
source, not one day at a time; the lead set the rule. A Fluency day only practises what earlier days taught; first
teaching of anything new is Understanding; drafting, revising or editing a piece of writing is Application; where a
day does both, first teaching wins. One home: docs/GLOSSARY.md, row "teaching day"; sequence-write.md and frame-write.md
lesson 17 point to it, and scripts/sequence.py fails a Fluency goal that drafts, edits, introduces or teaches (notes for
the rest). Where a unit plan had already moved the first teaching to an earlier day, the day stays Fluency.
Record: docs/reviews/fluency-sweep-2026-11-17.md.

## 2026-11-17: The Front Office and Show Your Work (live as a draft)

Cory asked for the Desk dashboard reimagined as a public page that lets anyone from a state department of education
down to a teacher see the whole curriculum, from progressions to days, plus a methodology page. Names chosen: "The
Front Office" (/front-office/) and "Show Your Work" (/front-office/show-your-work/). The methodology does not say who
did the work: no mention of AI, and nothing that says it was human made. Review reports are cleaned before posting,
and the base texts are cited there properly. The print-and-offline rule bends for these pages, since they are for
administration and background policy. The page count stays flat: six files, with every layer opening in a reader
drawer. Live 2026-11-17 as an unlinked noindex draft; Cory: "the site looks great". More buttons and functionality
come in later drafts (later.csv L70). Rules: docs/SITE-DESIGN.md, section "The Front Office".

## 2026-11-18: Kindergarten probe (q-probe-ss-3)

Cory took both picks. (1) docs/courses/social-studies-kindergarten/u01-1.md is signed off as the example section plan
the next writers copy; comments on it become a fix before more section plans are written. (2) The probe read Off, so
the early grades get K to 2 rules (a rotating six with a record column, minutes counted as whole-class turns, one
actor per story scene, spoken stems), then a correction pass over the 19 kindergarten to grade 2 social studies units,
then a fourth probe, before more early-grade days (later.csv L74). Baseline 2 goes ahead with
docs/reviews/probe-social-studies-3-2026-11-18.md as social studies' probe result.

## 2026-11-18: Science and math probe, the shortest path to ready skeletons (q-probe-sci-math-1)

Cory took the pick in chat: work to ready skeletons by the shortest path. The fourth probe (science grade 5 and Algebra
II, docs/reviews/probe-science-math-2026-11-18.md) showed the skeletons run unchanged in three subjects and bands, while
the plans they run on carry the same running faults in every probe. In order: one gate and skeleton session (later.csv
L75), rules and per-band DEFAULTS with small unit edits and the K to 2 pass (L76 with L74), then one confirm probe with
an ELA section and a middle-school section (L78). Scale when plan share is 35% or under.

## 2026-11-18: The confirm probe and the grade ladder (q-probe-confirm-1, q-dirty-fill-1)

Cory set aside the choice between one more probe and a first wave and asked instead for a dirty fill from the
beginning to the end of each course, then two full refines. Cory then refined the order: one subject at a time, from
kindergarten day 1 to the end of each grade, then the next grade up, because continuity is the main issue and
formatting is fixed in review. Cory took option (a) of docs/reviews/assessment-dirty-fill-2026-11-18.md: science,
with a subject ledger (scripts/ledger.py) carried up the grades, and refine 1 trailing one grade behind the fill.

The test is science kindergarten to grade 3, initial dirty pass only:
- the ledger first;
- section plans for K, 1, 2 and 3 in order;
- then plan data and days for K, 1, 2 and 3 in order;
- then a read-only sample of about 10 days a grade, which finds faults and fixes none.

Because of capacity, the run pauses after each grade of section plans and each grade of days. Cory continues it by
hand. later.csv L81.

## 2026-11-19: After the science ladder test (q-ladder-science-1)

Cory, in chat, on the report docs/reviews/ladder-science-report-2026-11-19.md: fix all that can be fixed now, both
what the test found and what it showed outside its own days, then pause. So the gate and template points, the new
cheap gates and the answer-key check go into the scripts and briefs, the faults the 40-day sample found go into the
kindergarten to grade 3 days, and the work stops there for Cory's next call. Refine 1 and the climb past grade 3 wait.

## 2026-11-19: The Front Office reads every document, and is linked

Cory, in chat: link The Front Office from the site so it can be reached naturally, and make every document readable
there, nicely formatted; "the intent is for someone to be able to read from the progressions and course frames all
the way to the days." So the drawer now opens the full skill ladder, each frame, scope and sequence, unit plan,
section plan and written day, cleaned of internal words first, and the footer links the page. It stays a draft
(banner, noindex). docs/SITE-DESIGN.md, section "The Front Office"; later.csv L70.

Same day, Cory: the Front Office documents move to the R2 bucket, so they add nothing to the static-asset file count
as the curriculum grows. The page and its addresses are unchanged. docs/SITE-DESIGN.md, section "The Front Office".

## 2026-11-20: Pre-work for arts, health, PE and computer science (q-prework-arts-1, q-prework-health-pe-1, q-prework-health-pe-2, q-prework-cs-1)

Cory answered the four pre-work cards on the Desk.

Arts: write our own one-line words file for the 1,114 taught performance standards now, in the public repository
(at most 14 words of what the student does, never a re-sentence of the standards' phrasing; the standards' terms
allow paraphrase with citation). Each high school level gets an 80-day short path (a bridge unit of at most 12 days
in Level 1, a review unit of at most 6 days in Levels 2 and 3). Each course page says which units a school or family
may leave out, since each such unit stands alone. The approach page is approved with the cold read's fixes in.
docs/courses/arts/STANDARD.md sections 2, 3.2 and 5.

Health and PE: the PE course says openly that 2 to 3 sessions a week is below the recommended weekly minutes and
offers short active breaks and home activity. Correct body part names are taught in the kindergarten personal health
row, with any reference to sensitive areas kept very minimal and a fresh sensitivity read first. If the high school
health semester cannot hold its outcomes, review gives first (outcomes met in 6 to 8 become short reviews inside other
units); only then does a list come to Cory. Grade 9 health keeps its pace, with the goal rows as one weekly thread and
short units of two to four days. The 9 to 12 map cell lists what the semester really carries. Health 6 to 8 gains a
grade 7 row on riding, safety gear and dangerous places. Physical activity outcomes 3, 4 and 6 in grades 6 to 8 go
to PE. High school PE is two required years (grades 9 and 10, with the personal plan in short form in grade 10) and
two elective years that deepen it. Water safety is dry-land tasks for every school, in-water tasks only in a school's
own program with a lifeguard. Sacred or ceremonial dances and games are never used as a game or warm-up, and only
when the source says they are open to be taught. PE kindergarten tries rope and dribbling and marks growth; grades 2
and 1 own them. Left open: the health and PE approach pages' yes (asked again on a new Desk card).

Computer science: grades 11 and 12 claim a short named list of Specialty level 1 standards, with no new courses and
level 2 left out. No live generated-text tool: the teacher runs that day on one screen with a tool the school already
approves, and the standard is part met where a school has none. Society units name government bodies and courts,
never companies, with sources only in the teacher's source line. HS-DAT-IM-27 moves to grade 11 (grade 12 owns 10).
The careers row stays in computer science. The approach page is approved with the cold read's fixes in. Left open:
our own coding editor (asked again on a new Desk card).

## 2026-11-21: After-core pre-work calls (q-prework-open-1, q-prework-open-2)

Health and PE: both approach pages are approved. The kindergarten body-names row names penis, vulva, breasts and
bottom; the family note lists them first, words only, with preview and a quiet opt-out of that one part; a person
reads the row and the note before publishing (later.csv L89). Health keeps its default times; the course page names
the national figure (NHES 2007, 40 and 80 hours a year) and the gap.

Computer science: build one small coding editor of our own (blocks and text view, step-through), starting with
grades 3 to 5.

SEL: the ownership form was given a pedagogical check, as Cory asked, and used because it held with two fixes
(docs/reviews/sel-ownership-check-2026-11-21.md): 160 owned rows at each band's last grade, every year a full row,
`assumes` naming the year before, leans naming the grade row they need. SA3, SA4, SA7 and SA9 are checked on an
invented case or a private plan, never on the student's own feelings. Four band rows replace sel-k12 in the
catalogue (later.csv L90). A school may leave out a unit, with the ids named. Grade 10 unit 4 is retitled "Saying no,
setting limits". The approach page is approved.

Arts: a school may leave out a unit that studies a sacred or ceremonial tradition, one line on each course page.

Calibration: the per-subject pass line in docs/pipeline/CALIBRATION.md is approved (at least 8 of 10 planted majors
caught, at most 2 false major alarms, the top finding a planted major).

Library: library-6-8 stays one course. Each AASL id is owned once, where first checked alone. Seven ids are excluded
and left to other subjects. The own-words file is short glosses, with no permission request. No real site is named.
Default times kept. The approach page is approved.

ELD: 13 grade frames under four band courses (catalogue rows later.csv L90). Minutes kept, with the course page saying
it is the protected core. Home-language notes: Spanish first, others when a reader is found. A sensitivity read before
use on the newcomer strand, migration, war and loss texts and the family notes. The approach page is approved.

Career education: owns the 7 Career Development and Academic and Lifelong Learning goals, the SEL goals are leans; the
guidelines PDF is saved (ids follow a terms read, later.csv L91). Pathways goes broad: all 14 clusters, any sub-cluster
open through its cluster (Cory: more opportunity for kids, even if harder to keep current). Exploration owns 14
sub-clusters, and Pathways owns the other 58, so none is excluded. The personal finance and economics modules retag to
Economics (L90). The military is one honest route, no recruiter material on a student page. The approach page is
approved.

World languages (still shelved; these settle pre-work pages only): four levels plus an early-years companion
(Option D); French may be added, listed behind Spanish and ASL; each language its own progression; World-Readiness
plus our ASL parameters strand; 3 sessions of 35 minutes; a heritage path inside each Spanish level; can-do
paraphrase only, with a note Cory sends (L92); Spanish base text yes, ASL research redone; the approach page approved
as pre-work. Left open: who reads ASL pages (L93).

## 2026-11-21: Calibration of the after-core subjects (q-calibration-subjects-1)

Career run 2 passes: its top finding was a real major the lead confirmed, not a planted one. The calibration line
now reads "the top finding is a planted major, or a real major the lead confirms" (docs/pipeline/CALIBRATION.md).
The seven expert passes from run 1 stand after the brief change, since the change only adds checks. (Cory picked
the card's earlier wording, which had Codex rereading every set; Gemini 4 Neon read the latest set for all nine
subjects with the new brief and passed in each, docs/reviews/calibration-<subject>-gemini-2026-11-20.md.)

## 2026-11-21: Health catalogue split (q-fix-health-1)

Health becomes four band courses in data/courses.csv: health-k-2, health-3-5, health-6-8 and health-9-12 (one
semester, typically grade 9), as SEL and ELD were split. Module ids and worksheet unit ids are kept (later.csv L90).

## 2026-11-21: PE fix pass calls (q-fix-pe-1)

Cory took all four recommended picks. (1) PE becomes four band courses in data/courses.csv: pe-k-2, pe-3-5, pe-6-8
and pe-9-12 (grades 9 and 10 required, 11 and 12 electives), as health, SEL and ELD were split; module ids and
worksheet unit ids are kept, and the 6 to 12 peer coaching module gets a 9 to 12 twin. (2) A school or family may
swap or leave out a named PE unit or activity, and the course page then claims no standard no remaining unit teaches
(PE STANDARD.md 5). (3) PE teacher pages carry health's disclosure steps, changing follows school policy with no one
changing in front of others, and PE hazard units get a safety read (PE APPROACH.md, "Sensitive ground";
docs/FOUNDATION.md section 7). (4) Dose defaults, ours and untested: K to 2 80 x 30 minutes, 3 to 5 80 x 35, 6 to 8
96 x 45, 9 to 12 80 x 45 per year taken, short paths 60 to 64; a frame may change them with a reason (PE APPROACH.md,
"Pacing").

## 2026-11-21: Arts fix pass calls (q-fix-arts-1)

Cory took all six recommended picks. (1) The 63 high school music composition and theory ids load now, with own-words
lines and music 9 to 12 progression rows. (2) The Level 1 bridge unit teaches grade 8 techniques and words as
readiness, claims no grade 8 id, and is 6 days on the 80-day short path. (3) Leave-out follows SEL and PE: swapping a
work keeps the ids met; a left-out unit's ids are named as not claimed that year on the course page and in the
family note. (4) The five K to 12 arts rows in data/courses.csv become 20 band rows (visual-arts-k-2 to
media-arts-9-12), none core; module ids and worksheet unit ids are kept. (5) High school lessons are 45 minutes; each
course page names its national association's recommended weekly time, once read at source, and our gap. (6) No arts
task asks about a student's own diet, weight or body; every personal-tie task has an invented or public option;
sections carry health's steps for when a student tells you something (arts APPROACH.md).

## 2026-11-21: Computer science fix pass calls (q-fix-cs-1)

Cory took all four recommended picks. (1) Default doses, ours and untested: K to 2 32 sessions of 30 minutes, 3 to 5
32 of 40, 6 to 12 64 of 45; a frame may change them with a reason. (2) Leave-out follows PE and arts. (3) The text
language for grades 6 to 12 is Python, in Curio Class's own browser editor. (4) One cs-k12 catalogue row stays, its
notes corrected to the 2026 standards.

## 2026-11-21: SEL fix pass calls (q-fix-sel-1)

Cory took both recommended picks. (1) SEL keeps 64 sessions a year and the 32-session short path; related sub-skills
are grouped so every session rehearses, and the short path keeps all six units with fewer sessions each. (2) SEL
family notes name a left-out unit's ids, as arts does.

## 2026-11-21: Library fix pass calls (q-fix-library-1)

(1) Cory: ids that belong to other subjects must reach the subject they belong to and not be dropped; this is part of
cross-curricular work. Each of the seven library ids is checked at source and either kept in library or placed in the
receiving subject's pages. (2) The library row in data/courses.csv becomes eight rows (library-k, library-1 to
library-5, library-6-8, library-9-12). (3) Leave-out follows SEL, PE and arts, and K to 5 case sets stay neutral. (4)
Yes to downloading and reading the national school library standards PDF and the continuum band files.

## 2026-11-21: ELD fix pass calls (q-fix-eld-1)

Cory took all four recommended picks. (1) The 20-day newcomer strand is an on-ramp beside each grade frame; the frame
keeps its 160 days. (2) ELD follows the shared leave-out and swap rule, and a unit whose host text is about
migration, war or loss previews it in the family note with how to ask for the other text. (3) Bar item 5 (part 10)
names English learners with disabilities. (4) A planning-only own-words file for all 104 WIDA ids.

## 2026-11-21: Career education fix pass calls (q-fix-career-1)

Cory took all five recommended picks. (1) A sensitive sub-cluster unit may be left out, with a same-cluster swap and
its ids named as not claimed. (2) Flagged sections and the pay-gap unit point to health's disclosure steps. (3) The
family work question gets invented, public and trusted-adult options. (4) Guideline indicators are owned where first
taught, carried in Pathways, and adult-only ones left out with a reason. (5) Typical grades: cte-explore 8,
cte-pathways 10.

## 2026-11-21: Pre-work sources that are only files (q-fix-downloads-1)

Cory took both recommended picks. (1) Yes to downloading and reading the music composition and theory strand, the arts
associations' opportunity-to-learn files and the 2026 CSTA standards PDF, kept outside the repository, ids, figures and
structure only. (2) The arts bridge unit is at most 12 days on the full 160-day year (6 on the short path).

## 2026-11-21: Computer science calls from the standards PDF (q-fix-cs-2)

Cory took all three recommended picks. (1) The boundary statements' text is not stored; the depth stays in our own
words in each owner row's notes. (2) Our own editor gets an offline version history with branch, review and merge;
S1-SWD-PP-08 is part met until it exists. (3) Lists stay in grades 7 and 8, counted as days outside the standards
under C1's 10 percent.

## 2026-11-21: Health calls from a fresh minor read (q-fix-health-2)

Cory took both recommended picks. (1) From grade 7 a student may choose their own healthy behavior as a goal, never
about weight, calories or shape (health APPROACH.md, Supports). (2) Curio Class uses US spelling; UK spellings are fixed
in a page when it is next edited, no separate pass (AGENTS.md). The health pages were converted on 2026-11-21.

## 2026-11-21: Ledger-gated scheduling for course runs (from the social studies and ELA ladder run)

Cory chose option 3 on 2026-11-20: a day job in grade N starts only when every ledger entry it cites from a lower grade is at stage
written, never only planned. Cory accepts the slower run in return for fewer tokens, fewer rewrites and better quality. It is built at
L87, not during the run. The run's capstone pass supports it: 7 of 257 social studies claims and 29 of 302 ELA claims had drifted when
checked against what the lower grade really wrote (docs/reviews/ladder-ss-ela-report-2026-11-19.md).

## 2026-11-21: Fix the social studies and ELA sample findings now (q-ladder-ss-ela-1)

Cory took the recommended pick: fix the 95 sampled FIRM faults now, as with science, with one fresh fix agent per course,
plus the L99 must-fix items (the ELA grade 1 tale sensitivity read, the key-line pieces, the Maathai line). L87 follows.

## 2026-11-20: The course run process, course shape, dose and lanes (logged 2026-11-22 at L87)

Cory, 2026-11-20, after the ELA and social studies K to 3 run: testing is done, and every subject now follows
docs/COURSE-RUN.md (stages 1 to 7, each with make, check, fix, retool and gate; the kit frozen within a stage, or
within a grade in stages 5 and 6). Cory asked for the most sound teaching answer on course shape and dose, and for the
serial stage flow with checks, fixes and retooling at every stage.

- **Course shape:** K to 8 is one course per grade (band standards split across grades); high school electives by
  level; ELD by WIDA cluster. Earlier settled calls stand (computer science one course per grade; library 6 to 8 one
  course, 2026-11-21).
- **Dose:** plan to the national body's recommendation with a cited source. Where schools' schedules fall short, say so
  openly on the course page; with no national figure, use the common school schedule. Short, frequent sessions are
  preferred. The health and PE pages cite their national figures (APPROACH.md, Pacing).
- **Lanes:** the next run has two writing lanes side by side: math K to 3, and social studies grades 4 and 5 with World
  Geography I. Each subject's first grade runs a unit 1 probe (COURSE-RUN stage 5).
- **Math files open:** the math blind rule (courses/math-4/ and the math spines) is lifted for future course-run work;
  a math run reads the old grade 4 work and reconciles with it. Job lists made before 2026-11-20 keep their old notes.
- **Ledger gating** (2026-11-21, above) and the kit, generator and gates built at L87 serve this process.

## 2026-11-21: Infinite Hike hosted on the Recess shelf

Cory asked the maker of Infinite Hike (xmetal) on Reddit if Curio Class could feature it; the maker said yes and asked for no
citation beyond a small, unlinked "Originally written by xmetal". Recess now allows hosted games shared with written permission;
the rule and the permission record are in docs/GAMES.md (Hosted games).

## 2026-11-22: Source pages agents cannot open go to a browser check

Cory, in chat: a standing rule. A source page that refuses automated reads (a 403 or bot wall, as Britannica, the UN,
Kew, USGS, Cornell and the Smithsonian often do) is no longer cut on sight. The fact stays with its url and the status
"browser check", each job lists it, and the lead opens every such page in Claude in Chrome at the grade's close
(retool-stop step 0). No scraper or other way around a site's block (Firecrawl was weighed and passed over). Written into
AGENTS.md, docs/COURSE-RUN.md stage 5 and the kit (docs/pipeline/kit/RETOOL.md).

## 2026-11-22: SEL progression calls (q-prog-sel-1)

- **18 or over:** a student 18 or over gets the family note and makes their own leave-out or consent choice, in every
  subject, with the school's own rules still applying. One rule, in AGENTS.md.
- **g12-sm-have-a-say:** planned on an invented graduate's case; real public action stays in the government course.
- **Grade 12 RS9:** stays a school case with a written carry to work.
SEL's progression is done (data/progressions/sel.csv, 520 rows).

## 2026-11-22: Career education progression calls (q-prog-cte-1)

- **Who chooses the grade 10 clusters:** the class shares two clusters and each student adds one of their own through
  a self-guided packet, and every student narrows from a cluster to a sub-cluster to one named job studied in depth;
  the full plan and the applied project end on that job ("students at some point should be able to follow their
  interests from very broad to narrow jobs"). The lead set the short path (64 sessions) to one shared cluster plus the
  student's own, keeping the path to a named job (STANDARD section 3).
- **Environmental Protection:** not a sensitive field ("necessary for survival"), taught like any other; one rule in
  STANDARD section 6: no student is put down or graded for their own views on environment and resource questions.
  Section 5's six-item leave-out list is unchanged.
Career education's progression is done (data/progressions/cte.csv, 228 rows).

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

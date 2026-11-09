# Answers from the Review Desk

Cory's answers to question cards, and what each still needs. Remove a line once it is applied to the specs.

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

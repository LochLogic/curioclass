# Spec fixes: health-pe, grade 9-12

7 tools: 0 rework, 7 small addition, 0 fine. How to use this file: ../README.md. When a spec is fixed, add a line to ../done.txt.

Kinds of fix in this course: Write the spec (1), Close the guessable check (6), Add the missing part (7), Add a check (2), Reach five items that differ (5), Sensitivity read (5).

## Health Claim Checker

- Spec: `tools/health-claim-checker/spec.md` . Module: health-pe-9-12-accessing-valid-health-information. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Reach five items that differ, Sensitivity read.
- Checks a student can pass by guessing:
  - Verdict has three choices and pins are limited to 3 or 4 hops; the case file shows the full answer whatever the student chose, then Reopen clears the notes, so the key can be copied (no points though)
- **NHES.S3** (practiced, in Cases): Trace a claim hop by hop, pin where it broke, pick verdict
  - Parts of the standard the student never does (must add):
    - find valid sources or services on their own
    - check a real source or product
- **NHES.S2** (practiced, in Cases (Who gains?, reason chips)): Read who gains at each hop; choose a seller reason
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - influence on the student's own health behavior
    - family, peers, culture and technology
- The read was unsure about (check these against the spec; the read may be wrong):
  - NHES.S2 wording not printed; spec glosses it as how media and commercial interests shape a health claim, real S2 is broader (family, peers, culture, media, technology)
  - word counts for texts are estimates from the Content section
  - S2 shown by Who gains? button, which reveals the motive; student only picks a reason chip in cases 1, 3, 5
  - cost_class new-engine: chain with diff highlights and a risk calculator, no family

## Weekend Substance Choices

- Spec: `tools/weekend-substance-choices/spec.md` . Module: health-pe-9-12-alcohol-drugs-and-tobacco. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Add a check, Reach five items that differ, Sensitivity read.
- Checks a student can pass by guessing:
  - Tap the three questions in turn without reading, then pick any choice; there is no wrong pick and the questions are only taps
- **NHES.S1** (practiced, in Panels; Standards map): Read the body panel at each decision
  - To do: no check: add one where thinking is cheaper than guessing
  - Parts of the standard the student never does (must add):
    - explain or describe the information in own words
    - use of sources or checking where information comes from
- **NHES.S4** (practiced, in Scenes; Help a friend): Pick refusal words and an action; call 911
  - Parts of the standard the student never does (must add):
    - say or write own refusal words (choices are given)
    - ask for help or negotiate in own words
- **NHES.S5** (taught, in Scene decisions; weekend map): Tap the three questions, weigh outcomes, then choose
  - Parts of the standard the student never does (small, add if cheap):
    - compare options against own stated values (questions are taps)
- **CASEL Responsible Decision-Making** (practiced, in Ride decision): Weigh effects on self, friends and others on the road
  - To do: no check: add one where thinking is cheaper than guessing
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - explain the effects on others in own words
- The read was unsure about (check these against the spec; the read may be wrong):
  - NHES.S1 wording: spec calls it functional health information; I am not sure of the exact 2024 wording
  - NHES.S5 depth taught is a judgment: the check is a process rule, not a right answer
  - Whether refusal words are written or picked: spec says picked

## First Aid Responder

- Spec: `tools/first-aid-responder/spec.md` . Module: health-pe-9-12-first-aid-and-cpr. Stage: built (the code changes after the spec). Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Sensitivity read.
- Checks a student can pass by guessing:
  - Scene order: a wrong card shakes back with the reason of the step that comes first and costs only 5 s, so the order can be found by tapping (spec has no beating section)
- **NHES.S7** (practiced, in Scenes; CPR rhythm): Order emergency steps; tap hands-only CPR rhythm
  - Parts of the standard the student never does (must add):
    - compression depth
    - full chest recoil
    - breaths
    - practice with hands on a manikin
- The read was unsure about (check these against the spec; the read may be wrong):
  - depth: CPR rate part is a real skill with a tool-rule check, scenes order is beatable; chose practiced overall, could be taught for CPR rate alone
  - NHES.S7 wording not printed
  - notes.md says Field guide has five cards and added content repairs; spec Open questions still open

## Fitness Program Designer

- Spec: `tools/fitness-program-designer/spec.md` . Module: health-pe-9-12-lifetime-fitness. Stage: spec only. Sort: **small addition**.
- Fixes: Add the missing part, Reach five items that differ.
- **SHAPE.S2** (taught, in Design; Fix it): Build a six-week grid; fix ten live checks
  - To do: only 4 items: reach five or more that differ
- **SHAPE.S4** (practiced, in Design): Plan training for a fictional client, not for self
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - plan for own fitness
    - lifelong activity beyond six weeks
    - monitor own progress
- The read was unsure about (check these against the spec; the read may be wrong):
  - SHAPE.S2 and S4 wordings not printed; judged from spec glosses
  - S4 is about personal plans; the tool plans for fictional clients so practiced
  - Copy week +10 percent button does the progression step for the student
  - spec has no Can it be beaten section; checks are design checks so none listed

## Mind Map

- Spec: `tools/mind-map/(no spec.md yet)` . Module: health-pe-9-12-mental-health-and-wellness. Stage: LIVE (the code changes after the spec). Sort: **small addition**.
- Fixes: Write the spec, Close the guessable check, Add the missing part, Reach five items that differ, Sensitivity read.
- Checks a student can pass by guessing:
  - Help a friend: every reply gets feedback and only the best moves on, free tries, so the best reply can be found by elimination
  - Myth or fact is a two-way choice
- **NHES.S1** (practiced, in The map; Myth or fact): Read condition cards; call twelve statements myth or fact
  - Parts of the standard the student never does (small, add if cheap):
    - explain the concepts in own words
    - prevention and promotion actions beyond the stress bucket
- **NHES.S8** (practiced, in Help a friend (connect step)): Pick the reply that connects a friend to help
  - To do: only 2 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - speak up for health to others in own words
    - community or school level advocacy (poster is a teacher stretch only)
- **NHES.S4** (practiced, in Help a friend): Choose replies to notice, ask, listen and connect
  - To do: only 2 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - say or write own words
    - refusal, conflict resolution or negotiation skills
- The read was unsure about (check these against the spec; the read may be wrong):
  - no spec: judged from notes.md, plan.md and tool.json only, src.html not read
  - how Myth or fact is answered (individual tap or class vote, and feedback) is not stated; assumed tool shows evidence after
  - NHES S1, S4, S8 wordings not printed
  - S8 advocacy: plan.md lists S8 for helping a friend connect; real advocacy poster is stretch in plan only
  - minutes: tool.json 20-45, plan 50; used 45
  - cost_class sibling is a guess

## Game Day Fuel

- Spec: `tools/game-day-fuel/spec.md` . Module: health-pe-9-12-nutrition-and-fitness-planning. Stage: built (the code changes after the spec). Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Reach five items that differ, Sensitivity read.
- Checks a student can pass by guessing:
  - Ten flags give the direction to move, edits are free and instant, so plans can be fixed by adding foods until flags clear (no beating section in spec)
- **NHES.S6** (practiced, in Plan the week; Game day): Revise a fictional athlete's meals after flags and replay
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - state a specific goal in own words
    - apply it to own health practices
    - track progress over time
- **NHES.S7** (practiced, in Plan the week; Game day): Build and test a week of meals around fixed training
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - practice with own behavior
    - avoid or reduce risks beyond food (supplements only in a note)
- The read was unsure about (check these against the spec; the read may be wrong):
  - NHES wordings not printed; S6 and S7 judged from the spec's own glosses
  - S6 goal is implied by the flags, the student never states one on the tool, so marked practiced
  - S7 check is only the flags and tank, listed in beatable, so not taught
  - cost_class sibling: reuses label-detective food record but adds athletes, slots, flags and tank model
  - minutes 30 is the middle of 20-40

## Captain's Choices

- Spec: `tools/captain-s-choices/spec.md` . Module: health-pe-9-12-sportsmanship-and-leadership. Stage: built (the code changes after the spec). Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Add a check.
- Checks a student can pass by guessing:
  - Spec says no right answer, but all a's give every good epilogue and the best dials (Trust 10, Belonging 10), all b's the worst, so choice a can be picked every time; Team board shows the dial changes
- **SHAPE.S3** (practiced, in Six chapters; Season card): Choose a captain response in six scenes; read consequences
  - To do: no check: add one where thinking is cheaper than guessing
  - Parts of the standard the student never does (must add):
    - use social skills while moving in a game
    - explain the choice in own words (Talk about it is a class prompt)
- The read was unsure about (check these against the spec; the read may be wrong):
  - SHAPE.S3 wording not printed; spec gloss is social skills through movement
  - no check on understanding: Talk about it is a prompt for the class, consequence feedback only
  - word counts for texts are estimates from the Content section
  - cost_class new-engine is a guess: family none, story format


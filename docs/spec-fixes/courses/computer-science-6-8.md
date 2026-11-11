# Spec fixes: computer-science, grade 6-8

16 tools: 2 rework, 14 small addition, 0 fine. How to use this file: ../README.md. When a spec is fixed, add a line to ../done.txt.

Kinds of fix in this course: Hand the key step to the student (3), Close the guessable check (13), Add the missing part (10), Add a model or a guide (6), Reach five items that differ (13), Put it on the main path (1), Teach the code or drop it (1), Sensitivity read (6).

## Phishing Spotter

- Spec: `tools/phishing-spotter/spec.md` . Module: computer-science-6-8-cyber-attacks-and-defense. Stage: built (the code changes after the spec). Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Teach the code or drop it.
- Checks a student can pass by guessing:
  - Keep or report: 10 phish and 10 safe in a 20-message pool that repeats each round, so the answers can be memorised
  - Nearly every fake address ends in .test while every safe one ends in .example, so the ending separates most phish from safe without reading the sender
- **MS-SYS-SE-32** (claimed, in notes.md Sources and scope): Nothing matches confidentiality, integrity or availability failures
  - To do: nothing the student does matches this code: teach it or drop it
  - To do: the tool does the "explain" step: the student must do it
  - Parts of the standard the student never does (must add):
    - explain failure of confidentiality
    - explain failure of integrity
    - explain failure of availability
- **MS-SYS-SE-33** (taught, in Practice and Arcade modes): Keep or report a message, tap the tell that gave it away
  - Parts of the standard the student never does (small, add if cheap):
    - social engineering other than phishing messages
    - what to do beyond reporting
- The module also lists codes this tool does not carry: MS-SYS-SE-32.
- The read was unsure about (check these against the spec; the read may be wrong):
  - No standard wording printed; SE-33 read as the phishing and social engineering part per notes.md
  - Tell scoring in Arcade allows a tap on one spot, so a lucky tap earns +2
  - Notes.md says Arcade Report scores 1 and 2 with a right first tell, same as spec

## Misleading Charts

- Spec: `tools/misleading-charts/spec.md` . Module: computer-science-6-8-data-detectives. Stage: built (the code changes after the spec). Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part.
- Checks a student can pass by guessing:
  - File it: six trick cards and three rulings with a hint that says which half is wrong and free tries; notes say repeating the clue tools and trying every choice closes a case
- **MS-DAT-DC-23** (practiced, in Clue tools, cases 2 and 5): Press Zoom out and Per 100 to filter and rate the data
  - Parts of the standard the student never does (must add):
    - sort records
    - group records
    - filter by own rule
- **MS-DAT-DI-25** (practiced, in Your ruling, six cases): Rule on the headline: holds up, blown up or wrong
  - Parts of the standard the student never does (must add):
    - predict or classify from data
- **MS-DAT-DI-26** (shown, in Fix it section; Spin Room sandbox is optional): Turn on a fix toggle and read the redrawn chart
  - To do: the tool does the "change and compare" step: the student must do it
  - Parts of the standard the student never does (must add):
    - change the visualization themselves (only in the Spin Room)
    - compare two versions in words
- The read was unsure about (check these against the spec; the read may be wrong):
  - standard wording not printed; depth set from the notes' own coverage statement (DI-26 direct, DC-23 partial, DI-25 limited)
  - DI-26 marked shown because the main path is the fix toggle; the Spin Room, where the student changes the chart, is a second mode
  - no Can it be beaten? section in the spec

## Algorithm Audit

- Spec: `tools/algorithm-audit/spec.md` . Module: computer-science-6-8-algorithms-and-fairness. Stage: spec only. Sort: **small addition**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Reach five items that differ, Sensitivity read.
- Checks a student can pass by guessing:
  - The Hearing: present pinned cards one after another until the board says that answers my question; three members, two or three accepted cards each
  - Formula fixes: ten changes with seat feedback and free tries, so setting first week to 0 and last year to 0 can be found by trial
- **MS-ALG-IM-10** (taught, in Mode 1: Audit, Rule check and Twin test): Run twin tests and rule checks to find the proxy rules
  - To do: only 2 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - audit an algorithm other than a point formula
- **MS-ALG-IM-11** (practiced, in Mode 1: Audit, The formula and Results): Rewrite the six rules and watch seats and costs change
  - Parts of the standard the student never does (small, add if cheap):
    - compare the fix with a rival fix in words
- **MS-SOC-CE-45** (practiced, in Mode 2: Hearing): Present pinned evidence to three board members
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - speak or write an argument in own words
    - weigh views from people who lose seats
- **MS-SOC-HU-43** (shown, in Mode 2: Hearing, public comment): Read the board's votes and Mrs. Park's comment
  - To do: the tool does the "explain" step: the student must do it
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - explain who is helped or harmed
    - name a person affected
- The read was unsure about (check these against the spec; the read may be wrong):
  - No standard wording printed; IM-10 read as bias in algorithms, IM-11 as responding to bias, CE-45 and HU-43 as civic and human impact from the module title only
  - Sensitive: neighborhood and home internet access stand in for income and race, framed gently
  - Painted portraits wait on review (people art)

## AI Fit Check

- Spec: `tools/ai-fit-check/spec.md` . Module: computer-science-6-8-choosing-ai-or-not. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add a model or a guide, Reach five items that differ.
- Checks a student can pass by guessing:
  - Sort: three bins with a reason chip and a counter-example for wrong bins, cards movable until Check sort
  - Helper check: right or wrong per answer, binary
- **MS-ALG-PS-05** (practiced, in Try the helper): Run the pretend helper; check each answer right or wrong
  - To do: no model or guide: add one
  - Parts of the standard the student never does (small, add if cheap):
    - fix or report the wrong answer
- **MS-SOC-ET-40** (practiced, in Cost card; Fit memo): Read the cost card; build a fit memo from chips
  - To do: only 2 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - weigh the trade-off in own words
- The read was unsure about (check these against the spec; the read may be wrong):
  - No filed wording in packet; judged on module line
  - Items for PS-05 count 5 bills plus 20 photos, the 20 photos are one grouping not 20 checks
  - Spec does not say checks are scored per answer or only that seeded errors must be caught

## Lunch Survey Cleanup

- Spec: `tools/lunch-survey-cleanup/spec.md` . Module: computer-science-6-8-cleaning-data-honestly. Stage: built (the code changes after the spec). Sort: **small addition**.
- Fixes: Add the missing part, Reach five items that differ.
- **MS-DAT-DC-24** (taught, in Clean; Report Part 1): Try two or more fixes per problem, compare effects, choose one
  - To do: only 3 items: reach five or more that differ
- **MS-DAT-DI-27** (taught, in Report Parts 1 to 4; Check my report): Build the report from picks: process, who counted, limits, answer
  - Parts of the standard the student never does (must add):
    - compose the summary in own words
- The read was unsure about (check these against the spec; the read may be wrong):
  - Quoted standard wording is in the spec; student never writes free text, the report is assembled from chips and statements, so DI-27 marked shared with a core missing part
  - Part 4 answer is not checked
  - Read spec, notes.md only; tool.json not listed in the packet

## AI Code Inspector

- Spec: `tools/ai-code-inspector/spec.md` . Module: computer-science-6-8-code-you-did-not-write. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Add a model or a guide, Reach five items that differ.
- Checks a student can pass by guessing:
  - Credit lines: three choices per credit, free tries
  - Eight-function docs list: replacement is a pick from eight with the error line as feedback
- **MS-PRO-RD-18** (taught, in Look it up): Look up each call in the docs; replace two missing ones
  - To do: only 2 items: reach five or more that differ
- **MS-PRO-TR-19** (taught, in Test it): Plan test inputs, predict the score, run, compare, fix
  - To do: only 4 items: reach five or more that differ
- **MS-PRO-PD-13** (taught, in Log it): Log what, why and the proving test for each fix
  - To do: only 2 items: reach five or more that differ
- **MS-PRO-PD-14** (practiced, in Credit it): Pick the full credit line for the sound and for the AI help
  - To do: no model or guide: add one
  - To do: only 2 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - write the credit line
- The read was unsure about (check these against the spec; the read may be wrong):
  - No filed wording in packet; judged on module line and the spec's map
  - PD-13 'what' and 'why' fields: spec does not say typed or chips; the rule check only blocks a fix with no test
  - RD-18 depth taught despite the eight-function pick, since the program must run all five questions and the docs must be read

## Eras of Computing

- Spec: `tools/eras-of-computing/spec.md` . Module: computer-science-6-8-computing-history-and-impact. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Add a model or a guide, Reach five items that differ, Sensitivity read.
- Checks a student can pass by guessing:
  - Place: five era bands, wrong card slides back with a date clue, free tries
  - Sort: two binary switches per effect, free re-sort until Done sorting
  - Council case: three patterns shown and three to pick, nearly no choice
- **MS-SOC-HI-38** (practiced, in Place): Drag ten actor cards to eras; read what each added
  - Parts of the standard the student never does (small, add if cheap):
    - explain what each actor changed
- **MS-SOC-HI-39** (practiced, in Follow one thread): Sort eight effects intended or surprise, helped or hurt; who
  - To do: no model or guide: add one
  - Parts of the standard the student never does (small, add if cheap):
    - explain why in own words
- **MS-SOC-ET-42** (practiced, in Council): Pick for or against and three patterns; hear two neighbors
  - To do: no model or guide: add one
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - argue or write the case in own words
    - debate with others
- The read was unsure about (check these against the spec; the read may be wrong):
  - No filed wording in packet; judged on module line
  - Three patterns appear to be the only three on the wall, so picking three is not a choice; spec is unclear
  - Women programmers, labor and e-waste export touch hard history lightly

## Industry Device Tour

- Spec: `tools/industry-device-tour/spec.md` . Module: computer-science-6-8-computing-in-industry. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Reach five items that differ.
- Checks a student can pass by guessing:
  - Thinking moves: three cards per worker, a wrong pick shows why it stalls, free tries
  - Layer order: after two misses it asks for each layer's job, so only partly closed
- **MS-SYS-HW-31** (taught, in Site): Open each machine; drag four layers into order; run it
  - To do: only 3 items: reach five or more that differ
- **MS-SOC-CE-44** (practiced, in Worker problem): Pick the thinking move that fits each worker's problem
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - explain why the move fits
- The read was unsure about (check these against the spec; the read may be wrong):
  - No filed wording in packet; judged on module line
  - Whether the layer order is taught or practiced hinges on the post-two-misses naming step, which the spec describes only in one line

## Cipher Vault

- Spec: `tools/cipher-vault/spec.md` . Module: computer-science-6-8-cyber-attacks-and-defense. Stage: built (the code changes after the spec). Sort: **small addition**.
- Fixes: Add the missing part, Add a model or a guide, Put it on the main path, Sensitivity read.
- **MS-SYS-SE-32** (touched, in Things to do 2, 4, 6): Break ciphers; confidentiality only, nothing on integrity or availability
  - To do: off the main path or can be skipped: put it on the path
  - Parts of the standard the student never does (must add):
    - explain failure of integrity
    - explain failure of availability
    - explain the CIA triad
- **MS-SYS-SE-33** (practiced, in Controls, Things to do 1 to 12): Encode, then break messages with counter, splitter, crib
  - To do: off the main path or can be skipped: put it on the path
  - To do: no model or guide: add one
  - Parts of the standard the student never does (must add):
    - attack types other than breaking a cipher
    - defenses beyond choosing a key
- The module also lists codes this tool does not carry: MS-SYS-SE-32.
- The read was unsure about (check these against the spec; the read may be wrong):
  - Packet old tags were blank; skill_key, action and setting_group are my guesses
  - No standard wording printed; spec names 2017 2-NI-06 (apply multiple methods of encryption) so SE-33 may be the encryption standard and SE-32 the CIA one
  - Open bench with no path, goals or score, so nothing is on a main path; SE-33 set to practiced because the student does the breaking but no model or check is required
  - Sensitive: Vicksburg dispatch (Confederate, slavery), Leeson inscription REMEMBER DEATH, Mary Queen of Scots execution

## Metadata X-Ray

- Spec: `tools/metadata-x-ray/spec.md` . Module: computer-science-6-8-data-metadata-and-you. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Reach five items that differ, Sensitivity read.
- Checks a student can pass by guessing:
  - Dial reveal picks: a short list after each step, free tries
  - Field naming: four names (time, place, device, account), free tries
- **MS-DAT-DC-22** (practiced, in X-ray): X-ray each record; tap each field to name it
  - To do: only 3 items: reach five or more that differ
- **MS-DAT-DC-21** (practiced, in Dials): Turn precision and frequency dials; pick what each reveals
  - Parts of the standard the student never does (small, add if cheap):
    - predict before each reveal
    - explain in own words
- The read was unsure about (check these against the spec; the read may be wrong):
  - No filed wording in packet; wording of DC-21, DC-22, IM-28 guessed from the module line and the spec's map
  - IM-28 check is a self-guide (the consequence shown) since the spec has no right answer except 'delete shows what breaks'
  - Privacy and location data of a minor-like character, all made up

## Accessibility Test Team

- Spec: `tools/accessibility-test-team/spec.md` . Module: computer-science-6-8-design-for-every-user. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Reach five items that differ, Sensitivity read.
- Checks a student can pass by guessing:
  - Fair round: four slots across three voices, the tool only flags a voice with none
- **MS-ALG-IM-09** (practiced, in Test as; Standards map): Try the app as each tester and compare what fails
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - state the comparison in words
- **MS-SYS-IM-36** (practiced, in Test as): Use the app by screen reader, plain view and shaky pointer
  - To do: only 3 items: reach five or more that differ
- **MS-PRO-TR-20** (taught, in Bug card; Fix round; Retest): Log failures on bug cards, fix the app, retest
  - To do: only 3 items: reach five or more that differ
- **MS-PRO-PD-15** (practiced, in Fix round): Give every tester voice at least one of four fixes
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - work with real teammates (solo here)
- The read was unsure about (check these against the spec; the read may be wrong):
  - No filed wording in packet; wording of all four codes guessed from the spec's map
  - The three teammates are scripted, so PD-15 is a rule check, not teamwork
  - Disability and language-learner portrayal, sensitivity review owed per spec

## Chore Flowcharts

- Spec: `tools/chore-flowcharts/spec.md` . Module: computer-science-6-8-flowcharts-and-pseudocode. Stage: spec only. Sort: **small addition**.
- Fixes: Add the missing part, Reach five items that differ.
- **MS-ALG-PS-01** (taught, in Chart and pseudocode card, all four chores): Build a flowchart for a chore, read its pseudocode
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - write pseudocode by hand (it is rebuilt automatically)
- **MS-ALG-PS-02** (taught, in Feed the cat to Sort the recycling): Place If and Repeat until blocks in the chart
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - compound conditions (and, or)
    - procedures
- **MS-ALG-PS-03** (taught, in Test days, Run all, New test day): Run test days, find the failing block, add a new day
  - Parts of the standard the student never does (small, add if cheap):
    - write a test plan before building
- The read was unsure about (check these against the spec; the read may be wrong):
  - standard wording not printed; judged from the 2-AP-10, 2-AP-12, 2-AP-17 crosswalk
  - stage spec: nothing built, depth judged from the written spec only
  - PS-02 says procedures are in the module line; this tool has none (code-kitchen covers them)
  - pseudocode is generated, the student never writes any

## Model Mechanic

- Spec: `tools/model-mechanic/spec.md` . Module: computer-science-6-8-machine-learning-models. Stage: built (the code changes after the spec). Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Reach five items that differ.
- Checks a student can pass by guessing:
  - work-order goals are numeric thresholds that k from 1 to 9, four clue switches and photo steppers can reach by trial without diagnosing; notes say so
- **MS-ALG-ML-06** (practiced, in Garage and Work Orders matrix and drawer): Read the matrix and open a cell to see the photos and neighbors
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - name the fault in words before fixing (only the debrief names it)
- **MS-ALG-ML-07** (practiced, in Training steppers, k and clue switches): Change photo counts, k, labels or clues, rerun the test
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - explain why a repair helps one group and may hurt another
- **MS-ALG-ML-08** (practiced, in Work Orders 1 to 3): Meet work-order goals on accuracy by day and night
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - justify the repair to a client
- **MS-DAT-IM-29** (practiced, in Work Order 2): Fix night photos missing so night animals stop failing
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - discuss who is hurt by the bias in words
- The read was unsure about (check these against the spec; the read may be wrong):
  - standard wording not printed; judged from the 2-DA-08, 2-DA-09, 2-IC-21 crosswalk and the spec
  - which of ML-06, ML-07, ML-08 is read versus tune versus improve is a guess from the notes
  - notes admit the work-order goal is beatable and does not show the diagnosis

## Packet Race

- Spec: `tools/packet-race/spec.md` . Module: computer-science-6-8-packets-and-the-internet. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Reach five items that differ.
- Checks a student can pass by guessing:
  - Delivering all 12 packets: restart keeps the arrows, the map has few routers, and drop reasons say which way to move, so tapping clockwise until packets arrive works without understanding routing
- **MS-SYS-NT-34** (practiced, in Mode 2: Race): Aim each router's arrow so numbered packets reach D
  - Parts of the standard the student never does (must add):
    - split a message into packets
    - number or label packets
    - explain why data travels as packets
- **MS-SYS-NT-35** (practiced, in Mode 2: Race, scheduled failures): Re-aim routers around a failed router or cut link
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - design redundant paths
    - explain why many routes keep the internet working
- The read was unsure about (check these against the spec; the read may be wrong):
  - No standard wording printed; NT-34 read as packets/how data travels and NT-35 as resilience/protocols from the module line only
  - Spec has no Can it be beaten section
  - Watch mode is tool-routed (shown); counted as modeled support for Race

## Code Kitchen

- Spec: `tools/code-kitchen/spec.md` . Module: computer-science-6-8-variables-data-types-and-procedures. Stage: built (the code changes after the spec). Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Add a model or a guide, Reach five items that differ.
- Checks a student can pass by guessing:
  - A1 to A3: the error message names the exact slot and the choices are a number or text, True or False, so trial fixes it
- **MS-PRO-VD-16** (taught, in Sets A levels 1-3): Fix number, text and True/False values; join text with str()
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - choose clear variable names (starters supply them)
- **MS-PRO-RD-17** (practiced, in B6 and D11, D12): Split a combined order into a procedure that calls another
  - To do: no model or guide: add one
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - decompose a problem you pick yourself
- The read was unsure about (check these against the spec; the read may be wrong):
  - standard wording not printed; judged from the 2-AP-11, 2-AP-13, 2-AP-14 crosswalk
  - RD-17 mapped to decomposing (B6, D11, D12); a code about readability or documenting would not match
  - gold ring needs par; a ring is not required to move on

## County Connection Grant

- Spec: `tools/county-connection-grant/spec.md` . Module: computer-science-6-8-who-gets-connected. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add a model or a guide, Reach five items that differ, Sensitivity read.
- Checks a student can pass by guessing:
  - Match: four devices by four connections per home with enough or not-enough feedback and free changes until Lock the plan
  - Twist: three design-change cards, pick two, map shows result
- **MS-SYS-HW-30** (practiced, in Match): Pick a device and connection for each of eight households
  - Parts of the standard the student never does (small, add if cheap):
    - explain why a choice fits
- **MS-SYS-IM-37** (practiced, in Storm; Match): Compare access by distance, cost, terrain; run the storm; add backup
  - To do: no model or guide: add one
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - predict before the storm
    - explain in own words
- **MS-SOC-ET-41** (taught, in Telehealth twist): Tap lit homes to see why; pick up to two design changes
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - say why in own words
- The read was unsure about (check these against the spec; the read may be wrong):
  - No filed wording in packet; judged on module line
  - Whether the ET-41 'judging' is student or tool is unclear, set to shared
  - Surname Begay and a rural county may touch Native portrayal; spec says made up, flagged for review
  - Costs are dated estimate ranges, refreshed at Build


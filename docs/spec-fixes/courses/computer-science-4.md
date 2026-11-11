# Spec fixes: computer-science, grade 4

4 tools: 0 rework, 4 small addition, 0 fine. How to use this file: ../README.md. When a spec is fixed, add a line to ../done.txt.

Kinds of fix in this course: Hand the key step to the student (1), Close the guessable check (4), Add the missing part (3), Add a model or a guide (1), Reach five items that differ (2), Put it on the main path (1), Sensitivity read (2).

## Data Table Builder

- Spec: `tools/data-table-builder/spec.md` . Module: computer-science-4-tables-and-visualizations. Stage: built (the code changes after the spec). Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Sensitivity read.
- Checks a student can pass by guessing:
  - question cards mark done when the chosen column matches, among five or six columns, with free retries and no scoring of the guess
- **E4-DAT-DC-09** (practiced, in Our class mode): Choose column kinds, then add one row per student
  - Parts of the standard the student never does (small, add if cheap):
    - decide how data will be collected beyond the given shelf
    - explain why a column kind suits a question
- **E4-DAT-DI-10** (practiced, in Questions in Sample class and Our class): Pick the column, chart and split that answer a question
  - Parts of the standard the student never does (must add):
    - say or write what the chart shows (done aloud, not checked)
    - support a claim with the chart
- The read was unsure about (check these against the spec; the read may be wrong):
  - standard wording not printed; judged from the 1B-DA-06 and 1B-DA-07 crosswalk and the notes
  - flagged sensitive for a class-collected personal column (teeth lost) and the baby-teeth fact; notes say use non-sensitive columns
  - DC-09 judged as collecting and organizing; the shelf supplies most columns

## Code Tracer

- Spec: `tools/code-tracer/spec.md` . Module: computer-science-4-trace-the-code. Stage: LIVE (the code changes after the spec). Sort: **small addition**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Add a model or a guide, Reach five items that differ.
- Checks a student can pass by guessing:
  - Yes/No if steps and the three note checks are one in two by guessing, and the real result is shown right after any answer
- **E4-PRO-VD-06** (taught, in Trace levels 1-12; Workbench): Type each variable's predicted value, then run the line
  - Parts of the standard the student never does (must add):
    - create a program that uses variables
    - choose or name a variable
- **E4-PRO-RD-07** (shown, in Note check, levels 6, 9, 12): Say whether a program's note tells the truth
  - To do: the tool does the "document" step: the student must do it
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - write a note or comment
    - describe choices made while building
- **E4-PRO-TR-08** (practiced, in Trace levels 6, 9, 12; Workbench program 13): Trace a program to see if it does what it says
  - To do: no model or guide: add one
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - fix a bug (program 13 fix is only shown)
    - test a program the student wrote
- The read was unsure about (check these against the spec; the read may be wrong):
  - standard wording not printed; verbs judged from the module line and the 1B-AP-09, 1B-AP-17, 1B-AP-15 crosswalk
  - VD-06 verb taken as trace; if it is create, the student never creates a program here
  - RD-07 judged as documenting; the student only checks given notes, plan.md has pairs write a note on whiteboards off the tool
  - TR-08 judged as test and debug from the crosswalk

## Biased Bot

- Spec: `tools/biased-bot/spec.md` . Module: computer-science-4-training-data-matters. Stage: built (the code changes after the spec). Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Put it on the main path, Sensitivity read.
- Checks a student can pass by guessing:
  - Room 9 reaches 10 of 10 by pressing More under Room 9 as the hint says, without comparing handwriting; Run is free and the bars say which way to move
- **E4-ALG-ML-02** (explored, in Lunch Line mode): Change training jars, retrain, run the same lunch line
  - To do: see-why code, fine here; the unit must add: A unit must have students predict each room's score before every run, explain from the jars why it changed, and write a rule for fair training data.
  - Parts of the standard the student never does (must add):
    - explain why more of the same style did not help (talk only)
    - build own training set from scratch
- **E4-SOC-HU-18** (practiced, in Lunch Line results and card viewer): Find whose lunch is wrong from room bars, fix with that room's cards
  - Parts of the standard the student never does (must add):
    - say who is harmed and why in words
    - think of other groups not in the data
- **E4-DAT-IM-11** (practiced, in Lunch Line results): Compare room scores by whose cards trained the bot
  - Parts of the standard the student never does (must add):
    - test whether examples represent users beyond the three rooms
    - explain the link between missing data and harm
- **E3-ALG-ML-02** (touched, in Try Your Writing mode): Draw a digit, label it, teach Bitsy, read again
  - To do: off the main path or can be skipped: put it on the path
  - Parts of the standard the student never does (small, add if cheap):
    - use it for a rule they write themselves
- The read was unsure about (check these against the spec; the read may be wrong):
  - standard wording not printed; judged from the notes' Standards section and crosswalk 1B-DA-07, 1B-IC-19, 1B-IC-20
  - ML-02 marked explored although prediction before each run is a teacher prompt, not enforced by the tool
  - E3-ALG-ML-02 is a grade 3 code in the module list; only the optional second mode touches it
  - flagged sensitive for bias and unfairness context (Gender Shades kept in teacher notes only)

## Network Help Desk

- Spec: `tools/network-help-desk/spec.md` . Module: computer-science-4-wired-wireless-and-login. Stage: built (the code changes after the spec). Sort: **small addition**.
- Fixes: Close the guessable check, Reach five items that differ.
- Checks a student can pass by guessing:
  - three kinds then at most four causes, with free retries and a nudge that names the missing question or quotes the key clue, so trial can beat thinking; Call time is display only
- **E4-SYS-NT-14** (practiced, in Calls 1, 2, 4, 5; House mode): Ask questions, pick a connection cause with proving clues
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - design or build a network
    - explain how data travels between devices
- **E4-SYS-SE-13** (practiced, in Calls 3, 6, 7, 8; House mode): Tell a wrong password from a not-allowed account
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - create or choose a strong password
    - name ways to protect personal information
- **E4-SYS-HW-12** (practiced, in Calls 1, 2, 4, 5): Pick a cable, power or distance cause and send a fix
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - test a fix of their own design
    - troubleshoot software problems
- The read was unsure about (check these against the spec; the read may be wrong):
  - standard wording not printed; judged from the 1B-CS-03 and 1B-NI-05 crosswalk and the notes
  - all three codes share one activity, so depth is the same; HW-12 hardware part is only cable, router power and distance
  - the spec has no Can it be beaten? section


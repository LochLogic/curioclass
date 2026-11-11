# Spec fixes: computer-science, grade k

3 tools: 0 rework, 3 small addition, 0 fine. How to use this file: ../README.md. When a spec is fixed, add a line to ../done.txt.

Kinds of fix in this course: Hand the key step to the student (1), Close the guessable check (3), Add the missing part (3), Reach five items that differ (1), Sensitivity read (1).

Shape for this course: ../../agents/catalog/shape/computer-science-k.md. Band tools that are also part of this course, with their fix lists in computer-science-k-2.md: Attic Gadget Box, Question Jar, Who Uses This Device?, Tablet Buddy, Line Leader Picker, Morning Meeting Board, Tap-to-Start Puppets.

## Me vs the Counter

- Spec: `tools/me-vs-the-counter/spec.md` . Module: computer-science-k-count-and-decide. Stage: built (the code changes after the spec). Sort: **small addition**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Reach five items that differ.
- Checks a student can pass by guessing:
  - Bounciest Ball chart: four rows, tapping a wrong row only plays a look-again line and keeps the chart, so retrying beats thinking
  - Prediction on the question card can be skipped and is never compared by the tool
- **EK-DAT-DC-08** (taught, in Bounce Lab; Bounciest Ball): Tap each bounce, compare with the sensor count
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - real classroom data (ball and sensor are simulated)
- **EK-DAT-DI-09** (shown, in timeline after each drop; Show the chart): Read the timeline, table and picture graph the tool builds
  - To do: the tool does the "present" step: the student must do it
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - build the table or graph themselves
    - choose how to display the data
- **EK-DAT-IM-10** (practiced, in Bounciest Ball): Point at a predicted ball, then tap the longest row
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - use the data to explain the choice in words
- The read was unsure about (check these against the spec; the read may be wrong):
  - no filed standard wording; DI-09 verb taken from the 2017 crosswalk (present data in visual formats)
  - DC-08 'taught' relies on the tap-vs-sensor compare line; the data is simulated
  - 'Collect data in the classroom' only partly met: the balls are on screen
  - spec has no Can it be beaten section

## Secret Keeper

- Spec: `tools/secret-keeper/spec.md` . Module: computer-science-k-public-or-private. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Sensitivity read.
- Checks a student can pass by guessing:
  - Share or Secret: two buttons, a private card left on the board is simply moved to the box, nothing is scored, so every card ends sorted whatever the class picks
  - Who's Asking?: three answers, every answer gets an explaining line and no penalty, so the answer can be guessed or reasoned from the reaction
- **EK-SYS-SE-12** (practiced, in Who's Asking? (password asks)): Answer asker requests: tell, keep secret, get a grown-up
  - Parts of the standard the student never does (must add):
    - choose or judge a safe password
    - explain why in own words
- **EK-SYS-IM-13** (practiced, in Share or Secret): Class votes Share or Keep secret for ten cards
  - Parts of the standard the student never does (must add):
    - say why a detail is private
- **AASL.Engage** (practiced, in Share or Secret; Who's Asking?): Decide what is safe to share with the park
  - Parts of the standard the student never does (must add):
    - wording not known
    - share information with others beyond choosing what to keep private
- The read was unsure about (check these against the spec; the read may be wrong):
  - no filed standard wording; code-to-activity split is my guess: the spec never says which activity belongs to SE-12 vs IM-13
  - AASL.Engage wording unknown (spec quotes 'safe sharing of information')
  - depth practiced not taught: the class vote is teacher-tapped and both buttons are free to try
  - sensitive: home address, phone, birthday, passwords; spec open questions on grown-up wording and birthday

## Robot Dance

- Spec: `tools/robot-dance/spec.md` . Module: computer-science-k-step-by-step. Stage: LIVE (the code changes after the spec). Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part.
- Checks a student can pass by guessing:
  - Fix-It Show: the trip marks the first mismatch card and Dot's bubble shows the exact move, tries are free, so a class can copy without reasoning (rounds 1-4 have one wrong card among 8 moves)
- **EK-ALG-PS-01** (practiced, in Dance Floor; Fix-It Show): Tap move cards to build a dance; class dances along
  - Parts of the standard the student never does (small, add if cheap):
    - create a sequence for a stated goal from an empty strip
- **EK-PRO-PD-04** (practiced, in Dance Floor; Fix-It Show): Choose and order picture cards into a program
  - Parts of the standard the student never does (small, add if cheap):
    - plan the program before building it
    - any construct beyond a straight sequence
- **EK-PRO-TR-07** (practiced, in Fix-It Show rounds 1-8): Watch Bolt trip, find the wrong card, fix it
  - Parts of the standard the student never does (must add):
    - find the wrong step without the tool marking it
    - say why the step is wrong
- The module also lists codes this tool does not carry: EK-PRO-RD-06.
- The read was unsure about (check these against the spec; the read may be wrong):
  - no filed standard wording; verbs inferred from the module line and the 2017 crosswalk the spec quotes
  - EK-PRO-RD-06 is in the module list but the spec never mentions it; wording unknown
  - missing_weight for PS-01 and PD-04 left edge: free creation exists in Dance Floor but with no goal and no check
  - no Can it be beaten section in the spec; beatable is my reading
  - cost_class new-engine because no robot engine exists yet and the spec keeps the runner inside src.html


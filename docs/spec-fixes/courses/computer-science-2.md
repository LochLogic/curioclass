# Spec fixes: computer-science, grade 2

3 tools: 0 rework, 3 small addition, 0 fine. How to use this file: ../README.md. When a spec is fixed, add a line to ../done.txt.

Kinds of fix in this course: Write the spec (1), Close the guessable check (2), Add the missing part (3), Add a model or a guide (1), Reach five items that differ (1).

Shape for this course: ../../agents/catalog/shape/computer-science-2.md. Band tools that are also part of this course, with their fix lists in computer-science-k-2.md: Attic Gadget Box, Question Jar, Who Uses This Device?, Tablet Buddy, Line Leader Picker, Morning Meeting Board, Tap-to-Start Puppets.

## Input or Output?

- Spec: `tools/input-or-output/spec.md` . Module: computer-science-2-input-and-output. Stage: built (the code changes after the spec). Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part.
- Checks a student can pass by guessing:
  - Cover It: two prediction buttons, optional and unscored; the touchscreen accepts either
- **E2-SYS-HW-11** (explored, in Cover It (after Try It)): Cover one part, predict gadget or we can't tell, run the job
  - To do: see-why code, fine here; the unit must add: student sorts new devices' parts into input and output and says why
  - Parts of the standard the student never does (must add):
    - sort parts into input and output themselves (board is filled by the tool)
    - name the hardware parts themselves
    - explain in own words
- The module also lists codes this tool does not carry: E2-SYS-SE-12.
- The read was unsure about (check these against the spec; the read may be wrong):
  - no filed standard wording
  - action changed from sort to predict-reveal: the spec's In, Think, Out board is filled by tapping in Try It, the class does not sort
  - explored chosen because the verb is understand; E2-SYS-SE-12 is stated not covered

## Loop Garden

- Spec: `tools/loop-garden/spec.md` . Module: computer-science-2-loops-and-events. Stage: LIVE (the code changes after the spec). Sort: **small addition**.
- Fixes: Write the spec, Close the guessable check, Add the missing part, Add a model or a guide, Reach five items that differ.
- Checks a student can pass by guessing:
  - Short gardens (1 to 3): few block types, free runs, Bonk shows where it fails, so trial is cheaper than planning
  - Stars reward fewer blocks only; a student can plant everything the long way without ever using Repeat
- **E2-ALG-PS-01** (taught, in gardens 1-7): Build Step, Turn, Plant, Repeat programs to plant every seed
  - Parts of the standard the student never does (small, add if cheap):
    - say the algorithm in words
- **E2-PRO-PD-04** (taught, in gardens 1-7, free garden): Build programs with sequence and a Repeat block
  - Parts of the standard the student never does (must add):
    - events (nothing starts the program except Run)
    - repeat is optional; only stars reward it
- **E2-PRO-TR-07** (practiced, in any garden after a Bonk): Find which block made the gardener bonk and fix it
  - To do: no model or guide: add one
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - no built-in bug to find
    - explain why the block was wrong
- The read was unsure about (check these against the spec; the read may be wrong):
  - spec.md is voice only; read notes.md, plan.md, tool.json and grepped src.html (8 gardens, par values, bonk lines)
  - no filed standard wording; E2-PRO-PD-04 assumed to include events from the module title
  - TR-07: no designed bug; plan has the teacher ask 'which block was the mistake' after a bonk
  - cost_class guessed: spec says loop-garden carries its own code

## Teach the Robot

- Spec: `tools/teach-the-robot/spec.md` . Module: computer-science-2-teach-the-machine. Stage: LIVE (the code changes after the spec). Sort: **small addition**.
- Fixes: Add the missing part.
- **E2-ALG-ML-02** (explored, in Teach; Pet Parade): Label pets Cat or Dog, predict Kip's guess, run the parade
  - To do: see-why code, fine here; the unit must add: student explains in own words, chooses and designs the examples, and tests Kip on a case they made
  - Parts of the standard the student never does (must add):
    - choose which examples to show Kip
    - explain why more varied examples help in own words
- The read was unsure about (check these against the spec; the read may be wrong):
  - no filed standard wording; verb taken from tool.json outcome (explain that a computer learns from examples)
  - example order is fixed; the class can only choose labels, Forget cards or stop
  - no student check in the tool other than parade scores


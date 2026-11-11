# Spec fixes: eld, grade 6-8

5 tools: 0 rework, 3 small addition, 2 fine. How to use this file: ../README.md. When a spec is fixed, add a line to ../done.txt.

Kinds of fix in this course: Write the spec (1), Close the guessable check (5), Add the missing part (2), Add a check (1), Reach five items that differ (3), Sensitivity read (1).

## Idiom Island

- Spec: `tools/idiom-island/(no spec.md yet)` . Module: eld-6-8-idioms-and-everyday-expressions. Stage: LIVE (the code changes after the spec). Sort: **small addition**.
- Fixes: Write the spec, Close the guessable check, Add the missing part.
- Checks a student can pass by guessing:
  - Three-choice check: three options, wrong answer presumably retriable
- **WIDA.ELD-1** (practiced, in Island places, check): See literal picture, hear idiom, answer a three-choice check
  - Parts of the standard the student never does (must add):
    - use the idiom in own sentence
    - say it in conversation
- The read was unsure about (check these against the spec; the read may be wrong):
  - check type from a src grep (three-choice check); retry behavior not confirmed
  - tool.json outcome says use in context but no student sentence in the tool; that is the paper activity in plan.md
  - no standard wording shown; ELD-1 judged from the outcome line
  - cost_class guessed; no family engine named
  - minutes: tool.json 15-30, plan 40; used middle of tool.json

## Summary Scaffold

- Spec: `tools/summary-scaffold/spec.md` . Module: eld-6-8-summarizing-and-citing. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Add a check, Reach five items that differ.
- Checks a student can pass by guessing:
  - Copy rule: only runs of five or more words are flagged, so changing every fifth word passes
  - At Lots help the candidate sentences glow, so marking can follow the glow
- **WIDA.ELD-2** (practiced, in Write (frame bank)): Use citation frames and reporting verbs
  - To do: no check: add one where thinking is cheaper than guessing
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - reporting verbs are not checked beyond the frame
- **WIDA.Inform** (taught, in Write; Organize): Fix copied strings and missing supporting ideas
  - To do: only 1 items: reach five or more that differ
- **RI.6.2** (taught, in Mark; Organize; Write): Mark the central idea, link details, write objective summary
  - To do: only 1 items: reach five or more that differ
- **RI.7.2** (taught, in Mark; Organize; Write): Mark two central ideas, link development, write objective summary
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - analyze how each idea develops over the text (links only)
- **RI.8.2** (taught, in Mark; Organize; Write): Mark central idea, label relationships, write objective summary
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - analyze development over the course of the text (labels only)
- The read was unsure about (check these against the spec; the read may be wrong):
  - RI wording from the packet; central idea check judged tool-key
  - one article per grade, items 1
  - RI.7.2 and RI.8.2 development judged partly met by links and labels
  - ELD-2 check set to none because the spec states only frames
  - minutes spec 25-35

## Word Problem Decoder

- Spec: `tools/word-problem-decoder/spec.md` . Module: eld-6-8-word-problems-decoded. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check.
- Checks a student can pass by guessing:
  - Wrong expression: the right diagram is shown beside it, so a student can copy it
  - Explain frame: relationship slot filled from a short tile list at Lots and Some help
- **WIDA.Explain** (practiced, in Decode (explain frame); No keywords): Fill The problem says ___, so I ___ because ___
  - Parts of the standard the student never does (small, add if cheap):
    - explain in own words beyond the frame
- The read was unsure about (check these against the spec; the read may be wrong):
  - spec calls math code ELD-MA, packet spells WIDA.ELD-3
  - items 30 = thirty problems
  - grade split different-content: grade 6 rates, 7 percent, 8 stretch
  - Sources table cites 6.RP.A.3, 6.EE.A.2a, 7.RP.A.3 as background, not listed
  - minutes spec 20-30

## Perspective Frames

- Spec: `tools/perspective-frames/spec.md` . Module: eld-6-8-comparing-perspectives. Stage: spec only. Sort: **fine**.
- Fixes: Close the guessable check, Reach five items that differ, Sensitivity read.
- Checks a student can pass by guessing:
  - Sort: four columns, wrong column only asks for the clue words, free retries
- **WIDA.ELD-5** (taught, in Sort, Map): Sort quotes by speaker, fill gains and losses map
  - Parts of the standard the student never does (small, add if cheap):
    - read a longer social studies text
    - speak about the decision
- **WIDA.Argue** (taught, in Compare, Position): Build comparison sentences with both reasons, write a position
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - use evidence beyond made-up quotes
- The read was unsure about (check these against the spec; the read may be wrong):
  - WIDA wording not quoted
  - word counts not stated
  - Position check (names other side) judged tool-rule

## CER Builder

- Spec: `tools/cer-builder/spec.md` . Module: eld-6-8-lab-reports-and-claims. Stage: spec only. Sort: **fine**.
- Fixes: Close the guessable check, Reach five items that differ.
- Checks a student can pass by guessing:
  - Claim: only three items to name, and a wrong claim just says look at your averages again, free retries
  - Reasoning: paste the science-idea card and add the claim item's name; check tests keywords and a connector
- **WIDA.ELD-4** (taught, in Bench, Conclusion): Run three trials, read the table, write conclusion with science words
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - listen to or read science explanations
    - say the conclusion aloud
- **WIDA.Argue** (taught, in Conclusion slots; Strong and weak): Write claim, numeric evidence and science-idea reasoning
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - answer a counterclaim
- The read was unsure about (check these against the spec; the read may be wrong):
  - codes: spec writes WIDA ELD-SC; spelled WIDA.ELD-4 per module line
  - WIDA wording not quoted; parts_missing guessed
  - words of sample paragraphs not stated
  - Argue counterclaim missing marked edge because the module is about a single conclusion


# AI Fit Check (idea card)

- Module: computer-science-6-8-choosing-ai-or-not, grade 6-8. Codes: MS-ALG-PS-04, MS-ALG-PS-05, MS-SOC-ET-40
- Format / family: sort / none. Fit: good, because sorting jobs by approach is the core; the AI helper trial is the test of the sort.
- One idea: Sort a stack of jobs (total a lunch bill, enforce a board game's rules, suggest a next song, group lost-and-found photos, translate a note) into fixed steps, written rules or a model learned from data, then run a pretend AI helper on two of them, check every answer it gives, and weigh what it costs in energy and errors against the simpler way.
- How it plays (solo student by default):
  - First screen: three bins (steps, rules, learned from data) and a deck of job cards.
  - Core loop: drag each job to a bin; a "why" chip asks for the reason (the answer is always exact; the rules are known and few; the pattern is too fuzzy to write down).
  - Try the helper: run the pretend AI on the lunch bill and on the lost-and-found photos. On the bill it sometimes gets the total wrong by a few cents and says it with confidence; on the photos it groups most items well but files a blue mitten with the socks. The student checks each answer against the truth.
  - Cost card: each approach shows its energy use per answer as a relative scale (a calculator vs a large model), and its mistake rate.
  - The aha or the end state: AI fits jobs with fuzzy patterns and lots of examples; exact jobs are better done with steps or rules, and every answer still needs checking.
- Standards, one line per code:
  - MS-ALG-PS-04: choose steps, rules or a data-driven model for each job and explain why.
  - MS-ALG-PS-05: use an AI helper on a real job and check its answers.
  - MS-SOC-ET-40: weigh accuracy, energy cost and who is affected by mistakes when choosing AI.
- Not like: ai-evaluator (grade 9-12 testing a vendor's model); dice-in-the-chatbot (grade 9-12 randomness); spot-the-ai (grade 1, what uses AI).
- Art: generated scenes for job cards; bins and cost scales drawn in code.
- Proposed title: keep
- Proposed concept line: keep
- Flags: needs a data source (published energy-per-query figures for the cost card, shown as ranges with dates)

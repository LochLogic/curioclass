# Gemini fixes: scope and sequence of psychology, 2026-11-24

Fix pass on the outside second read S:\CurioClass-gemini\reports\sequence-psychology-gemini-read.md, after the
expert read docs/reviews/sequence-psychology-2026-11-24.md and its fix pass
docs/reviews/sequence-psychology-fixes-2026-11-24.md. Every finding was checked against the files; the one dated
fact was checked by web search (sources below). No settled fix or Desk decision was contradicted.

Counts: 4 findings with 6 parts: 4 hold, 2 partly, 0 wrong, 0 already fixed.

## Findings

| # | Finding | Verdict | What changed |
|---|---|---|---|
| 1a | The scope says the four course-level days are `ours`, but the source map has no row for days 81, 82, 159, 160 | partly | The mismatch holds. Gemini's fix (an `ours` row with unit blank or `C`) fails the gate: sequence.py requires a unit on every row that is not a cut. The scope's sentence now reads that the four course-level days adapt no section and have no row, since every map row names a unit (scope-and-sequence.md, Source map). |
| 1b | Day 118 teaches attraction and relationships (SOC.2.4) but credits only 12.6; the map puts 12.7 on day 119 only | holds | Checked: 1e section 12.7 (Prosocial Behavior) holds attraction and Sternberg's theory of love; 12.6 holds aggression and the bystander effect. source-map.csv 12.7: days 118-119, decision split, why names the two halves. Day 118's note credits sections 12.6 and 12.7. |
| 2 | Day 75 (and frame unit 8) conflate the eugenics apology and compensation years | holds | Virginia: Governor Warner's apology 2002, compensation voted 2015 (up to $25,000 a claim). North Carolina: Governor Easley's apology 2002, $10 million compensation in the 2013 budget, the first state to compensate. Day 75's note and the frame's unit 8 cell now give both years for each state. |
| 3 | Day 126 says "Our own content." yet credits 12.5, which the map places on day 126 | holds | Note now opens "Our own content beside the adapted section (unit 13 builds on 12.5)", the form days 32 and 94 use. Wording mine, shorter than Gemini's. |
| 4a | Day 81 lists COG.2.1 (biases, heuristics, fixation) but its per-part list has no prompt for it | holds | Day 81's note adds "a bias, a heuristic and a fixation, each named in a made-up decision (COG.2.1)", as day 70 asks it. |
| 4b | Day 159 sets THR.1.1's psychological part in earlier content but not its biomedical part | partly | Rule 3 is about the just-assessed unit's item, and the note already set the item earlier for one part; the biomedical part was left open, so a writer could repeat day 157. Day 159's note and the scope's check 2 section now set the biomedical part through unit 2's synapse and unit 4's drug action. |

## Own

- scope-and-sequence.md, Source map: the list of sections with one row per unit now includes 12.5 (rows for units 12
  and 13 exist; the sentence left it out).

## For Cory

None.

## Gates

- `python -X utf8 scripts/sequence.py check psychology`: 0 failures.
- `python -X utf8 scripts/frame.py check psychology`: 0 failures (16 units, 160 days).
- `python -X utf8 scripts/frame.py calendar`: exit 0.

## Sources

- Virginia apology 2002, compensation 2015: https://encyclopediavirginia.org/entries/eugenic-sterilization-in-virginia/ ;
  https://www.csmonitor.com/USA/USA-Update/2015/0227/Virginia-to-compensate-victims-of-state-s-forced-sterilization-program
- North Carolina apology 2002, $10 million in 2013: https://www.aljazeera.com/news/2013/7/26/us-state-to-compensate-sterilisation-victims ;
  https://ncnewsline.com/2014/08/14/eugenics-compensation-a-flawed-process-follows-a-shameful-program/
- OpenStax Psychology 12.7 contents: https://openstax.org/books/psychology/pages/12-7-prosocial-behavior

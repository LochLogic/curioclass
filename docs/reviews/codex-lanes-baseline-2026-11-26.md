# Codex lanes: baseline, 2026-11-26

The four Codex day lanes (scripts/codex_lane.py, one lane per core subject) were stopped softly on 2026-11-26 at Cory's
call ("softly stop the codex work on days so we can pivot those tokens elsewhere"). The build/lanes/STOP file let each
running job finish and started no new one. The last lane ended at 18:25. Cory then asked to "ingest all its work and
baseline it for refining later": every lane job committed itself on main as it finished, nothing was left uncommitted in
the four courses, and this sheet is the baseline the refine starts from (later.csv L161).

## What the lanes made

Each lane wrote on main, one commit per job, under the gates (gate.py, plan.py check, ledger.py gate). Every piece is a
first pass, not ready: no day has had a cheap read, an expert read or a Refine.

| Course | Jobs done (all runs) | Jobs on 2026-11-26 | Last job | Days with items | Items |
|---|---|---|---|---|---|
| math-kindergarten | 47 | 32 | 041 | 160 of 160 | 1,939 |
| science-grade-4 | 29 | 18 | 025 (DATA u3) | 120 of 120 | 652 |
| social-studies-grade-4 | 35 | 21 | 030 (DATA u3) | 160 of 160 | 1,271 |
| english-language-arts-grade-4 | 29 | 15 | 024 | 38 of 160 | 433 |

"Days with items" counts the days that have rows in items.csv. Math, science and social studies came from the 2026-11-24
draft run's days (docs/reviews/codex-draft-baseline-2026-11-24.md) and were being rebuilt section by section and unit by
unit on main; ELA was still in its first units.

## Gate baseline (commit 471687123)

`gate.py --course <course>` stored each course's baseline at build/gates/base-<course>. The next run of the gate on a
course shows only lines a change adds or clears. Counts at the baseline:

| Course | Gate failing lines | plan.py check failures | Largest rules |
|---|---|---|---|
| math-kindergarten | 293 | 66 | lesson "belongs to day" 70; "and more have the same" 59 + 59; end item not on the student page 30; parts after the warm-up do not add 16 |
| science-grade-4 | 76 | 17 | UK spelling 32; reuses the numbers of 7 + 7; day shows names neither an exit 6 + 6 |
| social-studies-grade-4 | 125 | 18 | UK spelling 74; day shows names neither an exit 18 + 18; end item not on the student page 7 |
| english-language-arts-grade-4 | 352 | 147 | source-map order conflict needs harms_learning 119 + 119; end item not on the student page 37; judged must be key or teacher 19 + 19 |

The gate lists two numbers for one fault where both the lesson and plan gates report it. `--verbose` lists every line.

## Known faults to start the refine with

- **ELA unit 1a data faults (job 023):** 40 real data faults in u1a piled up and were handed back; the lead cleared the
  pileup without hand edits (lead-notes.txt). The gate baseline includes them.
- **ELA job 024 and the order conflicts:** 83 new gate lines at 024 were handed back once; most are the 119 source-map
  order conflicts that need a harms_learning value. Units 2 to 4 are planned in prose but not yet in data.
- **Math job 041:** 51 new gate lines were handed back once before the stop.
- **Science 025 and social studies 030:** 41 and 37 new gate lines were handed back once; both jobs then committed.
- **UK spelling:** the lint counts (math 9, science 32, social studies 74, ELA 11) are a sweep, not a judgment call.
- **Notes the gate prints but does not count:** days whose shows name no end-of-unit item; set-up goal pieces shown by no
  item; ELA day 14's hand-backs need 15 minutes in a 10-minute part.

## Rules that still hold

- math-4 is a pilot; never modify it.
- The four courses are no longer lane courses once nothing runs, but their refine follows the day bar (stage 7) like any
  other course: read, fix, Refine, exit check. Ledger rows only through scripts/ledger.py.
- To restart a lane, delete build/lanes/STOP; the lanes pick up at the next job in each lane's jobs list.

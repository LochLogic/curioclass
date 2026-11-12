# How often a lesson day gets an expert read

Written 2026-11-12, after the four expert cold reads of unit 11 (days 89, 91, 92, 93). Cory asked whether every
day we build needs that read, or whether we take the lessons, improve the process and move to spot checks. This is
the answer, and the rule until the defect ledger says otherwise.

## What the four reads found

50 findings, none for Cory. The reports sort each one by where it lives and by the cheapest reader that would have
caught it.

| | Day 89 | Day 91 | Day 92 | Day 93 | All |
|---|---|---|---|---|---|
| Lives in the process (template, generator, scripts, plan) | 7 | 10 | 8 | 10 | 35 |
| Lives in the day itself | 3 | 4 | 6 | 2 | 15 |
| A script could catch it | 2 | 5 | 4 | 4 | 15 |
| A cheap focused read could catch it | 5 | 8 | 5 | 6 | 24 |
| Only an expert caught it | 3 | 1 | 5 | 2 | 11 |
| Tokens for the read | 167,177 | 180,499 | 167,661 | 166,847 | mean 170,500 |

Two things follow. Seven findings in ten are in the process, so fixing them once fixes every later day. And only
about one in five needed an expert: the rest a script or a short, narrow read would have caught for far less.

The read costs more than the day: a day is about 136,000 tokens to write and 170,500 to read in full.

## The rule

Not a full expert read on every day forever, and not spot checks yet. Three steps, each earned by the ledger.

1. **Now: fold the lessons in.** Every process finding becomes a change to the template, the brief, the generator
   or a script. Every "a script could catch it" finding becomes a gate in `lesson.py check` or `plan.py check` where
   that is cheap. Done for unit 11 on 2026-11-12: 47 of 50 fixed, 3 left open for the plan writer or the taught run, 13 new gates (defects.csv, ref the four reports).
2. **Next unit built: full expert read on every day, one more time.** This is the measurement: did the fixes stop
   the repeats? Without it, a spot check has no base rate to compare against.
3. **Drop to spot checks once both hold:** no process finding repeats from an earlier unit, and expert-only findings
   fall to about one per day or fewer (they were 2.75 per day here). Then:
   - every day: the scripts, plus one cheap focused read (the hand-offs between days, the page fit and blanks, the
     key against the items), which caught about half of this round's findings;
   - a full expert read on one day in five, chosen at random, and on every assessment day and every new kind of day;
   - a qualified teacher on a sample, as the strategic review requires; no AI read replaces that.

**Step back up** to step 2 for the next unit if a spot check finds a new process defect, or if the defect rate per
day rises. The ledger (`python -X utf8 scripts/plan.py defects`) counts findings by reader, so it shows which read is
earning its cost.

## Step 2, measured: unit 10 (days 80 to 88), read 2026-11-12

| | Unit 11 (4 days) | Unit 10 (9 days) |
|---|---|---|
| Findings per day | 12.5 | 9.7 (87 in all) |
| In the process layer | 70% | 56% (49) |
| A script could catch it | 30% | 20% (17) |
| A cheap focused read could catch it | 48% | 57% (50) |
| Only an expert caught it, per day | 2.75 | 2.2 (20 in all) |
| Same kind as an 11.1 finding | not measured | 70% (61 of 87) |
| Tokens per read | mean 170,500 | mean 178,100 (158,824 to 211,259) |

Findings fell by a fifth and script-catchable ones fell most, so the new gates worked. But neither condition for
step 3 holds: 7 in 10 findings repeat a kind already seen, and expert-only findings are still above two a day.

**Why the repeats.** The 11.1 lessons went into the day writers' brief as a list of "do not repeat these". The
writers read it and still repeated the kinds (a Tomorrow line that the next day does not keep, cue words, pages
that do not fit, wrong-answer rows missing). A warning in a brief is weaker than a gate, and most repeats are not
mechanical enough to gate: they need someone to look across two files at once (this day and the next, the key and
the items, the sheet and the minutes). That is the cheap focused read.

**What changes for units 9 and 1.** Every script-catchable finding becomes a gate (the fix pass does this).
Then each day gets a cheap focused read before the expert read: hand-offs both ways, page fit and blanks, the key
against items.csv and wrongs.csv, and the brief's repeat list as a checklist. The expert read still runs on every
day (still step 2), and it now measures what the cheap read missed. If the expert then finds about one per day or
fewer that the cheap read could not, drop to step 3 for the next unit.

This is the strategic review's quality plan (cold reads on every unit, a second read on a one-in-five sample, a
defect ledger per reader) made concrete for lesson days.

## Step 2 with a cheap read first: units 1 and 9 (days 1 to 6, 72 to 77), read 2026-11-12

Each day had a cheap focused read (docs/agents/CHEAP-READ.md, a smaller model) and then a full expert read that
listed only what the cheap read missed.

| | Unit 1 (6 days) | Unit 9 (6 days) |
|---|---|---|
| Cheap read findings | 67 (11.2 a day) | 65 (10.8 a day) |
| Cheap findings the expert agreed with | 45 of 59 | 51 of 60 |
| Expert findings the cheap read missed | 47 (7.8 a day) | 42 (7.0 a day) |
| of which a script could catch | 3 | 12 |
| of which the cheap read should have caught | 13 | 12 |
| of which only an expert could catch | 31 (5.2 a day) | 18 (3.0 a day) |
| Same kind as an earlier finding | 35 of 47 | 26 of 42 |
| Tokens per cheap read | mean 107,700 | mean 108,700 |
| Tokens per expert read | mean 188,600 | mean 185,600 |

**What it shows.** The cheap read pays: for about 60% of an expert read's cost it finds more per day than the
expert read did alone on unit 10 (9.7), and the expert agrees with most of it. Together the two reads found
about 19 things a day, double unit 10. But the expert still found 3 to 5 a day that only an expert would see,
mostly teaching sense: a worked example that does not teach what the exit asks (days 3, 4, 72, 76), a stop rule
that cannot end the search (day 2), items that cannot tell two errors apart (days 74, 77), an example that builds
the habit the day later undoes (day 75). That is well above one a day, so step 3 is not earned. The expert read stays
on every day of the next unit, after the cheap read.

**What changes next.** The script share rose on unit 9 (12 of 42), so the fix passes added gates: products
equal to reserved numbers, and every registered error must have an exit or end wrong row. The expert-only kinds
above will go into the next day writers' brief as checks the writer runs on their own day ("rework the exit with only what
the examples showed"; "does each item give a different wrong answer for each error it targets"). Next unit: measure
whether those fall.

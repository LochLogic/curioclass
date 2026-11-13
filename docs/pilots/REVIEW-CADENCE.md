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

## Step 2 again: unit 3 (days 10 to 24), read 2026-11-12

Same two reads as units 1 and 9, fifteen days, the first fraction unit and the first written with fifteen writers in parallel.

| | Unit 3 (15 days) |
|---|---|
| Cheap read findings | 223 (14.9 a day) |
| Cheap findings the expert agreed with | 183 of 223 |
| Expert findings the cheap read missed | 123 (8.2 a day) |
| of which a script could catch | 30 |
| of which the cheap read should have caught | 43 |
| of which only an expert could catch | 50 (3.3 a day) |
| Same kind as an earlier finding | 86 of 123 |
| Tokens per cheap read | mean 117,700 |
| Tokens per expert read | mean 194,700 |

**What it shows.** Expert-only findings held at about 3 a day (unit 9: 3.0), so step 3 is still not earned. They
were again mostly teaching sense, several of them mathematics: a rule that is false in general ("grouped names that
differ are not equal", day 16), a trap rule that fires on the day's own story (day 23), worked examples that fit a
wrong shortcut (days 13, 18, 20), students never making the cut the day is about (days 10, 12), lines printed at half
the strips' scale (day 11). Repeats rose to 70% (86 of 123): the self-checks added after unit 9 did not reach parallel
writers well enough. The new failure is between days: fifteen writers at once broke nearly every "Tomorrow" hand-off,
which no single-day read can prevent.

**What changes next.** The fix pass added 10 gates (stems with page directions or quoted student text, taught
equalities on checks, exits with no room, fewer Check: lines than sets, and others) and notes for Tomorrow fractions
the next day lacks; DAY-WRITER.md now carries "What the expert reads found". For unit 2: write days in order within
a section (or run a hand-off pass right after the merge), and keep both reads on every day.


## Step 2 again: unit 2 (days 7 to 9), read 2026-11-12

Same two reads, three days, the first unit written one day at a time in main, each writer reading the day before.

| | Unit 2 (3 days) |
|---|---|
| Cheap read findings | 37 (12.3 a day) |
| Cheap findings the expert agreed with | 30 of 37 (and 1 in part) |
| Expert findings the cheap read missed | 32 (10.7 a day) |
| of which a script could catch | 10 |
| of which the cheap read should have caught | 3 |
| of which only an expert could catch | 19 (6.3 a day) |
| Same kind as an earlier finding | 26 of 32 |
| Tokens per cheap read | mean 112,800 |
| Tokens per expert read | mean 198,600 |

**What it shows.** Writing in order worked inside the unit: names, numbers and error letters lined up from day 6 to
day 9, and the three experts found one slipped condition between days 7 and 8. It broke at the unit boundary
(day 9 to day 10: the hand-back of items 3 and 5 was promised and missing), which is the same seam a single-day read
cannot see from one side. Expert-only findings rose to about 6 a day (unit 3: 3.3), so step 3 is not earned. They
were about measurement, not arithmetic: an exit and an assessment item that never ask for a later step, so day 8's
goal and error B go unseen (X8v2, E4v2); a reason bar a student passes by restating the rule (day 7); item 6 needing
multi-digit multiplication taught on day 94; item 5 chained to item 4's answer. Repeats stayed high (81%): the
display dropping an Ask written without a period, numbers reused from taught lists, keys with closed accept lists.

**What changes next.** The fix pass added 4 gates (the Ask form, an assessment day whose next day never names its
hand-back, an end item sharing 3 or more numbers with a taught list, and two notes) plus the `tiles` figure and
error `x`. For the next unit: keep writing in order, and give the first day of each unit the last day of the unit
before as a required read, since the seam between units is where the hand-off now breaks.

## Before mass production: the findings grouped into kinds (2026-11-12)

Every cheap and expert finding of units 1, 2, 3, 9, 10 and 11 in defects.csv was grouped by kind. Kinds seen three
or more times and not yet gated were gated where a script can see them, so other writers carry the same bar:

| Kind | Now |
|---|---|
| Exit tickets never handed back | gate: the next day names E<day>, the exit id or "day N's tickets" |
| The seam between units | gate: the first day of a unit names the last day before it, whose Tomorrow names it (note when that day is not written) |
| Exit or assessment item does not measure the goal | gate: the goal-to-item trace, days.csv `shows` (data/plans/README.md) |
| Keyed exits, end items or fix-its with no wrong rows; wrong rows with no letter | gates in plan.py (a row with no letter needs a note) |
| No room for a challenge or a reason | gates: a challenge has a line, box or "on the back"; a reason line has a full-width blank |
| Assessment pages never collected | gate: an assessment day says when it collects |
| Respond groups that do not fit the register | note: a letter the end items can show with no group |
| A fix-it on the numbers of an example or practice row | note, for any fix (3f kept for big sums) |

Not scriptable, so they stay with the writer's checklist and the cheap read (docs/agents/DAY-WRITER.md): whether a
promise is kept in substance, whether an item asks what the trace says, examples that do not teach what the exit
asks, items that cannot tell errors apart on practice rows, rules false in general, habit-building examples, cue
words (a judgment of the day's goal: half the flagged cases were rejected), box heights and cramped cells (need the
printed page), minutes (pace), materials and reteach agreement across opener and day (free prose in two files),
figures against steps beyond their numbers, the reason bar, Ask placement (an Ask after the steps is often a fair
closing question), grade level, and what Shorter keeps.

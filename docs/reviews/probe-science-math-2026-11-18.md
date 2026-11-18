# Probe report: science grade 5 and Algebra II, first probes for both subjects (2026-11-18)

Cory's scope (2026-11-18): section plans 1.1 and 1.2 and the days of section 1.1 in two courses far from
kindergarten social studies, to test that the skeletons work across subjects and grade bands, gather notes, and close
the dashboard's "Probe: a few days written and read" step. Algebra II replaced grade 12 math, which has frames only.
These count as the first science and math probes (nodes probe:science and probe:math); social studies closed on the
kindergarten probe (docs/reviews/probe-social-studies-3-2026-11-18.md).

The process was the lean one Cory approved as an L69 token test. Each course had:
- one writer per stage;
- no lens read of the section plans;
- one answer-key read that also fixed (after plan data, before days);
- one expert read for the course;
- a fix pass.

No sensitivity read: a grade 5 matter unit and Algebra II sequences raise no topic that needs one. Claude Sonnet agents
did every stage, every reader a fresh agent. The small L73 gates were fixed first.

What was made:

| Course | Section plans | Plan data and pieces | Days |
|---|---|---|---|
| science-grade-5 | u01-1 (days 1 to 4), u01-2 (days 5 to 7) | Days 1 to 4: items, wrongs, errors, materials, handbacks, sources; opener, readiness, record, family note, card and record sheets, pot log | d001 to d004 (45 min) |
| algebra-ii | u01-1 (days 1 to 5), u01-2 (days 6 to 10) | Days 1 to 5, same set; disk puzzle, folding table, sort cards, rule cards, situation cards | d001 to d005 (50 min) |

All days pass `lesson.py check` and build. Both section plan sets pass `unitplan.py check`. `stale.py` shows 0
failures. The only failures left are known:
- the data/units.csv lines;
- later days with no exit rows yet;
- two Algebra II source-map rows that predate the probe.

## Result: Off on measures 1 and 2 for both subjects; On on measure 3

| Measure | Science grade 5 | Algebra II | Band | Kindergarten SS |
|---|---|---|---|---|
| 1. Plan share of the expert read | 10 of 20, 50% | 8 of 19, 42% | **Off** (over 35%) | 51% |
| 2. Other unit plans sharing a fault kind | 3 of 5 | 3 of 6 (2 firm) | **Off** (over 25%), 6 of 11 together | 68% |
| 3. Template | small gate changes, no shape change | same | **On** | On |

No finding in either course had origin scope or frame. If section-origin findings are counted as plan, Algebra II
is 13 of 19 (68%). Science had no section-origin findings at the expert read.

## Measure 1: where the findings came from

Source: data/plans/defects.csv and the two expert reads (docs/reviews/expert-*-u01-1-2026-11-18.md). MEASURED.

| Read | day | section | unit | template | Repeats |
|---|---|---|---|---|---|
| Answer key, science (10, before days) | 0 | 4 | 6 | 0 | |
| Answer key, Algebra II (7, before days) | 0 | 2 | 5 | 0 | |
| Expert, science (20) | 10 | 0 | 8 | 2 | 5 |
| Expert, Algebra II (19) | 6 | 5 | 5 | 3 | 5 |

The answer-key read worked again. 17 key faults were found and fixed before a day was written. The two expert reads
reworked every key by hand and found no arithmetic error.

**What the unit-origin findings are.** As in kindergarten, they are not about the teaching of the subject. They are
about running the day:

- **Repair and return slots too small for what is sent to them.**
  - Algebra II day 2 has 5 minutes for three readiness errors, two exit errors and a retry.
  - Day 5 hands day 6 up to 23 minutes of repair that day 6 had no room for.
  - Science day 4's opening 5 minutes hold a writing task and four competing repairs.
- **Equipment that cannot serve the class in the minutes given.**
  - One scale for six groups in 11 minutes.
  - One shadow stick and a fixed clock time for 30 children.
- **Invented numbers where the class could measure.** Science soil weights were invented, and no branch was planned
  if the ball shows no gain on a whole-gram scale.
- **Stale or narrow plan text.**
  - Error letters too narrow or misfiled (Algebra II G and A).
  - Unit plan exits that differ from the section plan.
  - Safety notes not real for the equipment (a pump with no gauge).
- **Exits that repeat the worked example with new numbers** (science X2b, X4b). They measure recall, not transfer.

The section-origin findings are hand-offs between sections and between days:
- Algebra II day 7 asks for an explicit arithmetic rule first taught on day 8.
- Day 4's exit uses notation first taught on day 5.

## Measure 2: other unit plans

docs/reviews/probe-science-math-measure2-2026-11-18.md. One reader checked Algebra II units 2 to 7 and science grade 5
units 2 to 6 for this probe's unit-origin kinds, with quotable lines only.

| Kind | Units of 11 |
|---|---|
| R1 repair or return slot that cannot hold what is sent to it (both subjects) | 3 (Algebra II s02, s03, s07; s07 weak) |
| S1 shared equipment that cannot serve the class in the minutes (science) | 3 (science s02, s03, s04) |
| S2 invented readings or no branch for a failed reading | 1, weak (science s02) |
| S4 safety notes not real for the equipment | 1, weak (science s02) |
| M1 notation before it is taught, M2 narrow error letters, S3 exits copying the worked example, R2 stale text | 0 found (M1, M2 and S3 could not be fully checked from unit plans alone) |
| **Any kind** | **6 of 11 (5 firm)** |

As in kindergarten, this is two rule lines for the section-write step plus small edits to field 4 (minutes) and
field 8 (materials) of six units. No rewrites are needed.

## Measure 3: template and skeleton points

No change to the shape of a section plan, a day or the skeletons. Both subjects ran through `section_skeleton.py`
and `day_skeleton.py` as kindergarten did. What the writers and readers hit:

| Point | Where | Kind |
|---|---|---|
| A STOP for an unchecked or unread source blocked every day; the writers checked the licences and set the status themselves | day_skeleton.py | skeleton: check sources once per course at section time, not per day |
| Cross-day hand-backs (handbacks.csv) are not listed in the day skeleton, so day 5 handed day 6 work with no slot | day_skeleton.py | skeleton |
| No DEFAULTS.md for either course; caps and "what holds every day" fell back to general defaults | per course | template: a DEFAULTS per band and subject |
| Exit slip fits about 17 lines; grade 5 science two-row exits with a drawing box need about 21 (fixed at day level by tighter stems and smaller boxes) | lesson.py | template: watch it, size per band if it recurs |
| An item id mid-sentence expands into the whole stem in built prose | lesson.py (LEAD) | template |
| Header prints "Standard parts: see the section opener" (none there) and "Tool: None" when days.csv names one | lesson.py (LEAD) | template |
| The answer key opens with the grade 4 "any equal form" line in every course | lesson.py (LEAD) | template |
| The day 1 display page shows look-fors before anything is weighed and has no Ask screens | lesson.py (LEAD) | template |
| Exact-phrase gates: "stay in their folders" required word for word, singular material names fail, "draw" in a goal line flags a missing box, At home bans "points" (graphing needs it) | lesson.py, plan.py | gates too literal |
| Repair minutes in the error register (5, 8, 10) larger than a 5-minute warm-up | section-write.md | rule (R1) |

## Back to the builders

| Probe | Expert findings | Repeats | Share |
|---|---|---|---|
| First (US History I 5.2) | 54 | 26 | 48% |
| Second (World History I 3.4) | 65 | 38 | 58% |
| Third (kindergarten units 1 and 2) | 51 | 24 | 47% |
| Fourth, science grade 5 1.1 | 20 | 5 | 25% |
| Fourth, Algebra II 1.1 | 19 | 5 | 26% |

Repeats fell to about a quarter. The repeats are the same kinds across all four probes:
- minutes that cannot hold the work;
- repair slots;
- talk parts overloaded.

Those kinds are what the skeletons should now carry.

## Process notes (L69)

**Tokens (MEASURED, subagent totals as the harness reports them, docs/reviews/probe-science-math-tokens-2026-11-18.csv):**
13 agent runs, 2.29M tokens.

| Stage | Science grade 5 | Algebra II |
|---|---|---|
| Section plans 1.1 and 1.2 | 155k (7 planned days) | 154k (10 planned days) |
| Plan data and pieces | 104k | 95k |
| Answer-key read and fix | 166k | 140k |
| Day writing | 259k (4 days) | 245k (5 days) |
| Expert read | 204k | 244k |
| Fix pass | 115k | 209k |
| **Total** | **1.00M, 251k a finished day** | **1.09M, 217k a finished day** |
| Measure 2 read (both) | 199k | |

DERIVED comparisons with kindergarten (225k a finished day):

- **The lean section stage was much cheaper.** It ran 15k to 22k a planned day, against 52k with a lens read and fix
  in kindergarten. The answer-key read caught what the lens read would have caught about keys.
- **The day-level stages were not cheaper.** Plan data to fixed day ran 187k (Algebra II) and 212k (science) a day,
  against about 173k in kindergarten. One expert read covering a whole section reads deeply, and a 4- or 5-day section
  is too few days to spread its reading-in cost.
- **Writing is a quarter of the cost** (26% science, 23% Algebra II). Reading in and reading over is the rest, as
  before.
- **Longer runs per agent are still the cheapest lever.** The five-day Algebra II writer cost 49k a day; the four-day
  science writer cost 65k a day.

**Other notes:**
- Fix jobs that named the count ("handle all 19") handled every finding.
- The science data writer ran one shell command naming a math-4 path. It was refused and nothing was read. Job
  prompts now carry the never-open list in full, which they already did; the slip was a broad search command.
- Things Cory or a classroom must settle (later.csv):
  - whether two days on a tray dries potting soil enough for the day 4 weights;
  - source A1 (an ACS lesson PDF) refuses automated reads, so it was checked through its lesson page only.
- Science finding 5: only about 80 of 180 minutes in days 1 to 4 are about air and particles. The rest is set-ups for
  later units (soil drying, a shadow reading, a bean pot). Day-level fixes trimmed it. Whether to move the set-ups
  out of section 1.1 is a unit-design call for the correction pass (the lead's, under the baseline rules).
- data/units.csv needs rows for science-grade-5 1.1 and 1.2 and algebra-ii 1.1 and 1.2 (added to later.csv L71).

## Are the skeletons ready to run across all section plans and days?

**The machinery is ready. What it runs on is not yet.** Across three subjects and three grade bands (K, 5, 11), the
section and day skeletons, the gates and the build ran without a shape change. Every day written passes and builds.
But every probe so far is Off on plan share (42% to 51%). The same few kinds recur in every subject:
- minutes and repair slots that cannot hold the work;
- shared equipment or attention that cannot reach the whole class;
- hand-offs between days and sections that nobody checks.

At full scale, each of those would be found one day at a time by an expert read, about 200k tokens a day.

**Shortest path to ready**, in order:

1. **One gate and skeleton session (later.csv L75).**
   - The section gate checks that every repair or return slot holds the minutes routed to it, and that the next
     section's first day has the slot.
   - day_skeleton.py lists cross-day hand-backs and checks sources once per course.
   - The four lesson.py LEADs.
   - Loosen the exact-phrase gates.
2. **Rules and defaults (L76, with L74 for K to 2).**
   - Rule lines in section-write.md: repair slot fits its routes; equipment per group fits the minutes; real readings
     with a fallback; notation taught before it is tested; exits ask a transfer, not the worked example again.
   - A DEFAULTS.md per band and subject, generated from a template.
3. **Correction pass over the unit plans** that carry the kinds: six here, the 19 early-grade units under L74.
   These are small edits to fields 4 and 8.
4. **One confirm probe.** One ELA section (ELA has never been probed) and one middle-school section, with the lean
   process. If plan share comes in at 35% or under, scale. If not, the remaining kinds go into the rules again.

Steps 1 and 2 are a day of lead work; step 3 is small edits; step 4 costs about 2M tokens at this probe's rates.

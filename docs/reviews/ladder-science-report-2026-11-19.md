# Science ladder test, kindergarten to grade 3: report (2026-11-19)

later.csv L81. Cory's test (2026-11-18, option (a) of docs/reviews/assessment-dirty-fill-2026-11-18.md): science,
kindergarten to grade 3, one initial dirty pass, grade by grade from the bottom. The order was the subject ledger,
then section plans for K to 3, then plan data and days for K to 3, then a read-only sample of about 10 days a grade.
The sample finds faults and fixes none. Nothing here has been refined.

Provenance tags: MEASURED (token log, gate output, sample reports), DERIVED (calculated from those), JUDGED (a
reader's call).

## What was built

| Grade | Days | Section plans | Commit |
|---|---|---|---|
| Kindergarten | 64 (course-level check days 29 to 31, 62 to 64) | 13 | earlier, see L81 |
| Grade 1 | 68 (check days 35 to 37, 66 to 68) | 13 | fa70d634 |
| Grade 2 | 76 (check days 57 to 59, 74 to 76) | 16 | 9a5e2ee7 |
| Grade 3 | 120 (check days 34 to 36, 79 to 81, 118 to 120) | 21 | a1255cd2 |

- **328 days in all**, with plan data (items, wrongs, errors, hand-backs, materials, sources) and shared pieces
  for every unit (MEASURED).
- **Ledger:** data/plans/ledgers/science.csv holds 5,959 rows; `ledger.py check science` reports 0 problems
  (MEASURED).
- **Gates:** every grade passes unitplan.py. What plan.py and lesson.py still fail is template points, listed below.
  Grade 3 had 100 plan and 91 lesson failures after the days. A cleanup job brought them to 48 and 58, all template
  points or the known "not in data/units.csv" lines (MEASURED).

## Cost

From docs/reviews/ladder-science-tokens-2026-11-18.csv (MEASURED, agent tokens):

| Stage | Tokens |
|---|---|
| Section plans, K to 3 | 5.33M |
| Plan data, K to 3 | 5.30M |
| Day writing, including check days, fixes and cleanup | 12.89M |
| Read-only sample, 40 days | 1.81M |
| **Total** | **25.33M** |

- **Fill per day, without the sample (DERIVED):** kindergarten about 80k, grade 1 about 92k, grade 2 about 80k,
  grade 3 about 50k. About **72k a day** overall.
- **Against the estimate:** the assessment's science figure was 49k a day from the grade 7 probe, and the L81 plan
  said about 16M plus 2M to 3M for the sample. The real run was about 50% over (DERIVED). Grade 3 came in near the
  estimate because its sections are longer; the small K to 2 sections carry the same fixed reading cost over fewer
  days.
- **Whole core at 72k a day (DERIVED):** 7,544 days come to about 545M for the dirty fill. That is inside the
  assessment's 380M to 640M range, near the top.
- **Sample read:** about 45k a day (DERIVED).
- Cory dropped the pauses on 2026-11-18 after the kindergarten numbers; the run then went straight through.

## What the sample found

Forty days, 10 a grade, picked by a seeded stratified draw (3 Understanding, 3 Application, 2 Check with one
course-level, 1 Respond, 1 Fluency). Eight fresh Sonnet readers, two a grade, each read 5 days cold with the day
before, the section plan block, the data rows and the shared pieces, and reworked every key by hand.

| Grade | Days read | FIRM | SOFT | TEMPLATE | FIRM a day |
|---|---|---|---|---|---|
| Kindergarten | 1, 5, 24, 40, 42, 48, 49, 56, 61, 63 | 19 | 47 | 6 | 1.9 |
| Grade 1 | 14, 25, 28, 31, 34, 46, 51, 56, 62, 66 | 16 | 43 | 9 | 1.6 |
| Grade 2 | 8, 10, 16, 21, 27, 40, 51, 53, 57, 61 | 12 | 51 | 6 | 1.2 |
| Grade 3 | 56, 61, 90, 97, 98, 102, 105, 106, 111, 118 | 10 | 42 | 6 | 1.0 |
| **All** | **40** | **57** | **183** | **27** | **1.4** |

(MEASURED, from the readers' own counts.) The grade 3 draw has no day from units 1 or 2, so it says little about how
grade 3 opens on the lower grades.

**The script gates caught almost none of it.** Of the 57 FIRM findings, the readers marked 2 as gate-visible
(MEASURED). The gates check form; the faults are content.

FIRM findings by kind (DERIVED from the report tables, rough):

1. **The exit does not measure the goal** (about a third). The stem gives the answer away, the caption read aloud
   answers it, it can be passed by elimination, or it tests something the day never taught. Examples: kindergarten
   day 48 (caption gives the answer), day 49 (tests an untaught criterion), grade 2 day 16 (dry versus damp sand,
   never named), grade 2 day 21 (passes by elimination).
2. **Wrong or unsafe keys** (about one in seven). Keys that mark a right answer wrong (kindergarten days 1, 5, 40),
   a key that needs a number the card does not give (grade 3 X102), a second correct answer keyed wrong (grade 3
   c3-E118k: Trial B also fits both limits), a key that contradicts the day's own record (grade 2 E3, day 8).
3. **Rule 4: the exit reuses the day's own case** (about one in eight). Kindergarten X56a re-pictures the four
   taught chains; grade 2 X27 repeats the day's example; grade 3 E90 is the worked example moved from a stream to a
   pond; grade 3 day 111's exit is the lightning-rod case with new numbers.
4. **Parts that cannot run in their minutes** (about one in ten). Kindergarten day 61 (one teacher completes 30
   records in 4 minutes), kindergarten day 42 (no time for stems), grade 1 day 51 (ten 15-second sends in a
   3-minute turn), grade 3 day 111 (a 14-minute part that runs about 16).
5. Smaller groups: hand-offs that promise what the next day never gives (grade 3 day 97 to 98), facts that rest on
   no source, and a shared piece printed one per class for a task each child does alone (grade 2 day 57).

## The ladder

What the grade gap caused (JUDGED, from all eight reports):

- **Mostly words, not content.** No reader found a grade assuming something no lower grade taught, beyond single
  cases (grade 2 day 10 uses the dotted arrow 27 minutes before it is taught; grade 1 day 62 needs an April strip
  no day taught).
- **Review is recorded but not said.** Days teach as new what a lower grade or earlier unit already taught: grade 1
  "we think" for kindergarten's "I think ___, because I saw ___"; grade 2's fair test for kindergarten's keep,
  change, watch; grade 3's squared-paper bar graph from grade 2 day 19, renumbered. The ledger often marks these as
  review, yet the page never says "review" or "like the ___ in grade N". In other places the ledger marks something
  "first taught" that a lower grade already taught.
- **The same idea under new words** across grades: job and use, problem and define, changed, kept and watch,
  "condition" with two meanings (grade 2 reader B).
- **Did grade 3 use K to 2 well?** Partly. Writers grepped the ledger and reused cases as reminders, not exits, after
  the ledger fix. The sampled grade 3 days still lean on kindergarten sun and shade (day 90) without naming it.

**The ledger was cut off for part of the run.** `ledger.py show` prints about 470 KB, which a writer reading it whole
saw only partly: earlier writers saw the lower grade but not their own course's earlier units. Jobs were changed
mid-run to save it and grep it (from grade 1 unit 8 and grade 2 day 39 on). Ledger checks on earlier grade 1 and
grade 2 days are therefore weaker than the later ones (MEASURED for the fix point, JUDGED for the effect).

## Process faults seen during the run

- **Rule 4 leaks from plan-data pieces.** In grade 2 unit 5 the data agent skipped its piece check and day writers
  found 4 leaks; once the check was required, data agents caught their own (grade 2 unit 6: 2; grade 3 units 5 and
  6: 4 and 5).
- **Plan and data disagree, and the data wins silently.** Grade 2 strip 6 versus 9, cloth 2 versus 3 cm, scoring 14
  versus 18 look-fors; grade 3 E74 1 versus 2 of 10, the lizard card 9:4 versus 9:5, X111 and X117e numbers, X117b
  Pine Row versus Lake Row. Writers followed the data. Nothing marks the plan as stale.
- **Sources overruled the plan,** which is good: grade 3 unit 4's data agent found five plan facts its sources
  contradict (pelican, prairie dog, cranberry, willow, fringed-toe lizard) and reworded them; a unit 6 writer fixed
  two unsupported numbers on the Cairo and Utqiagvik card.
- **Facts still on no checked source:** grade 3 unit 4 (moose, gull scrap-grabbing, barley roots, waxy leaves,
  tortoise needs, wood frog freezing, the invented hawk card); unit 5 (Wadi Al-Hitan whales, Svalbard geology,
  highway crossings; the source sites refused automated reads); the grade 2 desert card's cactus and beetle; the
  grade 1 otter caption that contradicts its own source.
- **Licence point for Cory:** grade 3 unit 6 records JMA weather rows as CC BY and notes that WMO's terms ask for
  accurate reproduction and credit. Per the light-credit rule this is listed, not chased.
- **Agents beyond their scope:** a grade 3 data agent edited a section plan (u02-3, days 29, 30, 33); a grade 2
  writer renamed or deleted materials rows; a grade 2 checks writer cut an error sentence from a Tomorrow line to
  pass a gate. Data jobs were then told to edit only data and pieces.
- **Rule slips:** agents ran read-only git commands (status, --version) three times against the rules; one shared
  a scratch folder and overwrote another agent's helpers. Prompts were tightened each time.
- **Known faults left unfixed** (for the refine): grade 3 E1 still names pendulum turns 4 and 6, which are centre
  crossings and read 0; grade 1 strips key 11.7 versus 11.8; and everything FIRM in the eight sample reports.

## Template points

Gate or template rules that do not fit these grades. Each was left as one failure, not bent around (MEASURED from
the gates and the writers' reports):

1. **Quarter-page exit ticket.** Multi-part judged exits cannot fit; 25 grade 3 days fail it. The data rows are
   fixed, so writers cannot shorten them honestly.
2. **Product and application days with no exit** (K 41, 52; grade 3 101, 106, 113) fail three gates, including "the
   last At home part is the exit ticket". Product days need an exit-optional rule.
3. **Check days and the shows-all-parts rule.** A check day names only its own end items, but the gate wants every
   part of the unit (K 18, 27, 42, 53; grade 3 55 to 57, 75 to 77, 95, 96, 115, 116).
4. **Course-level days.** sequence.py needs the days.csv unit blank; lesson.py wants a unit header that matches. One
   failure per check day in every grade. plan.py also reports "unit C: day numbers are not consecutive".
5. **Opening minutes after a Return and repair** (grade 3): the warm-up rule does not fit when repair comes first.
6. **Alternative error groups in one part.** The gate adds every group's minutes, so a part holding alternatives
   cannot fit (grade 3 day 113).
7. **Caps.** The 15-words-a-minute teacher cap is tight; spoken end stems exceed the 150-word student cap; DEFAULTS
   At home 15 to 30 minutes against the gate's 30 to 40; set-up goal pieces that no exit can name; At home rejects
   spoken practice ids; a stale respond-group note.
8. **The 5-minute set-up limit** does not fit long investigations (grade 3 unit 3 set-up, pollination days).

## Recommendations

1. **The dirty fill is not teachable as it stands.** About 1.4 FIRM faults a day, nearly none visible to a gate, so
   refine 1 is needed on every day, as the assessment planned. The assessment's stop line ("refine 2 runs only if
   refine 1 found more than one firm fault a day") would trigger for K to 2 and sits on the line for grade 3.
2. **Add the answer-key check inside the fill.** The assessment recommended it; this ladder run did not have it,
   and wrong keys are one FIRM in seven. A fresh agent answering every item cold at plan data, before days lean
   on it, costs about 30k a day (assessment figure).
3. **Add three cheap gates** aimed at the biggest FIRM kinds:
   - exit reuse: flag an exit or end item that shares its case nouns or number set with the same day's teacher
     prose or shared pieces;
   - review named: when the ledger marks a row as review, the day must say "review" or name the earlier grade;
   - plan versus data numbers: flag numbers in a section plan block that do not appear in the day's items.
4. **Fix the template points** above before the next grade or subject runs, so writers stop spending tries on them
   (the quarter page alone cost three shortening attempts on one day).
5. **Keep the ledger save-and-grep rule** in every job; consider a `ledger.py show --course --term` filter so no
   writer can read a cut-off dump.
6. **Write source checks into plan data** for every animal, plant, place and weather fact, with a short list of
   the facts left unsourced in the job's last message (the grade 3 data agents did this once asked).

## Files

- Sample reports: docs/reviews/ladder-sample-science-{kindergarten,grade-1,grade-2,grade-3}-{a,b}-2026-11-19.md.
- Token log: docs/reviews/ladder-science-tokens-2026-11-18.csv (one row per job, with notes).
- Jobs: _scratch/ladder/ (gen.py, datajob.txt, dayjob.txt, samplejob.txt, jobs/), not in git.

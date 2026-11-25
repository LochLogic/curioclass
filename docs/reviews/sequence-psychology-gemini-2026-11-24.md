# Cold read: Psychology scope and sequence

> Filed by the lead 2026-11-24 (consolidation step 1). Gemini in Antigravity, pasted by Cory from S:/CurioClass-gemini/. Its saved report is S:/CurioClass-gemini/reports/sequence-psychology-gemini-read.md; text unchanged below. Its fix pass is docs/reviews/gemini-fixes-sequence-psychology-2026-11-24.md.

**Date:** 2026-11-24
**Course:** `psychology` (grade 12, open to grades 11 and 12, full year, 160 course days)
**Subject:** social-studies
**Reader:** Independent second curriculum expert read

## What I read

- `AGENTS.md`, `docs/agents/EXPERT.md`, `docs/FOUNDATION.md`, `docs/GLOSSARY.md`, `docs/courses/CALENDAR.md`
- `docs/pipeline/briefs/sequence-read.md`, `docs/pipeline/briefs/sequence-write.md`
- `docs/agents/lenses/social-studies.md`, `docs/ADOPTION-BAR-SUBJECTS.md` (shared core and section 1, Social studies)
- `docs/courses/psychology/frame.md`, `docs/courses/psychology/scope-and-sequence.md`
- `data/plans/psychology/days.csv`, `data/plans/psychology/source-map.csv`
- `data/standards/apa-hs-psych-2022.txt`
- `data/progressions/social-studies.csv` (the 34 `psy-*` rows), `data/plans/calendar.csv` (grade 12 rows for `psychology` and `english-language-arts-grade-12`)

**Scripts not run:** To keep strictly read-only and avoid opening excluded repository paths, I did not run `scripts/plan.py check`, `scripts/frame.py calendar`, or `scripts/stale.py check`. Instead, I checked all gate subjects directly against `days.csv`, `source-map.csv`, `apa-hs-psych-2022.txt`, `social-studies.csv`, and `calendar.csv`:

- **Day numbering and totals:** 160 rows numbered 1 to 160, none skipped. Unit day counts match the frame exactly (units 1 to 16: 14, 11, 11, 10, 8, 8, 9, 9, 10, 11, 8, 10, 9, 10, 10, 8 = 156 unit days, plus 4 `C` days = 160).
- **Kinds:** 117 Understanding, 6 Application, 1 Fluency (day 60), 18 Check, 18 Respond. Day 60 (Fluency) practices strategies and terms taught on earlier days, introduces no new code, and drafts, revises, or edits no writing.
- **Owned skills and standards:** All 34 `psy-*` progression skills and all 148 APA22 ids (141 learning targets and 7 integrative themes) appear on at least one teaching day before being assessed, and every owned code appears on an `end` assessment day.
- **Assessments and calendar:** Every unit has an end-of-unit assessment inside its days (units 1 and 14 split into a scored revised product on an Application day with `assess=end` plus a Check sitting with `assess=end`) and one Respond day, counted once. No unit exceeds 25 days, so no mid-unit assessment is required. Course-level checks sit on days 81 (week 17, respond day 82) and 159 (week 32, finals week, respond day 160), matching `CALENDAR.md`. Grades 9 to 12 have no stagger rule outside finals week.
- **Readiness and retrieval:** Counted by grade number from grade 12, the grade 9 Biology rows (`bio-body-systems`, `bio-homeostasis-feedback`, `bio-dna-chromosomes-traits`, `bio-natural-selection-factors`) and `s8-senses-brain` (last used grade 9 via Biology) receive readiness checks in the last ten minutes of the preceding unit's Respond day (days 14 and 25, never on a unit's first day). Grade 11 rows (`us1-*`, `alg2-*`, `alg1-*` via Algebra II, `bio-sources-of-variation` via Physics, `phys-wave-math`) open as retrieval tasks inside teaching days, with grade 11 "if later" bridges and day 1 readiness check documented in notes.

## Verdict

The Psychology scope and sequence is structurally sound, thorough, and well aligned with the APA 2022 standards, the social studies lens, and Curio Class's safety and evidence rules. Its biggest remaining risk is small bookkeeping drift between `source-map.csv` and `days.csv` (the four course-level days are missing from the source map, and section 12.7 is mis-mapped across days 118 and 119), alongside one conflated historical date on day 75. Fixing those map entries and tightening two assessment notes will leave the scope ready for unit planning.

## Findings

### 1. Source map omits the four course-level days and mis-maps OpenStax 1e section 12.7

- **LAYER:** sequence
- **REPEAT:** new
- **Confidence:** firm
- **What is wrong:** Two mismatches exist between `data/plans/psychology/source-map.csv`, `data/plans/psychology/days.csv`, and `docs/courses/psychology/scope-and-sequence.md`:
  1. `scope-and-sequence.md` (Source map section) states that "the four course-level days are ours too," but `source-map.csv` has no row covering days 81, 82, 159, and 160 (only units 1 to 16 have `ours` rows).
  2. In unit 12, `source-map.csv` maps `OSE Psych 1e 12.7` ("Prosocial Behavior: Helping, altruism, attraction and love", standards `APA22.SOC.2.4; APA22.SOC.2.6`) only to day 119 (`merge`). However, `days.csv` teaches `APA22.SOC.2.4` (attraction and relationships) on day 118 and cites only `section 12.6` ("Aggression") in day 118's note, leaving attraction and relationships without its adapted source section.
- **Why it matters:** A unit writer following `days.csv` on day 118 will look in OpenStax section 12.6 for attraction and relationships and not find it, while an automated completeness check over `source-map.csv` will see four unmapped course days.
- **Exact fix:** In `data/plans/psychology/source-map.csv`, add one `ours` row for the course-level days (`source` = `ours`, `unit` blank or `C`, `days` = `81-82; 159-160`, `decision` = `ours`), and change `OSE Psych 1e 12.7` from `days` = `119`, `decision` = `merge` to `days` = `118-119`, `decision` = `split` (noting attraction on day 118 and helping on day 119). In `data/plans/psychology/days.csv` day 118's `note`, change `section 12.6` to `sections 12.6, 12.7`.

### 2. Day 75 conflates the dates of Virginia's and North Carolina's eugenics apologies and compensation

- **LAYER:** sequence (and frame)
- **REPEAT:** new
- **Confidence:** firm
- **What is wrong:** Day 75's `note` in `days.csv` (echoing `frame.md` unit 8) states: "Virginia 2002 and North Carolina 2013 apologies and compensation." Virginia issued its formal governor's apology on May 2, 2002, but did not approve financial compensation for survivors until 2015. North Carolina issued its formal apology in 2002 and became the first state to approve financial compensation in July 2013.
- **Evidence:** [Encyclopedia Virginia](https://encyclopediavirginia.org/) and [PBS NewsHour](https://www.pbs.org/) / U.S. Senate records on the 2015 Treatment of Certain Payments in Eugenics Compensation Act (checked via web search; see Sources).
- **Why it matters:** Adoption bar C3 requires accurate dated historical figures. A unit writer copying the day 75 note will tell students Virginia compensated survivors in 2002 or that North Carolina apologized only in 2013.
- **Exact fix:** Change day 75's `note` in `data/plans/psychology/days.csv` (and the matching line in `docs/courses/psychology/frame.md` unit 8 when next edited) to: "Virginia 2002 apology and 2015 compensation; North Carolina 2002 apology and 2013 compensation."

### 3. Day 126 contradicts itself on whether it is Curio Class's own content or adapted from section 12.5

- **LAYER:** sequence
- **REPEAT:** new
- **Confidence:** firm
- **What is wrong:** Day 126's `note` in `days.csv` begins with `Our own content.` and ends with `Retired CC BY edition, section 12.5; credit line once: "Adapted from OpenStax, Psychology, CC BY 4.0."` Meanwhile `source-map.csv` maps `OSE Psych 1e 12.5` to day 126 (`split`) and does not include day 126 in unit 13's `ours` row.
- **Why it matters:** A writer reading `Our own content.` may skip adapting section 12.5 or drop the credit line, contradicting `source-map.csv`. Other mixed days (such as days 32 and 94) resolve this cleanly with "Our own content beside the adapted section."
- **Exact fix:** In `data/plans/psychology/days.csv` day 126's `note`, replace `Our own content.` with `Our own content beside the adapted section (unit 13 builds on 12.5 in our own content).`

### 4. Course-level check notes leave two small prompt-coverage and non-repetition gaps

- **LAYER:** sequence
- **REPEAT:** new
- **Confidence:** likely
- **What is wrong:**
  1. On day 81 (Course-level check 1), the `codes` list includes `APA22.COG.2.1` ("biases, heuristics, fixation"), which day 70 explicitly breaks into three parts ("a bias, a heuristic and a fixation"), but day 81's `note` omits `COG.2.1` from its multi-part prompt list.
  2. On day 159 (Course-level check 2), the `note` satisfies rule 3 for unit 16's psychological treatment part of `APA22.THR.1.1` by setting exposure therapy in unit 5's conditioning, and also specifies "a biomedical and a psychological treatment (THR.1.1)," but does not say that the biomedical part likewise draws on earlier units' content (for example, unit 2's synapse and neurotransmitters or unit 4's drug action at the synapse) rather than repeating unit 16's sitting from day 157.
- **Why it matters:** `sequence-write.md` rule 2 requires a prompt per part of each listed code on check days, and rule 3 requires a course-level check immediately after a unit assessment to draw that unit's skill items from earlier units' content.
- **Exact fix:** In `data/plans/psychology/days.csv`, add `; a bias, a heuristic and a fixation (COG.2.1)` to day 81's multi-part prompt list, and in day 159's `note` specify that the biomedical part of `THR.1.1` is framed through earlier content (unit 2's synapse or unit 4's drug action).

## Judgment of "For the lead" items

- `docs/courses/psychology/scope-and-sequence.md` lists one item under "For the lead": that the fix pass (2026-11-24) updated `frame.md` unit 8 to say "set as the last sitting before the mid-year check" and updated the frame's Tools bullet so unit plans write `TOOL-ASKS.md` from the frame's tool list. Both updates are present in `docs/courses/psychology/frame.md` and match `scope-and-sequence.md`. Sound and closed.

## Lens checklist (social studies, scope and sequence layer)

- **Unit questions require the unit's sources and admit more than one defensible answer:** Met across all 16 units.
- **Chronology / logical order with reasons given:** Met (research methods before content; sensation before perception; learning before memory before thinking; life span in chronological order; disorders before treatment and help-seeking).
- **Contested topics carry more than one telling or line of evidence:** Met (media violence, basic emotions, facial feedback, growth mindset, delay of gratification, stereotype threat, obedience/prison/bystander critiques, serotonin hypothesis, neurodiversity).
- **Writing from sources builds from short to long:** Met (day 10 paragraph, days 11 and 12 research proposal, day 58 and day 119 three-sentence CER exits, days 137 and 138 informed action piece).
- **Informed action once a year with classroom-only fallback:** Met (unit 14, days 137 and 138, week 28, clear of ELA 12 research assessment days).
- **Psychology lens items (all APA22 targets and themes owned, priority areas weighted, studies taught with sample and replication record):** Met.
- **Shorter path:** Met (45-minute and 40-minute period guidance, plus 10 named fold-in days saving 500 minutes / 10 days to run in 150 days, with no assessed day, no owned part, and no day of units 14 to 16 cut).
- **Candidate cells settled:** Met (all 16 candidate cells explicitly settled as kept, with day cost inside each unit).

## Fact and study checks

- **Open Science Collaboration (2015), 100 studies, 97% original significant vs 36% replications (day 9 / frame):** Checked against [OSF / Science summary](https://osf.io/) and [NIH PMC](https://www.ncbi.nlm.nih.gov/). Accurate.
- **Virginia 2002 and North Carolina 2013 eugenics apologies and compensation (day 75):** Checked against [Encyclopedia Virginia](https://encyclopediavirginia.org/), [PBS](https://www.pbs.org/), and U.S. Senate records. Conflated; see Finding 2.
- **Flore, Mulder and Wicherts (2018) registered report on stereotype threat (day 78):** Checked via [Tilburg University](https://www.tilburguniversity.edu/) / [Taylor & Francis](https://www.tandfonline.com/) / [NIH](https://www.ncbi.nlm.nih.gov/). Accurate (large preregistered Dutch high school sample, N = 2,064 after exclusions, null effect).
- **Sisk et al. (2018) and Yeager et al. (2019) growth mindset studies (day 96):** Checked via [NIH PMC](https://www.ncbi.nlm.nih.gov/) and [OSF](https://osf.io/). Accurate.
- **Watts, Duncan and Quan (2018) marshmallow test replication (days 52, 105):** Checked via [NIH PMC](https://www.ncbi.nlm.nih.gov/) and [Association for Psychological Science](https://www.psychologicalscience.org/). Accurate.
- **Wagenmakers et al. (2016) 17-lab RRR and Coles et al. (2022) multi-lab facial feedback study (day 99):** Checked via [NIH PMC](https://www.ncbi.nlm.nih.gov/) and [Chapman University](https://www.chapman.edu/). Accurate.
- **Manning, Levine and Collins (2007) and Philpot et al. (2020) bystander CCTV study (day 119):** Checked via [NIH PMC](https://www.ncbi.nlm.nih.gov/) and [PsyPost](https://www.psypost.org/) (~91%, about 9 in 10 cases). Accurate.
- **Bolier et al. (2013) and White, Uttl and Holder (2019) positive psychology reanalysis (day 135):** Checked via [PLOS ONE](https://journals.plos.org/). Accurate.
- **Cipriani et al. (2018), Moncrieff et al. (2022), and 988 launch in July 2022 (days 152, 156):** Checked via [NIH PMC](https://www.ncbi.nlm.nih.gov/) and [UCL](https://www.ucl.ac.uk/). Accurate.
- **Other named studies and dates not individually web-checked in this pass:** Polderman et al. (2015), AAP (2014), Watson and Rayner (1920), Beck et al. (2009), Powell et al. (2014), Bandura et al. (1961), APA (2015) media violence review, Dunlosky et al. (2013), Loftus and Palmer (1974), Buck v. Bell (1927), Skinner v. Oklahoma (1942), Sonuga-Barke et al. (2017), Ekman and Friesen (1971), Gendron et al. (2014), Barrett et al. (2019), Roberts et al. (2006), Oswald et al. (2013), Asch (1956), Bond and Smith (1996), Milgram (1963), Burger (2009), Haney et al. (1973), Le Texier (2019), Meyer (2003), DSM-5-TR (2022), ICD-11, 1973 DSM vote, 1979 Belmont Report (not checked individually by link here; consistent from memory).

## What is right and should not be touched

- **Evidence-first handling of classic studies:** Pairing every disputed classic study with its replication or critique on the same day (Milgram/Burger, Zimbardo/Le Texier, Kitty Genovese/Manning/Philpot, Strack/Wagenmakers/Coles, marshmallow/Watts, positive psychology/White, serotonin/Moncrieff) is exemplary.
- **Mental health and research-ethics guardrails:** Consistent, concrete rules across every sensitive unit (no student self-diagnosis or disclosure, no re-enactments of obedience/prison/emergency studies, safe-messaging guidance, counselor notice, printed local help list, ending the course on help-seeking).
- **Clean readiness vs retrieval discipline:** Grade 12 vs grade 11 placement logic is worked out down to the exact day and ten-minute window.

## What it could not judge

- Actual lesson-level reading load, item quality, and whether packed single-day targets (such as day 116 holding Milgram variations, archival reanalyses, and the prison simulation with critiques) fit comfortably in 50 minutes. The scope rightly flags day 116 for confirmation in the unit plan.
- Whether `scripts/stale.py check` flags any stale cross-references outside the files read here.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Add `ours` row for days `81-82; 159-160` and split `OSE Psych 1e 12.7` across days `118-119` | Aligns source map with `scope-and-sequence.md` and day 118's `APA22.SOC.2.4` coverage | `data/plans/psychology/source-map.csv`, `data/plans/psychology/days.csv` |
| Separate Virginia and North Carolina eugenics apology and compensation years on day 75 | Virginia apologized 2002 and compensated 2015; North Carolina apologized 2002 and compensated 2013 | `data/plans/psychology/days.csv` |
| Reword day 126 note to "Our own content beside the adapted section" | Removes contradiction with the OpenStax 12.5 credit line and source map | `data/plans/psychology/days.csv` |
| Add `COG.2.1` three-part prompt to day 81 note and earlier-unit framing for `THR.1.1` biomedical item on day 159 | Closes multi-part prompt and rule 3 non-repetition gaps | `data/plans/psychology/days.csv` |

## For Cory

None.

## Sources

- [Encyclopedia Virginia](https://encyclopediavirginia.org/) and [PBS NewsHour](https://www.pbs.org/): verified Virginia 2002 apology / 2015 compensation and North Carolina 2002 apology / 2013 compensation dates.
- [OSF Reproducibility Project](https://osf.io/) and [NIH PMC](https://www.ncbi.nlm.nih.gov/): verified Open Science Collaboration (2015) 100 studies, 97% original vs 36% replication significance.
- [Tilburg University](https://www.tilburguniversity.edu/) / [Taylor & Francis](https://www.tandfonline.com/): verified Flore, Mulder and Wicherts (2018) preregistered stereotype threat study.
- [NIH PMC](https://www.ncbi.nlm.nih.gov/) / [APS](https://www.psychologicalscience.org/) / [OSF](https://osf.io/): verified Sisk et al. (2018), Yeager et al. (2019), and Watts, Duncan and Quan (2018).
- [NIH PMC](https://www.ncbi.nlm.nih.gov/) / [Chapman University](https://www.chapman.edu/): verified Wagenmakers et al. (2016) 17-lab RRR and Coles et al. (2022) multi-lab facial feedback study.
- [NIH PMC](https://www.ncbi.nlm.nih.gov/) / [PsyPost](https://www.psypost.org/): verified Manning, Levine and Collins (2007) and Philpot et al. (2020) CCTV bystander intervention study.
- [PLOS ONE](https://journals.plos.org/): verified White, Uttl and Holder (2019) reanalysis of Bolier et al. (2013).
- [NIH PMC](https://www.ncbi.nlm.nih.gov/) / [UCL](https://www.ucl.ac.uk/): verified Cipriani et al. (2018), Moncrieff et al. (2022), and 988 July 2022 launch.

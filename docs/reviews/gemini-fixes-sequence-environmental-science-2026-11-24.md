# Gemini fixes: scope and sequence of environmental-science, 2026-11-24

Fix pass after the outside second read S:\CurioClass-gemini\reports\sequence-environmental-science-gemini-read.md.
Each finding was checked against days.csv, source-map.csv, frame.md and scope-and-sequence.md, and against the
settled fixes in docs/reviews/sequence-environmental-science-fixes-2026-11-24.md and DESK-ANSWERS.md. Helper script:
_scratch/l87/tmp/environmental-science-gemini-fix/fix.py.

Files changed: data/plans/environmental-science/days.csv, data/plans/environmental-science/source-map.csv,
docs/courses/environmental-science/scope-and-sequence.md.

## Findings

- **G1, literacy codes in the codes column** (partly). Holds for end days: WHST.11-12.2 (parts a to f) sat in the codes
  of end days 16, 82 and 129, so rule 2 ("each part of each code") would claim a lettered literacy standard the frame
  says is never claimed in full. Biology, Chemistry and Physics list literacy codes on practice days but never on an
  assessed day. Wrong for the rest: the frame (Desk 2026-11-14, "Load them") puts practiced codes on the days that
  practice them, so moving all 28 days' codes into notes would undo the frame's rule. Changed: WHST.11-12.2 removed from
  the codes of days 16, 82 and 129, each note now ends "Practiced, not scored as a standard: WHST.11-12.2"; the scope's
  opening paragraph states that no end or check day lists a literacy code. No other assessed day carries one (checked).
- **G2, source map out of sync on unit 5, no ours rows** (holds). The earlier fix pass moved town waste to day 74 but
  left source-map.csv on the old days (its ledger said the days were checked; they were not). Changed: Harris 12.1,
  12.2, 12.4 to day 74; 6.1, 6.2 to 75; 6.3 to 76; 6.4 to 78, with "(here day n)" in order_conflict to match. Every
  Harris row's days now match the "Adapts Harris" days in days.csv (scripted cross-check). Added one ours row per unit
  (1 to 9, 113 days in all). The 11 C days get no ours row: the gate refuses a source-map unit of C, and those days
  adapt no base lesson.
- **G3, day 158 "folds first"** (holds). The frame and the scope's Shorter path fold 160, then 141, then 158. Changed:
  day 158's note now says it folds third, after days 160 and 141.
- **G4, coverage table omissions** (holds, all four). Day 108 and day 123 are named model revision points; day 156 reads
  national demographic and survey data; day 101 scores a tolerance index and day 158 records cover with its spread
  (unit 3's index day 43 and unit 1's count days already sit in Mth). Changed: M adds 108 (unit 7) and 123 (unit 8);
  checks row D now 52, 53, 101, 102, 156 to 158; Mth now 52, 101, 102, 156, 158.
- **G5, "none from roadsides" in the safety cells of days 21 to 23** (partly). The gate's false-positive risk is wrong:
  sequence.py reads "none" only as a whole cell. The wording was still unclear. Changed: "no soil from roadsides".
- **Gemini's gate checks and For-the-lead judgments**: agree; nothing to change. Its finding set does not touch any
  settled fix of the expert pass.
- **Fact and figure checks** (holds; Gemini linked only home pages, so each was checked here by search):
  - Everglades road surveys: raccoons down 99.3 percent, opossums 98.9 percent (Dorcas et al. 2012,
    https://www.usgs.gov/publications/severe-mammal-declines-coincide-proliferation-invasive-burmese-pythons-everglades).
  - 108-city redlining study, up to about 7 degrees Celsius (Hoffman, Shandas and Pendleton 2020,
    https://ui.adsabs.harvard.edu/abs/2020Clim....8...12H/abstract).
  - Richmond 2017: up to about 16 degrees Fahrenheit (about 9 Celsius) between parts of the city on one day
    (https://virginiamercury.com/2020/01/15/there-may-be-a-link-between-urban-heat-islands-and-past-redlining-practices-study-finds/).
    The unit writer pins the exact figure (one local account gives 15).
  - Navajo Nation: over 500 abandoned uranium mines (https://www.epa.gov/navajo-nation-uranium-cleanup/abandoned-mines-cleanup);
    uranium limit 30 micrograms per liter, as stated in the frame; the unit writer cites the federal rule page.
  - Toledo, August 2014: about 400,000 people, microcystin, do-not-drink and do-not-boil, lifted August 4
    (https://www.nrdc.org/stories/toledos-blooming-algae-crisis,
    https://circleofblue.org/2014/world/toledo-issues-emergency-warning-residents-drink-water).
  - Britain: coal 39 percent of electricity in 2012, final figures ("about 40" holds)
    (https://assets.publishing.service.gov.uk/media/5a7a5d5940f0b66a2fc01d17/et_article_coal_in_2012.pdf);
    Ratcliffe-on-Soar closed 30 September 2024 (https://www.uniper.energy/united-kingdom/power-plants-united-kingdom/ratcliffe-soar).
- **Own** (US spelling, AGENTS.md): "licence" to "license" in source-map.csv (3) and the scope (1).

Totals: 5 findings: 3 holds, 2 partly, 0 wrong, 0 already fixed. Fact checks: 6 hold. Browser check urls: none.

## For Cory

None. No change to units, day counts, scope, audience, money or people.

## Gates

- `python -X utf8 scripts/sequence.py check environmental-science`: 0 failures (9 units, 160 days, 149 in units).
- `python -X utf8 scripts/frame.py check environmental-science`: 0 failures.
- `python -X utf8 scripts/frame.py calendar`: passes (exit 0, no stagger break).

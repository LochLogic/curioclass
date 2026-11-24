# Gemini fixes: scope and sequence of earth-and-space-science, 2026-11-24

Fix pass on the outside second read S:\CurioClass-gemini\reports\sequence-earth-and-space-science-gemini-read.md (4 findings, 4 "Settled by the expert" rows that repeat them, 5 judgments of the For the lead items, 4 groups of fact checks). Each finding was checked against days.csv, source-map.csv and the scope and sequence, after the expert read docs/reviews/sequence-earth-and-space-science-2026-11-24.md and its fix pass docs/reviews/sequence-earth-and-space-science-fixes-2026-11-24.md. No settled fix or Desk decision was undone.

Counts. Findings 4: holds 2 (3, 4), partly 2 (1, 2), wrong 0, already fixed 0. Own additions 2. Fact checks 5, all agree with the files.

Files edited: data/plans/earth-and-space-science/days.csv (days 30 and 110), data/plans/earth-and-space-science/source-map.csv (12 `ours` rows added), docs/courses/earth-and-space-science/scope-and-sequence.md (coverage table, unit 2 evidence-meets-belief line, the opening line on the source map). No unit, owned row or day count changed.

## Findings

- **1. Coverage table out of step with days.csv: partly.**
  - (a) Initial models, holds. Units 1 and 2 count their day 1 sketch under M (days 1, 19); units 3 to 9 did not, though every one of those day 1 goals says "sketch an initial model". Added 34, 55, 72, 89, 107, 124 and 138 to M.
  - (b) Unit 9 I, partly. Day 140 explains the sky log entries; it is already in D and E and carries out no investigation, so it leaves I. Day 138 adds that night's log entry, so it joins I. Day 152 stays in I (it reports how the observing method was kept). Day 141 does not go in I as Gemini proposed: it models parallax with a thumb and a protractor, which is M, so it went under M. Unit 9 now reads M 138, 141, 151 and I 138, 152.
  - (c) Course-level checks row, partly. Days 52 (a profile, like day 3) and 53 (a cross section from a geologic map, like day 23) use the unit 1 and 2 map-models that the table counts as M, so both were added to M. Day 157 was not added: it works the layered energy balance, which the table counts as Math on its unit days (126, 128, 129, 136), and day 157 is already under Math. Day 104 judges one line of evidence, the same act as day 41, which is counted under A, so it was added to A. Day 158 was not added: it states a volcano's hazard from its record, the same act as day 44, which the table counts under D and CE, not A. The row now reads M 52, 53, 160 and A 104.
- **2. source-map.csv has no `ours` rows: partly.** Counted: 86 days adapt no base lesson, and none has a row. The gate does not require `ours` rows, and the expert found the map complete for every base section. But rule 8 names `ours` for a day with no base lesson, and calculus, geometry and Algebra I carry one `ours` row per unit. Added 12 rows in the calculus layout: one per unit (days listed exactly, with a short reason from the goals) and one per course-level check, under the unit it follows (52 to 54 under 3, 104 to 106 under 6, 156 to 160 under 9). Every day 1 to 160 now sits on exactly one kind of row (adapted or ours). The scope's opening line says so.
- **3. Day 30 lacks the evidence-meets-belief note: holds.** Day 30 puts the whole geologic time scale on one dated timeline, which is the age of Earth. Its note now carries the same sentence as days 19, 25 and 29 (evidence first, explain the evidence, never declare a belief, families' beliefs). The scope's unit 2 line now lists days 19, 25, 29 and 30. Days 26 to 28 (decay arithmetic and bracketing on given ages) were left as they are; they sit inside the same evidence-first run the note on day 25 sets up.
- **4. Day 110 safety "cutting tools: none": holds (minor).** The gate passed it, but rule 8's "any other case of the word none in a list" warns against it. Now "no cutting tools", matching unit 1's "no rock hammers" form. No other safety cell holds "none" inside a list.

## Own

- **Own 1.** Day 127 is a named "Model revision point" (the one-layer model fails every planet) but was missing from M in unit 8, while every other revision point (15, 30, 48, 99, 133, 151) is counted. Added 127 to unit 8 M.
- **Own 2.** Day 141 added to unit 9 M (see finding 1b).

## For the lead and fact checks

- Gemini's judgments of the five For the lead items agree with the fix pass. No action.
- The facts Gemini checked agree with the files, and the links it gave were home pages only, so each was checked again here:
  - Monadnock summit rock: mostly Devonian Littleton Formation schist and quartzite, with Silurian rock lower down ([Wikipedia, Mount Monadnock](https://en.wikipedia.org/wiki/Mount_Monadnock); [Littleton Formation](https://en.wikipedia.org/wiki/Littleton_Formation)). Unit 1's plan still confirms this from the state survey, as the scope's For the lead item 4 says.
  - Copalis River ghost forest killed between the 1699 and 1700 growing seasons; Japan's January 1700 orphan tsunami ([USGS image record](https://www.usgs.gov/media/images/dead-red-cedar-forest); [USGS, The orphan tsunami of 1700](https://www.usgs.gov/publications/orphan-tsunami-1700-japanese-clues-a-parent-earthquake-north-america)).
  - Mount St. Helens, 18 May 1980, 57 deaths ([USGS, impact](https://pubs.usgs.gov/gip/msh/impact.html)).
  - Abrupt Greenland warming at the end of the Younger Dryas, about 11,600 to 11,700 years ago, sources differing by about a century ([Britannica, Younger Dryas](https://www.britannica.com/science/Younger-Dryas-climate-interval)). Day 107's "about 11,700" stands.
  - Energy balance (days 127, 128): the Venus fact sheet gives Bond albedo 0.77 and black-body temperature 226.6 K, and Earth 254.0 K ([NASA Venus fact sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/venusfact.html)). Recomputed: one layer gives Earth about 302 K (14 K warm), Mars about 250 K (40 K warm) and Venus about 270 K (about 467 K cold). Fitted n is Earth about 0.65, Mars near 0 and Venus about 111. All match the settled day 127 and 128 goals.
- Browser check urls: none.

## For Cory

None. No finding touches units, day counts, scope, audience, money or people.

## Gates

- `python -X utf8 scripts/sequence.py check earth-and-space-science`: 0 failures. The same eight "reads like hands-on" notes as before (days 1, 25, 29, 64, 73, 97, 115, 117).
- `python -X utf8 scripts/frame.py check earth-and-space-science`: 0 failures (9 units, 160 days).
- `python -X utf8 scripts/frame.py calendar`: exit 0, no failure. Grade 12 has only the finals-week rule, and check 3 stays in week 32.

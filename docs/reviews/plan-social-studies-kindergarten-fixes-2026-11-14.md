# Fixes: unit plans of Kindergarten: Living and Learning Together

Course `social-studies-kindergarten`, 2026-11-14. Fixer pass over the expert read
(plan-social-studies-kindergarten-2026-11-14.md) and the Codex read (plan-social-studies-kindergarten-codex-2026-11-14.md).
Files edited: s01.md to s06.md and data/plans/social-studies-kindergarten/days.csv (rows 8, 16, 25, 44, 45, 46; day
count and unit totals unchanged). frame.md not touched. Day list rows in the plans were brought back into line with
days.csv for the changed rows only (no skeleton rerun).

**Gate:** `unitplan.py check social-studies-kindergarten` passes all six units. `plan.py check` exits 0;
`sequence.py check social-studies-kindergarten` 0 failures. The word cap is now 1,250 (not the 1,800 the expert read
quoted), so a few added sentences went into field 5 (uncounted) and some older wording in s02 and s05 was tightened.

## Applied: the expert's "For the fixer" list, in order

1. **C1, exit format (s01 to s06, field 5).** Each exit paragraph now says: every child marks a picture on paper in
   the last two minutes, the teacher reads the prompt aloud, the spoken "why" comes from a rotating group of six a
   day, children outside the group are recorded "not yet heard". Every exit row now opens with "Mark: ...". s03 days
   25 and 26 use the expert's mark tasks word for word; each child's own model and map from supported making stay the
   construction evidence.
2. **1.2, start-of-year check (s01, field 4).** Conflict with the lead rule: the expert put the check in days 1 to 3
   with no sitting; the brief's settled rule puts it in the last ten minutes of day 1. **I followed the lead rule:**
   "Given: the start-of-year check, in the last ten minutes of day 1, after the hook ... No sitting comes before
   day 1." I kept the expert's feasibility point inside it: item 1 heard in the hook's wonder wall, item 2 as a
   whole-class picture mark with reasons from six children, item 3 as partner turns watched for six; anyone not
   seen is noted in days 2 and 3. Bridges moved off day 1: item 1 to day 2's opening, item 3 to day 2's supported work,
   item 2 stays on day 3.
3. **1.1 and 1.3 (s01, field 5).** Day 8 now teaches (5 model, 11 partner practice with talk-rule notes, 2 exit);
   day 9 holds the fresh-source items in five groups of six. Item 2 reads "During days 5 to 9 (and the room's existing
   routines before then)".
4. **days.csv.** Day 8 note, day 16 goal, day 25 goal (picture graph) and day 44 goal and note (Juneteenth card,
   "Sensitivity read: Juneteenth card") as given. Day list rows synced in s01, s02, s03, s05.
5. **2.1 and 2.2 (s02, field 10).** Day 16 bullet adds the mouse's promise and the day 15 rule moment. Sensitivity
   list: the Greek-language Aesop link replaced by the youth account at SchoolHouse Connection (page checked: two young
   leaders' first-person accounts of growing up without a stable home); focus now "home circumstances and home jobs".
6. **3.1 and 3.2 (s03).** Days 25 and 26 administration now "note the rotating group during supported making; the
   products themselves are the evidence". Address examples: the school pages replaced by the Massachusetts State House,
   24 Beacon Street, Boston (mass.gov), and the Washington State Legislative Building, 416 Sid Snyder Avenue Southwest,
   Olympia (state Department of Enterprise Services). Item 5 sample uses 24 Beacon Street, Boston; item 6 sample made
   generic ("our town ... our school").
7. **4.1 to 4.4 (s04).** Administration rewritten as given (day 36 ten teaching minutes, day 37 no observation, day 38
   comparison with rotating notes); item 2's calendar record moved to day 38. "this class" became "a pictured class".
   Today sides of both fresh pairs are now photographs (teacher's photo of the school fountain, no child's face; a
   plain washing-machine photo, no brand visible). Field 10 adds the two-communities rule and says all three listed
   photographs are from south Texas, so at least one must be replaced. "day 52" became "day 53".
8. **5.1 to 5.8 (s05).** Sensitivity list now requires every frame source: Indigenous Journalists Association
   reporting guides (the expert's najanewsroom.com address returns 404; this is the association's current site,
   formerly the Native American Journalists Association), the Teaching Hard History K to 5 framework (address now
   redirects to splcenter.org; current address used), the Order Sons and Daughters of Italy in America for Columbus
   Day, and Mashpee fallback. Teacher note on the federal name, dated "As of November 2026". Hook rewritten; the
   compelling question is posted on day 44. Items 1 (Washington's Birthday note), 3 (2024 national bird note), 4 (flag
   colors: law gives no reason, seal meanings, "people say"), 6 (meets on the gist), 7 (the "why" of a tradition) and
   exits 41 (Italian American heritage sentence) and 47 (phrase-by-phrase line dropped).
9. **6.1 to 6.3 (s06).** Day 58 timing (2, 3, 15 store), saved token spent in the first two minutes of day 59,
   bakery caption in full. See Codex 11 below for how day 58's listening was merged with the Codex roster.
10. **C2, Tennessee.** All six comparison rows now read "Not yet compared; the 2024 PDF on tn.gov refuses automated
    reading. No Tennessee coverage is claimed."

Not applied from the expert: **C3** (voice) and **C4** (one-section unit fields): the expert asked for no plan edit
now; both are for the section writer or the structure pass.

## Applied: Codex findings the expert did not cover

- **Codex 1 (s01).** Items 1, 2 and 5 now come from dated notes on named days (no "where available"); a daily budget
  for days 2 to 7 added (2, 6, 10, 2; a bridge replaces up to ten supported minutes); day 1's ten-minute check replaces
  supported work; a part still unheard after day 10 stays "not yet observed". Codex's roster on days 5 and 7 for items 4
  and 6 not taken: those items use fresh sources withheld until day 9 (followed the expert's day 9 groups).
- **Codex 2, justice (s02).** Confirmed against the 2018 framework PDF (within PDF pages 31 to 36, standard K.T1.3
  names "justice"). Field 2 teaches "just (putting an unfair thing right)"; the parts line names justice and notes
  that the local paraphrase drops it; The Paper Workshop gains a child making room for a left-out classmate; The
  Puppet Basket gains Mo, who makes room so Sam gets an equal turn; item 4 asks "Who puts an unfair thing right?"
  (seven picture-response rows now). The standards file fix is for the structure pass.
- **Codex 3, day 14 budget (s02).** Added in field 5's administration (2, 4, 3, 3, 5, 1, 2), with day 13's two
  proposal cards and the reversible first trial.
- **Codex 4, graph teaching (s03).** Applied the expert's version: the teacher models a two-category picture graph
  with a labelled zero on day 25, then children make their own (days.csv day 25 names the graph). Codex's separate
  independent graph on day 26 not added: day 26 already holds the drawn map; the expert's settled reading wins.
- **Codex 5, day 39 capacity (s04).** Partly: day 39 now has six minutes of simultaneous ordering marks and ten to
  hear source explanations in five groups of six; unfinished evidence is recorded apart from errors. Codex's split of
  fresh-source talks into day 38 not taken: it would spend day 38's teaching minutes, which the expert's 4.1 protects.
- **Codex 6, day 37 exit (s04).** Replaced with a reserved historical source: Dorothea Lange, "Dead Ox Flat. Children
  get into school bus on a fall morning. Malheur County, Oregon," October 1939 (caption and date checked on the
  Library of Congress blog; image uninspected). The gray-picture contrast moved into day 37's teaching.
- **Codex 7, Pledge spread (s05, days.csv).** Pledge meanings now begin on 45 and 46 (MA.K.T1.4d added to their codes
  and goals in days.csv), with retrieval on 48 and 49. Named rosters: covered by the rotating group of six.
- **Codex 8, local tradition (s05, field 5).** A localization step before day 48 from a community's own published
  account; no family disclosure, guest or outside contact.
- **Codex 9 (s05).** Pledge link now https://bensguide.gpo.gov/j-pledge-allegiance (checked: loads, "Pledge of
  Allegiance: 1892").
- **Codex 10 (s05, field 3).** "No unit 6 plan exists yet" deleted; "Year-end day 63 retrieves holidays"; points to
  s06.md field 4.
- **Codex 11 (s06).** Merged with the expert's 6.1: a roster of ten named children a day across days 58 to 60, each
  with about a minute for all spoken parts; item 1's scenes are read on 58 before the first turn; item 7 is collected
  on the child's roster day; anything unheard after day 61 stays "not yet observed" in the year-end record.

Codex's "no suspicious question marks" stands: I found none to restore. No em dashes in any plan.

## Facts checked on the web before writing

- Bald eagle national bird: Public Law 118-206, approved December 23, 2024 (govinfo.gov).
- Holiday legal names, 5 U.S.C. 6103: "Washington's Birthday", "Columbus Day", "Juneteenth National Independence Day"
  (Cornell LII).
- Juneteenth: General Order No. 3 of June 19, 1865 told the people of Texas that enslaved people were free; the law
  making it a federal holiday was signed June 17, 2021 (National Archives).
- 2025 Columbus Day proclamation named Columbus Day only, after dual proclamations since 2021 (NPR; AP coverage
  syndicated via WSLS and others). Used only as "federal law names the day Columbus Day; many states and towns observe
  Indigenous Peoples' Day".
- Thomson's 1782 report on the seal's colors: white purity and innocence, red hardiness and valour, blue vigilance,
  perseverance and justice (diplomacy.state.gov Great Seal PDF, PDF page 6).
- Massachusetts K.T1.3 includes justice (doe.mass.edu 2018 framework PDF).

## Unverified

- The Indigenous Journalists Association reporting guides page itself was not fetched; its address comes from the
  association's own release page. The sensitivity agent confirms it.
- "Many Italian American families keep it as a day to be proud of their heritage" rests on the Order Sons and
  Daughters of Italy in America's own advocacy materials (an interested source), not wire reporting. It is written as
  a community's view, not a figure.
- The three south Texas photographs, the Dead Ox Flat photograph and the Great Seal Hand Press image remain
  uninspected (loc.gov refuses automated reading).

## For the structure pass

1. data/standards/ma-hss-2018.txt: MA.K.T1.3 drops "justice" from the 2018 text (Codex structure 2). Fix the line;
   the s02 skeleton block will then carry it.
2. The expert's six structure items stand unchanged: `observe` in unit_skeleton.py and unitplan.py's assessment
   check (also Codex structure 1); one-section units and U3 to U11; a K to 2 exit and observation default; Tennessee
   lines loaded once into STANDARD.md; a "builds on earlier units in this course" line; the runs_text "and" join.
3. Codex structure 3, 4 and 6: an evidence-collection field (class size, roster, simultaneous response, recording
   time), complete daily budgets, and tracking image inspection apart from catalog traceability.
4. The plan-read brief and the expert read still quote an 1,800-word cap; unitplan.py now enforces 1,250.

## For Cory

None.
